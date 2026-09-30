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
            self.assertIn("core_16_amendment_ratification.md", index)
            self.assertNotIn("](../core_", index)
            corpus_index = (out / "corpus_index.md").read_text(encoding="utf-8")
            self.assertIn("](core_00_preamble.md)", corpus_index)
            self.assertTrue((out / "_config.yml").is_file())
            self.assertIn("jekyll-redirect-from", (out / "_config.yml").read_text(encoding="utf-8"))

    def test_relative_link_targets(self) -> None:
        text = (
            "[a](b.md#x) [c](../d/e.md) [f](<g h.md>) [ext](https://x.org/y.md) "
            "[frag](#only) [root](/abs.md) [t](k.md \"title\")\n"
            "[ref]: ref.md#anchor\n"
        )
        got = generate_pages_site.relative_link_targets("sub/page.md", text)
        self.assertEqual(sorted(got), ["d/e.md", "sub/b.md", "sub/g h.md", "sub/k.md", "sub/ref.md"])

    def test_link_gaps_are_filled_without_touching_copies(self) -> None:
        with tempfile.TemporaryDirectory(prefix="pages-site-gaps-") as tmp:
            root = Path(tmp) / "repo"
            (root / "docs").mkdir(parents=True)
            (root / "docs/index.md").write_text("# Door\n", encoding="utf-8")
            (root / "extra").mkdir()
            (root / "extra/notes.md").write_text("# Notes\n", encoding="utf-8")
            (root / "extra/pack").mkdir()
            (root / "extra/pack/a.md").write_text("# A\n", encoding="utf-8")
            (root / "extra/schema.json").write_text("{}\n", encoding="utf-8")
            page = (
                "# Page\n[n](extra/notes.md#s) [p](extra/pack/) [j](extra/schema.json) "
                "[gone](nowhere.md) [ci](.github/x.yml)\n"
            )
            (root / "page.md").write_text(page, encoding="utf-8")
            (root / ".github").mkdir()
            (root / ".github/x.yml").write_text("x: 1\n", encoding="utf-8")
            out = Path(tmp) / "site"
            out.mkdir()
            (out / "page.md").write_text(page, encoding="utf-8")
            copied, unresolved = generate_pages_site.fill_link_gaps(root, out, {"page.md"})
            self.assertEqual((out / "page.md").read_text(encoding="utf-8"), page)
            stub = (out / "extra/notes.md").read_text(encoding="utf-8")
            self.assertIn("redirect_to: " + generate_pages_site.BLOB + "extra/notes.md", stub)
            dir_stub = (out / "extra/pack/index.md").read_text(encoding="utf-8")
            self.assertIn("redirect_to: " + generate_pages_site.TREE + "extra/pack", dir_stub)
            self.assertEqual(copied, ["extra/schema.json"])
            self.assertEqual((out / "extra/schema.json").read_text(encoding="utf-8"), "{}\n")
            self.assertEqual(set(unresolved), {"missing", "excluded"})
            self.assertIn("nowhere.md", unresolved["missing"])
            self.assertIn(".github/x.yml", unresolved["excluded"])

    def test_real_corpus_leaves_only_known_gaps(self) -> None:
        with tempfile.TemporaryDirectory(prefix="pages-site-real-") as tmp:
            out = Path(tmp) / "site"
            rels, unresolved = generate_pages_site.assemble_with_report(ROOT, out)
            self.assertEqual(generate_pages_site.copies_match(ROOT, out, rels), [])
            self.assertTrue((out / "implementation/PRE_PUBLICATION_SPEC.md").is_file())
            self.assertEqual(set(unresolved) - {"missing", "excluded", "outside"}, set())


if __name__ == "__main__":
    unittest.main()
