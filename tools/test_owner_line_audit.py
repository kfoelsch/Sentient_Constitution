#!/usr/bin/env python3
"""Tests for the owner-line audit (OWNER-OPENING-01, NAV-IMPL-SUBFILE-01)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import owner_line_audit as ola

WIDGET = "<details>\n<summary>Corpus placement</summary>\n\n> placement\n\n</details>\n\n<br>\n\n"


def core(body: str, *, widget_claim: str = "") -> str:
    inner = f"> {widget_claim}\n" if widget_claim else "> placement\n"
    return f"# CHAPTER\n\n<details>\n<summary>x</summary>\n\n{inner}\n</details>\n\n<br>\n\n{body}"


def impl(body: str, *, headings: str = "## CS-4.1 Purpose\n") -> str:
    return f"# CS-4: Critical system stewardship\n\n{WIDGET}{body}\n\n{headings}"


class CoreTests(unittest.TestCase):
    def check(self, name: str, text: str) -> list[str]:
        return ola.check_core(name, text)

    def test_standard_line_passes(self):
        body = "Chapter Seven is the constitutional owner of **System Charters**.\n\n*In plain terms: x*\n\n### 1. A\n"
        self.assertEqual(self.check("core_07_charters.md", core(body)), [])

    def test_claim_only_in_widget_fails(self):
        body = "*In plain terms: x*\n\n### 1. A\n"
        text = core(body, widget_claim="Chapter Seven is the constitutional owner of **X**.")
        self.assertTrue(any("needs a visible" in f for f in self.check("core_07_charters.md", text)))

    def test_claim_after_gloss_fails(self):
        body = "*In plain terms: x*\n\nChapter Seven is the constitutional owner of **X**.\n"
        self.assertTrue(any("before the first gloss" in f for f in self.check("core_07_charters.md", core(body))))

    def test_wrong_chapter_fails(self):
        body = "Chapter Eight is the constitutional owner of **X**.\n\n*In plain terms: x*\n"
        self.assertTrue(any("must start 'Chapter Seven'" in f for f in self.check("core_07_charters.md", core(body))))

    def test_part_letter_required(self):
        body = "Chapter Nine is the constitutional owner of **X**.\n\n*In plain terms: x*\n"
        name = "core_09_a_system_alignment_certification_evaluation.md"
        self.assertTrue(any("name 'Part A'" in f for f in self.check(name, core(body))))
        ok = "Chapter Nine, **Part A**, is the constitutional owner of **X**.\n\n*In plain terms: x*\n"
        self.assertEqual(self.check(name, core(ok)), [])

    def test_chapter_six_part_a_may_omit_part(self):
        body = "Chapter Six is the constitutional owner of **Rights Floors**.\n\n### 1. A\n"
        self.assertEqual(self.check("core_06_rights_part_a.md", core(body)), [])
        self.assertTrue(self.check("core_06_rights_part_b.md", core(body)))

    def test_part_heading_before_claim_is_allowed(self):
        body = "### Part B: Personhood\n\nChapter Six, Part B, is the constitutional owner of **X**.\n\n*In plain terms: x*\n"
        self.assertEqual(self.check("core_06_rights_part_b.md", core(body)), [])

    def test_where_material_and_unbolded_domain_fail(self):
        a = "Chapter Seven is the constitutional owner of **X** where material.\n\n*In plain terms: x*\n"
        self.assertTrue(any("where material" in f for f in self.check("core_07_charters.md", core(a))))
        b = "Chapter Seven is the constitutional owner of X.\n\n*In plain terms: x*\n"
        self.assertTrue(any("in bold" in f for f in self.check("core_07_charters.md", core(b))))

    def test_bold_in_list_under_the_line_counts(self):
        body = "Chapter Nine, Part B, is the constitutional owner of these parts:\n\n- **Phase III:** review\n\n*In plain terms: x*\n"
        name = "core_09_b_system_alignment_certification_record_process.md"
        self.assertEqual(self.check(name, core(body)), [])

    def test_preamble_form(self):
        ok = "The Preamble is the constitutional owner of **the Model**.\n\n*In plain terms: x*\n"
        self.assertEqual(self.check("core_00_preamble.md", core(ok)), [])
        bad = "Chapter Zero is the constitutional owner of **the Model**.\n\n*In plain terms: x*\n"
        self.assertTrue(self.check("core_00_preamble.md", core(bad)))

    def test_non_owner_files_must_say_so(self):
        name = "core_10-13_application_vignettes.md"
        ok = "These vignettes are illustrative and own no rule.\n\n*In plain terms: x*\n"
        self.assertEqual(self.check(name, core(ok)), [])
        self.assertTrue(self.check(name, core("*In plain terms: x*\n")))

    def test_two_claims_before_the_first_section_fail(self):
        body = ("Chapter Seven is the constitutional owner of **X**.\n\n"
                "Chapter Seven is the constitutional owner of **Y**.\n\n### 1. A\n")
        self.assertTrue(any("once" in f for f in self.check("core_07_charters.md", core(body))))


class ImplTests(unittest.TestCase):
    def check(self, rel: str, text: str):
        return ola.check_impl(rel, text)

    def test_standard_sentence_passes(self):
        text = impl("This file is the systems implementation home for **CS-4** (*Critical system stewardship*).")
        findings, keys = self.check("corpus_systems/cs_04_x.md", text)
        self.assertEqual(findings, [])
        self.assertEqual(keys, [("CS-4", None)])

    def test_missing_sentence_fails(self):
        findings, _ = self.check("corpus_systems/cs_04_x.md", impl("Some prose."))
        self.assertTrue(any("needs a visible" in f for f in findings))

    def test_sentence_only_in_widget_fails(self):
        text = ("# CS-4: X\n\n<details>\n<summary>p</summary>\n\n"
                "This file is the systems implementation home for **CS-4**.\n\n</details>\n\n## CS-4.1 A\n")
        findings, _ = self.check("corpus_systems/cs_04_x.md", text)
        self.assertTrue(any("needs a visible" in f for f in findings))

    def test_after_first_heading_fails(self):
        text = "# CS-4: X\n\n## CS-4.1 A\n\nThis file is the systems implementation home for **CS-4**.\n"
        findings, _ = self.check("corpus_systems/cs_04_x.md", text)
        self.assertTrue(any("before the first '##'" in f for f in findings))

    def test_wrong_layer_and_prefix_fail(self):
        text = impl("This file is the forum implementation home for **CF-4** (*X*).")
        findings, _ = self.check("corpus_systems/cs_04_x.md", text)
        self.assertTrue(any("layer word" in f for f in findings))
        self.assertTrue(any("not a CS ID" in f for f in findings))

    def test_claimed_id_must_be_a_heading(self):
        text = impl("This file is the systems implementation home for **CS-5** (*X*).")
        findings, _ = self.check("corpus_systems/cs_04_x.md", text)
        self.assertTrue(any("not a heading in this file" in f for f in findings))

    def test_ids_after_the_first_sentence_are_pointers_not_claims(self):
        text = impl("This file is the systems implementation home for **CS-4** (*X*). The rest is in [f.md](f.md), **CS-9** (*Y*).")
        findings, keys = self.check("corpus_systems/cs_04_x.md", text)
        self.assertEqual(findings, [])
        self.assertEqual(keys, [("CS-4", None)])

    def test_part_letter_is_part_of_the_claim(self):
        text = ("# CS-2, Part A: X\n\n" + WIDGET +
                "This file is the systems implementation home for **CS-2** (*X*), **Part A**. It owns **y**.\n\n## CS-2.1 A\n")
        findings, keys = self.check("corpus_systems/cs_02_a_x.md", text)
        self.assertEqual(findings, [])
        self.assertEqual(keys, [("CS-2", "A")])

    def test_exempt_file_keeps_its_role_sentence(self):
        rel = "corpus_joint_structure/cjs_reader_guide.md"
        ok = "# Guide\n\nThis file is the joint-structure reader guide. It is reader guidance only.\n"
        self.assertEqual(self.check(rel, ok)[0], [])
        self.assertTrue(self.check(rel, "# Guide\n\nHello.\n")[0])


class CorpusTests(unittest.TestCase):
    def test_two_files_claiming_one_id_fail(self):
        root = Path(tempfile.mkdtemp())
        (root / "corpus_systems").mkdir()
        for n in ("a", "b"):
            (root / "corpus_systems" / f"cs_04_{n}.md").write_text(
                impl("This file is the systems implementation home for **CS-4** (*X*)."), encoding="utf-8")
        found = ola.audit(root)
        self.assertTrue(any("CS-4 is claimed by 2 files" in f for f in found))

    def test_copy_artifacts_are_ignored(self):
        root = Path(tempfile.mkdtemp())
        (root / "core_07_charters 2.md").write_text("junk\n", encoding="utf-8")
        self.assertEqual(ola.core_files(root), [])


if __name__ == "__main__":
    unittest.main()
