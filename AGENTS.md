# Agent instructions

This repo is a ranked list of free AI learning tracks. Markdown is the product. Do not add a site, app, or package.

Public writing follows the no-ai-slop skill: no emoji headings, no pep talk, no filler, no synonym cycling. Lead with the point.

## Do not

- Push, add a remote, or open a GitHub repo unless the user said to.
- Fill more than one track in a session.
- Copy another repo's README, groupings, or blurbs. Discover URLs, then write original one-line whys.
- Add paid resources, certificate walls, or "free audit" courses whose lectures are not enough on their own.
- Add general DSA or software-interview material.
- Put stub tracks in the root README Contents.
- Put Contributing or Footnotes in Contents.
- Add a CI badge to the README. Link-check Actions are fine; the badge is not.
- Commit `.env`, keys, or credentials.
- Invent links. Every URL must be opened (or fetched) and confirmed live and free.

## Quality gates (every resource)

- Free. No paywall on the core material.
- AI/ML. Fits the track goal.
- You (or the maintainer) would actually recommend it.
- Ranked table of 5–15 rows. Fewer is better than padding.
- Table columns: `Step | Use this | YouTube`. Put lecture playlists in **YouTube**. Leave that cell empty when there is no video.
- Short file. No stage essays. No pep talk.
- Original wording. Do not paste other lists.

## Track file shape

Copy `tracks/_template.md`. Title, one-line goal, prereqs, status, then the table. Stub files keep the empty table. No fake links.

## Fill-one-track workflow

1. Read this file and `STATUS.md`.
2. Pick the track:
   - If the user named a slug, use that.
   - Else use the first `stub` in `STATUS.md`.
3. Set that slug to `filling` in `STATUS.md` and in `tracks/<slug>/README.md`.
4. Search live primary pages (course sites, arXiv, official playlists, project docs). Do not paste another list.
5. Keep 5–15. Rank. Write original whys. Verify each URL is reachable and free.
6. Write the full track README. Set `Status: done`.
7. Set the slug to `done` in `STATUS.md`.
8. Add the track to root README **Contents** (only `done` tracks). Keep Contents as the first section. One level of nesting at most.
9. Stop. Do not start the next stub.

## /loop prompt

Use this text with `/loop` when you want the next track. Do not start a loop from a scaffold session.

```
Read AGENTS.md and STATUS.md in this repo. Complete the next stub track only. Verify every link is free and live. Then stop.
```

## Git

- `git init -b main` is allowed locally.
- No `git remote add`, no `git push`, unless the user asked in this conversation.
- First public push waits until at least one track is `done`.
- No AI co-author trailers in commits.
