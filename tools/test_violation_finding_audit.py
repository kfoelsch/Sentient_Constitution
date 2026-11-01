#!/usr/bin/env python3
"""Tests for VIOLATION-FINDING-01 (a bare "finding" where a violation finding is meant)."""

from __future__ import annotations

import unittest

from violation_finding_audit import bare_finding_phrases, scan_text
from lexical_vocabulary_audit import _mask_inline_code_and_link_targets


def phrases(line: str) -> list[str]:
    return bare_finding_phrases(_mask_inline_code_and_link_targets(line))


class ViolationFindingTests(unittest.TestCase):
    def test_flags_verified_finding_on_a_lock_line(self) -> None:
        self.assertEqual(phrases("A lock attaches only to a verified finding."), ["verified finding"])

    def test_flags_determiner_finding_on_a_violation_line(self) -> None:
        self.assertEqual(phrases("The lock ends if the finding it rested on is set aside."), ["the finding"])

    def test_flags_plural_after_the(self) -> None:
        self.assertEqual(phrases("Standing effects rest on the findings of the merits matter."), ["the findings"])

    def test_flags_adverse_finding(self) -> None:
        self.assertEqual(phrases("A holder sees any adverse finding on a misconduct charge."), ["adverse finding"])

    def test_accepts_violation_finding(self) -> None:
        self.assertEqual(phrases("A lock attaches only to a verified violation finding."), [])

    def test_accepts_qualified_findings(self) -> None:
        self.assertEqual(
            phrases("The component finding, the cause finding, and a non-compliance finding stay apart from a lock."),
            [],
        )

    def test_accepts_finding_of_violation(self) -> None:
        self.assertEqual(phrases("For a verified finding of violation, the matter goes to the standing lock process."), [])
        self.assertEqual(phrases("A finding that misconduct occurred opens a lock."), [])
        self.assertEqual(phrases("The lock ends on a published finding of independent review."), [])

    def test_accepts_back_reference_after_violation_finding(self) -> None:
        self.assertEqual(phrases("A violation finding is verified, and the finding is then recorded under the lock."), [])

    def test_accepts_finding_as_modifier(self) -> None:
        self.assertEqual(phrases("Identify the finding authority for the lock; a finding profile is optional for a violation."), [])

    def test_ignores_lines_with_no_violation_cue(self) -> None:
        self.assertEqual(phrases("The forum reviews the findings and reaches an outcome."), [])
        self.assertEqual(phrases("Each finding on the seven items carries its evidence."), [])

    def test_ignores_inline_code_and_link_targets(self) -> None:
        self.assertEqual(phrases("A lock rests on `a verified finding` and [the rule](core_12.000_a_finding.md)."), [])

    def test_scan_skips_fences_and_exempt_file(self) -> None:
        text = "```\nA lock rests on a verified finding.\n```\nA lock rests on a verified finding.\n"
        found = scan_text("core_12.000_standing_integration.md", text)
        self.assertEqual([f.line for f in found], [4])
        self.assertEqual(scan_text("doc_architecture.md", "A lock rests on a verified finding.\n"), [])


if __name__ == "__main__":
    unittest.main()
