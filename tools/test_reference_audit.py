#!/usr/bin/env python3
"""Tests for the reference audit's semantic-rule staleness guard."""

from __future__ import annotations

import re
import unittest
from pathlib import Path
from unittest import mock

import reference_audit
from reference_audit import (
    SEMANTIC_RULES,
    canonical_map_from_paths,
    validate_semantic_rules,
)

ROOT = Path(__file__).resolve().parents[1]


class SemanticRuleGuardTests(unittest.TestCase):
    def live_map(self) -> dict[str, str]:
        return {
            "V": "Resource Allocation, Dependencies, and Ecosystem Funding",
            "VI": "Equal Basic Rights",
            "XVII": "System Lifecycle, Environments, and Reversibility",
            "XIX": "Standing and Participation Status",
            "XXIII": "Comprehensibility and Complexity Stewardship",
            "XXIV": "Root Cause Analysis and Adaptive Response",
            "XX": "Justice After Verified Violation",
        }

    def test_shipped_rules_match_the_live_corpus(self) -> None:
        """The real Chapter Six must still back every rule.

        This is the check that catches drift: renumber or retitle an Article
        and the rule pointing at it stops matching, here rather than in a
        report that tells authors to insert a wrong citation.
        """
        validate_semantic_rules(canonical_map_from_paths(ROOT, "core_06_rights_part_a.md"))

    def test_shipped_rules_match_their_articles(self) -> None:
        """Every rule keyword must appear in the heading it points at."""
        validate_semantic_rules(self.live_map())

    def test_every_rule_is_covered_by_this_test(self) -> None:
        expected = {article for _, article, _ in SEMANTIC_RULES}
        self.assertEqual(expected, set(self.live_map()))

    def test_renumbered_article_is_rejected(self) -> None:
        rules = [(re.compile(r"\bstanding\b", re.I), "XIII", "standing")]
        with mock.patch.object(reference_audit, "SEMANTIC_RULES", rules):
            with self.assertRaises(SystemExit) as caught:
                validate_semantic_rules(
                    {"XIII": "Right to Reliable and Trustworthy Systems"}
                )
        self.assertIn("standing", str(caught.exception))
        self.assertIn("XIII", str(caught.exception))

    def test_missing_article_is_rejected(self) -> None:
        rules = [(re.compile(r"\bstanding\b", re.I), "XCIX", "standing")]
        with mock.patch.object(reference_audit, "SEMANTIC_RULES", rules):
            with self.assertRaises(SystemExit) as caught:
                validate_semantic_rules({"XIX": "Standing and Participation Status"})
        self.assertIn("no longer exists", str(caught.exception))


if __name__ == "__main__":
    unittest.main()
