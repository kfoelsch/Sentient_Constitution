#!/usr/bin/env python3
"""Tests for the Sentience-Status Adjudication Record validator."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from sentience_status_adjudication_record_validate import self_check, validate_record

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "implementation" / "schemas" / "examples"


class SentienceStatusAdjudicationRecordTests(unittest.TestCase):
    def test_valid_contested_fixture_passes(self) -> None:
        record = json.loads(
            (
                EXAMPLES / "sentience_status_adjudication_record.valid.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(validate_record(record), [])

    def test_valid_narrowed_fixture_passes(self) -> None:
        record = json.loads(
            (
                EXAMPLES
                / "sentience_status_adjudication_record.narrowed.valid.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(validate_record(record), [])

    def test_invalid_fixture_fails(self) -> None:
        record = json.loads(
            (
                EXAMPLES / "sentience_status_adjudication_record.invalid.json"
            ).read_text(encoding="utf-8")
        )
        errors = validate_record(record)
        blob = " ".join(errors)
        self.assertIn("subject_entity.id", blob)
        self.assertIn("review_trigger", blob)

    def test_narrowed_without_timeline_fails(self) -> None:
        record = json.loads(
            (
                EXAMPLES
                / "sentience_status_adjudication_record.narrowed.valid.json"
            ).read_text(encoding="utf-8")
        )
        record["narrowing"]["expected_closure_timeline"] = None
        errors = validate_record(record)
        self.assertTrue(any("expected_closure_timeline" in e for e in errors))

    def test_missing_independent_representative_fails(self) -> None:
        record = json.loads(
            (
                EXAMPLES / "sentience_status_adjudication_record.valid.json"
            ).read_text(encoding="utf-8")
        )
        del record["independent_representative"]
        errors = validate_record(record)
        self.assertTrue(any("independent_representative" in e for e in errors))

    def test_declined_filing_without_indicator_fails(self) -> None:
        record = json.loads(
            (
                EXAMPLES / "sentience_status_adjudication_record.valid.json"
            ).read_text(encoding="utf-8")
        )
        record["independent_representative"]["appointed"] = False
        del record["independent_representative"]["appointee_id"]
        record["intake_decline_log"]["this_filing_declined"] = True
        record["intake_decline_log"]["indicator_cited"] = None
        record["intake_decline_log"]["reason"] = None
        errors = validate_record(record)
        blob = " ".join(errors)
        self.assertIn("intake_decline_log.indicator_cited", blob)
        self.assertIn("intake_decline_log.reason", blob)

    def test_self_check_passes(self) -> None:
        self.assertEqual(self_check(ROOT), [])


if __name__ == "__main__":
    unittest.main()
