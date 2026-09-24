#!/usr/bin/env python3
"""Tests for MD-HEADING-RUNIN-01 (no bold run-in that restates its heading)."""

from __future__ import annotations

import unittest

from heading_runin_echo_audit import scan_text


class HeadingRuninEchoTests(unittest.TestCase):
    def _labels(self, text: str, rel_path: str = "core_01_c.md") -> list[str]:
        return [finding.label for finding in scan_text(rel_path, text)]

    def test_flags_period_runin_restating_heading(self) -> None:
        text = (
            '<a id="111-governance-as-authorized-structure"></a>\n'
            "#### 11.1 Governance as Authorized Structure\n"
            "<details>\n<summary>Trace</summary>\n- Upstream: skip\n</details>\n\n"
            "<br>\n\n"
            "*In plain terms: gloss.*\n\n"
            "**Governance as authorized structure.** At principle layer, "
            "governance is how authorized systems are directed.\n"
        )
        findings = scan_text("core_01_c.md", text)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].line, 12)
        self.assertEqual(findings[0].heading, "11.1")

    def test_flags_colon_label_above_a_list(self) -> None:
        text = (
            "#### 9.1 Distributed Understanding\n\n"
            "*In plain terms: gloss.*\n\n"
            "**Distributed understanding:**\n"
            "- **What it is:** the community-facing facet of Pillar 3.\n"
        )
        self.assertEqual(self._labels(text), ["Distributed understanding"])

    def test_flags_label_that_adds_only_a_generic_word(self) -> None:
        text = (
            "#### 11.2 Segregation of Duties\n\n"
            "**Segregation-of-duties principle.** Oversight requires "
            "functional independence between action and its checking.\n"
        )
        self.assertEqual(self._labels(text), ["Segregation-of-duties principle"])

    def test_flags_label_covering_part_of_a_compound_heading(self) -> None:
        text = (
            "#### 12.6 Successor Responsibility and Formal-Structure Non-Escape\n\n"
            "**Formal-structure non-escape:**\n\n"
            "- **What does not extinguish duties:** receivership.\n"
        )
        self.assertEqual(self._labels(text), ["Formal-structure non-escape"])

    def test_accepts_functional_label(self) -> None:
        text = (
            "#### 14.2 Pro-Competition and Anti-Domination\n\n"
            "**What this subsection does:**\n\n"
            "- **What it states:** principle-layer rules.\n"
        )
        self.assertEqual(self._labels(text), [])

    def test_accepts_label_that_names_a_different_idea(self) -> None:
        text = (
            "#### 12.3 Misalignment Detection\n\n"
            "**Plural detection and review:**\n"
            "- Detection must not sit with one actor.\n"
        )
        self.assertEqual(self._labels(text), [])

    def test_accepts_heading_term_as_sentence_subject(self) -> None:
        text = (
            "### 14. Market Structure\n\n"
            "**[Market Structure](core_05_band_accountability.md#market-structure)** "
            "governs whether sentients can take part in productive systems.\n"
        )
        self.assertEqual(self._labels(text), [])

    def test_accepts_one_word_overlap(self) -> None:
        text = (
            "#### 12.5 Contingent Claims, Games of Chance, and Event-Contract Markets\n\n"
            "**Contingent settlement systems:**\n"
            "- Authorization must be proportionate.\n"
        )
        self.assertEqual(self._labels(text), [])

    def test_only_the_first_body_line_is_in_scope(self) -> None:
        text = (
            "#### 9.1 Distributed Understanding\n\n"
            "Understanding must scale with materiality and dependency.\n\n"
            "**Distributed understanding:**\n"
            "- the community-facing facet of Pillar 3.\n"
        )
        self.assertEqual(self._labels(text), [])

    def test_skips_widgets_gloss_and_fenced_code(self) -> None:
        text = (
            "#### 9.2 Institutional Development\n"
            "<details>\n<summary>Trace</summary>\n"
            "- **Institutional development:** widget line\n"
            "</details>\n\n"
            "<br>\n\n"
            "*In plain terms: institutional development is the gloss.*\n\n"
            "```\n**Institutional development:**\n```\n\n"
            "Organizations must learn from what their systems do.\n"
        )
        self.assertEqual(self._labels(text), [])


if __name__ == "__main__":
    unittest.main()
