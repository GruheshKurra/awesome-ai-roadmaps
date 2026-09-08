# frozen_string_literal: true

require 'json'
require 'pathname'
require 'uri'
require 'yaml'

# Derived catalog fields come from README Contents and the published track tables.
# No network access: resource availability and relevance need a separate review.
class Catalog
  ROW = /^\| \[([^\]]+)\]\(tracks\/([a-z0-9-]+)\/\) \| (.+?) \| (\d+) \|$/

  def initialize(root)
    @root = Pathname(root)
    @errors = []
  end

  def read(path)
    @root.join(path).read
  end

  def check(condition, message)
    @errors << message unless condition
  end

  def cells(line)
    line.strip.sub(/^\|/, '').sub(/\|$/, '').split(/(?<!\\)\|/, -1).map(&:strip)
  end

  def link?(cell, youtube: false)
    return true if cell.empty?

    pattern = youtube ? /\A\*\*\[[^\[\]\n]+\]\((https?:\/\/[^\s)]+)\)\*\*\z/ : /\A\[[^\[\]\n]+\]\((https?:\/\/[^\s)]+)\)\z/
    match = pattern.match(cell)
    return false unless match

    uri = URI.parse(match[1])
    return false if uri.host.nil? || uri.userinfo
    return true unless youtube

    query = URI.decode_www_form(uri.query || '').to_h
    %w[youtube.com www.youtube.com m.youtube.com].include?(uri.host) &&
      uri.path == '/watch' && query.fetch('v', '').match?(/\A[\w-]{11}\z/) && !query.key?('list')
  rescue URI::InvalidURIError, ArgumentError
    false
  end

  def sync(write: false)
    readme = read('README.md')
    contents = readme.split("## Contents\n", 2)[1]&.split(/^## /, 2)&.first.to_s
    tracks = contents.scan(ROW).map do |label, slug, covers, _count|
      { label: label, slug: slug, covers: covers }
    end
    slugs = tracks.map { |track| track[:slug] }
    check(!tracks.empty?, 'README Contents must contain published tracks')
    check(slugs.uniq == slugs, 'README Contents contains duplicate tracks')
    check(contents.lines.count { |line| line.match?(/^\| \[/) } == tracks.length,
          'Contents rows must use folder links and numeric step counts')
    files = @root.glob('tracks/*/README.md').map { |path| path.parent.basename.to_s }
    check(files.sort == slugs.sort, 'Track folders and README Contents disagree')
    ignore = read('.gitignore')

    tracks.each do |track|
      slug = track[:slug]
      path = @root.join("tracks/#{slug}/README.md")
      next unless path.file?

      text = path.read
      check(text.match?(/^# .+$/), "#{slug}: missing title")
      check(text.match?(/^Goal: .+$/), "#{slug}: missing goal")
      check(text.match?(/^Prereqs: .+$/), "#{slug}: missing prerequisites")
      check(text.match?(/^Status: done$/), "#{slug}: only done tracks may be published")
      table = text.lines.select { |line| line.start_with?('|') }
      check(cells(table.first.to_s).map { |cell| cell.delete('*') } == %w[Step Concept YouTube Read],
            "#{slug}: expected Step | Concept | YouTube | Read")
      check(cells(table[1].to_s).length == 4 && cells(table[1].to_s).all? { |cell| cell.match?(/\A:?-{3,}:?\z/) },
            "#{slug}: invalid table separator")
      rows = table.drop(2).map { |line| cells(line) }
      track[:count] = rows.length
      check((5..15).cover?(rows.length), "#{slug}: expected 5–15 steps")
      rows.each_with_index do |row, index|
        step = "#{slug} step #{index + 1}"
        check(row.length == 4, "#{step}: expected four cells; escape pipes inside text")
        next unless row.length == 4

        check(row[0] == (index + 1).to_s, "#{step}: steps must be sequential")
        check(!row[1].empty?, "#{step}: missing concept")
        check(!row[2].empty? || !row[3].empty?, "#{step}: missing resource")
        check(link?(row[2], youtube: true), "#{step}: expected one bold YouTube watch link")
        check(link?(row[3]), "#{step}: expected one reading link")
      end
      check(ignore.lines.map(&:chomp).include?("!tracks/#{slug}/") &&
            ignore.lines.map(&:chomp).include?("!tracks/#{slug}/**"), "#{slug}: missing .gitignore exceptions")
    end

    config_text = read('_config.yml')
    config = YAML.safe_load(config_text)
    check(config_text.include?('  # BEGIN CATALOG DESCRIPTIONS') &&
          config_text.include?('  # END CATALOG DESCRIPTIONS'), 'Missing catalog description markers')
    check(config_text.match?(/^track_nav:\n.*?(?=^\S|\z)/m), 'Missing track_nav block')
    raise @errors.join("\n") unless @errors.empty?

    total = tracks.sum { |track| track[:count] }
    check(readme.match?(/\b\d+ tracks, \d+ steps\b/), 'README is missing its track and step totals')
    updated_readme = readme.sub(/\b\d+ tracks, \d+ steps\b/, "#{tracks.length} tracks, #{total} steps")
    updated_readme = updated_readme.gsub(ROW) do |line|
      match = ROW.match(line)
      count = tracks.find { |track| track[:slug] == match[2] }[:count]
      "| [#{match[1]}](tracks/#{match[2]}/) | #{match[3]} | #{count} |"
    end

    labels = (config['track_nav'] || []).to_h { |item| [item['slug'], item['label']] }
    nav = tracks.map do |track|
      "  - slug: #{track[:slug]}\n    label: #{JSON.generate(labels.fetch(track[:slug], track[:label]))}\n"
    end.join
    updated_config = config_text.sub(/^track_nav:\n.*?(?=^\S|\z)/m, "track_nav:\n#{nav}\n")
    descriptions = tracks.map do |track|
      label = labels.fetch(track[:slug], track[:label])
      description = "#{label} roadmap: #{track[:covers]} Free videos, papers, and chapters in learning order."
      "  - scope:\n      path: tracks/#{track[:slug]}\n    values:\n      description: #{JSON.generate(description)}\n"
    end.join
    updated_config = updated_config.sub(/  # BEGIN CATALOG DESCRIPTIONS\n.*?  # END CATALOG DESCRIPTIONS/m,
                                        "  # BEGIN CATALOG DESCRIPTIONS\n#{descriptions}  # END CATALOG DESCRIPTIONS")
    # Parse before writing to avoid publishing a malformed generated config.
    YAML.safe_load(updated_config)

    tracker = read('tracker.md')
    updated_tracker = tracker.gsub(/\[([ x])\] `([^`]+)`/) do
      checked, slug = Regexp.last_match.captures
      check(checked != 'x' || slugs.include?(slug), "#{slug}: checked in tracker but not published")
      "[#{slugs.include?(slug) ? 'x' : ' '}] `#{slug}`"
    end
    queue_count = updated_tracker.scan(/\[ \] `([^`]+)`/).length
    check(tracker.match?(/^\| Done \| \d+ \|$/) && tracker.match?(/^\| Queue \| \d+ \|$/),
          'Tracker is missing its Done or Queue totals')
    updated_tracker = updated_tracker.sub(/^\| Done \| \d+ \|$/, "| Done | #{tracks.length} |")
                                     .sub(/^\| Queue \| \d+ \|$/, "| Queue | #{queue_count} |")
    raise @errors.join("\n") unless @errors.empty?

    changes = { 'README.md' => updated_readme, '_config.yml' => updated_config, 'tracker.md' => updated_tracker }
              .reject { |path, text| read(path) == text }
    if write
      changes.each { |path, text| @root.join(path).write(text) }
    elsif !changes.empty?
      raise "Catalog metadata is stale: #{changes.keys.join(', ')}. Run ruby scripts/catalog.rb --write."
    end
    puts "Catalog verified: #{tracks.length} tracks, #{total} steps, #{queue_count} queued."
  end
end

if $PROGRAM_NAME == __FILE__
  abort 'Usage: ruby scripts/catalog.rb [--write]' unless (ARGV - ['--write']).empty?
  begin
    Catalog.new(File.expand_path('..', __dir__)).sync(write: ARGV.include?('--write'))
  rescue StandardError => e
    warn e.message
    exit 1
  end
end
