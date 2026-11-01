#!/usr/bin/env python3
"""Tests for PART-CITE-CHAPTER-01: a Part-and-section citation outside its chapter names the chapter."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import part_cite_chapter_audit as audit

ROOT = Path(__file__).resolve().parents[1]

CH9_B = "core_09.005_system_alignment_certification_record_process.md"
CH9_C = "core_09.010_system_alignment_certification_record_recertification.md"
CH10 = "core_10.000_institutional_alignment_certification.md"
CH1_A = "core_01.000_values_principles.md"
CS_A = "corpus_systems/cs_06.305_information_types_and_handling.md"
CS_B = "corpus_systems/cs_06.310_data_classifications.md"
CJS = "corpus_joint_structure/cjs_05.110_oversight_operations.md"
CH9_A = "core_09.000_system_alignment_certification_evaluation.md"
CH5 = "core_05.000_definitions_home.md"
CS9_A = "corpus_systems/cs_09.305_system_classification_machinery.md"
CS9_B = "corpus_systems/cs_09.310_system_impact_classifications.md"
CS9_ILL = "corpus_systems/cs_09.320_system_alignment_certification_illustrations.md"

B_LINK = f"{CH9_B}#72-certification-defects-and-correction"
B_TEXT = "Part B §7.2 Certification Defects and Correction"

CHAPTERS = [
    ("CORE", CH1_A, "1.000"),
    ("CORE", CH9_B, "9.005"),
    ("CORE", CH9_C, "9.010"),
    ("CORE", CH10, "10.000"),
    ("CS", CS_A, "CS-6.305"),
    ("CS", CS_B, "CS-6.310"),
    ("CJS", CJS, "CJS-5.110"),
    ("CORE", CH9_A, "9.000"),
    ("CORE", CH5, "5.000"),
    ("CS", CS9_A, "CS-9.305"),
    ("CS", CS9_B, "CS-9.310"),
    ("CS", CS9_ILL, "CS-9.320"),
]

FILES = {
    CH1_A: "# CHAPTER 01, PART A: VALUES PRINCIPLES\n\n### 7. Duties\n\n#### 7.2 Another Section\n",
    CH9_B: (
        "# CHAPTER NINE, PART B: PROCESS\n\n### 7. Certification Outcomes\n\n"
        "#### 7.2 Certification Defects and Correction\n\nText.\n"
    ),
    CH9_C: "# CHAPTER NINE, PART C: RECORD\n\n### 8. Record\n",
    CH10: "# CHAPTER TEN: INSTITUTIONS\n\n",
    CS_A: "# CS-6.305, Part A: Information types\n\n## CS-6.305 §5 Cross-domain principles\n\n### 5.0 Access posture bands\n",
    CS_B: "# CS-6.310, Part B: Data classifications\n\n",
    CJS: "# CJS-5.110: Oversight operations\n\n",
    CH9_A: "# CHAPTER NINE, PART A: EVALUATION\n\n### 3. Whole-System Evaluation\n",
    CH5: "# CHAPTER FIVE: DEFINITIONS\n\n> It contains **Chapter Five, Part A** — reader guidance.\n",
    CS9_A: "# CS-9.305, Part A: Classification machinery\n\n",
    CS9_B: "# CS-9.310, Part B: Impact classifications\n\n",
    CS9_ILL: "# CS-9.320: Illustrations\n\n",
}


def make_root(tmp: str, extra: dict[str, str]) -> Path:
    root = Path(tmp)
    (root / "tools" / "architecture").mkdir(parents=True)
    (root / "tools" / "architecture" / "chapter_numbers.json").write_text(
        json.dumps({
            "chapters": [
                {"layer": layer, "destination_file": rel, "display_id": display}
                for layer, rel, display in CHAPTERS
            ]
        }),
        encoding="utf-8",
    )
    for rel, body in {**FILES, **extra}.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
    return root


def findings_for(extra: dict[str, str]) -> list[audit.Finding]:
    with tempfile.TemporaryDirectory() as tmp:
        root = make_root(tmp, extra)
        ctx = audit.build_context(root)
        return audit.scan(root, audit.default_scope(root), ctx)


def fixed_text(extra: dict[str, str], rel: str, *, clean: bool = True) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        root = make_root(tmp, extra)
        ctx = audit.build_context(root)
        rels = audit.default_scope(root)
        audit.apply_fixes(root, audit.scan(root, rels, ctx))
        if clean:
            assert not audit.scan(root, rels, ctx), "a second scan must be clean"
        return (root / rel).read_text(encoding="utf-8")


class PartCiteChapterTests(unittest.TestCase):
    def test_chapter_ten_bare_link_is_flagged_and_fixed(self) -> None:
        body = f"See [{B_TEXT}]({B_LINK}) for the rule.\n"
        found = findings_for({CH10: FILES[CH10] + body})
        self.assertEqual([f.kind for f in found], ["missing-chapter"])
        self.assertIn("Chapter Nine", found[0].message)
        self.assertEqual(
            fixed_text({CH10: FILES[CH10] + body}, CH10).splitlines()[-1],
            f"See [Chapter Nine {B_TEXT}]({B_LINK}) for the rule.",
        )

    def test_same_chapter_bare_cite_is_fine(self) -> None:
        body = f"See [{B_TEXT}]({B_LINK}) and [Part C §8 Record]({CH9_C}#8-record).\n"
        self.assertEqual(findings_for({CH9_B: FILES[CH9_B] + body}), [])

    def test_qualified_forms_are_accepted(self) -> None:
        link = f"({B_LINK})"
        lines = [
            f"[Chapter Nine {B_TEXT}]{link}",
            f"Chapter Nine, [{B_TEXT}]{link}",
            f"Chapter Nine's [{B_TEXT}]{link}",
            f"Chapter Nine [{B_TEXT}]{link}",
            f"**Chapter Nine** [{B_TEXT}]{link}",
            f"[Ch9 {B_TEXT}]{link}",
            f"[Chapter 9 {B_TEXT}]{link}",
        ]
        self.assertEqual(findings_for({CH10: FILES[CH10] + "\n".join(lines) + "\n"}), [])

    def test_wrong_chapter_is_reported_and_never_fixed(self) -> None:
        body = f"See [Chapter One {B_TEXT}]({B_LINK}).\n"
        found = findings_for({CH10: FILES[CH10] + body})
        self.assertEqual([f.kind for f in found], ["wrong-chapter"])
        self.assertIsNone(found[0].fix_col)
        self.assertIn("Chapter One", fixed_text({CH10: FILES[CH10] + body}, CH10, clean=False))
        self.assertNotIn("Chapter Nine", fixed_text({CH10: FILES[CH10] + body}, CH10, clean=False))

    def test_part_letter_that_disagrees_with_target_is_reported(self) -> None:
        body = f"See [Chapter Nine Part C §7.2 Certification Defects]({B_LINK}).\n"
        found = findings_for({CH10: FILES[CH10] + body})
        self.assertEqual([f.kind for f in found], ["part-mismatch"])
        self.assertIsNone(found[0].fix_col)

    def test_unlinked_repeat_is_fixed_when_its_title_confirms_the_chapter(self) -> None:
        body = f"[Chapter Nine {B_TEXT}]({B_LINK}) applies. Later, {B_TEXT} sets three things.\n"
        found = findings_for({CH10: FILES[CH10] + body})
        self.assertEqual([f.kind for f in found], ["missing-chapter"])
        self.assertTrue(
            fixed_text({CH10: FILES[CH10] + body}, CH10).splitlines()[-1].endswith(
                "Later, Chapter Nine Part B §7.2 Certification Defects and Correction sets three things."
            )
        )

    def test_unlinked_cite_with_no_chapter_to_infer_is_unresolved(self) -> None:
        found = findings_for({CH10: FILES[CH10] + "The Part A §99 rule applies.\n"})
        self.assertEqual([f.kind for f in found], ["unresolved"])
        self.assertIsNone(found[0].fix_col)

    def test_connector_run_inherits_the_chapter_but_a_second_link_does_not(self) -> None:
        run = "Chapter Nine Part A §3 and Part B §5 govern this.\n"
        self.assertEqual(findings_for({CH10: FILES[CH10] + run}), [])
        two_links = (
            f"[Chapter Nine {B_TEXT}]({B_LINK}) and [Part C §8 Record]({CH9_C}#8-record).\n"
        )
        found = findings_for({CH10: FILES[CH10] + two_links})
        self.assertEqual([f.kind for f in found], ["missing-chapter"])

    def test_adopted_implementation_family_uses_the_document_id(self) -> None:
        sibling = f"See [Part A §5.0 Access posture bands](cs_06.305_information_types_and_handling.md#50-access-posture-bands).\n"
        self.assertEqual(findings_for({CS_B: FILES[CS_B] + sibling}), [])
        cross = "See [Part A §5.0](../corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands).\n"
        self.assertEqual(
            fixed_text({CJS: FILES[CJS] + cross}, CJS).splitlines()[-1],
            "See [CS-6.305 Part A §5.0](../corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands).",
        )
        qualified = "See [CS-6.305 Part A §5.0](../corpus_systems/cs_06.305_information_types_and_handling.md#50-x).\n"
        self.assertEqual(findings_for({CJS: FILES[CJS] + qualified}), [])

    def test_code_headings_and_dated_rows_are_out_of_scope(self) -> None:
        body = (
            f"`[{B_TEXT}]({B_LINK})`\n"
            f"```\n[{B_TEXT}]({B_LINK})\n```\n"
            f"## Notes on [{B_TEXT}]({B_LINK})\n"
            f"| 2026-10-12 | v0.30 | Part B §7.2 moved ([{B_TEXT}]({B_LINK})) |\n"
        )
        self.assertEqual(findings_for({CH10: FILES[CH10] + body}), [])

    def test_write_is_idempotent_and_changes_only_the_qualifier(self) -> None:
        body = f"A [{B_TEXT}]({B_LINK}) and B [Part C §8 Record]({CH9_C}#8-record).\n"
        once = fixed_text({CH10: FILES[CH10] + body}, CH10)
        self.assertEqual(once.count("Chapter Nine"), 2)
        self.assertEqual(
            once.replace("Chapter Nine ", ""), FILES[CH10] + body,
        )

    # ---- bare Part mentions (no section number) ----------------------------------------------

    def test_the_reported_chapter_ten_sentence_is_flagged_not_fixed(self) -> None:
        body = (
            f"[Chapter Nine {B_TEXT}]({B_LINK}) applies. The findings take the place of the "
            "Part A evaluations that Part B lists.\n"
        )
        found = findings_for({CH10: FILES[CH10] + body})
        self.assertEqual([f.kind for f in found], ["unqualified-part", "unqualified-part"])
        self.assertTrue(all(f.fix_col is None for f in found))
        self.assertIn("Chapter Nine", found[0].message)  # the hint: the same line cites Chapter Nine
        fixed = (
            f"[Chapter Nine {B_TEXT}]({B_LINK}) applies. The findings take the place of the "
            "Chapter Nine Part A evaluations that Chapter Nine Part B lists.\n"
        )
        self.assertEqual(findings_for({CH10: FILES[CH10] + fixed}), [])

    def test_bare_part_inside_the_owning_chapter_is_fine(self) -> None:
        self.assertEqual(findings_for({CH9_B: FILES[CH9_B] + "Part A sets the evaluations; Parts B and C follow.\n"}), [])

    def test_bare_part_forms_are_each_one_mention(self) -> None:
        for sentence in ("Parts A–B apply.", "Part A and B apply.", "Part A or Part B applies.", "Parts A, B, and C apply."):
            found = findings_for({CH10: FILES[CH10] + sentence + "\n"})
            self.assertEqual([f.kind for f in found], ["unqualified-part"], sentence)

    def test_a_qualifier_on_a_run_covers_the_whole_run(self) -> None:
        for sentence in (
            "Chapter Nine Parts A–C apply.",
            "Chapter Nine (Parts A, B, and C) apply.",
            "**Ch 9:** Part B applies.",
            "**Chapter 9**: Part A and Part B apply.",
        ):
            self.assertEqual(findings_for({CH10: FILES[CH10] + sentence + "\n"}), [], sentence)

    def test_qualifier_naming_a_part_the_chapter_lacks_is_unknown_part(self) -> None:
        for sentence in ("Chapter Nine (Parts A, B, C, and D) govern.", "Chapter Ten Part B governs."):
            found = findings_for({CH1_A: FILES[CH1_A] + sentence + "\n"})
            self.assertEqual([f.kind for f in found], ["unknown-part"], sentence)

    def test_chapter_five_part_a_comes_from_its_own_placement_note(self) -> None:
        self.assertEqual(findings_for({CH10: FILES[CH10] + "Chapter Five Part A holds the compass.\n"}), [])
        found = findings_for({CH10: FILES[CH10] + "Chapter Five Part B holds nothing.\n"})
        self.assertEqual([f.kind for f in found], ["unknown-part"])

    def test_linked_bare_part_needs_the_chapter_and_the_right_letter(self) -> None:
        link = f"[Part B]({CH9_B})"
        found = findings_for({CH10: FILES[CH10] + f"See {link}.\n"})
        self.assertEqual([f.kind for f in found], ["missing-chapter"])
        self.assertEqual(
            fixed_text({CH10: FILES[CH10] + f"See {link}.\n"}, CH10).splitlines()[-1],
            f"See [Chapter Nine Part B]({CH9_B}).",
        )
        wrong = findings_for({CH10: FILES[CH10] + f"See [Chapter Nine Part D]({CH9_B}).\n"})
        self.assertEqual([f.kind for f in wrong], ["part-mismatch"])
        self.assertIn("is Part B, not Part D", wrong[0].message)
        not_a_part = findings_for({CH10: FILES[CH10] + f"See [Chapter Nine Part A]({CH10}).\n"})
        self.assertEqual([f.kind for f in not_a_part], ["part-mismatch"])
        self.assertEqual(
            [f.kind for f in findings_for({CH10: FILES[CH10] + f"See [Chapter One Part B]({CH9_B}).\n"})],
            ["wrong-chapter"],
        )

    def test_navigation_row_carries_the_chapter_across_links(self) -> None:
        row = f"| **Chapter 9**: [Part A]({CH9_A}) · [Part B]({CH9_B}) · [Part C]({CH9_C}) |\n"
        self.assertEqual(findings_for({CH10: FILES[CH10] + row}), [])

    def test_a_lettered_part_file_beside_the_mention_names_the_chapter(self) -> None:
        self.assertEqual(findings_for({CH10: FILES[CH10] + f"Plan: [{CH9_B}]({CH9_B}) (Part B).\n"}), [])
        wrong = findings_for({CH10: FILES[CH10] + f"Plan: [{CH9_B}]({CH9_B}) (Part C).\n"})
        self.assertEqual([f.kind for f in wrong], ["part-mismatch"])

    def test_family_document_id_must_match_the_letter(self) -> None:
        self.assertEqual(findings_for({CH10: FILES[CH10] + "CS-6.310 Part B holds the types.\n"}), [])
        self.assertEqual(
            [f.kind for f in findings_for({CH10: FILES[CH10] + "CS-6.310 Part A holds the types.\n"})],
            ["part-mismatch"],
        )
        pair = "This file contains **CS-6.305 and CS-6.310, Part A** and more.\n"
        self.assertEqual(findings_for({CS_A: FILES[CS_A] + pair}), [])

    def test_family_document_that_is_not_a_part_cannot_use_a_bare_letter(self) -> None:
        found = findings_for({CS9_ILL: FILES[CS9_ILL] + "The Part A requirements apply.\n"})
        self.assertEqual([f.kind for f in found], ["ambiguous-part"])
        self.assertEqual(findings_for({CS9_ILL: FILES[CS9_ILL] + "The Chapter Nine Part A requirements apply.\n"}), [])
        # a lettered family Part keeps the short form for its own family chapter
        self.assertEqual(findings_for({CS9_A: FILES[CS9_A] + "Part B holds the classes.\n"}), [])

    def test_link_text_chapter_must_match_the_target(self) -> None:
        wrong = findings_for({CH10: FILES[CH10] + f"See [Chapter One §3 Whole-System]({CH9_A}#3-whole).\n"})
        self.assertEqual([f.kind for f in wrong], ["link-chapter-mismatch"])
        self.assertIsNone(wrong[0].fix_col)
        for fine in (
            f"See [Chapter Nine §3 Whole-System]({CH9_A}#3-whole).",
            f"See [Chapters Two through Four]({CH9_A}).",
            "See [Chapter Seven and Chapter Eight](#5-charters).",
        ):
            self.assertEqual(findings_for({CH10: FILES[CH10] + fine + "\n"}), [], fine)

    def test_bare_mentions_in_code_headings_and_dated_rows_are_out_of_scope(self) -> None:
        body = "`Part A and Part B`\n```\nPart A\n```\n## Notes on Part B\n| 2026-10-12 | v0.30 | Part B moved |\n"
        self.assertEqual(findings_for({CH10: FILES[CH10] + body}), [])

    def test_corpus_has_no_unqualified_part_cites(self) -> None:
        ctx = audit.build_context(ROOT)
        found = audit.scan(ROOT, audit.default_scope(ROOT), ctx)
        self.assertEqual([], [f.render() for f in found])


if __name__ == "__main__":
    unittest.main()
