#!/usr/bin/env python3
"""Tests for MD-LIST-INTRO-01, MD-HTML-BLOCK-BLANK-01, and MD-GLOSS-CLOSE-01."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_markdown_audit import (
    check_gloss_italic_closed,
    check_html_block_following_blank,
    check_list_intro_colon,
)


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
            "> **Operative steward statement.** **Owner:** Chapter Ten §5.4.",
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
            "- **Adopted implementation text.**",
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

    def test_non_ascii_period_header_before_bullets_fails(self) -> None:
        lines = [
            "**अधिकार-तल न्यूनतम सिद्धांत।**",
            "- **एक:** पहला मद।",
        ]
        findings = check_list_intro_colon(lines, "translations/hi/example.md")
        self.assertEqual(len(findings), 1)
        self.assertIn("translations/hi/example.md:1", findings[0])

    def test_cjk_period_list_item_label_fails(self) -> None:
        lines = [
            "- **保全证据。** 不要让案件失效。",
        ]
        findings = check_list_intro_colon(lines, "translations/zh/example.md")
        self.assertEqual(len(findings), 1)
        self.assertIn("translations/zh/example.md:1", findings[0])

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


class HtmlBlockFollowingBlankTests(unittest.TestCase):
    def test_heading_directly_after_br_fails(self) -> None:
        lines = ["</details>", "", "<br>", "### Part B: Personhood", "", "Body."]
        errors = check_html_block_following_blank(lines, "core_example.md")
        self.assertEqual(len(errors), 1)
        self.assertIn("core_example.md:4:", errors[0])
        self.assertIn("MD-HTML-BLOCK-BLANK-01", errors[0])

    def test_blank_line_after_br_passes(self) -> None:
        lines = ["<br>", "", "### Part B: Personhood"]
        self.assertEqual(check_html_block_following_blank(lines, "core_example.md"), [])

    def test_br_variants_and_closing_details_fail(self) -> None:
        for tag in ("<br/>", "<br />", "<BR>", "</details>", "</div>"):
            with self.subTest(tag=tag):
                errors = check_html_block_following_blank([tag, "Prose."], "x.md")
                self.assertEqual(len(errors), 1)

    def test_html_directly_after_br_passes(self) -> None:
        lines = ["<br>", "<details>", "<summary>Trace</summary>", "</details>", ""]
        self.assertEqual(check_html_block_following_blank(lines, "core_example.md"), [])

    def test_fenced_example_is_skipped(self) -> None:
        lines = ["```markdown", "<br>", "### Heading", "```"]
        self.assertEqual(check_html_block_following_blank(lines, "core_example.md"), [])

    def test_inline_br_in_prose_passes(self) -> None:
        lines = ["Line one<br>", "Line two"]
        self.assertEqual(check_html_block_following_blank(lines, "core_example.md"), [])


class GlossItalicClosedTests(unittest.TestCase):
    def test_unclosed_gloss_with_nested_title_fails(self) -> None:
        lines = [
            "*In plain terms: **Article XXVIII** (*Transition Governance*) is the moving-day floor.",
            "",
        ]
        findings = check_gloss_italic_closed(lines, "core_example.md")
        self.assertEqual(len(findings), 1)
        self.assertIn("core_example.md:1", findings[0])
        self.assertIn("MD-GLOSS-CLOSE-01", findings[0])

    def test_unclosed_gloss_ending_in_link_fails(self) -> None:
        lines = ["*In plain terms: see [Section 5.1](#51-x)."]
        self.assertEqual(len(check_gloss_italic_closed(lines, "f.md")), 1)

    def test_closed_gloss_passes(self) -> None:
        lines = ["*In plain terms: **Article I** (*Survival*) is the floor.*"]
        self.assertEqual(check_gloss_italic_closed(lines, "f.md"), [])

    def test_trailing_bold_does_not_close_italic(self) -> None:
        self.assertEqual(len(check_gloss_italic_closed(["*In plain terms: a **b**"], "f.md")), 1)

    def test_bold_then_italic_closer_passes(self) -> None:
        self.assertEqual(check_gloss_italic_closed(["*In plain terms: a **b***"], "f.md"), [])

    def test_multiline_gloss_checks_last_line(self) -> None:
        lines = ["*In plain terms: first line", "second line.*", "", "next"]
        self.assertEqual(check_gloss_italic_closed(lines, "f.md"), [])
        lines = ["*In plain terms: first line", "second line.", "", "next"]
        self.assertEqual(len(check_gloss_italic_closed(lines, "f.md")), 1)

    def test_paragraph_stops_at_block_start(self) -> None:
        lines = ["*In plain terms: ok.*", "- a bullet", "<details>"]
        self.assertEqual(check_gloss_italic_closed(lines, "f.md"), [])

    def test_bold_and_other_italic_openers_are_out_of_scope(self) -> None:
        lines = ["**In plain terms: bold lead-in**", "*Plain-language version of Article XX", "*Note:* text"]
        self.assertEqual(check_gloss_italic_closed(lines, "f.md"), [])

    def test_fenced_example_is_skipped(self) -> None:
        lines = ["```", "*In plain terms: unclosed", "```"]
        self.assertEqual(check_gloss_italic_closed(lines, "f.md"), [])


if __name__ == "__main__":
    unittest.main()
