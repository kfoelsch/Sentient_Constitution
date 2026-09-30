#!/usr/bin/env python3
"""Tests for MD-SECTION-LEAD-01 (sections open with lead-in prose, not a list)."""

from __future__ import annotations

import unittest

from section_bullet_lead_audit import is_carved_out, scan_text

WIDGETS = (
    "<details>\n<summary>Trace</summary>\n\n- Upstream: skip\n\n</details>\n\n"
    "<details>\n<summary>Definitions · Assessment · Compliance</summary>\n\n"
    "- [Term](x.md#term)\n\n</details>\n\n<br>\n\n"
    "*In plain terms: gloss.*\n\n"
)


class SectionBulletLeadTests(unittest.TestCase):
    def _lines(self, text: str, rel_path: str = "core_06_rights_part_a.md") -> list[int]:
        return [finding.line for finding in scan_text(rel_path, text)]

    def test_flags_bullet_after_widgets_and_gloss(self) -> None:
        text = "#### Article III-D: Safe Working Conditions\n\n" + WIDGETS + (
            "- **Safe working conditions:** Productive activity must be safe.\n"
        )
        findings = scan_text("core_06_rights_part_a.md", text)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].heading, "Article III-D: Safe Working Conditions")
        self.assertTrue(findings[0].preview.startswith("- **Safe"))

    def test_bullets_inside_widgets_are_not_the_opening(self) -> None:
        text = "### 4. Title\n\n" + WIDGETS + "This section sets the floor:\n\n- one\n- two\n"
        self.assertEqual(self._lines(text), [])

    def test_flags_star_and_ordered_items(self) -> None:
        self.assertEqual(len(self._lines("## A\n\n* item\n")), 1)
        self.assertEqual(len(self._lines("## A\n\n1. item\n")), 1)

    def test_accepts_lead_in_prose(self) -> None:
        text = "### Article V: Resources\n\nThis Article states floors:\n\n- **Flourishing:** x\n"
        self.assertEqual(self._lines(text), [])

    def test_container_section_with_child_heading_is_out_of_scope(self) -> None:
        text = "### Article III: Parent\n\n#### Article III-A: Child\n\nLead-in prose.\n\n- a\n"
        self.assertEqual(self._lines(text), [])

    def test_only_first_body_line_counts(self) -> None:
        text = "### 2. Title\n\nOpening prose.\n\n- a\n\n**Label:**\n\n- b\n"
        self.assertEqual(self._lines(text), [])

    def test_bullet_inside_code_fence_is_ignored(self) -> None:
        text = "### 2. Title\n\n```\n- not a list\n```\n\n- later bullet\n"
        self.assertEqual(self._lines(text), [])

    def test_blockquote_callout_is_chrome(self) -> None:
        text = "### 2. Title\n\n> **Note:** architecture.\n\n- a\n"
        self.assertEqual(len(self._lines(text)), 1)

    def test_chapter_five_files_are_carved_out(self) -> None:
        self.assertTrue(is_carved_out("core_05_band_continuity.md"))
        self.assertTrue(is_carved_out("core_05__definitions_home.md"))
        self.assertTrue(is_carved_out("core_05_apex_flourishing_aim.md"))
        self.assertFalse(is_carved_out("core_06_rights_part_a.md"))
        self.assertFalse(is_carved_out("corpus_systems/cs_05_safety.md"))


if __name__ == "__main__":
    unittest.main()
