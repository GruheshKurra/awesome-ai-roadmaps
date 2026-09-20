"""Run one researched update per London day, then validate and publish it."""

import argparse
import fcntl
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

if __package__:
    from .audit import audit, resource_links
else:
    from audit import audit, resource_links

REPOSITORY = 'GruheshKurra/awesome-ai-roadmaps'
REMOTE = f'https://github.com/{REPOSITORY}.git'
TIMEZONE = ZoneInfo('Europe/London')
PUBLIC = {'README.md', 'contributing.md', 'tracker.md', '.gitignore', '_config.yml',
          '_layouts/default.html', '_includes/sidebar.html', 'assets/css/site.css',
          'assets/favicon.svg', 'assets/og-image.png', '404.html', 'robots.txt'}


def allowed(path):
    return path in PUBLIC or re.fullmatch(r'tracks/[a-z0-9-]+/README\.md', path) is not None


def read_json(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(data, indent=2) + '\n')
    temp.replace(path)


def command(args, cwd, timeout=120, stdin=None):
    result = subprocess.run(args, cwd=cwd, input=stdin, capture_output=True, text=True, timeout=timeout)
    if result.returncode:
        raise RuntimeError(f'{args[0]} {args[1]} failed ({result.returncode}):\n{result.stderr[-3000:]}')
    return result.stdout.strip()


def reserve(state, now):
    """Called under an exclusive process lock. Failed attempts also consume the day."""
    local = now.astimezone(TIMEZONE)
    if (local.hour, local.minute) < (18, 45):
        return None
    day = local.date().isoformat()
    record = state / 'runs' / day
    try:
        record.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        return None
    write_json(record / 'result.json', {'date': day, 'status': 'started', 'started_at': local.isoformat()})
    return record


def metrics(root):
    data = json.loads(command(['gh', 'api', f'repos/{REPOSITORY}'], root))
    result = {key: data[key] for key in ('stargazers_count', 'forks_count', 'subscribers_count', 'open_issues_count')}
    for kind in ('views', 'clones'):
        try:
            traffic = json.loads(command(['gh', 'api', f'repos/{REPOSITORY}/traffic/{kind}'], root))
            result[f'{kind}_14_days'] = {key: traffic[key] for key in ('count', 'uniques')}
        except RuntimeError:
            result[f'{kind}_14_days'] = None
    return result


def check_changes(work, base):
    if command(['git', 'rev-parse', 'HEAD'], work) != base:
        raise RuntimeError('Editor changed git history; publication stopped')
    if command(['git', 'diff', '--cached', '--name-only'], work):
        raise RuntimeError('Editor staged files; publication stopped')
    tracked = set(command(['git', 'ls-tree', '-r', '--name-only', base], work).splitlines())
    changed = set(command(['git', 'diff', '--name-only', base], work).splitlines())
    changed.update(command(['git', 'ls-files', '--others', '--exclude-standard'], work).splitlines())
    for name in changed:
        path = work / name
        if not allowed(name) or path.is_symlink() or not path.is_file():
            raise RuntimeError(f'Unapproved path, deletion, or symlink: {name}')
    if '_config.yml' in changed:
        parser = ['ruby', '-ryaml', '-rjson', '-e', 'puts JSON.generate(YAML.safe_load(STDIN.read))']
        original = json.loads(command(parser, work, stdin=command(['git', 'show', f'{base}:_config.yml'], work)))
        candidate = json.loads(command(parser, work, stdin=(work / '_config.yml').read_text()))
        editorial = {'title', 'description', 'defaults', 'track_nav'}
        if {k: v for k, v in original.items() if k not in editorial} != {k: v for k, v in candidate.items() if k not in editorial}:
            raise RuntimeError('Jekyll execution or deployment configuration changed; publication stopped')
    # Also catch ignored new code hidden by an edited .gitignore before running Jekyll/tests.
    for path in work.rglob('*'):
        relative = path.relative_to(work)
        name = relative.as_posix()
        if relative.parts[0] in ('.git', 'tasks', '.jekyll-cache', '_site') or name in ('AGENTS.md', '.jekyll-metadata'):
            continue
        if path.is_symlink():
            raise RuntimeError(f'Symlink in candidate checkout: {name}')
        if path.is_file() and name not in tracked and not allowed(name):
            raise RuntimeError(f'Unexpected candidate file: {name}')
    new_tracks = {name for name in changed if name.startswith('tracks/') and name not in tracked}
    if len(new_tracks) > 1:
        raise RuntimeError('At most one new track may be published per day')
    return sorted(changed)


def verify_new_sources(work, original_urls):
    new_urls = set(resource_links(work)) - set(original_urls)
    evidence = read_json(work / 'tasks/source-evidence.json', {})
    missing = [url for url in new_urls if evidence.get(url, {}).get('verified_free') is not True
               or len(evidence.get(url, {}).get('note', '').strip()) < 30]
    if missing:
        raise RuntimeError('New resources lack direct free-access evidence: ' + ', '.join(missing))
    checked = audit(work, urls=new_urls) if new_urls else {}
    unavailable = [url for url, result in checked.items() if result['status'] == 'unavailable']
    if unavailable:
        raise RuntimeError('New resources returned unavailable: ' + ', '.join(unavailable))
    return checked


def run_editor(work, record, prompt):
    args = ['codex', 'exec', '--sandbox', 'workspace-write',
            '-c', 'approval_policy="never"', '-c', 'sandbox_workspace_write.network_access=true',
            '-c', 'web_search="live"', '--cd', str(work),
            '--output-last-message', str(work / 'tasks/editor-report.md'), '-']
    with (record / 'editor.log').open('w') as log:
        process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=log, stderr=log,
                                   text=True, cwd=work, start_new_session=True)
        try:
            process.communicate(prompt, timeout=2700)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
            raise RuntimeError('Editor exceeded its 45-minute limit; nothing was published')
        if process.returncode:
            raise RuntimeError(f'Editor exited with status {process.returncode}; see editor.log')


def validate(work, record):
    commands = [['ruby', 'scripts/catalog.rb', '--write'], ['ruby', 'scripts/catalog.rb'],
                [sys.executable, '-m', 'unittest', 'discover', '-s', 'scripts/tests'],
                ['git', 'diff', '--check'],
                ['jekyll', 'build', '--source', str(work), '--destination', str(record / 'site')]]
    with (record / 'checks.log').open('w') as log:
        for args in commands:
            log.write('$ ' + ' '.join(args) + '\n' + command(args, work, timeout=300) + '\n')
        for file in (record / 'site').rglob('*.md'):
            file.unlink()
        log.write(command([sys.executable, 'scripts/check_site.py', str(record / 'site')], work) + '\n')


def publish(work, base, changed, day):
    command(['git', 'fetch', 'origin', 'main'], work)
    if command(['git', 'rev-parse', 'origin/main'], work) != base:
        raise RuntimeError('Remote main changed during the run; retained edits for review, no push')
    command(['git', 'add', '--', *changed], work)
    command(['git', 'diff', '--cached', '--check'], work)
    new_tracks = [name.split('/')[1] for name in changed if name.startswith('tracks/') and
                  not command(['git', 'ls-tree', base, '--', name], work)]
    message = f'Add {new_tracks[0]} roadmap and refresh resources' if new_tracks else 'Refresh learning resources and roadmap discovery'
    command(['git', 'commit', '-m', message], work)
    identity = command(['git', 'log', '-1', '--format=%an %ae%n%cn %ce%n%B'], work)
    if re.search(r'\b(Cursor|Copilot|Claude|GPT|agent)\b|Co-authored-by:', identity, re.I):
        raise RuntimeError('Unexpected commit attribution; no push')
    sha = command(['git', 'rev-parse', 'HEAD'], work)
    command(['git', 'push', 'origin', 'HEAD:main'], work)
    return sha


def deployment(work, sha, timeout=600):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        runs = json.loads(command(['gh', 'run', 'list', '--repo', REPOSITORY, '--workflow', 'pages.yml',
                                   '--commit', sha, '--json', 'status,conclusion,url', '--limit', '1'], work))
        if runs and runs[0]['status'] == 'completed':
            if runs[0]['conclusion'] != 'success':
                raise RuntimeError('Pages deployment failed: ' + runs[0]['url'])
            return runs[0]['url']
        time.sleep(15)
    raise RuntimeError('Push succeeded but Pages did not finish within ten minutes')


def execute(root, state, record):
    day = record.name
    work = record / 'checkout'
    result = read_json(record / 'result.json', {})
    try:
        command(['git', 'clone', '--quiet', '--single-branch', '--branch', 'main', REMOTE, str(work)], root)
        base = command(['git', 'rev-parse', 'HEAD'], work)
        result['base_commit'] = base
        if (root / 'AGENTS.md').exists():
            shutil.copyfile(root / 'AGENTS.md', work / 'AGENTS.md')
        (work / 'tasks').mkdir(exist_ok=True)
        before = resource_links(work)
        links = audit(work, read_json(state / 'links.json', {}))
        write_json(record / 'links.json', links)
        write_json(state / 'links.json', links)
        snapshot = metrics(root)
        result['metrics'] = snapshot
        recent = []
        for previous in sorted((state / 'runs').glob('*/result.json'))[-15:]:
            if previous.parent == record:
                continue
            item = read_json(previous, {})
            report = previous.parent / 'report.md'
            item['report'] = report.read_text()[-6000:] if report.exists() else ''
            recent.append(item)
        tracks = sorted(path.parent.name for path in (work / 'tracks').glob('*/README.md'))
        if not tracks:
            raise RuntimeError('No published tracks found; daily editing stopped')
        offset = datetime.now(TIMEZONE).date().toordinal() * 3 % len(tracks)
        rotate = [tracks[(offset + index) % len(tracks)] for index in range(min(3, len(tracks)))]
        context = {'date': day, 'metrics': snapshot, 'recent_runs': recent,
                   'review_tracks': rotate,
                   'availability': {'total': len(links), 'reachable': sum(x['status'] == 'reachable' for x in links.values())},
                   'links_needing_review': {url: data for url, data in links.items() if data['status'] != 'reachable'}}
        write_json(work / 'tasks/daily-context.json', context)
        write_json(record / 'context.json', context)
        run_editor(work, record, (Path(__file__).with_name('prompt.md')).read_text())
        report = work / 'tasks/editor-report.md'
        if report.is_file():
            shutil.copyfile(report, record / 'report.md')
        changed = check_changes(work, base)
        if not changed:
            result['status'] = 'no_changes'
            shutil.rmtree(work)
            return
        checked = verify_new_sources(work, before)
        write_json(record / 'new-sources.json', checked)
        if (work / 'tasks/source-evidence.json').exists():
            shutil.copyfile(work / 'tasks/source-evidence.json', record / 'source-evidence.json')
        validate(work, record)
        changed = check_changes(work, base)
        sha = publish(work, base, changed, day)
        result.update(status='pushed', commit=sha, changed_files=changed)
        write_json(record / 'result.json', result)
        result['deployment_url'] = deployment(work, sha)
        result['status'] = 'deployed'
        # Reclaim only this run's disposable clone/build after a confirmed successful deployment.
        shutil.rmtree(work)
        shutil.rmtree(record / 'site')
    except Exception as error:
        result['status'] = 'deployment_unconfirmed' if result.get('commit') else 'failed'
        result['error'] = str(error)
        (record / 'failure.txt').write_text(str(error) + '\n')
        raise
    finally:
        result['finished_at'] = datetime.now(TIMEZONE).isoformat()
        write_json(record / 'result.json', result)
        print(json.dumps(result, indent=2), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--state-dir', type=Path, required=True)
    parser.add_argument('--check', action='store_true', help='Check prerequisites without running the daily task')
    args = parser.parse_args()
    root, state = args.repo.resolve(), args.state_dir.resolve()
    for name in ('git', 'gh', 'codex', 'ruby', 'jekyll'):
        if not shutil.which(name):
            parser.error(f'Missing executable: {name}')
    if command(['git', 'remote', 'get-url', 'origin'], root) != REMOTE:
        parser.error('The source repository has an unexpected origin')
    if args.check:
        print(command(['codex', 'login', 'status'], root))
        print(json.dumps(metrics(root)))
        print('Prerequisites checked. Daily schedule: 18:45 Europe/London. No daily run started.')
        return
    state.mkdir(parents=True, exist_ok=True)
    with (state / 'run.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print('Skipped: another daily run is active.')
            return
        record = reserve(state, datetime.now(TIMEZONE))
        if record is None:
            print('Skipped: before 18:45 London time or this date already has a run.')
            return
        execute(root, state, record)


if __name__ == '__main__':
    main()
