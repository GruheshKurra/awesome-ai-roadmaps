"""Tell IndexNow search engines (Bing, Yandex, Seznam, Naver) which site pages exist.

Run after scripts/build.py, usually from the deploy workflow:

    python3 scripts/indexnow.py

Reads _site/sitemap.xml and submits every URL in one request. Google does not use
IndexNow; it finds pages through the sitemap submitted in Search Console.
"""
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import INDEXNOW_KEY, ROOT, SITE_URL  # noqa: E402


def main():
    sitemap = (ROOT / "_site/sitemap.xml").read_text()
    urls = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    host = SITE_URL.split("/")[2]
    body = json.dumps({"host": host, "key": INDEXNOW_KEY, "keyLocation": f"{SITE_URL}/{INDEXNOW_KEY}.txt", "urlList": urls}).encode()
    request = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                     headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            print(f"IndexNow: submitted {len(urls)} URLs, HTTP {response.status}")
    except urllib.error.HTTPError as error:
        # 422 or 403 usually means the key file is not live yet; the next deploy retries.
        sys.exit(f"IndexNow: HTTP {error.code} {error.read().decode(errors='replace')[:200]}")


if __name__ == "__main__":
    main()
