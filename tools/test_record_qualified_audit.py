#!/usr/bin/env python3
"""Tests for RECORD-QUALIFIED-01 (a bare "the record" on a line that names both a System and an Institution)."""

from __future__ import annotations

import unittest

from lexical_vocabulary_audit import _mask_inline_code_and_link_targets
from record_qualified_audit import bare_record_phrases, scan_text


def phrases(line: str) -> list[str]:
    return bare_record_phrases(_mask_inline_code_and_link_targets(line))


class RecordQualifiedTests(unittest.TestCase):
    def test_flags_bare_record_beside_both_kinds(self) -> None:
        line = "Each System Certification Record is cited by the Institution, and the record states the cause."
        self.assertEqual(phrases(line), ["the record"])

    def test_flags_this_and_that_record(self) -> None:
        self.assertEqual(
            phrases("A System Certification Record offered by an Institution does not satisfy this record."),
            ["this record"],
        )
        self.assertEqual(
            phrases("The Institutional Certification Record carries facts a System takes; that record is bounded."),
            ["that record"],
        )

    def test_accepts_a_line_that_names_one_kind(self) -> None:
        self.assertEqual(phrases("The Institutional Certification Record is published and the record names the seat."), [])
        self.assertEqual(phrases("The System Certification Record is complete when the record states the outcome."), [])

    def test_accepts_qualified_use(self) -> None:
        line = "The Institutional Certification Record cites each System Certification Record."
        self.assertEqual(phrases(line), [])

    def test_ignores_other_nouns_and_possessives(self) -> None:
        line = "The Institutional Certification Record is kept by the record seat holder for each System."
        self.assertEqual(phrases(line), [])
        self.assertEqual(phrases("The System Certification Record and the Institution's own rules apply to the record-keeping."), [])

    def test_ignores_link_targets_and_inline_code(self) -> None:
        line = "See [the Institution](core_10.000_the_record_x.md) and `the record` in a System Certification Record."
        self.assertEqual(phrases(line), [])

    def test_exempts_the_move_log(self) -> None:
        text = "The System Certification Record, the Institution, and the record."
        self.assertEqual(scan_text("doc_architecture.md", text), [])
        self.assertEqual(len(scan_text("core_10.000_x.md", text)), 1)

    def test_skips_fences(self) -> None:
        text = "```\nThe System Certification Record, the Institution, and the record.\n```\n"
        self.assertEqual(scan_text("core_10.000_x.md", text), [])


if __name__ == "__main__":
    unittest.main()
