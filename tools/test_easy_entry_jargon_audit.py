#!/usr/bin/env python3
"""Tests for the easy-entry jargon audit."""

from __future__ import annotations

import unittest

from easy_entry_jargon_audit import (
    CONFIG_PATH,
    audit_text,
    load_jargon_config,
    visible_scan_text,
)


class ConfigTests(unittest.TestCase):
    def test_config_loads_terms(self) -> None:
        allow, terms = load_jargon_config(CONFIG_PATH)
        self.assertIn("Sentient Constitution", allow)
        avoids = {term.avoid for term in terms}
        self.assertIn("standing record", avoids)
        self.assertIn("adopter", avoids)
        self.assertIn("forum", avoids)
        self.assertIn("offtake", avoids)


class ScanTests(unittest.TestCase):
    def setUp(self) -> None:
        self.allow, self.terms = load_jargon_config(CONFIG_PATH)

    def _audit(self, text: str) -> list[str]:
        findings = audit_text(
            text,
            rel_path="implementation/adoption/easy_entry/E99.md",
            terms=self.terms,
            allow_phrases=self.allow,
        )
        return [item.avoid for item in findings]

    def test_flags_standing_record_in_body(self) -> None:
        hits = self._audit("It is not a Chapter Eight standing record.\n")
        self.assertIn("standing record", hits)

    def test_flags_offtake_in_body(self) -> None:
        hits = self._audit(
            "Take the loan, the sensor, and the exclusive offtake, or lose next season’s input.\n"
        )
        self.assertIn("offtake", hits)

    def test_skips_markdown_link_text(self) -> None:
        hits = self._audit(
            "See: [Occupancy Continuity](../../../core_05_band_continuity.md#occupancy-continuity-constitutional).\n"
        )
        self.assertEqual(hits, [])

    def test_keeps_sentient_constitution_name(self) -> None:
        hits = self._audit(
            "Your situation with the Sentient Constitution\n"
        )
        self.assertEqual(hits, [])

    def test_skips_quoted_objection_header(self) -> None:
        hits = self._audit(
            '- **“I am not a person here.”** This text does not use a human legal label as the gate.\n'
        )
        self.assertEqual(hits, [])

    def test_flags_jargon_in_objection_answer(self) -> None:
        hits = self._audit(
            '- **“This isn’t law.”** Filing still opens a standing record.\n'
        )
        self.assertIn("standing record", hits)

    def test_skips_details_widgets(self) -> None:
        hits = self._audit(
            "<details>\n"
            "<summary>Trace</summary>\n"
            "This page is operations-guide support and a standing record.\n"
            "</details>\n"
            "\n"
            "Pick the brief that sounds like your situation.\n"
        )
        self.assertEqual(hits, [])

    def test_skips_do_not_use_section(self) -> None:
        hits = self._audit(
            "## Do not use in these briefs\n"
            "\n"
            "| Do not use | Use instead |\n"
            "| standing record | official record |\n"
            "\n"
            "## How to read a brief\n"
            "\n"
            "Cite the named homes if you want the real text.\n"
        )
        self.assertEqual(hits, [])

    def test_visible_scan_strips_links(self) -> None:
        visible = visible_scan_text(
            "See: [Reproductive Autonomy](../../../core_05_band_participation.md#reproductive-autonomy-constitutional).",
            self.allow,
        )
        self.assertNotIn("Reproductive Autonomy", visible)
        self.assertIn("See:", visible)


if __name__ == "__main__":
    unittest.main()
