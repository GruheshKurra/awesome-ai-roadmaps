"""Check daily publication boundaries without using an AI service or GitHub writes."""

import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch
from urllib.request import Request

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from daily import audit as link_audit
from daily import run


class DailyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_before_evening_does_not_reserve(self):
        self.assertIsNone(run.reserve(self.root, datetime(2026, 9, 20, 18, 44, tzinfo=run.TIMEZONE)))
        self.assertFalse((self.root / 'runs').exists())

    def test_date_guard_includes_failed_attempts(self):
        evening = datetime(2026, 9, 20, 18, 45, tzinfo=run.TIMEZONE)
        record = run.reserve(self.root, evening)
        self.assertIsNotNone(record)
        run.write_json(record / 'result.json', {'status': 'failed'})
        self.assertIsNone(run.reserve(self.root, evening.replace(hour=21)))
        self.assertIsNotNone(run.reserve(self.root, evening.replace(day=21)))

    def test_london_time_in_winter_and_summer(self):
        for month, utc_hour in ((1, 18), (7, 17)):
            with tempfile.TemporaryDirectory() as directory:
                at_due = datetime.fromisoformat(f'2026-{month:02}-20T{utc_hour}:45:00+00:00')
                self.assertIsNotNone(run.reserve(Path(directory), at_due))

    def test_publication_paths(self):
        for name in ('README.md', '_config.yml', 'tracks/mlops/README.md', 'assets/css/site.css'):
            self.assertTrue(run.allowed(name), name)
        for name in ('AGENTS.md', '.env', 'scripts/daily/run.py', '.github/workflows/pages.yml',
                     'tracks/../../README.md', 'tracks/mlops/notes.md', 'LICENSE'):
            self.assertFalse(run.allowed(name), name)

    def git_fixture(self):
        # Test identity is passed per command, never written to any git configuration.
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        (self.root / 'README.md').write_text('# Catalog\n')
        subprocess.run(['git', '-C', str(self.root), 'add', 'README.md'], check=True)
        subprocess.run(['git', '-C', str(self.root), '-c', 'user.name=Fixture',
                        '-c', 'user.email=fixture@example.invalid', 'commit', '-qm', 'Fixture'], check=True)
        return run.command(['git', 'rev-parse', 'HEAD'], self.root)

    def test_content_edits_are_allowed(self):
        base = self.git_fixture()
        (self.root / 'README.md').write_text('# Improved catalog\n')
        self.assertEqual(run.check_changes(self.root, base), ['README.md'])

    def test_jekyll_execution_settings_cannot_change(self):
        self.git_fixture()
        config = self.root / '_config.yml'
        config.write_text('title: Original\nplugins: []\n')
        run.command(['git', 'add', '_config.yml'], self.root)
        run.command(['git', '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                     'commit', '-m', 'Add configuration'], self.root)
        base = run.command(['git', 'rev-parse', 'HEAD'], self.root)
        config.write_text('title: Better title\nplugins: []\n')
        self.assertEqual(run.check_changes(self.root, base), ['_config.yml'])
        config.write_text('title: Better title\nplugins: []\nplugins_dir: tasks\n')
        with self.assertRaisesRegex(RuntimeError, 'execution or deployment configuration'):
            run.check_changes(self.root, base)

    def test_protected_and_ignored_files_block_publication(self):
        base = self.git_fixture()
        (self.root / '.gitignore').write_text('_plugins/\n')
        (self.root / '_plugins').mkdir()
        (self.root / '_plugins/hidden.rb').write_text('# hidden executable code\n')
        with self.assertRaisesRegex(RuntimeError, 'Unexpected candidate file'):
            run.check_changes(self.root, base)

    def test_deletion_and_symlink_block_publication(self):
        base = self.git_fixture()
        (self.root / 'README.md').unlink()
        with self.assertRaisesRegex(RuntimeError, 'deletion, or symlink'):
            run.check_changes(self.root, base)
        (self.root / 'README.md').symlink_to(self.root / 'missing')
        with self.assertRaisesRegex(RuntimeError, 'deletion, or symlink'):
            run.check_changes(self.root, base)

    def test_more_than_one_new_track_blocks_publication(self):
        base = self.git_fixture()
        for slug in ('one', 'two'):
            path = self.root / 'tracks' / slug
            path.mkdir(parents=True)
            (path / 'README.md').write_text('# New track\n')
        with self.assertRaisesRegex(RuntimeError, 'At most one new track'):
            run.check_changes(self.root, base)

    def test_new_links_require_evidence(self):
        track = self.root / 'tracks/example'
        track.mkdir(parents=True)
        (track / 'README.md').write_text('| 1 | Concept | | [Paper](https://example.com/paper) |\n')
        with self.assertRaisesRegex(RuntimeError, 'lack direct free-access evidence'):
            run.verify_new_sources(self.root, {})
        evidence = {'https://example.com/paper': {'verified_free': True,
                    'note': 'Opened the complete paper without login; the author provides the PDF.'}}
        run.write_json(self.root / 'tasks/source-evidence.json', evidence)
        with patch.object(run, 'audit', return_value={'https://example.com/paper': {'status': 'unavailable'}}):
            with self.assertRaisesRegex(RuntimeError, 'returned unavailable'):
                run.verify_new_sources(self.root, {})

    def test_remote_race_stops_before_commit_or_push(self):
        with patch.object(run, 'command', side_effect=['', 'someone-elses-commit']) as command:
            with self.assertRaisesRegex(RuntimeError, 'Remote main changed'):
                run.publish(self.root, 'base', ['README.md'], '2026-09-20')
            self.assertEqual(command.call_count, 2)

    def test_editor_failure_never_publishes(self):
        record = self.root / 'runs/2026-09-20'
        record.mkdir(parents=True)
        def fake_clone(args, cwd, **kwargs):
            if args[1] == 'clone':
                (record / 'checkout/tracks/example').mkdir(parents=True)
                (record / 'checkout/tracks/example/README.md').write_text('# Example\n')
            return 'base'
        with patch.object(run, 'command', side_effect=fake_clone), \
             patch.object(run, 'audit', return_value={}), \
             patch.object(run, 'metrics', return_value={}), \
             patch.object(run, 'run_editor', side_effect=RuntimeError('editor failed')), \
             patch.object(run, 'publish') as publish:
            with self.assertRaisesRegex(RuntimeError, 'editor failed'):
                run.execute(self.root, self.root, record)
            publish.assert_not_called()
        self.assertEqual(run.read_json(record / 'result.json', {})['status'], 'failed')

    def test_private_network_urls_are_rejected(self):
        with patch.object(link_audit.socket, 'getaddrinfo', return_value=[(2, 1, 6, '', ('127.0.0.1', 80))]):
            with self.assertRaisesRegex(ValueError, 'Private or reserved'):
                link_audit.public_url('http://example.com/private')
        with self.assertRaises(ValueError):
            link_audit.public_url('file:///etc/passwd')

    def test_permanent_redirects_keep_public_destination_checks(self):
        with patch.object(link_audit, 'public_url') as validate:
            request = link_audit.PublicRedirect().redirect_request(
                Request('https://example.com/old'), None, 308, 'Permanent redirect', {},
                'https://example.com/new')
            self.assertEqual(request.full_url, 'https://example.com/new')
            validate.assert_called_once_with('https://example.com/new')

    def test_only_resource_table_urls_are_audited(self):
        folder = self.root / 'tracks/example'
        folder.mkdir(parents=True)
        (folder / 'README.md').write_text('[Intro](https://example.com/intro)\n| 1 | Topic | | [Paper](https://example.com/paper) |\n')
        self.assertEqual(list(link_audit.resource_links(self.root)), ['https://example.com/paper'])


if __name__ == '__main__':
    unittest.main()
