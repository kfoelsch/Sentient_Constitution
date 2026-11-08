#!/usr/bin/env python3
"""Tests for RECORD-KIND-01 (a bare "record" with no kind named)."""

from __future__ import annotations

import unittest

from lexical_vocabulary_audit import _mask_inline_code_and_link_targets
from record_kind_audit import bare_record_phrases, scan_text


def phrases(line: str) -> list[str]:
    return bare_record_phrases(_mask_inline_code_and_link_targets(line))


class RecordKindTests(unittest.TestCase):
    def test_flags_the_record(self) -> None:
        self.assertEqual(phrases("The custodian holds the record."), ["the record"])
        self.assertEqual(phrases("Both seats sit on the same record."), ["same record"])

    def test_flags_a_record_and_its_own_record(self) -> None:
        self.assertEqual(phrases("A record whose subject is a Chartered Party is flagged."), ["a record"])
        self.assertEqual(phrases("Each act makes its own record."), ["own record"])

    def test_flags_plural_and_generic_modifiers(self) -> None:
        self.assertEqual(phrases("The custodian holds the records it opened."), ["the records"])
        self.assertEqual(phrases("A single record may be moved."), ["single record"])
        self.assertEqual(phrases("It keeps the verified record."), ["verified record"])
        self.assertEqual(phrases("It keeps the official record."), [])
        self.assertEqual(phrases("A verified record is entered."), ["verified record"])

    def test_flags_possessive_use(self) -> None:
        self.assertEqual(phrases("The record's subject may not act."), ["the record"])

    def test_accepts_a_named_kind(self) -> None:
        self.assertEqual(phrases("The standing record is entered."), [])
        self.assertEqual(phrases("A contribution standing record and a violation record."), [])
        self.assertEqual(phrases("The Forum Case Record is separate."), [])
        self.assertEqual(phrases("The System Certification Record is kept."), [])
        self.assertEqual(phrases("The classification record names the class."), [])
        self.assertEqual(phrases("Standing records are axis-pure."), [])

    def test_accepts_record_of_or_for(self) -> None:
        self.assertEqual(phrases("It keeps a record of the refusal."), [])
        self.assertEqual(phrases("The records for review are listed."), [])

    def test_accepts_defined_compounds(self) -> None:
        self.assertEqual(phrases("The record custodian enters it."), [])
        self.assertEqual(phrases("The record-opening authority verifies it."), [])
        self.assertEqual(phrases("Each seat is a record seat."), [])
        self.assertEqual(phrases("The record span is stated."), [])
        self.assertEqual(phrases("Each amendment is a new Record Version."), [])
        self.assertEqual(phrases("The published record challenge path opens."), [])

    def test_accepts_the_verb_and_idioms(self) -> None:
        self.assertEqual(phrases("An adopter must record the reasons."), [])
        self.assertEqual(phrases("It records the determination."), [])
        self.assertEqual(phrases("A result that records verified readiness is kept."), [])
        self.assertEqual(phrases("A holder with no prior history is on record."), [])
        self.assertEqual(phrases("Records and review pathways stay open."), [])

    def test_ignores_inline_code_and_link_targets(self) -> None:
        self.assertEqual(phrases("It rests on `the record` and [the rule](core_13.000_the_record.md)."), [])

    def test_scan_skips_fences_and_exempt_file(self) -> None:
        text = "```\nThe custodian holds the record.\n```\nThe custodian holds the record.\n"
        found = scan_text("core_11.000_standing_assessment.md", text)
        self.assertEqual([f.line for f in found], [4])
        self.assertEqual(scan_text("doc_architecture.md", "The custodian holds the record.\n"), [])


if __name__ == "__main__":
    unittest.main()
