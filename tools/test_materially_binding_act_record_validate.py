#!/usr/bin/env python3
"""Tests for the Materially Binding Act Record validator."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from materially_binding_act_record_validate import SCHEMA_REL, self_check, validate_record

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "implementation" / "schemas" / "examples"


class MateriallyBindingActRecordTests(unittest.TestCase):
    def load_valid(self) -> dict:
        return json.loads(
            (EXAMPLES / "materially_binding_act_record.valid.json").read_text(
                encoding="utf-8"
            )
        )

    def test_valid_fixture_passes(self) -> None:
        self.assertEqual(validate_record(self.load_valid()), [])

    def test_missing_contest_seat_fails(self) -> None:
        record = self.load_valid()
        del record["seats"]["contest"]
        errors = validate_record(record)
        self.assertTrue(any("seats.contest" in error for error in errors))

    def test_prohibited_seat_combination_fails(self) -> None:
        record = self.load_valid()
        record["seats"]["verify_or_authorize"]["holder_or_route"] = record["seats"][
            "initiating"
        ]["holder_or_route"]
        errors = validate_record(record)
        self.assertTrue(any("same holder" in error for error in errors))

    def test_custody_version_must_match_record_version(self) -> None:
        record = self.load_valid()
        record["custody"]["version_entered"] = 1
        errors = validate_record(record)
        self.assertTrue(any("version_entered" in error for error in errors))

    def test_nonpending_determination_requires_attribution(self) -> None:
        record = self.load_valid()
        record["determination"]["determined_by"] = None
        record["determination"]["determined_at"] = None
        errors = validate_record(record)
        self.assertTrue(any("determined_by" in error for error in errors))
        self.assertTrue(any("determined_at" in error for error in errors))

    def test_repo_self_check_passes(self) -> None:
        self.assertTrue((ROOT / SCHEMA_REL).is_file())
        errors = self_check(ROOT)
        self.assertEqual(errors, [], msg="\n".join(errors))


if __name__ == "__main__":
    unittest.main()
