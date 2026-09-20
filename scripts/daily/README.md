# Daily maintenance

One scheduled run at 18:45 Europe/London. The owner runs it on a Mac using an existing Codex CLI sign-in. GitHub Pages deploys after a successful push to `main`.

## What a run does

1. Claims the current London date under an exclusive process lock. Restarts and duplicate triggers cannot start a second run that day. Failed attempts also consume the date.
2. Clones the latest `main` into private run storage, leaving the working project untouched.
3. Checks every unique published resource URL with four concurrent workers, request timeouts, and one retry for transient errors. Records redirects, response status, and repeated unavailability. YouTube uses its public oEmbed endpoint. This is an availability signal, not proof of access or teaching quality.
4. Gives Codex the audit, three rotating tracks, previous reports, and GitHub metrics. Codex researches corrections, better sources, one new track, short introductions, and discovery improvements. It opens proposed sources and records evidence of free access.
5. Independently checks changed paths, new-source evidence, the catalog, regression tests, the Jekyll build, and the built site. The editor cannot publish changes to the scheduler, tests, workflows, or maintenance scripts through this controller.
6. Commits and pushes one validated batch if there are useful changes and remote `main` has not moved. It never force-pushes. A concurrent edit stops publication and leaves the checkout for review.
7. Waits for the Pages workflow and records the result. The next run reads earlier reports and adjusts its priorities. No-change days produce a report without a commit.

The research stage has a 45-minute limit. New resources need direct free-access evidence; 403, 429, timeouts, and bot challenges are uncertain. A failed availability check alone does not justify deleting a resource. A failed post-push deployment is reported, not silently rolled back.

## Growth measurements

The private report records stars, forks, watchers, open issues, and 14-day repository view/clone totals when the account can access them. These are repository metrics, not website analytics. Compare weekly trends; overlapping 14-day totals must not be added together. Metric changes do not establish which edit caused them.

Prioritize useful topic coverage, precise titles and descriptions, clear prerequisites, good navigation, and current free resources. The loop does not buy stars, manufacture activity, publish outreach, or post promotional messages. It can draft suggestions in its private report. No paid services or new analytics systems are created.

## Local operation

The installation keeps a copy of `run.py`, `audit.py`, and `prompt.md` outside the checkout. This prevents daily editorial work from changing its own publication gates. Reinstall those files intentionally after reviewing maintenance-code changes.

Install with `python3 scripts/daily/install.py` from the intended repository. If a schedule already exists, the installer stops before changing it. Pause it before reinstalling. The controller also protects Jekyll plugin, execution, exclusion, and deployment settings; daily configuration edits are limited to catalog metadata, titles, and descriptions.

The launch agent uses `StartCalendarInterval` for 18:45 and `RunAtLoad` for login recovery. The Mac's system timezone must remain Europe/London. A wake after the scheduled time can trigger that day's run; login recovery before 18:45 does nothing. There are no backlog runs for missed days. The Mac must be on, logged in, and online, with Codex/GitHub authentication and sufficient Codex usage available. The ChatGPT desktop app does not need to stay open.

The owner’s installation uses:

- Controller and reports: `~/Library/Application Support/awesome-ai-roadmaps-daily/`
- Schedule: `~/Library/LaunchAgents/com.karthik.awesome-ai-roadmaps-daily.plist`
- Daily result: `runs/YYYY-MM-DD/result.json`
- Editorial report: `runs/YYYY-MM-DD/report.md`
- Validation output: `runs/YYYY-MM-DD/checks.log`
- Failure details: `runs/YYYY-MM-DD/failure.txt`

Check prerequisites without starting a daily run:

```sh
python3 scripts/daily/run.py --repo . --state-dir /path/to/private/state --check
```

Run the controller with the same arguments without `--check` to use the daily time/date guard. There is no force-run switch. Test fixtures use temporary state and remotes instead of bypassing the production guard.

Pause the installed schedule:

```sh
launchctl bootout gui/$(id -u) "$HOME/Library/LaunchAgents/com.karthik.awesome-ai-roadmaps-daily.plist"
```

Resume it:

```sh
launchctl bootstrap gui/$(id -u) "$HOME/Library/LaunchAgents/com.karthik.awesome-ai-roadmaps-daily.plist"
```

Codex uses its existing saved authentication. No credentials are copied into the repository or scheduler. See the official [non-interactive mode documentation](https://developers.openai.com/codex/noninteractive).
