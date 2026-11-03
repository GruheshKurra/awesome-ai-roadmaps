# Contributing

Thanks for helping people learn AI. The easiest way to help is an [issue](https://github.com/GruheshKurra/awesome-ai-roadmaps/issues/new/choose): suggest a better video, report a dead one, or propose a roadmap.

## What makes a good pick

- **A YouTube video first.** One specific video, not a playlist or a channel. Clear beats famous; short beats long when it teaches the same thing.
- **A GitHub repo when it helps.** Code to read or run alongside the video. Not archived.
- **Free.** No paid course, trial, or sign-up wall.
- **Honest.** Say if you made it or are affiliated with it.

## How the repo is built

Everything is generated from `data/`:

- `data/roadmaps/NN-slug.json` holds one roadmap: title, level, tagline, prerequisites, steps (`title`, `video` ID, `why`, optional `repo`), and `projects`.
- `data/meta.json` holds video titles, channels, lengths, and repo stars. Don't edit it by hand.
- `data/upcoming.json` lists the roadmaps planned next.

After changing a roadmap:

```sh
python3 scripts/refresh_meta.py   # fetch details for new videos and refresh repo stars
python3 scripts/build.py          # regenerate README.md, roadmaps/*.md, and the site in _site/
```

Preview the site with `python3 -m http.server --directory _site`. Don't edit `README.md` or `roadmaps/*.md` directly; CI fails if they don't match `data/`.

Run `python3 scripts/refresh_meta.py --all` now and then to re-check every video. It is slow on purpose so YouTube doesn't rate-limit you.
