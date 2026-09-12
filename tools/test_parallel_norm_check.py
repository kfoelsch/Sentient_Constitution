#!/usr/bin/env python3
"""Tests for tools/parallel_norm_check.py."""

from __future__ import annotations

import unittest
from pathlib import Path

import corpus_lookup
import parallel_norm_check

ROOT = Path(__file__).resolve().parents[1]


class ParallelNormCheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.indexes = corpus_lookup.load_indexes(ROOT)

    def test_flags_court_house_term(self) -> None:
        payload = parallel_norm_check.check_text(
            self.indexes, "The court must hear the case.", None
        )
        kinds = {flag["kind"] for flag in payload["flags"]}
        self.assertIn("house_term", kinds)
        self.assertFalse(payload["ok"])

    def test_missing_anchor_in_existing_file(self) -> None:
        text = "See [gone](core_00_preamble.md#this-anchor-does-not-exist)."
        payload = parallel_norm_check.check_text(self.indexes, text, None)
        kinds = {flag["kind"] for flag in payload["flags"]}
        self.assertIn("missing_anchor", kinds)

    def test_clean_pointer_is_ok(self) -> None:
        text = (
            "Open [Article XII-B](core_06_rights_part_c.md"
            "#article-xii-b-right-to-challenge-review-and-redress). "
            "The source binds."
        )
        payload = parallel_norm_check.check_text(self.indexes, text, None)
        self.assertTrue(payload["ok"], payload["flags"])


if __name__ == "__main__":
    unittest.main()
