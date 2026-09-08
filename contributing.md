---
description: Suggest a free AI/ML learning resource or report a broken link, paywall, missing prerequisite, or unclear learning step.
permalink: /contributing/
---

# Contributing

Use the [issue forms](https://github.com/GruheshKurra/awesome-ai-roadmaps/issues/new/choose) to suggest a resource or report a problem. Please use issues for resource suggestions rather than pull requests.

For a suggestion, include the track, concept, URL, and what it improves over the current step. Resources must be free to read or watch. Link one specific video, paper, article, or chapter. Course homepages, semester playlists, other resource lists, paid material, and DSA/interview content are outside this catalog's scope.

For a problem, include the track and step, what happened, and what you expected. Reports about missing prerequisites or confusing step order are welcome alongside broken links and paywalls.

## Repository checks

The track tables and README Contents define the published catalog. After adding or editing a track, run:

```sh
ruby scripts/catalog.rb --write
ruby scripts/catalog.rb
python3 -m unittest discover -s scripts/tests
```

The first command updates counts, sidebar entries, page descriptions, and queue checkboxes. The second checks that those agree and that each published track has 5–15 numbered steps with valid link syntax. These checks do not verify remote availability or teaching quality; review the resources separately.

The Pages workflow runs these checks, builds Jekyll, removes raw Markdown copies, and checks the resulting HTML before deployment. With Jekyll and the plugins in `_config.yml` installed, the same build can be checked locally:

```sh
jekyll build --destination /tmp/roadmaps-site
find /tmp/roadmaps-site -name '*.md' -delete
python3 scripts/check_site.py /tmp/roadmaps-site
```
