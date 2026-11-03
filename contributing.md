---
description: Suggest a free AI/ML learning resource, fix a link, or improve a roadmap step.
permalink: /contributing/
---

# Contributing

Thanks for helping people learn AI. The fastest way to contribute is an [issue](https://github.com/GruheshKurra/awesome-ai-roadmaps/issues/new/choose): suggest a resource, or report a broken link, a paywall, or a confusing step. Pull requests that fix links or improve a track are welcome too.

## What makes a good resource

- **Free.** No paid course, trial, certificate funnel, or login wall for the core content.
- **Specific.** One video, paper, article, or chapter. Not a course homepage, a playlist, a channel, or another list.
- **Better than what's there.** Say why it teaches the concept more clearly, more correctly, or more currently than the existing step.
- **Teaches, doesn't sell.** No product ads dressed as tutorials. Please say if you are affiliated with the author or publisher.

DSA and interview prep are out of scope.

## Track format

Each track lives in `tracks/<slug>/README.md` and has a title, `Goal:`, `Prereqs:`, `Time:`, `Status: done`, a numbered `Step | Concept | YouTube | Read` table with 5–15 steps, and a `## Build it` section with two or three projects. YouTube links are bold and use `youtube.com/watch?v=` URLs without playlists. Each cell holds one link.

## Checks

After editing a track or the README Contents tables, run:

```sh
ruby scripts/catalog.rb --write
python3 -m unittest discover -s scripts/tests
```

The first command refreshes step counts, the site sidebar, and page descriptions. The tests check table structure and the built-site rules. A weekly GitHub Action checks every link, and pull requests that touch tracks run it too.

To preview the website locally, install Jekyll with the plugins in `_config.yml`, then:

```sh
jekyll build --destination /tmp/roadmaps-site
find /tmp/roadmaps-site -name '*.md' -delete
python3 scripts/check_site.py /tmp/roadmaps-site
```
