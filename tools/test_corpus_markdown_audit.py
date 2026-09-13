#!/usr/bin/env python3
"""Tests for MD-LIST-INTRO-01 bold list-intro headers."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_markdown_audit import check_list_intro_colon


class ListIntroColonTests(unittest.TestCase):
    def test_period_header_before_bullets_fails(self) -> None:
        lines = [
            "**Record and showing.**",
            "- **Not standing:** A written self-report is not standing measurement.",
        ]
        findings = check_list_intro_colon(lines, "core_example.md")
        self.assertEqual(len(findings), 1)
        self.assertIn("colon", findings[0])
        self.assertIn("core_example.md:1", findings[0])

    def test_colon_header_before_bullets_passes(self) -> None:
        lines = [
            "**Record and showing:**",
            "- **Not standing:** A written self-report is not standing measurement.",
        ]
        self.assertEqual(check_list_intro_colon(lines, "core_example.md"), [])

    def test_period_header_without_list_passes(self) -> None:
        lines = [
            "**Duty to resist.**",
            "",
            "<a id=\"operative-steward-statement-unlawful-instruction\"></a>",
            "> **Operative steward statement.** **Owner:** Chapter Nine §5.4.",
        ]
        self.assertEqual(check_list_intro_colon(lines, "core_example.md"), [])

    def test_list_item_label_period_fails(self) -> None:
        lines = [
            "**Record and showing:**",
            "- **Not standing.** A written self-report is not standing measurement.",
            "- **Verified record.** Verified failures record on the Contribution and Violation axes.",
            "- **No AI-only showing.** An evaluation run only on AI stewards does not prove this.",
        ]
        findings = check_list_intro_colon(lines, "core_example.md")
        self.assertEqual(len(findings), 3)
        self.assertIn("core_example.md:2", findings[0])
        self.assertIn("core_example.md:3", findings[1])
        self.assertIn("core_example.md:4", findings[2])

    def test_list_item_label_colon_passes(self) -> None:
        lines = [
            "**Record and showing:**",
            "- **Not standing:** A written self-report is not standing measurement.",
            "- **Verified record:** Verified failures record on the Contribution and Violation axes.",
            "- **No AI-only showing:** An evaluation run only on AI stewards does not prove this.",
        ]
        self.assertEqual(check_list_intro_colon(lines, "core_example.md"), [])

    def test_bare_list_item_sentence_without_nested_list_passes(self) -> None:
        lines = [
            "- **Preserve the record.**",
            "Ordinary paragraph follows.",
        ]
        self.assertEqual(check_list_intro_colon(lines, "core_example.md"), [])

    def test_bare_list_item_label_before_nested_list_fails(self) -> None:
        lines = [
            "- **Companions.**",
            "  - may add logging",
        ]
        findings = check_list_intro_colon(lines, "core_example.md")
        self.assertEqual(len(findings), 1)
        self.assertIn("core_example.md:1", findings[0])

    def test_fenced_example_is_skipped(self) -> None:
        lines = [
            "```",
            "**Record and showing.**",
            "- skip me",
            "```",
        ]
        self.assertEqual(check_list_intro_colon(lines, "core_example.md"), [])

    def test_heading_echo_runin_period_before_list_fails(self) -> None:
        lines = [
            "##### 9.1.2 Symmetric Costly Constraints",
            "<details>",
            "<summary>Trace</summary>",
            "- Upstream: skip widget lists",
            "</details>",
            "",
            "*In plain terms: gloss.*",
            "",
            "**Symmetric costly constraints.** Do not accept:",
            "",
            "- proxy reward",
        ]
        findings = check_list_intro_colon(lines, "core_example.md")
        self.assertEqual(len(findings), 1)
        self.assertIn("core_example.md:9", findings[0])

    def test_heading_echo_runin_colon_before_list_passes(self) -> None:
        lines = [
            "##### 9.1.2 Symmetric Costly Constraints",
            "**Symmetric costly constraints:** Do not accept:",
            "- proxy reward",
        ]
        self.assertEqual(check_list_intro_colon(lines, "core_example.md"), [])

    def test_runin_non_echo_period_is_out_of_scope(self) -> None:
        lines = [
            "##### 5.3 Something Else",
            "**Admission scope.** This subsection applies to:",
            "- cluster member",
        ]
        self.assertEqual(check_list_intro_colon(lines, "core_example.md"), [])

    def test_heading_echo_period_without_list_passes(self) -> None:
        lines = [
            "#### 9.4 Openness Aspiration",
            "**Openness aspiration.** Shared systems should aspire to open hardware.",
            "More prose, not a list.",
        ]
        self.assertEqual(check_list_intro_colon(lines, "core_example.md"), [])


if __name__ == "__main__":
    unittest.main()
