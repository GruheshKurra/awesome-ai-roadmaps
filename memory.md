# memory.md — the agent's long-term memory

Keep under 300 lines. Compress every Sunday. Newest entries first in logs.

## Settings
- MODE: direct (fully autonomous; push to main, PR+self-merge only as fallback)
- Goal: one best free, underrated, verified resource per AI concept. Stars are a side effect of usefulness + human-led sharing.

## Diagnosis at start (2026-10-11)
- Repo: 35 tracks, 344 steps, 4 stars, created 2026-09-02. 
- Problems: mostly famous sources (3Blue1Brown, Karpathy, StatQuest) so no clear angle vs roadmap.sh and other lists; track-first structure forces long paths, not "one thing per concept"; queue of 864 candidates in tracker.md is bloat; Codex/launchd scripts in scripts/daily/ are Mac-only and superseded by this cloud routine.
- Plan: (1) rewrite README as a 5-second pitch + "Start here"; (2) add per-entry time/level/why-this-one; (3) audit all 344 steps, keep the best, replace generic ones; (4) shrink tracker.md to a small backlog; (5) retire scripts/daily once this routine works.

## Backlog (highest value first)
- [ ] Rewrite README front page (pitch, 3 start paths, how entries are chosen).
- [ ] Add TIPS.md (sourced).
- [ ] Add time/level/why columns to the 10 most-visited tracks first (llms, deep-learning, math-for-ml, nlp, rag).
- [ ] Prune tracker.md queue to <= 40 real gaps.
- [ ] Draft growth/ launch assets (Show HN, Reddit, X) for human posting.

## Rejected (never re-propose)
(none yet)

## Blocked
- 2026-10-11 run 2: the routine prompt assumes README tables (`Concept|Watch|Read|Why`), `data/links.json` and `scripts/check.py`. None exist: the repo is 35 `tracks/*/README.md` files (344 steps) with only `scripts/check_site.py`. Link verification, the 80-150 entry cap and the ledger cannot run until the structure is migrated (Backlog item 1).
- YouTube is unreachable from the cloud sandbox (curl 000, WebFetch ENOTFOUND www.youtube.com). Per the rules, no YouTube pick can be verified, so none was added or changed. Check whether the environment's network policy allows youtube.com; otherwise verification must use other sources (e.g. noembed or page metadata via an allowed host).
- Open issue count is 1; not inspected beyond the count.
- Owner decision needed: migrate to the one-pick-per-concept README + ledger + check.py, or update the prompt to the track structure.

## Metrics (one row per run)
| date | stars | forks | issues | change made |
|---|---:|---:|---:|---|
| 2026-10-11 | 4 | 0 | 0 | baseline |
| 2026-10-11 (run 2) | 4 | 0 | 1 | no content change (blocked, see below) |

## Lessons (hypothesis -> evidence -> status)
(none yet; add only when supported by 7+ days of data)

## Next run
Once YouTube access works, build `data/links.json` and `scripts/check.py` from the existing tracks, then do Backlog item 1. If YouTube is still blocked, build those with only non-YouTube links.
