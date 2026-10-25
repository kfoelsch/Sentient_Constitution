#!/usr/bin/env python3
"""Tests for REF-WRAPPER-01 (do not cite the layer wrapper)."""

from __future__ import annotations

import unittest

from wrapper_cite_audit import ALL_WRAPPERS, scan_line, scan_text


class WrapperCiteTests(unittest.TestCase):
    def _kinds(self, line: str, rel: str = "core_05.040_band_continuity.md", wrappers=("corpus_systems.md",)) -> list[str]:
        return [f.kind for f in scan_line(rel, 1, line, wrappers)]

    def test_flags_wrapper_link(self) -> None:
        self.assertEqual(self._kinds("- Read with: [corpus_systems.md](corpus_systems.md), CS-6.335."), ["link"])

    def test_flags_bold_wrapper_link_and_relative_target(self) -> None:
        self.assertEqual(self._kinds("**[corpus_systems.md](../corpus_systems.md)**, CS-6.335"), ["link"])

    def test_flags_wrapper_link_with_fragment(self) -> None:
        self.assertEqual(self._kinds("See [systems](corpus_systems.md#cs-6) for it."), ["link"])

    def test_flags_backticked_name(self) -> None:
        self.assertEqual(self._kinds("Follow `corpus_systems.md` CS-6.345 safety profiles."), ["text"])

    def test_counts_each_citation_on_a_line(self) -> None:
        line = "[corpus_systems.md](corpus_systems.md) and `corpus_systems.md`"
        self.assertEqual(self._kinds(line), ["link", "text"])

    def test_accepts_subfile_link(self) -> None:
        line = "[CS-6.335](corpus_systems/cs_06.335_resource_allocation_funding_stewardship.md)"
        self.assertEqual(self._kinds(line), [])

    def test_narrowed_wrapper_list_ignores_other_wrappers(self) -> None:
        self.assertEqual(self._kinds("[corpus_institutions.md](corpus_institutions.md)"), [])

    def test_default_checks_every_layer_wrapper(self) -> None:
        rel = "core_05.040_band_continuity.md"
        for name in ALL_WRAPPERS:
            findings = scan_text(rel, f"Body cites [{name}]({name}) here.\n")
            self.assertEqual([f.kind for f in findings], ["link"], name)

    def test_all_wrappers_flags_institutions(self) -> None:
        self.assertEqual(
            self._kinds("[corpus_institutions.md](corpus_institutions.md)", wrappers=ALL_WRAPPERS),
            ["link"],
        )

    def test_exempts_navigation_lines(self) -> None:
        for line in (
            "> This file is binding where [`corpus_systems.md`](../corpus_systems.md) is incorporated.",
            "| **CS** | [Systems and data](../corpus_systems.md) | Typing |",
            "**Previous file:** [corpus_systems.md](../corpus_systems.md)",
            "- [Systems and data landing page](../corpus_systems.md);",
            "## Section naming corpus_systems.md",
            "- [**CS**](../corpus_systems.md) — [System](../core_05.040_band_continuity.md#system) classification and stewardship",
        ):
            self.assertEqual(self._kinds(line), [], line)

    def test_inventory_entry_allowed_only_in_incorporating_files(self) -> None:
        line = "  - [corpus_systems.md](corpus_systems.md) (*systems implementation file*)"
        self.assertEqual(self._kinds(line, rel="core_18.000_incorporation.md"), [])
        self.assertEqual(self._kinds(line, rel="core_05.040_band_continuity.md"), ["link"])

    def test_citation_inside_incorporating_file_still_flagged(self) -> None:
        line = "Custody records follow *[corpus_systems.md](corpus_systems.md)*, CS-9.305."
        self.assertEqual(self._kinds(line, rel="core_18.000_incorporation.md"), ["link"])

    def test_fenced_code_is_skipped(self) -> None:
        text = "```\n[corpus_systems.md](corpus_systems.md)\n```\n"
        self.assertEqual(scan_text("core_01.000_values_principles.md", text), [])


if __name__ == "__main__":
    unittest.main()
