#!/usr/bin/env python3
"""Tests for MD-HEADING-TOPIC-01 (no heading restated as first topic sentence)."""

from __future__ import annotations

import unittest

from heading_echo_topic_audit import scan_text


class HeadingEchoTopicTests(unittest.TestCase):
    def _cites(self, text: str, rel_path: str = "core_01_c.md") -> list[str]:
        return [f"{finding.heading}:{finding.detail}" for finding in scan_text(rel_path, text)]

    def test_flags_title_only_self_cite(self) -> None:
        text = (
            '<a id="132-pro-competition-and-anti-domination"></a>\n'
            "#### 13.2 Pro-Competition and Anti-Domination\n"
            "<details>\n<summary>Trace</summary>\n- Upstream: skip\n</details>\n\n"
            "<br>\n\n"
            "*In plain terms: gloss.*\n\n"
            "**[§13.2 Pro-Competition and Anti-Domination]"
            "(#132-pro-competition-and-anti-domination):**\n\n"
            "- **What it states:** principle-layer rules.\n"
        )
        findings = scan_text("core_01_c.md", text)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].line, 12)
        self.assertIn("numbered § cite", findings[0].detail)

    def test_flags_self_cite_used_as_topic_sentence(self) -> None:
        text = (
            '<a id="10-governance-under-stewardship-discipline"></a>\n'
            "### 10. Governance Under Stewardship Discipline\n\n"
            "*In plain terms: gloss.*\n\n"
            "**[§10 Governance Under Stewardship Discipline]"
            "(#10-governance-under-stewardship-discipline)** carries Governance "
            "discipline downstream.\n"
        )
        self.assertTrue(self._cites(text))

    def test_accepts_functional_list_intro(self) -> None:
        text = (
            '<a id="132-pro-competition-and-anti-domination"></a>\n'
            "#### 13.2 Pro-Competition and Anti-Domination\n\n"
            "*In plain terms: gloss.*\n\n"
            "**What this subsection does:**\n\n"
            "- **What it states:** principle-layer rules.\n"
        )
        self.assertEqual(self._cites(text), [])

    def test_accepts_unnumbered_heading_echo_runin(self) -> None:
        text = (
            "##### 9.1.2 Symmetric Costly Constraints\n\n"
            "*In plain terms: gloss.*\n\n"
            "**Symmetric costly constraints:** The shared standard is not "
            "satisfied by applying costly tradeoffs only to machine agents.\n"
        )
        self.assertEqual(self._cites(text), [])

    def test_accepts_cross_chapter_same_number_cite(self) -> None:
        text = (
            '<a id="4-3-voluntary-public-accountability-expression"></a>\n'
            "### 4.3 Voluntary public accountability expression (anti-constitutional)\n\n"
            "*In plain terms: gloss.*\n\n"
            "[Chapter Nine §4.3](core_09_standing_integration.md"
            "#43-voluntary-public-accountability-expression) supplies the "
            "general rule.\n"
        )
        self.assertEqual(
            self._cites(text, "core_10_a_misconduct_designation.md"),
            [],
        )

    def test_accepts_later_self_cite_after_real_topic_sentence(self) -> None:
        text = (
            "#### 13.2 Pro-Competition and Anti-Domination\n\n"
            "Shared-system capacity must stay contestable in practice.\n\n"
            "See [§13.2 Pro-Competition and Anti-Domination]"
            "(#132-pro-competition-and-anti-domination) for the parent rule.\n"
        )
        self.assertEqual(self._cites(text), [])

    def test_accepts_child_section_cite_as_first_line(self) -> None:
        text = (
            "#### 13.2 Pro-Competition and Anti-Domination\n\n"
            "[§13.2.1 Pro-Competition Duties (Dos)](#1321-pro-competition-duties-dos) "
            "states the duties.\n"
        )
        self.assertEqual(self._cites(text), [])

    def test_skips_widgets_and_plain_terms_gloss(self) -> None:
        text = (
            "#### 13.2 Pro-Competition and Anti-Domination\n"
            "<details>\n<summary>Trace</summary>\n"
            "- [§13.2 Pro-Competition and Anti-Domination]"
            "(#132-pro-competition-and-anti-domination)\n"
            "</details>\n\n"
            "*In plain terms: this names the section.*\n\n"
            "Governing systems must preserve contestable participation.\n"
        )
        self.assertEqual(self._cites(text), [])


if __name__ == "__main__":
    unittest.main()
