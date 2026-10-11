#!/usr/bin/env python3
"""Tests for TERM-SYSTEM-CLASS-01 (tools/apply_system_class_term.py)."""

from __future__ import annotations

import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import apply_system_class_term as tool  # noqa: E402


def fix(line: str, heading: bool = False) -> str:
    return tool.rewrite_line(line, in_heading=heading)[0]


class RewriteTests(unittest.TestCase):
    def test_bare_class_gains_system(self) -> None:
        self.assertEqual(fix("A class decides how deep."), "A system class decides how deep.")
        self.assertEqual(fix("Higher classes need more."), "Higher system classes need more.")

    def test_sentence_start_capital(self) -> None:
        self.assertEqual(fix("Class sets the depth."), "System class sets the depth.")
        self.assertEqual(fix("- Class never permits skipping."), "- System class never permits skipping.")

    def test_title_case_phrase(self) -> None:
        self.assertEqual(
            fix("see [§5.5.4 Class Scaling and Escalation](#554-x)."),
            "see [§5.5.4 System Class Scaling and Escalation](#554-x).",
        )

    def test_heading_rewrite_before_chicago(self) -> None:
        self.assertEqual(fix("Class Scaling and Escalation", heading=True), "System Class Scaling and Escalation")
        self.assertEqual(fix("How class scales every evaluation", heading=True), "How system class scales every evaluation")

    def test_chicago_title(self) -> None:
        cases = {
            "How system class scales every evaluation": "How System Class Scales Every Evaluation",
            "Illustrative data-handling application by system class (non-exhaustive)":
                "Illustrative Data-Handling Application by System Class (Non-Exhaustive)",
            "3.4.8. Illustrative whole-system application by system class (non-exhaustive)":
                "3.4.8. Illustrative Whole-System Application by System Class (Non-Exhaustive)",
            "System Class Scaling and Escalation": "System Class Scaling and Escalation",
            "System-Class-Scaled Infrastructure Assurance": "System-Class-Scaled Infrastructure Assurance",
            "What to check in CS-3 and where it ends": "What to Check in CS-3 and Where It Ends",
        }
        for src, want in cases.items():
            self.assertEqual(tool.chicago_title(src), want)

    def test_heading_line_gets_chicago(self) -> None:
        lines = ["#### 2.1 How class scales every evaluation", "#### 2.2 Pilot certification"]
        out = [new for _i, _o, new, _r in tool.process_lines(lines)]
        self.assertEqual(out, ["#### 2.1 How System Class Scales Every Evaluation", "#### 2.2 Pilot certification"])

    def test_link_text_quoting_heading_takes_new_title(self) -> None:
        pair = ("Illustrative class profiles (non-exhaustive)", "Illustrative System Class Profiles (Non-Exhaustive)")
        self.assertEqual(
            tool.retitle_link_text("§5.1.5 Illustrative class profiles (non-exhaustive)", pair),
            "§5.1.5 Illustrative System Class Profiles (Non-Exhaustive)",
        )
        self.assertEqual(tool.retitle_link_text("Part C class profiles", pair), "Part C system class profiles")

    def test_scaled_compound_is_hyphenated_whole(self) -> None:
        self.assertEqual(fix("class-scaled assurance"), "system-class-scaled assurance")
        self.assertEqual(fix("Class-Scaled Infrastructure Assurance", heading=True), "System-Class-Scaled Infrastructure Assurance")

    def test_named_levels_stay(self) -> None:
        for text in ("**Class A** systems", "Classes A, B, and C", "a Class P or Class L system", "class B"):
            self.assertEqual(fix(text), text)

    def test_already_qualified_stays(self) -> None:
        for text in ("the system class", "the system's class", "an impact class", "a risk class", "a class of harms", "first-class"):
            self.assertEqual(fix(text), text)

    def test_idempotent(self) -> None:
        once = fix("the class and its classes")
        self.assertEqual(fix(once), once)

    def test_protected_spans_untouched(self) -> None:
        text = 'see `class` and [x](file.md#a-class-b) <a id="x-class"></a> https://e.org/class'
        self.assertEqual(fix(text), text)

    def test_hyphenated_forms_go_to_review(self) -> None:
        line = "a class-wide remedy for class-based harm"
        new, review = tool.rewrite_line(line)
        self.assertEqual(new, line)
        self.assertEqual(len(review), 2)  # both hyphenated-after

    def test_handling_class_goes_to_review(self) -> None:
        new, review = tool.rewrite_line("under the applicable handling class")
        self.assertEqual(new, "under the applicable handling class")
        self.assertEqual(len(review), 1)

    def test_fenced_block_untouched(self) -> None:
        lines = ["```", "class X", "```", "class decides"]
        out = [new for _i, _o, new, _r in tool.process_lines(lines)]
        self.assertEqual(out, ["```", "class X", "```", "system class decides"])


class HeadingRenameTests(unittest.TestCase):
    def test_rename_anchor_and_retarget_links_across_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            (root / "core_08_a.md").write_text(
                '<a id="513-class-scaling"></a>\n\n##### 5.1.3 Class Scaling\n\nA class decides. See [x](#513-class-scaling).\n',
                encoding="utf-8",
            )
            (root / "other.md").write_text(
                "See [§5.1.3 Class Scaling](core_08_a.md#513-class-scaling).\n", encoding="utf-8"
            )
            slugs = tool.heading_slugs("##### 5.1.3 Class Scaling", "##### 5.1.3 System Class Scaling")
            self.assertEqual(slugs, ("513-class-scaling", "513-system-class-scaling"))
            renames = {"core_08_a.md": {slugs[0]: slugs[1]}}
            text, count = tool.retarget(root, "other.md", (root / "other.md").read_text(encoding="utf-8"), renames)
            self.assertEqual(count, 1)
            self.assertEqual(text, "See [§5.1.3 System Class Scaling](core_08_a.md#513-system-class-scaling).\n")
            anchored, n = tool.rename_anchor_ids(
                (root / "core_08_a.md").read_text(encoding="utf-8"), renames["core_08_a.md"]
            )
            self.assertEqual(n, 1)
            self.assertIn('<a id="513-system-class-scaling"></a>', anchored)


if __name__ == "__main__":
    unittest.main()
