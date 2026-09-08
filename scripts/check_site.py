"""Check a built Pages artifact using only the Python standard library."""

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def elements(self, tag, **attrs):
        return [data for name, data in self.tags
                if name == tag and all(data.get(key) == value for key, value in attrs.items())]


def check_site(site, root):
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    readme = (root / "README.md").read_text()
    contents = readme.split("## Contents\n", 1)[1].split("\n## ", 1)[0]
    slugs = re.findall(r"\]\(tracks/([a-z0-9-]+)/\)", contents)
    config = (root / "_config.yml").read_text()
    origin = re.search(r"^url: (.+)$", config, re.M)[1].rstrip("/")
    base = re.search(r"^baseurl: (.*)$", config, re.M)[1].rstrip("/")
    expected_nav = [f"{base}/tracks/{slug}/" for slug in slugs]
    paths = ["", "contributing/"] + [f"tracks/{slug}/" for slug in slugs]
    descriptions = []
    sitemap = ElementTree.parse(site / "sitemap.xml")
    sitemap_urls = {element.text for element in sitemap.iter()
                    if element.tag.endswith("}loc")}

    for path in paths:
        name = path or "home"
        file = site / path / "index.html"
        check(file.is_file(), f"{name}: missing HTML")
        if not file.is_file():
            continue
        text = file.read_text()
        page = Page(text)
        canonical = f"{origin}{base}/{path}"
        check(text.lower().startswith("<!doctype html>"), f"{name}: not an HTML document")
        check(len(page.elements("h1")) == 1, f"{name}: expected one h1")
        check(len(page.elements("title")) == 1, f"{name}: expected one title")
        check(page.elements("link", rel="canonical") == [{"rel": "canonical", "href": canonical}],
              f"{name}: wrong canonical URL")
        check(canonical in sitemap_urls, f"{name}: absent from sitemap")
        metadata = page.elements("meta", name="description")
        check(len(metadata) == 1 and bool(metadata[0].get("content")), f"{name}: missing description")
        if metadata:
            descriptions.append(metadata[0].get("content"))
        for property_name in ("og:title", "og:description", "og:image", "og:image:alt"):
            check(bool(page.elements("meta", property=property_name)), f"{name}: missing {property_name}")
        for data in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
            json.loads(data)
        nav = [attrs for tag, attrs in page.tags
               if tag == "a" and "track-link" in attrs.get("class", "").split()]
        check([attrs.get("href") for attrs in nav] == expected_nav, f"{name}: sidebar/catalog mismatch")
        if path:
            check(bool(page.elements("a", href=f"{base}/", **{"class": "back"})), f"{name}: missing Home link")
        if path.startswith("tracks/"):
            current = [attrs.get("href") for attrs in nav if attrs.get("aria-current") == "page"]
            check(current == [f"{base}/{path}"], f"{name}: wrong highlighted track")
            check(bool(page.elements("table")), f"{name}: missing resource table")
        for tag, attrs in page.tags:
            check(attrs.get("target") != "_blank", f"{name}: forbidden new-tab target")
            url = attrs.get("href") if tag in ("a", "link") else attrs.get("src")
            if not url or url.startswith(("mailto:", "data:", "javascript:")):
                continue
            resolved = urlsplit(urljoin(canonical, url))
            if resolved.netloc != urlsplit(origin).netloc:
                continue
            check(resolved.path.startswith(base + "/"), f"{name}: link escapes site base: {url}")
            local = unquote(resolved.path.removeprefix(base + "/"))
            target = site / local
            if resolved.path.endswith("/"):
                target /= "index.html"
            check(target.is_file(), f"{name}: broken internal link: {url}")

    check(len(descriptions) == len(set(descriptions)), "Pages share duplicate descriptions")
    check(not list(site.rglob("*.md")), "Raw Markdown must not be deployed")
    check(not (site / "scripts").exists(), "Maintenance scripts must not be deployed")
    check((site / "404.html").is_file(), "Missing 404 page")
    check((site / "robots.txt").is_file(), "Missing robots.txt")
    check(not any("tracker" in url or "README.md" in url for url in sitemap_urls),
          "Sitemap exposes tracker or raw Markdown")
    if errors:
        raise ValueError("\n".join(errors))
    print(f"Site verified: {len(paths)} pages, metadata, navigation, internal links, and sitemap.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 scripts/check_site.py <built-site-directory>")
    try:
        check_site(Path(sys.argv[1]).resolve(), Path(__file__).resolve().parents[1])
    except (ValueError, OSError, ElementTree.ParseError) as error:
        sys.exit(str(error))
