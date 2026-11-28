#!/usr/bin/env python3
"""Tests for REF-ARTICLES-GLOSS (one title per Chapter Four article cite)."""

from __future__ import annotations

import pathlib
import tempfile
import unittest

from apply_article_cite_gloss import check_file, gloss_line, load_titles

TITLES = load_titles()
VB = "Cross-System Fairness and Sustainability"


class GlossLineTests(unittest.TestCase):
    def test_bare_cite_gains_its_title(self) -> None:
        self.assertEqual(
            gloss_line("Article V-B applies here.", TITLES),
            f"**Article V-B** (*{VB}*) applies here.",
        )

    def test_repeated_title_after_wrapped_cite_is_repaired(self) -> None:
        # The line that slipped through before: stray emphasis and a second gloss.
        line = f"- ***Article V-B** (*{VB}*)* (*{VB}*) sets the factors."
        self.assertEqual(
            gloss_line(line, TITLES),
            f"- **Article V-B** (*{VB}*) sets the factors.",
        )

    def test_italic_and_bold_italic_cites_are_rewritten(self) -> None:
        want = f"- **Article V-B** (*{VB}*) sets the factors."
        self.assertEqual(gloss_line("- *Article V-B* sets the factors.", TITLES), want)
        self.assertEqual(gloss_line("- ***Article V-B*** sets the factors.", TITLES), want)

    def test_repeated_title_after_bold_link_is_removed(self) -> None:
        t = "Assembly, Dissent, and Peaceful Protest"
        line = f"**[Article XI-D](x.md#a) (*{t}*)** (*{t}*) \u2014 gathering"
        self.assertEqual(
            gloss_line(line, TITLES),
            f"**[Article XI-D](x.md#a) (*{t}*)** \u2014 gathering",
        )

    def test_repeated_title_with_double_closing_emphasis(self) -> None:
        t = "Justice Objective and Scope"
        line = f"**Article XX-A** (*{t}*)** (*{t}*)** (justice objective)"
        self.assertEqual(
            gloss_line(line, TITLES),
            f"**Article XX-A** (*{t}*)** (justice objective)",
        )

    def test_gloss_inside_link_text_repeated_after_link(self) -> None:
        line = f"[Article V-B (*{VB}*)](x.md#a) (*{VB}*) text"
        self.assertEqual(gloss_line(line, TITLES), f"[Article V-B (*{VB}*)](x.md#a) text")

    def test_clean_lines_are_unchanged(self) -> None:
        for line in (
            f"**Article V-B** (*{VB}*) sets the floor.",
            f"[Article V-B](x.md#a) (*{VB}*) sets the floor.",
            f"**Article V-A** (*Dependency Mapping and Resource-Flow Transparency*) and "
            f"**Article V-B** (*{VB}*).",
            f"**Article V-B** (*{VB}*) and, later, **Article V-B** (*{VB}*) again.",
            "- *Chapter Three* defines the terms.",
        ):
            self.assertEqual(gloss_line(line, TITLES), line, line)


VIA = "Dignity and Equal Moral Standing"
VIC = "Nondiscrimination"
VI = "Equal Basic Rights"


class PluralCiteTests(unittest.TestCase):
    """REF-ARTICLES-LIST: plural cites name each Article in the singular format."""

    def test_bold_pair_gains_titles(self) -> None:
        self.assertEqual(
            gloss_line("consistent with **Articles VI-A** and **VI-C** here.", TITLES),
            f"consistent with **Articles VI-A** (*{VIA}*) and **VI-C** (*{VIC}*) here.",
        )

    def test_plain_list_is_bolded_and_glossed(self) -> None:
        self.assertEqual(
            gloss_line("under Articles VI-A, VI-C, and VI here.", TITLES),
            f"under **Articles VI-A** (*{VIA}*), **VI-C** (*{VIC}*), and **VI** (*{VI}*) here.",
        )

    def test_single_bold_run_is_split(self) -> None:
        self.assertEqual(
            gloss_line("with **Articles VI-A and VI-C** where", TITLES),
            f"with **Articles VI-A** (*{VIA}*) and **VI-C** (*{VIC}*) where",
        )

    def test_span_needs_no_title_but_listed_article_does(self) -> None:
        self.assertEqual(
            gloss_line("with **Articles I–IV and VI** and Chapter Two.", TITLES),
            f"with **Articles I–IV** and **VI** (*{VI}*) and Chapter Two.",
        )

    def test_list_stops_before_a_chapter(self) -> None:
        self.assertEqual(
            gloss_line("with **Articles VI**, **VI-C**, and **Chapter Two** limits", TITLES),
            f"with **Articles VI** (*{VI}*), **VI-C** (*{VIC}*), and **Chapter Two** limits",
        )

    def test_clean_plural_lines_are_unchanged(self) -> None:
        for line in (
            f"**Articles VI-A** (*{VIA}*) and **VI-C** (*{VIC}*) apply.",
            "**Articles III-A** through **III-F** each apply.",
            "**Articles I–V** below state these floors.",
            "Articles **I** through **XXIX**, in five parts",
            "**Articles II-A** to **II-F** | designs",
            "**What Articles VI-A and VI-C require here**",
            "Articles named in its Trace",
        ):
            self.assertEqual(gloss_line(line, TITLES), line, line)


class CheckFileTests(unittest.TestCase):
    def _kinds(self, text: str) -> list[tuple[int, str]]:
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "x.md"
            path.write_text(text, encoding="utf-8")
            return [(n, kind) for n, _line, kind in check_file(path, TITLES, None)]

    def test_reports_each_kind(self) -> None:
        text = (
            f"- ***Article V-B** (*{VB}*)* (*{VB}*) sets the factors.\n"
            "Article V-B applies.\n"
            f"- ***Article V-B** (*{VB}*)* sets the factors.\n"
            f"**Article V-B** (*{VB}*) is fine.\n"
            "under **Articles VI-A** and **VI-C** here.\n"
        )
        self.assertEqual(
            self._kinds(text),
            [(1, "repeated"), (2, "bare"), (3, "wrapped"), (5, "plural")],
        )

    def test_headings_are_not_flagged(self) -> None:
        self.assertEqual(self._kinds("#### Article V-B: Cross-System Fairness and Sustainability\n"), [])


if __name__ == "__main__":
    unittest.main()
