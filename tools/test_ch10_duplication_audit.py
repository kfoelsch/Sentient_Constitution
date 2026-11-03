#!/usr/bin/env python3
"""Tests for CH10-DUPLICATION-01 (a sentence copied from Chapter Nine into Chapter Ten)."""

from __future__ import annotations

import unittest

from ch10_duplication_audit import extract_sentences, near_copies, normalize

NINE = "core_09.010_system_alignment_certification_record_recertification.md"
TEN = "core_10.000_institutional_alignment_certification.md"


def sentences(path: str, text: str):
    return extract_sentences(path, text)


class Ch10DuplicationTests(unittest.TestCase):
    def test_noun_swap_is_a_copy(self) -> None:
        nine = "### 9.3.2 Failure\nA system holding provisional certification stays provisional and its count does not advance.\n"
        ten = "### 9.3.2 Failure\nAn Institution holding provisional certification stays provisional and its count does not advance.\n"
        found = near_copies(sentences(TEN, ten), sentences(NINE, nine))
        self.assertEqual(len(found), 1)
        self.assertGreaterEqual(found[0].ratio, 0.95)
        self.assertEqual(found[0].target.section, "9.3.2")

    def test_operator_and_governing_authority_count_as_the_same_word(self) -> None:
        nine = "The operator gives notice to the lead forum of each affected record and asks that the review reopen.\n"
        ten = "The Institution's governing authority gives notice to the lead forum of each affected record and asks that the review reopen.\n"
        self.assertEqual(len(near_copies(sentences(TEN, ten), sentences(NINE, nine))), 1)

    def test_different_meaning_is_not_a_copy(self) -> None:
        nine = "A system that is not yet operating has its challenge path opened when its first outcome is published.\n"
        ten = "An Institution with no stakeholders yet has its path opened at the record, whatever the outcome may be later.\n"
        self.assertEqual(near_copies(sentences(TEN, ten), sentences(NINE, nine)), [])

    def test_short_sentences_are_ignored(self) -> None:
        text = "Evasion is treated under the rule.\n"
        self.assertEqual(sentences(TEN, text), [])

    def test_details_widgets_and_code_fences_are_not_read(self) -> None:
        text = (
            "<details>\n<summary>Trace</summary>\nA system holding provisional certification stays provisional and its count does not advance.\n</details>\n"
            "```\nA system holding provisional certification stays provisional and its count does not advance.\n```\n"
        )
        self.assertEqual(sentences(TEN, text), [])

    def test_links_and_emphasis_do_not_hide_a_copy(self) -> None:
        nine = "A system holding provisional certification stays provisional and its count does not advance.\n"
        ten = "An **Institution** holding [provisional certification](core_05.040_band_continuity.md#provisional-certification) stays provisional and its count does not advance.\n"
        self.assertEqual(len(near_copies(sentences(TEN, ten), sentences(NINE, nine))), 1)

    def test_section_number_follows_the_last_heading(self) -> None:
        text = "### 10. Challenging\n#### 10.2 Paths\nThe record names the contest seat outside the Institution's own control line for every dispute.\n"
        found = sentences(TEN, text)
        self.assertEqual([s.section for s in found], ["10.2"])

    def test_normalize_collapses_the_swapped_words(self) -> None:
        self.assertEqual(normalize("The Institution's operator"), normalize("the system operator"))


if __name__ == "__main__":
    unittest.main()
