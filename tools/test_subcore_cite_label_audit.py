#!/usr/bin/env python3
"""Tests for SUBCORE-CITE-01 (cites into subcore files say "Subcore N-X")."""

from __future__ import annotations

import unittest

from subcore_cite_label_audit import scan_text

LABELS = {
    "subcore_10.010_system_certification_record_contents.md": "Subcore 10-A",
    "subcore_04.050_data_types.md": "Subcore 4-A",
}
T10 = "subcore_10.010_system_certification_record_contents.md#3-x"
T4 = "subcore_04.050_data_types.md#10133-reserved-rights"


class SubcoreCiteLabelTests(unittest.TestCase):
    def _scan(self, text: str, rel: str = "core_08.000_x.md") -> list[str]:
        return scan_text(rel, text, LABELS)

    def test_flags_unlabelled_link(self) -> None:
        self.assertEqual(len(self._scan(f"See the [record contents]({T10}).")), 1)

    def test_accepts_label_in_link_text(self) -> None:
        self.assertEqual(self._scan(f"See [Subcore 10-A §3 Record Contents]({T10})."), [])

    def test_accepts_bold_label_and_plural(self) -> None:
        self.assertEqual(self._scan(f"See [**Subcore 10-A** §3]({T10}) and [Subcores 10-A and 4-A]({T4})."), [])

    def test_accepts_label_elsewhere_on_line(self) -> None:
        self.assertEqual(self._scan(f"[**Type I**]({T4}) (Subcore 4-A) applies."), [])

    def test_label_must_match_target(self) -> None:
        self.assertEqual(len(self._scan(f"[**Type I**]({T4}) (Subcore 10-A) applies.")), 1)

    def test_label_prefix_does_not_match_longer_number(self) -> None:
        self.assertEqual(len(self._scan(f"[**Type I**]({T4}) (Subcore 4-AB) applies.")), 1)

    def test_skips_chapter_three_definitions(self) -> None:
        self.assertEqual(self._scan("[Band](subcore_03.075_band_continuity.md#band)"), [])

    def test_skips_footers_headings_fences_and_self_links(self) -> None:
        text = (
            f"**Next file:** [next]({T10})\n"
            f"## Heading [x]({T10})\n"
            "```\n"
            f"[x]({T10})\n"
            "```\n"
        )
        self.assertEqual(self._scan(text), [])
        self.assertEqual(self._scan("[x](#3-x)\n[y](subcore_04.050_data_types.md#a)", "subcore_04.050_data_types.md"), [])

    def test_flags_unknown_subcore_file(self) -> None:
        self.assertEqual(len(self._scan("[x](subcore_99.010_unknown.md)")), 1)


if __name__ == "__main__":
    unittest.main()
