"""Fetch title, channel, and length for every video and stars for every repo.

Updates data/meta.json in place. By default only videos missing from meta.json are
fetched from YouTube; pass --all to re-check every video (do this occasionally, not
daily, or YouTube will rate-limit you). Repo stars are always refreshed.

A video that is gone (removed, private, or blocked) or a repo that is missing,
archived, or renamed makes the script exit non-zero. Temporary errors such as rate
limits keep the previous values.

    python3 scripts/refresh_meta.py [--all]
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "data/meta.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"


class Gone(Exception):
    """The resource is permanently unavailable."""


def get(url, headers=None):
    request = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US", **(headers or {})})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.geturl(), response.read().decode("utf-8", "replace")


def video(video_id):
    # oEmbed answers 200 only for public videos (401 means public with embedding disabled).
    watch = f"https://www.youtube.com/watch?v={video_id}"
    try:
        get("https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(watch, safe=""))
    except urllib.error.HTTPError as error:
        if error.code in (400, 403, 404):
            raise Gone(f"video {video_id} is unavailable (oEmbed {error.code})") from error
        if error.code != 401:
            raise
    request = urllib.request.Request(
        "https://www.youtube.com/youtubei/v1/player?prettyPrint=false",
        data=json.dumps({"videoId": video_id, "context": {"client": {"clientName": "WEB", "clientVersion": "2.20240101.00.00", "hl": "en"}}}).encode(),
        headers={"User-Agent": UA, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        details = json.loads(response.read()).get("videoDetails", {})
    if details.get("videoId") != video_id or not details.get("lengthSeconds"):
        raise RuntimeError(f"video {video_id}: no details from YouTube")
    return {"title": details["title"], "channel": details["author"], "seconds": int(details["lengthSeconds"])}


def repo(name):
    headers = {"Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    try:
        _, body = get(f"https://api.github.com/repos/{name}", headers)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            raise Gone(f"repo {name} not found") from error
        raise
    data = json.loads(body)
    if data.get("archived"):
        raise Gone(f"repo {name} is archived")
    if data["full_name"] != name:
        raise Gone(f"repo {name} was renamed to {data['full_name']}; update data/roadmaps")
    return {"stars": data["stargazers_count"], "description": data.get("description") or ""}


def refresh(kind, keys, fetch, old, refetch, failures):
    fresh = {}
    for key in keys:
        if key in old.get(kind, {}) and not refetch:
            fresh[key] = old[kind][key]
            continue
        try:
            fresh[key] = fetch(key)
        except Gone as error:
            failures.append(str(error))
        except Exception as error:  # noqa: BLE001 - temporary: keep what we had
            if key in old.get(kind, {}):
                fresh[key] = old[kind][key]
                print(f"warning: kept old data for {key}: {error}", file=sys.stderr)
            else:
                failures.append(f"{key}: {error}")
        time.sleep(0.4 if kind == "videos" else 0)
    return fresh


def main():
    roadmaps = [json.loads(p.read_text()) for p in sorted((ROOT / "data/roadmaps").glob("*.json"))]
    videos = sorted({step["video"] for r in roadmaps for step in r["steps"]})
    repos = sorted({step["repo"] for r in roadmaps for step in r["steps"] if step.get("repo")})
    old = json.loads(META.read_text()) if META.exists() else {}
    failures = []
    meta = {
        "videos": refresh("videos", videos, video, old, "--all" in sys.argv, failures),
        "repos": refresh("repos", repos, repo, old, True, failures),
    }
    META.write_text(json.dumps(meta, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(meta['videos'])}/{len(videos)} videos, {len(meta['repos'])}/{len(repos)} repos")
    if failures:
        sys.exit("\n".join(failures))


if __name__ == "__main__":
    main()
