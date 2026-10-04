#!/usr/bin/env python3
"""Tests for local Markdown fragment resolution and audit scope."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from local_markdown_fragment_audit import (
    READER_ENTRY_DOCS,
    audit,
    fix_html_anchor_links,
    source_files,
)


class LocalMarkdownFragmentAuditTests(unittest.TestCase):
    def test_default_scope_includes_implementation_and_generated_docs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "core_10_standing_integration.md"
            target.write_text(
                '<a id="present"></a>\n# Chapter Ten\n',
                encoding="utf-8",
            )

            implementation = root / "implementation" / "guide.md"
            implementation.parent.mkdir()
            implementation.write_text(
                "[broken](../core_10_standing_integration.md#missing-implementation)\n",
                encoding="utf-8",
            )

            generated = root / "doc_architecture" / "generated" / "index.md"
            generated.parent.mkdir(parents=True)
            generated.write_text(
                "[broken](../../core_10_standing_integration.md#missing-generated)\n",
                encoding="utf-8",
            )

            paths = source_files(root)
            self.assertIn(implementation, paths)
            self.assertIn(generated, paths)

            findings = audit(root, paths, target.resolve())
            self.assertEqual(
                {finding.source for finding in findings},
                {
                    "implementation/guide.md",
                    "doc_architecture/generated/index.md",
                },
            )

    def test_all_targets_checked_when_no_target_selected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "core_00_preamble.md").write_text(
                '<a id="present"></a>\n# Present\n', encoding="utf-8"
            )
            source = root / "START_HERE.md"
            source.write_text(
                "[ok](core_00_preamble.md#present)\n"
                "[bad](core_00_preamble.md#absent)\n",
                encoding="utf-8",
            )
            findings = audit(root, [source], None)
            self.assertEqual([f.kind for f in findings], ["missing-fragment"])

    def test_reader_entry_docs_are_in_default_scope(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for name in READER_ENTRY_DOCS:
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                (root / name).write_text("# doc\n", encoding="utf-8")
            paths = source_files(root)
            for name in READER_ENTRY_DOCS:
                self.assertIn(root / name, paths, name)

    def test_footer_nav_rows_are_skipped(self) -> None:
        """footer_audit owns reading-chain footers and requires a bare filename."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "doc_architecture.md").write_text("# arch\n", encoding="utf-8")
            sub = root / "corpus_forum" / "cf_16.md"
            sub.parent.mkdir()
            sub.write_text(
                "**Next file:** [doc_architecture.md](doc_architecture.md)\n"
                "**Previous file:** [doc_architecture.md](doc_architecture.md)\n",
                encoding="utf-8",
            )
            self.assertEqual(audit(root, [sub], None), [])

            body = root / "corpus_forum" / "cf_17.md"
            body.write_text("See [arch](doc_architecture.md).\n", encoding="utf-8")
            self.assertEqual(
                [f.kind for f in audit(root, [body], None)], ["missing-file"]
            )

    def test_ellipsis_placeholder_targets_are_skipped(self) -> None:
        """doc_architecture.md illustrates path shapes; they are not real links."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "doc_architecture.md"
            source.write_text(
                "[shape](corpus_systems/cs_07_\u2026.md#\u2026)\n"
                "[shape](corpus_institutions/ci_23_\u2026.md)\n"
                "[real](missing_file.md#frag)\n",
                encoding="utf-8",
            )
            findings = audit(root, [source], None)
            self.assertEqual([f.target for f in findings], ["missing_file.md#frag"])

    def test_links_inside_code_spans_are_not_resolved(self) -> None:
        """Migration specs tabulate link syntax as an example, not as a link."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "spec.md"
            source.write_text(
                "| `[Chapter One, \u00a72 Purpose](#2-purpose)` | shape |\n"
                "Real prose [link](#also-absent) here.\n",
                encoding="utf-8",
            )
            findings = audit(root, [source], None)
            self.assertEqual([f.target for f in findings], ["#also-absent"])

    def test_custom_anchor_above_heading_must_link_heading_slug(self) -> None:
        """HTML-ANCHOR-LINK-01: the editor preview only follows heading anchors."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "core_05_band_continuity.md").write_text(
                '<a id="safety-constraint"></a>\n\n'
                "##### Safety (Constitutional Constraint)\n\n"
                '<a id="safety-constraint-a"></a>\n'
                "- **How to measure**\n",
                encoding="utf-8",
            )
            source = root / "START_HERE.md"
            source.write_text(
                "[flagged](core_05_band_continuity.md#safety-constraint)\n"
                "[heading](core_05_band_continuity.md#safety-constitutional-constraint)\n"
                "[sub-anchor](core_05_band_continuity.md#safety-constraint-a)\n",
                encoding="utf-8",
            )
            findings = audit(root, [source], None)
            self.assertEqual([f.kind for f in findings], ["html-anchor-link"])
            self.assertEqual(findings[0].line, 1)
            self.assertIn("#safety-constitutional-constraint", findings[0].detail)

    def test_duplicate_heading_slug_is_not_flagged(self) -> None:
        """A non-unique slug is a brittle target, so the stable id stays valid."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "core_05_band_continuity.md").write_text(
                '<a id="first"></a>\n## Repeated\n\n<a id="second"></a>\n## Repeated\n',
                encoding="utf-8",
            )
            source = root / "START_HERE.md"
            source.write_text(
                "[a](core_05_band_continuity.md#first)\n"
                "[b](core_05_band_continuity.md#second)\n",
                encoding="utf-8",
            )
            self.assertEqual(audit(root, [source], None), [])

    def test_fix_rewrites_only_whole_targets(self) -> None:
        """A target must not be rewritten inside a longer sibling on the same line."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "core_05_band_continuity.md").write_text(
                '<a id="x"></a>\n\n## Long Heading\n\n<a id="x-a"></a>\n- item\n',
                encoding="utf-8",
            )
            source = root / "START_HERE.md"
            source.write_text(
                "[t](core_05_band_continuity.md#x) [a](core_05_band_continuity.md#x-a)\n",
                encoding="utf-8",
            )
            findings = audit(root, [source], None)
            self.assertEqual(fix_html_anchor_links(root, findings), 1)
            self.assertEqual(
                source.read_text(encoding="utf-8"),
                "[t](core_05_band_continuity.md#long-heading) "
                "[a](core_05_band_continuity.md#x-a)\n",
            )
            self.assertEqual(audit(root, [source], None), [])


if __name__ == "__main__":
    unittest.main()
