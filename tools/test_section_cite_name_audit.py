#!/usr/bin/env python3
"""Tests for SECTION-CITE-NAME-01 (named § cites in body prose)."""

from __future__ import annotations

import unittest

from section_cite_name_audit import scan_line, scan_text


class SectionCiteNameTests(unittest.TestCase):
    def _cites(self, line: str) -> list[str]:
        return [finding.cite for finding in scan_line("core_01_c.md", 1, line)]

    def test_flags_number_only_link(self) -> None:
        self.assertEqual(
            self._cites("[§11.5](#115-contingent-claims-games-of-chance-and-event-contract-markets)"),
            ["§11.5"],
        )

    def test_flags_chapter_prefixed_number_only_link(self) -> None:
        self.assertEqual(
            self._cites("[Chapter One §11.5](#115-contingent-claims)"),
            ["Chapter One §11.5"],
        )

    def test_accepts_title_in_link_text(self) -> None:
        self.assertEqual(
            self._cites(
                "[§11.5 Contingent Claims, Games of Chance, and Event-Contract Markets]"
                "(#115-contingent-claims-games-of-chance-and-event-contract-markets)"
            ),
            [],
        )

    def test_accepts_parenthetical_gloss_after_link(self) -> None:
        self.assertEqual(
            self._cites(
                "[§11.5](#115-contingent-claims) (*Contingent Claims, Games of Chance, and Event-Contract Markets*)"
            ),
            [],
        )

    def test_flags_bare_bold_range(self) -> None:
        self.assertEqual(
            self._cites("the rules in **§§11.1–11.6** and **§§13.1–13.3**."),
            ["§§11.1–11.6", "§§13.1–13.3"],
        )

    def test_does_not_treat_and_or_through_as_a_title(self) -> None:
        self.assertEqual(
            self._cites("the rules in §§11.1–11.6 and §§13.1–13.3."),
            ["§§11.1–11.6", "§§13.1–13.3"],
        )

    def test_accepts_named_range_endpoints(self) -> None:
        self.assertEqual(
            self._cites(
                "rules in [§11.1 Alignment Requirement](#111-alignment-requirement) "
                "through [§11.6 Successor Responsibility and Formal-Structure Non-Escape]"
                "(#116-successor-responsibility-and-formal-structure-non-escape)."
            ),
            [],
        )

    def test_accepts_unlinked_title_after_number(self) -> None:
        self.assertEqual(
            self._cites("See §11.1 Alignment Requirement for the general standard."),
            [],
        )

    def test_accepts_preamble_cite_with_title(self) -> None:
        self.assertEqual(
            self._cites(
                "[Preamble §3.3 Governance Layers](core_00_preamble.md#33-governance-layers)"
            ),
            [],
        )

    def test_flags_bare_preamble_cite(self) -> None:
        self.assertEqual(
            self._cites("See Preamble §3.3 for the two layers."),
            ["Preamble §3.3"],
        )

    def test_skips_headings_tables_html_and_blockquotes(self) -> None:
        self.assertEqual(self._cites("#### 11.5 Contingent Claims"), [])
        self.assertEqual(self._cites("| §11.5 | special application |"), [])
        self.assertEqual(self._cites('<a id="115-contingent-claims"></a>'), [])
        self.assertEqual(
            self._cites("> **Failed-test home:** §11.1 Alignment Requirement."),
            [],
        )

    def test_skips_companion_family_section_tokens(self) -> None:
        self.assertEqual(
            self._cites("The CS-4 §10 log is not itself a finding."),
            [],
        )
        self.assertEqual(
            self._cites(
                "the **CS-4 — Critical system stewardship** §10 inspectable-action set"
            ),
            [],
        )

    def test_accepts_italic_title_inside_link(self) -> None:
        self.assertEqual(
            self._cites(
                "[Chapter One §10.2 *Segregation of duties*]"
                "(core_01_c_stewardship_capacity_principles.md#102-segregation-of-duties)"
            ),
            [],
        )

    def test_skips_backticks_and_details_widgets(self) -> None:
        self.assertEqual(self._cites("The token is `§11.5` in code."), [])
        findings = scan_text(
            "core_01_c.md",
            "<details>\n"
            "<summary>Trace</summary>\n\n"
            "- [§11.5](#115-contingent-claims)\n"
            "</details>\n\n"
            "[§11.5](#115-contingent-claims)\n",
        )
        self.assertEqual([finding.cite for finding in findings], ["§11.5"])
        self.assertEqual(findings[0].line, 7)


if __name__ == "__main__":
    unittest.main()
