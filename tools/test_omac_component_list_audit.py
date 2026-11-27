#!/usr/bin/env python3
"""Tests for the O/M/A/C component-list audit (OMAC-LIST-01)."""

from __future__ import annotations

import unittest

import omac_component_list_audit as oca


class ScanTests(unittest.TestCase):
    def scan(self, text: str) -> list[str]:
        return oca.scan_text("x.md", text)

    def test_tagged_list_without_m_fails(self):
        self.assertTrue(self.scan("Its Ontological (O), Assessment (A), and Compliance (C) components apply."))

    def test_full_list_passes(self):
        self.assertEqual(self.scan("Its Ontological (O), Measurement (M), Assessment (A), and Compliance (C) components apply."), [])

    def test_scope_phrase_without_measurement_fails(self):
        self.assertTrue(self.scan("Preserve their full semantic, assessment, and compliance scope."))
        self.assertEqual(self.scan("Preserve their full semantic, measurement, assessment, and compliance scope."), [])

    def test_letter_list_without_m_fails(self):
        self.assertTrue(self.scan("Check O, A, and C together."))
        self.assertEqual(self.scan("Check O/M/A/C together."), [])

    def test_single_component_mention_passes(self):
        self.assertEqual(self.scan("The Compliance (C) part says what must hold."), [])

    def test_check_is_per_sentence(self):
        text = "Measurement (M) is set here. Its Ontological (O) and Compliance (C) parts follow."
        self.assertTrue(self.scan(text))

    def test_code_blocks_are_skipped(self):
        self.assertEqual(self.scan("```\nOntological (O), Assessment (A)\n```\n"), [])


if __name__ == "__main__":
    unittest.main()
