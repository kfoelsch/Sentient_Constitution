#!/usr/bin/env python3
"""Regression checks for section migration planning and link resolution."""
import subprocess
import json
import sys
import tempfile
import unittest
from pathlib import Path
from section_migration import make_plan


class SectionMigrationTests(unittest.TestCase):
    def test_move_retargets_qualified_and_local_links_and_reports_unlinked(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            (root / 'part_a.md').write_text('<a id="1-first"></a>\n### 1. First\n\n<a id="2-moving"></a>\n### 2. Moving\n\n[§1 First](#1-first) and §2 Moving.\n\nEND\n', encoding='utf-8')
            (root / 'part_b.md').write_text('<a id="3-last"></a>\n### 3. Last\n', encoding='utf-8')
            (root / 'reader.md').write_text('[§2 Moving](part_a.md#2-moving) and [§2 Other](other.md#2-other)\n', encoding='utf-8')
            (root / 'other.md').write_text('### 2. Other\n', encoding='utf-8')
            subprocess.run(['git', 'add', '.'], cwd=root, check=True)
            spec = {'chapter_files': ['part_a.md', 'part_b.md'], 'sections': {'2': {'number': '3', 'file': 'part_b.md'}, '3': {'number': '2'}}, 'moves': [{'source': 'part_a.md', 'destination': 'part_b.md', 'start': '<a id="2-moving"></a>', 'end': 'END', 'before': '<a id="3-last"></a>'}]}
            outputs, report = make_plan(root, spec)
            self.assertIn('[§3 Moving](part_b.md#3-moving)', outputs['reader.md'])
            self.assertIn('[§2 Other](other.md#2-other)', outputs['reader.md'])
            self.assertIn('[§1 First](part_a.md#1-first)', outputs['part_b.md'])
            self.assertIn('### 3. Moving', outputs['part_b.md'])
            self.assertIn('### 2. Last', outputs['part_b.md'])
            self.assertTrue(any(x['kind'] == 'unlinked citation or range' for x in report['review']))
            self.assertIn('### 2. Moving', (root / 'part_a.md').read_text())

    def test_explicit_alias_is_retargeted(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            (root / 'a.md').write_text('<a id="2-legacy"></a>\n### 2. Moving\n', encoding='utf-8')
            (root / 'reader.md').write_text('[§2 Moving](a.md#2-legacy)\n', encoding='utf-8')
            subprocess.run(['git', 'add', '.'], cwd=root, check=True)
            spec = {'chapter_files': ['a.md'], 'sections': {'2': {'number': '3'}}, 'aliases': {'a.md#2-legacy': '3-custom'}}
            outputs, _ = make_plan(root, spec)
            self.assertIn('id="3-custom"', outputs['a.md'])
            self.assertIn('(a.md#3-custom)', outputs['reader.md'])

    def test_write_refuses_dirty_tracked_tree(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            (root / 'a.md').write_text('### 1. First\n', encoding='utf-8')
            subprocess.run(['git', 'add', 'a.md'], cwd=root, check=True)
            (root / 'spec.json').write_text(json.dumps({'chapter_files': ['a.md'], 'sections': {'1': {'number': '2'}}}), encoding='utf-8')
            script = Path(__file__).with_name('section_migration.py')
            result = subprocess.run([sys.executable, str(script), '--root', str(root), '--spec', str(root / 'spec.json'), '--write'], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('refusing to write', result.stderr)
            self.assertEqual((root / 'a.md').read_text(), '### 1. First\n')

    def test_rejects_ambiguous_move_marker(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            (root / 'a.md').write_text('START\n### 1. First\nEND\nSTART\nEND\n', encoding='utf-8')
            spec = {'chapter_files': ['a.md'], 'sections': {}, 'moves': [{'source': 'a.md', 'destination': 'a.md', 'start': 'START', 'end': 'END', 'before': 'END'}]}
            with self.assertRaises(ValueError):
                make_plan(root, spec)

if __name__ == '__main__':
    unittest.main()
