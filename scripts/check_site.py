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
    origin = re.search(r"^url: ([^\n]+)$", config, re.M)[1].strip().strip('"\'').rstrip("/")
    base = re.search(r"^baseurl:[ \t]*([^\n]*)$", config, re.M)[1].strip().strip('"\'').rstrip("/")
    expected_nav = [f"{base}/tracks/{slug}/" for slug in slugs]
    paths = ["", "contributing/"] + [f"tracks/{slug}/" for slug in slugs] + ["404.html"]
    descriptions = []
    sitemap = ElementTree.parse(site / "sitemap.xml")
    sitemap_urls = {element.text for element in sitemap.iter()
                    if element.tag.endswith("}loc")}
    parsed = {}

    def parse(file):
        if file not in parsed:
            parsed[file] = Page(file.read_text())
        return parsed[file]

    def check_link(url, canonical, name):
        resolved = urlsplit(urljoin(canonical, url))
        if resolved.netloc != urlsplit(origin).netloc:
            return
        if not resolved.path.startswith(base + "/"):
            check(False, f"{name}: link escapes site base: {url}")
            return
        local = unquote(resolved.path.removeprefix(base + "/"))
        target = (site / local).resolve()
        if not target.is_relative_to(site.resolve()):
            check(False, f"{name}: link escapes artifact: {url}")
            return
        if resolved.path.endswith("/"):
            target /= "index.html"
        check(target.is_file(), f"{name}: broken internal link: {url}")
        # Text fragments (#:~:text=...) are browser directives, not element IDs.
        fragment = unquote(resolved.fragment.split(":~:", 1)[0])
        if fragment and target.is_file() and target.suffix == ".html":
            ids = {attrs.get("id") for _, attrs in parse(target).tags}
            anchors = {attrs.get("name") for attrs in parse(target).elements("a")}
            check(fragment in ids | anchors, f"{name}: broken internal anchor: {url}")

    for path in paths:
        name = path or "home"
        file = site / path if path.endswith(".html") else site / path / "index.html"
        check(file.is_file(), f"{name}: missing HTML")
        if not file.is_file():
            continue
        text = file.read_text()
        page = parse(file.resolve())
        canonical = f"{origin}{base}/{path}"
        check(text.lower().startswith("<!doctype html>"), f"{name}: not an HTML document")
        check(len(page.elements("h1")) == 1, f"{name}: expected one h1")
        check(len(page.elements("title")) == 1, f"{name}: expected one title")
        check(len(page.elements("main", id="content")) == 1, f"{name}: missing main content landmark")
        check(bool(page.elements("html", lang="en")), f"{name}: missing document language")
        ids = [attrs["id"] for _, attrs in page.tags if "id" in attrs]
        check(len(ids) == len(set(ids)), f"{name}: duplicate element IDs")
        check(page.elements("link", rel="canonical") == [{"rel": "canonical", "href": canonical}],
              f"{name}: wrong canonical URL")
        if path == "404.html":
            check(canonical not in sitemap_urls, "404 page must not be in sitemap")
        else:
            check(canonical in sitemap_urls, f"{name}: absent from sitemap")
        metadata = page.elements("meta", name="description")
        check(len(metadata) == 1 and bool(metadata[0].get("content")), f"{name}: missing description")
        if metadata:
            descriptions.append(metadata[0].get("content"))
        for property_name in ("og:title", "og:description", "og:image", "og:image:alt"):
            values = page.elements("meta", property=property_name)
            check(len(values) == 1 and bool(values[0].get("content")), f"{name}: missing {property_name}")
            if property_name == "og:image" and values and values[0].get("content"):
                check_link(values[0]["content"], canonical, name)
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
            if tag == "img":
                check("alt" in attrs, f"{name}: image is missing alt text")
            for attribute in ("aria-controls", "aria-labelledby", "aria-describedby"):
                for reference in attrs.get(attribute, "").split():
                    check(reference in ids, f"{name}: {attribute} points to missing ID {reference}")
            url = attrs.get("href") if tag in ("a", "link") else attrs.get("src")
            if not url:
                continue
            scheme = urlsplit(url).scheme.lower()
            check(scheme in ("", "http", "https", "mailto", "tel", "data"),
                  f"{name}: unsafe URL scheme: {scheme}")
            if scheme not in ("", "http", "https"):
                continue
            check_link(url, canonical, name)

    check(len(descriptions) == len(set(descriptions)), "Pages share duplicate descriptions")
    check(not list(site.rglob("*.md")), "Raw Markdown must not be deployed")
    check(not (site / "scripts").exists(), "Maintenance scripts must not be deployed")
    for private in ("AGENTS.html", "LearningPreferences.html", "tracker.html", "tasks", ".git", ".github"):
        check(not (site / private).exists(), f"Private path must not be deployed: {private}")
    for file in site.rglob("*"):
        check(not (file.name.startswith((".env", "credentials.", "secrets.")) or
                   file.suffix in (".pem", ".key")), f"Secret-bearing path must not be deployed: {file.relative_to(site)}")
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
