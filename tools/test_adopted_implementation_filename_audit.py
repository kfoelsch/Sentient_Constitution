#!/usr/bin/env python3
"""Tests for NAV-IMPL-FILENAME-01 adopted-implementation filename parsing."""

from __future__ import annotations

import unittest

from adopted_implementation_filename_audit import audit_filenames, parse_adopted_implementation_filename


class ParseTests(unittest.TestCase):
    def test_undifferenced_home(self) -> None:
        item = parse_adopted_implementation_filename("cjs_18.110_specific_joint_interlocks.md")
        assert item is not None
        self.assertEqual(item.layer, "cjs")
        self.assertEqual(item.number, "18110")
        self.assertEqual(item.part, "")

    def test_five_digit_chapter_number(self) -> None:
        item = parse_adopted_implementation_filename("cjs_05.110_oversight_operations.md")
        assert item is not None
        self.assertEqual(item.number, "05110")

    def test_cs_part_letter(self) -> None:
        item = parse_adopted_implementation_filename("cs_06.305_information_types_and_handling.md")
        assert item is not None
        self.assertEqual(item.layer, "cs")
        self.assertEqual(item.number, "06305")
        self.assertEqual(item.part, "")

    def test_unparseable_numbered_name(self) -> None:
        self.assertIsNone(parse_adopted_implementation_filename("cjs_02hybrid.md"))


class AuditTests(unittest.TestCase):
    def test_same_chapter_parts_ok(self) -> None:
        findings = audit_filenames(
            [
                "cjs_18.110_specific_joint_interlocks.md",
                "cjs_05.105_cross_implementation_operational_terms.md",
                "cjs_05.110_oversight_operations.md",
                "cs_06.305_information_types_and_handling.md",
                "cs_06.310_data_classifications.md",
            ]
        )
        self.assertEqual(findings, [])

    def test_undifferenced_home_plus_part_letter_ok(self) -> None:
        findings = audit_filenames(
            [
                "cs_06.345_design_testing_verification_deployment.md",
                "cs_06.340_user_facing_capabilities.md",
            ]
        )
        self.assertEqual(findings, [])

    def test_duplicate_number_collision(self) -> None:
        findings = audit_filenames(
            [
                "cjs_18.110_specific_joint_interlocks.md",
                "cjs_18.110_hybrid_delegated_authority.md",
            ]
        )
        self.assertTrue(any("duplicate chapter number" in item for item in findings))

    def test_scope_and_identifier_chapters_have_distinct_numbers(self) -> None:
        findings = audit_filenames(
            [
                "cjs_00.105_registry_and_reading_rules.md",
                "cjs_00.110_scope_purpose_boundary_interface.md",
            ]
        )
        self.assertEqual(findings, [])

    def test_duplicate_chapter_number(self) -> None:
        findings = audit_filenames(
            [
                "cjs_05.110_oversight_operations.md",
                "cjs_05.110_other.md",
            ]
        )
        self.assertTrue(any("duplicate chapter number" in item for item in findings))


if __name__ == "__main__":
    unittest.main()
