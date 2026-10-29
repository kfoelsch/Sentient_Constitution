#!/usr/bin/env python3
"""Tests for TIME-REF-01 (every time reference shows its bound and tier or class)."""

from __future__ import annotations

import unittest

from time_reference_audit import Finding, load_registry, scan_text

REG = load_registry()


def findings(text: str) -> list[Finding]:
    return scan_text("core_demo.md", text, REG)


class ScaledReferences(unittest.TestCase):
    def test_bound_and_tier_in_one_sentence_pass(self) -> None:
        text = "The review must begin inside the intake target of the matching tier, 2 days for Tier B.\n"
        self.assertEqual(findings(text), [])

    def test_outer_bound_with_tier_letter_passes(self) -> None:
        self.assertEqual(findings("Every matter ends by the Tier B outer bound, 14 days.\n"), [])

    def test_bare_duration_fails_with_both_missing(self) -> None:
        result = findings("The operator must act within 14 days.\n")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].missing, ("bound", "basis"))

    def test_bound_without_tier_or_class_fails(self) -> None:
        result = findings("The outer bound is 14 days.\n")
        self.assertEqual(result[0].missing, ("basis",))

    def test_tier_without_bound_fails(self) -> None:
        result = findings("Tier B matters take 14 days.\n")
        self.assertEqual(result[0].missing, ("bound",))

    def test_class_interval_passes(self) -> None:
        text = "A Class C system is recertified at its certification interval, every 1 year.\n"
        self.assertEqual(findings(text), [])

    def test_lowercase_letter_is_not_a_tier(self) -> None:
        self.assertEqual(findings("The outer bound for tier a is 7 days.\n")[0].missing, ("basis",))


class VagueReferences(unittest.TestCase):
    def test_reasonable_timeframe_fails(self) -> None:
        result = findings("The transition happens within a reasonable timeframe.\n")
        self.assertEqual(result[0].kind, "vague")

    def test_pinned_reasonable_timeframe_passes(self) -> None:
        text = "The transition is completed within 14 days, the Tier B outer bound.\n"
        self.assertEqual(findings(text), [])

    def test_promptly_fails_without_window(self) -> None:
        self.assertEqual(len(findings("Notice goes out promptly.\n")), 1)

    def test_qualitative_on_purpose_passes_only_in_its_file(self) -> None:
        text = "Problems are spotted and fixed promptly, before the damage sets in.\n"
        self.assertEqual(scan_text("core_06.000_rights_part_a.md", text, REG), [])
        self.assertEqual(len(scan_text("core_demo.md", text, REG)), 1)

    def test_qualitative_list_never_excuses_a_number(self) -> None:
        text = "Problems are spotted and fixed promptly, within 3 days.\n"
        self.assertTrue(scan_text("core_06.000_rights_part_a.md", text, REG))

    def test_quoted_mention_is_not_a_use(self) -> None:
        self.assertEqual(findings('"As soon as feasible" is not the clock.\n'), [])

    def test_prompt_review_name_gloss_is_not_a_reference(self) -> None:
        text = "Review begins inside the prompt-review window (*Prompt review*).\n"
        self.assertEqual(findings(text), [])


class FixedPeriods(unittest.TestCase):
    def test_registered_name_passes(self) -> None:
        self.assertEqual(findings("The watch period is twelve months.\n"), [])

    def test_cooling_off_period_passes(self) -> None:
        self.assertEqual(findings("The default cooling-off period is five years.\n"), [])

    def test_unregistered_fixed_length_fails(self) -> None:
        self.assertEqual(len(findings("The quiet period is five years.\n")), 1)


class ScaledWindows(unittest.TestCase):
    def test_fixed_length_beside_scaled_name_fails(self) -> None:
        result = findings("The Chartered Party has a 7-day response window.\n")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].missing, ("basis",))

    def test_scaled_name_with_tier_passes(self) -> None:
        text = "The response window is 2 days at Tier B.\n"
        self.assertEqual(findings(text), [])

    def test_scaled_name_with_matching_tier_passes(self) -> None:
        text = "The resolution window is the outer bound of the matching tier, 14 days at Tier B.\n"
        self.assertEqual(findings(text), [])

    def test_week_and_thirty_days_without_window_fail(self) -> None:
        self.assertEqual(len(findings("The Chartered Party gets a week to respond and thirty days to resolve it.\n")), 1)

    def test_scaled_name_without_a_number_is_not_a_reference(self) -> None:
        self.assertEqual(findings("The response window runs from the request.\n"), [])


class Structure(unittest.TestCase):
    def test_table_row_reads_header_and_lead_in(self) -> None:
        text = (
            "Stage targets by tier:\n"
            "\n"
            "| Stage | Tier B target |\n"
            "| --- | --- |\n"
            "| Intake | 2 days |\n"
        )
        self.assertEqual(findings(text), [])

    def test_table_without_tier_header_fails(self) -> None:
        text = "| Stage | Time |\n| --- | --- |\n| Intake | 2 days |\n"
        self.assertEqual(len(findings(text)), 1)

    def test_code_fence_and_headings_are_skipped(self) -> None:
        text = "# Section (thirty days)\n\n```\nwithin 14 days\n```\n"
        self.assertEqual(findings(text), [])

    def test_link_targets_are_not_scanned(self) -> None:
        text = "See [the rule](core_14.000_forum.md#7-timely-resolution-90-days).\n"
        self.assertEqual(findings(text), [])

    def test_calibration_context_is_exempt(self) -> None:
        self.assertEqual(findings("An 80-year human lifespan is the calibration anchor.\n"), [])

    def test_each_sentence_is_checked_on_its_own(self) -> None:
        text = "The Tier B outer bound is 14 days. The operator then has 30 days.\n"
        result = findings(text)
        self.assertEqual(len(result), 1)
        self.assertIn("30 days", result[0].text)


class Keys(unittest.TestCase):
    def test_key_ignores_line_number(self) -> None:
        a = findings("Intro.\n\nThe operator must act within 14 days.\n")[0]
        b = findings("The operator must act within 14 days.\n")[0]
        self.assertNotEqual(a.line, b.line)
        self.assertEqual(a.key(), b.key())

    def test_key_changes_when_text_changes(self) -> None:
        a = findings("The operator must act within 14 days.\n")[0]
        b = findings("The operator must act within 15 days.\n")[0]
        self.assertNotEqual(a.key(), b.key())


if __name__ == "__main__":
    unittest.main()
