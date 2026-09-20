"""Publication checks against a small built-site fixture, without Jekyll or network."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("check_site", Path(__file__).parents[1] / "check_site.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SiteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.site = self.root / "site"
        self.site.mkdir()
        self.make_site("/roadmaps")

    def make_site(self, base):
        (self.root / "README.md").write_text("## Contents\n| [Example](tracks/example/) | Intro | 5 |\n")
        (self.root / "_config.yml").write_text(f"url: https://example.com\nbaseurl: {base}\n")
        urls = []
        for path in ("", "contributing/", "tracks/example/", "404.html"):
            file = self.site / path if path.endswith(".html") else self.site / path / "index.html"
            file.parent.mkdir(parents=True, exist_ok=True)
            canonical = f"https://example.com{base}/{path}"
            if path != "404.html":
                urls.append(f"<url><loc>{canonical}</loc></url>")
            current = ' aria-current="page"' if path.startswith("tracks/") else ""
            file.write_text(f'''<!DOCTYPE html><html lang="en"><head>
<title>Example</title><link rel="canonical" href="{canonical}">
<meta name="description" content="Description for {path or 'home'}">
<meta property="og:title" content="Example"><meta property="og:description" content="Example">
<meta property="og:image" content="https://example.com{base}/image.png">
<meta property="og:image:alt" content="Example"></head><body>
<a href="#content">Skip</a><a class="back" href="{base}/">Home</a>
<a class="track-link" href="{base}/tracks/example/"{current}>Example</a>
<main id="content"><h1>Example</h1><table></table></main></body></html>''')
        (self.site / "sitemap.xml").write_text('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(urls) + '</urlset>')
        (self.site / "robots.txt").write_text("User-agent: *\nAllow: /\n")
        (self.site / "image.png").touch()

    def replace(self, old, new, path="index.html"):
        file = self.site / path
        text = file.read_text()
        self.assertIn(old, text)
        file.write_text(text.replace(old, new))

    def check(self):
        MODULE.check_site(self.site, self.root)

    def test_valid_site(self):
        self.check()

    def test_empty_baseurl(self):
        self.make_site("")
        self.check()

    def test_missing_anchor(self):
        self.replace('href="#content"', 'href="#missing"')
        with self.assertRaisesRegex(ValueError, "broken internal anchor"):
            self.check()

    def test_cross_page_anchor(self):
        self.replace('href="#content"', 'href="tracks/example/#content"')
        self.check()
        self.replace('tracks/example/#content', 'tracks/example/#missing')
        with self.assertRaisesRegex(ValueError, "broken internal anchor"):
            self.check()

    def test_text_fragment(self):
        self.replace('href="#content"', 'href="#:~:text=Example"')
        self.check()

    def test_duplicate_ids(self):
        self.replace('<h1>', '<h1 id="content">')
        with self.assertRaisesRegex(ValueError, "duplicate element IDs"):
            self.check()

    def test_aria_reference(self):
        self.replace('<table>', '<table aria-labelledby="missing">')
        with self.assertRaisesRegex(ValueError, "points to missing ID"):
            self.check()

    def test_missing_main(self):
        self.replace('<main id="content">', '<article id="content">')
        with self.assertRaisesRegex(ValueError, "main content landmark"):
            self.check()

    def test_404_links_are_checked(self):
        self.replace('href="#content"', 'href="missing.html"', "404.html")
        with self.assertRaisesRegex(ValueError, "404.html: broken internal link"):
            self.check()

    def test_unsafe_scheme(self):
        self.replace('href="#content"', 'href="javascript:alert(1)"')
        with self.assertRaisesRegex(ValueError, "unsafe URL scheme"):
            self.check()

    def test_missing_social_image(self):
        (self.site / "image.png").unlink()
        with self.assertRaisesRegex(ValueError, "broken internal link"):
            self.check()

    def test_image_without_alt(self):
        self.replace('<table>', '<img src="image.png"><table>')
        with self.assertRaisesRegex(ValueError, "missing alt text"):
            self.check()

    def test_artifact_path_escape(self):
        self.replace('href="#content"', 'href="/roadmaps/%2e%2e/README.md"')
        with self.assertRaisesRegex(ValueError, "link escapes artifact"):
            self.check()

    def test_private_artifacts(self):
        for name in ("tracker.html", "AGENTS.html", "LearningPreferences.html", "notes.md", ".env.production", "test.key"):
            with self.subTest(name=name):
                file = self.site / name
                file.touch()
                with self.assertRaises(ValueError):
                    self.check()
                file.unlink()


if __name__ == "__main__":
    unittest.main()
