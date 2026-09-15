#!/usr/bin/env python3
"""Tests for the CS-4 §10 inspectable-action log validator."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from cs4_inspectable_action_log_validate import (
    SCHEMA_REL,
    published_tier_bounds,
    self_check,
    validate_log,
)

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "implementation" / "schemas" / "examples"


class Cs4InspectableActionLogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bounds = published_tier_bounds(ROOT)

    def test_valid_refusal_fixture_passes(self) -> None:
        log = json.loads(
            (EXAMPLES / "cs4_inspectable_action_log.valid.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(validate_log(log, self.bounds), [])

    def test_valid_tier_a_fixture_matches_published_bound(self) -> None:
        log = json.loads(
            (
                EXAMPLES / "cs4_inspectable_action_log.tier_a.valid.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(validate_log(log, self.bounds), [])
        self.assertEqual(log["tier_clock"]["bound"], self.bounds["A"])

    def test_missing_element_fails(self) -> None:
        log = json.loads(
            (EXAMPLES / "cs4_inspectable_action_log.valid.json").read_text(
                encoding="utf-8"
            )
        )
        del log["elements"]["authorized_by"]
        errors = validate_log(log, self.bounds)
        self.assertTrue(any("authorized_by" in err for err in errors))

    def test_missing_attribution_fails(self) -> None:
        log = json.loads(
            (EXAMPLES / "cs4_inspectable_action_log.valid.json").read_text(
                encoding="utf-8"
            )
        )
        del log["elements"]["decided"]["attributed_to"]
        errors = validate_log(log, self.bounds)
        self.assertTrue(any("attributed_to" in err for err in errors))

    def test_wrong_published_bound_fails(self) -> None:
        log = json.loads(
            (EXAMPLES / "cs4_inspectable_action_log.invalid.json").read_text(
                encoding="utf-8"
            )
        )
        errors = validate_log(log, self.bounds)
        self.assertTrue(any("bound" in err for err in errors))
        self.assertTrue(any("clock_deadline_at" in err for err in errors))

    def test_repo_self_check_passes(self) -> None:
        self.assertTrue((ROOT / SCHEMA_REL).is_file())
        errors = self_check(ROOT)
        self.assertEqual(errors, [], msg="\n".join(errors))

    def test_temp_log_without_five_elements_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "empty.json"
            path.write_text("{}", encoding="utf-8")
            log = json.loads(path.read_text(encoding="utf-8"))
            errors = validate_log(log, self.bounds)
            self.assertTrue(any("elements" in err for err in errors))


if __name__ == "__main__":
    unittest.main()
