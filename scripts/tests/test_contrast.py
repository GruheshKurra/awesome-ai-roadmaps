"""Keep the documented 6.5:1 text contrast floor in both color schemes."""

import re
import unittest
from pathlib import Path


def luminance(color):
    channels = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4
              for value in channels]
    return sum(value * weight for value, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


class ContrastTests(unittest.TestCase):
    def test_text_pairs_in_both_schemes(self):
        css = (Path(__file__).parents[2] / "assets/css/site.css").read_text()
        tokens = r"--([\w-]+): (#[a-f0-9]{6});"
        light = dict(re.findall(tokens, css.split("@media")[0]))
        dark_block = css.split("@media (prefers-color-scheme: dark)")[1].split("}", 1)[0]
        dark = light | dict(re.findall(tokens, dark_block))
        pairs = [(fg, bg) for fg in ("fg", "muted", "accent")
                 for bg in ("bg", "surface", "surface-hover")]
        pairs += [(fg, bg) for fg in ("sidebar-fg", "sidebar-muted", "sidebar-link", "sidebar-accent")
                  for bg in ("sidebar-bg", "sidebar-active-bg")]
        pairs += [("accent-contrast", "accent")]
        for scheme, palette in (("light", light), ("dark", dark)):
            for fg, bg in pairs:
                with self.subTest(scheme=scheme, foreground=fg, background=bg):
                    lower, upper = sorted((luminance(palette[fg]), luminance(palette[bg])))
                    self.assertGreaterEqual((upper + 0.05) / (lower + 0.05), 6.5)


if __name__ == "__main__":
    unittest.main()
