#!/usr/bin/env python3
"""Tests for SECTION-CITE-NAME-01 (named § cites in body prose)."""

from __future__ import annotations

import unittest

from collections import Counter

from section_cite_name_audit import apply_baseline, baseline_key, scan_line, scan_text


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
                "[Preamble §3.3 Governance Layers](core_00.000_preamble.md#33-governance-layers)"
            ),
            [],
        )

    def test_flags_bare_preamble_cite(self) -> None:
        self.assertEqual(
            self._cites("See Preamble §3.3 for the two layers."),
            ["Preamble §3.3"],
        )

    def test_skips_headings_html_and_blockquotes(self) -> None:
        self.assertEqual(self._cites("#### 11.5 Contingent Claims"), [])
        self.assertEqual(self._cites('<a id="115-contingent-claims"></a>'), [])
        self.assertEqual(
            self._cites("> **Failed-test home:** §11.1 Alignment Requirement."),
            [],
        )

    def test_skips_adopted_implementation_family_section_tokens(self) -> None:
        self.assertEqual(
            self._cites("The CS-16.305 §10 log is not itself a finding."),
            [],
        )
        self.assertEqual(
            self._cites(
                "the **CS-16.305 — Critical system stewardship** §10 inspectable-action set"
            ),
            [],
        )

    def test_accepts_italic_title_inside_link(self) -> None:
        self.assertEqual(
            self._cites(
                "[Chapter Seven §2 *Four-Seat Constitutional Requirement*]"
                "(core_08.000_functional_independence_separation_of_duties.md#2-four-seat-constitutional-requirement)"
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


    def test_flags_unnamed_cites_in_table_rows(self) -> None:
        findings = scan_line(
            "core_01_c.md",
            1,
            "| **Dimension** | [Chapter Eleven §12](#12-scale); **§8.2** | note |",
        )
        self.assertEqual([f.cite for f in findings], ["Chapter Eleven §12", "§8.2"])
        self.assertTrue(all(f.table for f in findings))

    def test_accepts_named_cites_in_table_rows(self) -> None:
        self.assertEqual(
            self._cites(
                "| **Dimension** | [Chapter Eleven §12 Unified proportional LEQU scale](#12-scale) | note |"
            ),
            [],
        )

    def test_table_separator_and_header_rows_have_no_findings(self) -> None:
        self.assertEqual(self._cites("| --- | ---: | :--- |"), [])
        self.assertEqual(self._cites("| **What to look at** | **Where they are set out** |"), [])

    def test_baseline_grandfathers_table_cites_but_never_prose(self) -> None:
        row = "| a | [§11.5](#115-x) |"
        prose = "See [§11.5](#115-x)."
        table_findings = scan_line("core_01_c.md", 7, row)
        prose_findings = scan_line("core_01_c.md", 9, prose)
        baseline = Counter(baseline_key(f) for f in table_findings + prose_findings)
        kept, grandfathered = apply_baseline(table_findings + prose_findings, baseline)
        self.assertEqual(grandfathered, 1)
        self.assertEqual([f.cite for f in kept], ["§11.5"])
        self.assertFalse(kept[0].table)

    def test_baseline_survives_line_moves_but_not_row_edits(self) -> None:
        row = "| a | [§11.5](#115-x) |"
        moved = scan_line("core_01_c.md", 99, row)
        edited = scan_line("core_01_c.md", 7, "| a, edited | [§11.5](#115-x) |")
        baseline = Counter(baseline_key(f) for f in scan_line("core_01_c.md", 7, row))
        self.assertEqual(apply_baseline(moved, baseline)[1], 1)
        kept, grandfathered = apply_baseline(edited, baseline)
        self.assertEqual((len(kept), grandfathered), (1, 0))


if __name__ == "__main__":
    unittest.main()
