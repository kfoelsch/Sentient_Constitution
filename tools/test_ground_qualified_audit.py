#!/usr/bin/env python3
"""Tests for GROUND-QUALIFIED-01 (a bare "ground" with no kind named)."""

from __future__ import annotations

import unittest

from ground_qualified_audit import bare_ground_phrases, scan_text
from lexical_vocabulary_audit import _mask_inline_code_and_link_targets


def phrases(line: str) -> list[str]:
    return bare_ground_phrases(_mask_inline_code_and_link_targets(line))


class GroundQualifiedTests(unittest.TestCase):
    def test_flags_a_ground(self) -> None:
        self.assertEqual(phrases("The System is denied only on a ground that rests on its own findings."), ["a ground"])

    def test_flags_the_grounds_and_that_ground(self) -> None:
        self.assertEqual(phrases("The forum states the grounds."), ["the grounds"])
        self.assertEqual(phrases("It must state that ground in writing."), ["that ground"])

    def test_flags_modifiers_that_do_not_name_a_kind(self) -> None:
        self.assertEqual(phrases("Each stated ground is on the record."), ["stated ground"])
        self.assertEqual(phrases("Each outcome follows its own ground."), ["own ground"])
        self.assertEqual(phrases("It acts on any lawful ground."), ["lawful ground"])
        self.assertEqual(phrases("It has two grounds."), ["two grounds"])

    def test_accepts_a_named_kind(self) -> None:
        self.assertEqual(phrases("A denial ground and a revocation ground are stated separately."), [])
        self.assertEqual(phrases("An institutional ground does not deny the System."), [])
        self.assertEqual(phrases("The hold grounds are listed in Chapter Thirteen."), [])
        self.assertEqual(phrases("Protected grounds include sex and age."), [])
        self.assertEqual(phrases("A technical-feasibility ground is not enough."), [])

    def test_accepts_ground_for_or_of(self) -> None:
        self.assertEqual(phrases("A ground for denial is stated."), [])
        self.assertEqual(phrases("The grounds for reopening are in Chapter Nine."), [])
        self.assertEqual(phrases("Treatment on grounds of sex is barred."), [])

    def test_accepts_the_verb(self) -> None:
        self.assertEqual(phrases("A rule that grounds the duty is cited."), [])
        self.assertEqual(phrases("None of those factors may ground denial or degradation of rights."), [])
        self.assertEqual(phrases("The plan must ground the claim in evidence."), [])

    def test_accepts_other_senses(self) -> None:
        self.assertEqual(phrases("The parties find common ground."), [])
        self.assertEqual(phrases("Ground truth is kept separate."), [])
        self.assertEqual(phrases("Staff on the ground report."), [])

    def test_ignores_inline_code_and_link_targets(self) -> None:
        self.assertEqual(phrases("It rests on `a ground` and [the rule](core_12.000_a_ground.md)."), [])

    def test_scan_skips_fences_and_exempt_file(self) -> None:
        text = "```\nThe forum states the grounds.\n```\nThe forum states the grounds.\n"
        found = scan_text("core_10.000_institutional_alignment_certification.md", text)
        self.assertEqual([f.line for f in found], [4])
        self.assertEqual(scan_text("doc_architecture.md", "The forum states the grounds.\n"), [])


if __name__ == "__main__":
    unittest.main()
