#!/usr/bin/env python3
"""Tests for NAV-IMPL-FILENAME-01 companion filename parsing."""

from __future__ import annotations

import unittest

from companion_filename_audit import audit_filenames, parse_companion_filename


class ParseTests(unittest.TestCase):
    def test_undifferenced_home(self) -> None:
        item = parse_companion_filename("cjs_02_specific_joint_interlocks.md")
        assert item is not None
        self.assertEqual(item.layer, "cjs")
        self.assertEqual(item.number, "02")
        self.assertEqual(item.part, "")

    def test_glued_letter(self) -> None:
        item = parse_companion_filename("cjs_03o_oversight_operations.md")
        assert item is not None
        self.assertEqual(item.part, "o")

    def test_cs_part_letter(self) -> None:
        item = parse_companion_filename("cs_02_a_information_types_and_handling.md")
        assert item is not None
        self.assertEqual(item.layer, "cs")
        self.assertEqual(item.number, "02")
        self.assertEqual(item.part, "a")

    def test_unparseable_numbered_name(self) -> None:
        self.assertIsNone(parse_companion_filename("cjs_02hybrid.md"))


class AuditTests(unittest.TestCase):
    def test_same_chapter_parts_ok(self) -> None:
        findings = audit_filenames(
            [
                "cjs_02_specific_joint_interlocks.md",
                "cjs_03_cross_implementation_operational_terms.md",
                "cjs_03o_oversight_operations.md",
                "cs_02_a_information_types_and_handling.md",
                "cs_02_b_data_classifications.md",
            ]
        )
        self.assertEqual(findings, [])

    def test_undifferenced_home_plus_part_letter_ok(self) -> None:
        findings = audit_filenames(
            [
                "cs_05_design_testing_verification_deployment.md",
                "cs_05_a_user_facing_capabilities.md",
            ]
        )
        self.assertEqual(findings, [])

    def test_undifferenced_collision(self) -> None:
        findings = audit_filenames(
            [
                "cjs_02_specific_joint_interlocks.md",
                "cjs_02_hybrid_delegated_authority.md",
            ]
        )
        self.assertTrue(any("undifferenced" in item for item in findings))

    def test_scope_page_must_be_unique(self) -> None:
        findings = audit_filenames(
            [
                "cjs_01_scope_purpose_boundary_interface.md",
                "cjs_01_drafting_contracts.md",
            ]
        )
        self.assertTrue(any("family 01" in item for item in findings))

    def test_duplicate_part_letter(self) -> None:
        findings = audit_filenames(
            [
                "cjs_03o_oversight_operations.md",
                "cjs_03o_other.md",
            ]
        )
        self.assertTrue(any("duplicate part letter" in item for item in findings))


if __name__ == "__main__":
    unittest.main()
