"""Search YouTube from the command line, for picking roadmap videos.

    python3 scripts/youtube_search.py "query one || query two" [results per query]

Prints: video ID | title | channel | length | views | age
"""
import json
import re
import subprocess
import sys
import urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"


def fetch(url):
    return subprocess.run(["curl", "-sL", "--max-time", "20", "-A", UA, "-H", "Accept-Language: en-US", url],
                          capture_output=True, text=True).stdout


def walk(o, out):
    if isinstance(o, dict):
        if "videoRenderer" in o:
            v = o["videoRenderer"]
            out.append({
                "id": v.get("videoId"),
                "title": "".join(r.get("text", "") for r in v.get("title", {}).get("runs", [])),
                "channel": "".join(r.get("text", "") for r in v.get("ownerText", {}).get("runs", [])),
                "length": v.get("lengthText", {}).get("simpleText", ""),
                "views": v.get("viewCountText", {}).get("simpleText", ""),
                "age": v.get("publishedTimeText", {}).get("simpleText", ""),
            })
        for x in o.values():
            walk(x, out)
    elif isinstance(o, list):
        for x in o:
            walk(x, out)


def search(q, n=6):
    h = fetch("https://www.youtube.com/results?search_query=" + urllib.parse.quote(q))
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", h)
    out = []
    if m:
        walk(json.loads(m.group(1)), out)
    return out[:n]


if __name__ == "__main__":
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    for q in sys.argv[1].split("||"):
        print(f"## {q.strip()}")
        for v in search(q.strip(), n):
            print(f"  {v['id']} | {v['title'][:80]} | {v['channel']} | {v['length']} | {v['views']} | {v['age']}")
