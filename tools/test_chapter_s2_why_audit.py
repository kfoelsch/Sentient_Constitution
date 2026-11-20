#!/usr/bin/env python3
"""Tests for CHAPTER-S2-WHY-01 (section 2 why with a Grounded in list)."""

from __future__ import annotations

import unittest

from chapter_s2_why_audit import in_scope, scan_text

GOOD = (
    "### 1. Purpose, Role, and Scope\n\nText.\n\n"
    "### 2. Why Things Exist\n\n*In plain terms: x.*\n\nWhy.\n\n"
    "**Grounded in:**\n\n- Chapter Two principles: [§1](a.md#1-x);\n\n"
    "### 3. Work\n\nText.\n"
)


class ChapterS2WhyTests(unittest.TestCase):
    def test_accepts_standard_section(self) -> None:
        self.assertEqual(scan_text("core_05.000_x.md", GOOD), [])

    def test_flags_missing_section(self) -> None:
        text = "### 1. Purpose\n\nText.\n\n### 3. Work\n"
        self.assertEqual([f.message for f in scan_text("x.md", text)], ["no `### 2.` section"])

    def test_flags_heading_not_why(self) -> None:
        text = GOOD.replace("### 2. Why Things Exist", "### 2. Things")
        self.assertEqual(len(scan_text("x.md", text)), 1)

    def test_flags_missing_grounded_in(self) -> None:
        text = GOOD.replace("**Grounded in:**", "Grounded in")
        self.assertIn("no `**Grounded in:**` label", scan_text("x.md", text)[0].message)

    def test_flags_grounded_in_without_list(self) -> None:
        text = GOOD.replace("- Chapter Two", "Chapter Two")
        self.assertIn("bulleted list", scan_text("x.md", text)[0].message)

    def test_grounded_in_after_section_does_not_count(self) -> None:
        text = GOOD.replace("**Grounded in:**\n\n- Chapter Two principles: [§1](a.md#1-x);\n\n", "")
        text += "\n**Grounded in:**\n\n- y\n"
        self.assertEqual(len(scan_text("x.md", text)), 1)

    def test_scope(self) -> None:
        self.assertTrue(in_scope("core_05.000_x.md"))
        self.assertTrue(in_scope("subcore_03.010_x.md"))
        self.assertFalse(in_scope("core_05.010_x.md"))
        self.assertFalse(in_scope("core_00.000_preamble.md"))
        self.assertFalse(in_scope("core_02.000_values_principles.md"))
        self.assertFalse(in_scope("corpus_systems/cs_08.305_x.md"))


if __name__ == "__main__":
    unittest.main()
