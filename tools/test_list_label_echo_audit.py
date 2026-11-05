#!/usr/bin/env python3
"""Tests for MD-LABEL-ECHO-01 (a bullet label is not restated by its own body)."""

from __future__ import annotations

import unittest

from list_label_echo_audit import scan_text


class ListLabelEchoTests(unittest.TestCase):
    def _labels(self, text: str) -> list[str]:
        return [finding.label for finding in scan_text("core_11_c.md", text)]

    def test_flags_label_restated_by_short_body(self) -> None:
        text = "- **Is invalid:** The charter is invalid.\n"
        findings = scan_text("core_11_c.md", text)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].line, 1)
        self.assertEqual(findings[0].label, "Is invalid")

    def test_flags_nested_and_numbered_items_and_colon_outside_bold(self) -> None:
        text = (
            "- **Parent:** adds a real idea about custody.\n"
            "  - **Notice given** notice is given.\n"
            "1. **Record sealed:** The record is sealed.\n"
        )
        self.assertEqual(self._labels(text), ["Notice given", "Record sealed"])

    def test_passes_label_with_distinct_body(self) -> None:
        text = (
            "- **Who may not act:** Until the gap is resolved, none of the "
            "Chartered Party's own offices may verify, enter, or contest.\n"
        )
        self.assertEqual(self._labels(text), [])

    def test_passes_short_body_that_adds_new_content(self) -> None:
        text = "- **Is invalid:** The charter is void and unenforceable from signing.\n"
        self.assertEqual(self._labels(text), [])

    def test_passes_long_body_even_when_it_repeats_the_label(self) -> None:
        text = (
            "- **Is invalid:** The charter is invalid until the named holders "
            "sign and the registrar records the change in the lane map.\n"
        )
        self.assertEqual(self._labels(text), [])

    def test_ignores_cross_reference_and_lead_in_bodies(self) -> None:
        text = (
            "- **Cross-system support** (§5.3 Proportionate Cross-System Support):\n"
            "- **Proportionate participation:** Participation must remain proportionate to:\n"
            "- **Truth** — Truth (Constitutional Constraint);\n"
        )
        self.assertEqual(self._labels(text), [])

    def test_passes_definition_that_reverses_label_word_order(self) -> None:
        text = "- **System Version:** which version of the system is being certified.\n"
        self.assertEqual(self._labels(text), [])

    def test_ignores_pointers_with_section_cites(self) -> None:
        text = "- **Denial and revocation:** The effects are in §7.5 Effects of denial and revocation.\n"
        self.assertEqual(self._labels(text), [])

    def test_ignores_links_in_body_text_when_comparing(self) -> None:
        text = "- **Duty to resist:** [Duty to Resist](core_01.md#175-duty-to-resist).\n"
        self.assertEqual(self._labels(text), ["Duty to resist"])

    def test_skips_fences_comments_and_details_blocks(self) -> None:
        text = (
            "```\n- **Is invalid:** The charter is invalid.\n```\n"
            "<!--\n- **Is invalid:** The charter is invalid.\n-->\n"
            "<details>\n<summary>Trace</summary>\n"
            "- **Is invalid:** The charter is invalid.\n</details>\n"
        )
        self.assertEqual(self._labels(text), [])

    def test_plain_bullets_without_bold_label_are_ignored(self) -> None:
        text = "- The charter is invalid.\n- Is invalid: the charter is invalid.\n"
        self.assertEqual(self._labels(text), [])


if __name__ == "__main__":
    unittest.main()
