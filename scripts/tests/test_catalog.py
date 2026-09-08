"""Regression checks for publication gates and derived catalog updates."""

import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source = Path(__file__).resolve().parents[2]
        for file in ("README.md", "_config.yml", ".gitignore", "tracker.md"):
            shutil.copyfile(source / file, self.root / file)
        shutil.copytree(source / "tracks", self.root / "tracks")
        (self.root / "scripts").mkdir()
        shutil.copyfile(source / "scripts/catalog.rb", self.root / "scripts/catalog.rb")

    def run_catalog(self, *args):
        return subprocess.run([os.environ.get("RUBY", "ruby"), str(self.root / "scripts/catalog.rb"), *args],
                              capture_output=True, text=True)

    def replace(self, path, old, new):
        file = self.root / path
        text = file.read_text()
        self.assertIn(old, text)
        file.write_text(text.replace(old, new, 1))

    def test_current_catalog_and_idempotent_sync(self):
        self.assertEqual(self.run_catalog().returncode, 0)
        before = {p: (self.root / p).read_bytes() for p in ("README.md", "_config.yml", "tracker.md")}
        self.assertEqual(self.run_catalog("--write").returncode, 0)
        self.assertEqual(before, {p: (self.root / p).read_bytes() for p in before})

    def test_stale_counts_and_queue_are_repaired(self):
        totals = re.search(r"\d+ tracks, \d+ steps", (self.root / "README.md").read_text())[0]
        self.replace("README.md", totals, "1 tracks, 1 steps")
        self.replace("tracker.md", "[x] `evals-safety`", "[ ] `evals-safety`")
        self.assertNotEqual(self.run_catalog().returncode, 0)
        self.assertEqual(self.run_catalog("--write").returncode, 0)
        self.assertEqual(self.run_catalog().returncode, 0)
        self.assertIn(totals, (self.root / "README.md").read_text())
        self.assertIn("[x] `evals-safety`", (self.root / "tracker.md").read_text())

    def test_unfinished_track_blocks_writes(self):
        self.replace("tracks/llms/README.md", "Status: done", "Status: filling")
        before = (self.root / "_config.yml").read_bytes()
        result = self.run_catalog("--write")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("only done tracks", result.stderr)
        self.assertEqual(before, (self.root / "_config.yml").read_bytes())

    def test_duplicate_track_is_rejected(self):
        file = self.root / "README.md"
        row = next(line for line in file.read_text().splitlines() if line.startswith("| [LLMs]"))
        self.replace("README.md", row, row + "\n" + row)
        self.assertIn("duplicate tracks", self.run_catalog().stderr)

    def test_step_gap_is_rejected(self):
        self.replace("tracks/llms/README.md", "| 2 |", "| 99 |")
        self.assertIn("steps must be sequential", self.run_catalog().stderr)

    def test_escaped_pipe_in_link_label_is_supported(self):
        path = self.root / "tracks/llms/README.md"
        text = path.read_text()
        row = next(line for line in text.splitlines() if line.startswith("| 1 |"))
        path.write_text(text.replace(row, r"| 1 | Introduction | **[Video \| introduction](https://www.youtube.com/watch?v=abcdefghijk)** | |"))
        self.assertEqual(self.run_catalog().returncode, 0)

    def test_missing_resource_is_rejected(self):
        path = self.root / "tracks/llms/README.md"
        text = path.read_text()
        row = next(line for line in text.splitlines() if line.startswith("| 1 |"))
        path.write_text(text.replace(row, "| 1 | Introduction | | |"))
        self.assertIn("missing resource", self.run_catalog().stderr)

    def test_multiple_readings_in_one_cell_are_rejected(self):
        path = self.root / "tracks/llms/README.md"
        text = path.read_text()
        row = next(line for line in text.splitlines() if line.startswith("| 1 |"))
        path.write_text(text.replace(row, "| 1 | Introduction | | [One](https://example.com/one) [Two](https://example.com/two) |"))
        self.assertIn("expected one reading link", self.run_catalog().stderr)

    def test_unbolded_youtube_link_is_rejected(self):
        path = self.root / "tracks/llms/README.md"
        text = path.read_text()
        row = next(line for line in text.splitlines() if line.startswith("| 1 |"))
        path.write_text(text.replace(row, "| 1 | Introduction | [Video](https://www.youtube.com/watch?v=abcdefghijk) | |"))
        self.assertIn("expected one bold YouTube watch link", self.run_catalog().stderr)

    def test_unlisted_folder_is_rejected(self):
        folder = self.root / "tracks/unpublished"
        folder.mkdir()
        (folder / "README.md").write_text("# Unpublished\n")
        self.assertIn("folders and README Contents disagree", self.run_catalog().stderr)


if __name__ == "__main__":
    unittest.main()
