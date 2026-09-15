#!/usr/bin/env python3
"""Tests for tools/generate_pages_site.py."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import generate_pages_site

ROOT = Path(__file__).resolve().parents[1]


class PagesSiteTests(unittest.TestCase):
    def test_publish_list_includes_core_and_first_hour(self) -> None:
        rels = generate_pages_site.publish_list(ROOT)
        self.assertIn("core_00_preamble.md", rels)
        self.assertIn("START_HERE.md", rels)
        self.assertIn("implementation/FAQ.md", rels)
        self.assertIn("implementation/adoption/easy_entry/README.md", rels)
        self.assertNotIn("implementation/adoption/easy_entry/_TEMPLATE.md", rels)

    def test_assemble_copies_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory(prefix="pages-site-test-") as tmp:
            out = Path(tmp) / "site"
            rels = generate_pages_site.assemble(ROOT, out)
            errors = generate_pages_site.copies_match(ROOT, out, rels)
            self.assertEqual(errors, [])
            preamble = (out / "core_00_preamble.md").read_bytes()
            self.assertEqual(preamble, (ROOT / "core_00_preamble.md").read_bytes())
            index = (out / "index.md").read_text(encoding="utf-8")
            self.assertIn("renders the same files", index)
            self.assertIn("core_15_amendment_ratification.md", index)
            self.assertNotIn("](../core_", index)
            corpus_index = (out / "corpus_index.md").read_text(encoding="utf-8")
            self.assertIn("](core_00_preamble.md)", corpus_index)
            self.assertTrue((out / "_config.yml").is_file())


if __name__ == "__main__":
    unittest.main()
