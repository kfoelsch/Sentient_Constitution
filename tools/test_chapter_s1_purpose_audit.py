#!/usr/bin/env python3
"""Tests for CHAPTER-S1-PURPOSE-01 (standard section 1 heading and lead-ins)."""

from __future__ import annotations

import unittest

from chapter_s1_purpose_audit import in_scope, scan_text

GOOD = (
    "# CHAPTER FIVE: X\n\n"
    "### 1. Purpose, Role, and Scope\n\n*In plain terms: x.*\n\n"
    "**Purpose:** Why.\n\n**Role:** Where.\n\n**Chapter scope:** What.\n\n"
    "### 2. Why Things Exist\n\n**Purpose:** not counted.\n"
)


class ChapterS1PurposeTests(unittest.TestCase):
    def test_accepts_standard_section(self) -> None:
        self.assertEqual(scan_text("core_05.000_x.md", GOOD), [])

    def test_accepts_anchor_before_lead_in(self) -> None:
        text = GOOD.replace("**Purpose:** Why.", '<a id="x"></a><a id="y"></a>**Purpose:** Why.')
        self.assertEqual(scan_text("x.md", text), [])

    def test_flags_missing_section(self) -> None:
        text = "# X\n\nText.\n"
        self.assertEqual([f.message for f in scan_text("x.md", text)], ["no `### 1.` section"])

    def test_flags_first_section_not_one(self) -> None:
        text = GOOD.replace("### 1. Purpose, Role, and Scope", "### 3. Purpose, Role, and Scope")
        self.assertIn("not §1", scan_text("x.md", text)[0].message)

    def test_flags_inexact_heading(self) -> None:
        text = GOOD.replace("Purpose, Role, and Scope", "Purpose and Role")
        self.assertEqual(len(scan_text("x.md", text)), 1)

    def test_flags_missing_lead_in(self) -> None:
        text = GOOD.replace("**Chapter scope:** What.", "Scope: what.")
        self.assertIn("`**Chapter scope:**`", scan_text("x.md", text)[0].message)

    def test_lead_in_after_section_does_not_count(self) -> None:
        text = GOOD.replace("**Purpose:** Why.\n\n", "")
        self.assertIn("`**Purpose:**`", scan_text("x.md", text)[0].message)

    def test_flags_order(self) -> None:
        text = GOOD.replace(
            "**Purpose:** Why.\n\n**Role:** Where.", "**Role:** Where.\n\n**Purpose:** Why."
        )
        self.assertIn("order", scan_text("x.md", text)[0].message)

    def test_ignores_fenced_headings(self) -> None:
        text = GOOD.replace("# CHAPTER FIVE: X\n\n", "# CHAPTER FIVE: X\n\n```\n### 9. Fake\n```\n\n")
        self.assertEqual(scan_text("x.md", text), [])

    def test_scope(self) -> None:
        self.assertTrue(in_scope("core_05.000_x.md"))
        self.assertTrue(in_scope("core_02.000_values_principles.md"))
        self.assertFalse(in_scope("core_05.010_x.md"))
        self.assertFalse(in_scope("core_00.000_preamble.md"))
        self.assertFalse(in_scope("subcore_03.010_x.md"))
        self.assertFalse(in_scope("corpus_systems/cs_08.305_x.md"))


if __name__ == "__main__":
    unittest.main()
