#!/usr/bin/env python3
"""Tests for VIS-CHART-SECNUM-09 (section number first in a chart box)."""

from __future__ import annotations

import unittest

from chart_section_number_audit import scan_text


def chart(*lines: str) -> str:
    body = "\n".join(f"    {line}" for line in lines)
    return f"```mermaid\nflowchart TB\n{body}\n```\n"


class ChartSectionNumberTests(unittest.TestCase):
    def _kinds(self, text: str) -> list[str]:
        return [finding.kind for finding in scan_text("core_07.md", text)]

    def test_accepts_number_first_title(self) -> None:
        text = chart('H["§5 Publish the statement<br/><br/>Who holds the offices"]')
        self.assertEqual(self._kinds(text), [])

    def test_accepts_multi_section_and_range_leads(self) -> None:
        text = chart(
            'A["§3, §4 Publish its charter<br/><br/>Purpose"]',
            'B["§3.1–§3.4 IIa — Always<br/><br/>Risk"]',
            'C["§7, §9.2 Full Certification"]',
        )
        self.assertEqual(self._kinds(text), [])

    def test_flags_title_with_trailing_dash_cite(self) -> None:
        text = chart('K["Keep it true — §7<br/><br/>Review on schedule"]')
        self.assertEqual(self._kinds(text), ["title"])

    def test_flags_title_with_cite_after_comma(self) -> None:
        text = chart('K["IIa, §3.1–§3.4 — Always<br/><br/>Risk"]')
        self.assertEqual(self._kinds(text), ["title"])

    def test_flags_parenthesized_cite_in_title(self) -> None:
        text = chart('subgraph NN["Non-Negotiable (§2.1)"]')
        self.assertEqual(self._kinds(text), ["title"])

    def test_flags_trailing_cite_on_content_line(self) -> None:
        text = chart(
            'P["Class P: voluntary<br/><br/>You do not need permission — §2"]'
        )
        self.assertEqual(self._kinds(text), ["trailing"])

    def test_flags_trailing_cite_on_wrapped_title_line(self) -> None:
        text = chart(
            'C["Publish its System Charter or<br/>Institutional Charter — §3, §4"]'
        )
        self.assertEqual(self._kinds(text), ["trailing"])

    def test_flags_trailing_cite_inside_parentheses(self) -> None:
        text = chart('Q{"Could it matter?<br/>(Class L or higher — §1)"}')
        self.assertEqual(self._kinds(text), ["trailing"])

    def test_accepts_content_line_that_starts_with_the_number(self) -> None:
        text = chart(
            'P["Class P: voluntary<br/><br/>§2 You do not need permission"]'
        )
        self.assertEqual(self._kinds(text), [])

    def test_accepts_bulleted_content_that_starts_with_the_number(self) -> None:
        text = chart('W["§3 Wellbeing<br/><br/>• §3.1 Fairness<br/>• §3.2 Aspiration"]')
        self.assertEqual(self._kinds(text), [])

    def test_ignores_edge_labels(self) -> None:
        text = chart(
            'A["§1 Start"] -->|"Becomes material — §1"| B["§2 Next"]',
            'B -.->|"§7"| A',
            'B -.->|VIb, §10 —<br/>verified inputs only| A',
        )
        self.assertEqual(self._kinds(text), [])

    def test_ignores_cites_qualified_by_another_document(self) -> None:
        text = chart(
            'D["2. Document<br/><br/>• Minimum record of the refusal<br/>(CS-14.305 §10)"]',
            'E["Outside — Chapter Nine §3<br/><br/>Checks scope"]',
        )
        self.assertEqual(self._kinds(text), [])

    def test_ignores_inline_cross_references_in_content(self) -> None:
        text = chart(
            'S["§16 Stewardship<br/><br/>• Carried downstream (§18, §19)<br/>• Role (§17)"]'
        )
        self.assertEqual(self._kinds(text), [])

    def test_ignores_boxes_without_section_numbers(self) -> None:
        text = chart(
            'X[["Chapter Nine — Alignment certification<br/><br/>Outside this chapter"]]',
            'Y["Articles VI–VII"]',
        )
        self.assertEqual(self._kinds(text), [])

    def test_ignores_text_outside_mermaid_fences(self) -> None:
        text = 'Publish it — §5\n\n```\nK["Keep it true — §7"]\n```\n'
        self.assertEqual(self._kinds(text), [])

    def test_reports_the_line_of_the_box(self) -> None:
        text = chart('A["§1 Fine"]', 'B["Late — §2"]')
        findings = scan_text("core_07.md", text)
        self.assertEqual([f.line for f in findings], [4])


if __name__ == "__main__":
    unittest.main()
