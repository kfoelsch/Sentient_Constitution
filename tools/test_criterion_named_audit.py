#!/usr/bin/env python3
"""Tests for CRITERION-NAMED-01 (a numbered anti-constitutional-misconduct criterion with no name)."""

from __future__ import annotations

import unittest

from criterion_named_audit import NAMES, fix_text, numbers_in, scan_text


def found(line: str, following: str = "") -> list[str]:
    text = line + "\n" + following
    return [f.phrase for f in scan_text("core_14.005_misconduct_pattern_applications.md", text)]


class CriterionNamedTests(unittest.TestCase):
    def test_numbers_expand_lists_and_ranges(self) -> None:
        self.assertEqual(numbers_in("3"), [3])
        self.assertEqual(numbers_in("1 and 2"), [1, 2])
        self.assertEqual(numbers_in("5**"), [5])
        self.assertEqual(numbers_in("1–4"), [1, 2, 3, 4])
        self.assertEqual(numbers_in("**1** **through** **4**"), [1, 2, 3, 4])
        self.assertEqual(numbers_in("3, 4, and 6"), [3, 4, 6])

    def test_flags_a_bare_number(self) -> None:
        self.assertEqual(found("It satisfies **criterion 3** where concentration is a workaround."), ["criterion 3**"])
        self.assertEqual(found("Criterion 4 applies."), ["Criterion 4"])

    def test_flags_groups_and_ranges(self) -> None:
        self.assertEqual(found("Criteria 1 and 2 apply."), ["Criteria 1 and 2"])
        self.assertEqual(found("It may implicate **criteria 1–4**."), ["criteria 1–4**"])
        self.assertEqual(found("Routes through **criteria 5** and **6** of the same section."), ["criteria 5** and **6**"])
        self.assertEqual(found("**criteria 1** **through** **4** on change pathways"), ["criteria 1** **through** **4**"])

    def test_flags_each_of_two_references_on_one_line(self) -> None:
        self.assertEqual(len(found("both **criterion 5** and **criterion 6** need proof")), 2)

    def test_accepts_the_name_after_the_number(self) -> None:
        self.assertEqual(found("It satisfies **criterion 3** (*Material rollback effect*) where it rolls back."), [])
        self.assertEqual(found("- **Criterion 4** (*Causally significant conduct*) — where it contributes."), [])
        self.assertEqual(found("Chapter Fourteen criterion 3 (*Material rollback effect*),"), [])

    def test_accepts_every_name_of_a_group_or_range(self) -> None:
        line = "**Criteria 1 and 2** (*Willful deceptive intent* and *Knowing falsification or suppression*) apply."
        self.assertEqual(found(line), [])
        rng = (
            "criteria 1–4 (*Willful deceptive intent*; *Knowing falsification or suppression*; "
            "*Material rollback effect*; and *Causally significant conduct*) show up."
        )
        self.assertEqual(found(rng), [])

    def test_flags_a_group_that_names_only_some(self) -> None:
        self.assertEqual(len(found("criteria 1 and 2 (*Willful deceptive intent*) apply.")), 1)
        self.assertEqual(len(found("criteria 1–4 (*Willful deceptive intent*) apply.")), 1)

    def test_accepts_a_definition_list_introduction(self) -> None:
        text = (
            "- **Criteria 5** and **6** cover forcible takeover:\n"
            "  - 5. **Insurrection or material forcible subversion:**\n"
            "  - 6. **Operative nullification:**\n"
        )
        self.assertEqual(found(text), [])
        self.assertEqual(len(found("- **Criteria 5** and **6** cover forcible takeover:\n  - 5. Something else.\n")), 1)

    def test_ignores_words_without_a_number_and_other_numbers(self) -> None:
        self.assertEqual(found("Assess the section 3 criteria and each criterion in turn."), [])
        self.assertEqual(found("Criteria apply to 5 cases."), [])
        self.assertEqual(found("It is criterion-based."), [])

    def test_ignores_inline_code_link_targets_fences_and_move_log(self) -> None:
        self.assertEqual(found("See `criterion 3` and [the rule](core_14_criterion_3.md)."), [])
        text = "```\ncriterion 3\n```\ncriterion 3\n"
        self.assertEqual([f.line for f in scan_text("core_14.000_misconduct_designation.md", text)], [4])
        self.assertEqual(scan_text("doc_architecture.md", "criterion 3\n"), [])

    def test_fix_inserts_names(self) -> None:
        text = "It satisfies **criterion 4** where it blocks.\nCriteria 1 and 2 apply.\n"
        new, n = fix_text("core_14.005_misconduct_pattern_applications.md", text)
        self.assertEqual(n, 2)
        self.assertIn("**criterion 4** (*Causally significant conduct*) where", new)
        self.assertIn(
            "Criteria 1 and 2 (*Willful deceptive intent* and *Knowing falsification or suppression*) apply.", new
        )
        self.assertEqual(scan_text("core_14.005_misconduct_pattern_applications.md", new), [])

    def test_fix_uses_or_for_an_or_group_and_semicolons_for_a_range(self) -> None:
        new, _ = fix_text("core_14.000_misconduct_designation.md", "It never excuses **criteria 5** or **6** conduct.\n")
        self.assertIn("**criteria 5** or **6** (*Insurrection or material forcible subversion* or *Operative nullification*) conduct", new)
        new, _ = fix_text("core_14.000_misconduct_designation.md", "covered by criteria 1–4.\n")
        self.assertIn(
            "criteria 1–4 (*Willful deceptive intent*; *Knowing falsification or suppression*; "
            "*Material rollback effect*; and *Causally significant conduct*).",
            new,
        )

    def test_fix_leaves_plain_names_inside_an_italic_span(self) -> None:
        new, _ = fix_text("core_14.000_misconduct_designation.md", "(*change-path conduct may implicate criteria 3*)\n")
        self.assertEqual(scan_text("core_14.000_misconduct_designation.md", new), [])

    def test_fix_is_idempotent_and_skips_an_existing_gloss(self) -> None:
        text = "It meets criterion 3 (a workaround that rolls back protections).\n"
        new, n = fix_text("core_01.000_values_principles.md", text)
        self.assertEqual((new, n), (text, 0))
        self.assertEqual(len(scan_text("core_01.000_values_principles.md", text)), 1)
        once, _ = fix_text("core_14.005_misconduct_pattern_applications.md", "Criterion 6 applies.\n")
        twice, n2 = fix_text("core_14.005_misconduct_pattern_applications.md", once)
        self.assertEqual((once, 0), (twice, n2))

    def test_names_cover_all_six_criteria(self) -> None:
        self.assertEqual(sorted(NAMES), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
