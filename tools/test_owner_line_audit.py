#!/usr/bin/env python3
"""Tests for the owner-line audit (OWNER-OPENING-01, NAV-IMPL-SUBFILE-01)."""

from __future__ import annotations

import tempfile
import unittest
from unittest import mock
from pathlib import Path

import owner_line_audit as ola

WIDGET = "<details>\n<summary>Corpus placement</summary>\n\n> placement\n\n</details>\n\n<br>\n\n"


def core(body: str, *, widget_claim: str = "") -> str:
    inner = f"> {widget_claim}\n" if widget_claim else "> placement\n"
    return f"# CHAPTER\n\n<details>\n<summary>x</summary>\n\n{inner}\n</details>\n\n<br>\n\n{body}"


def impl(body: str, *, headings: str = "## CS-21.305 §1 Purpose\n") -> str:
    return f"# CS-21.305: Critical system stewardship\n\n{WIDGET}{body}\n\n{headings}"


class CoreTests(unittest.TestCase):
    def check(self, name: str, text: str) -> list[str]:
        return ola.check_core(name, text)

    def test_standard_line_passes(self):
        body = "Chapter Five is the constitutional owner of **System Charters**.\n\n*In plain terms: x*\n\n### 1. A\n"
        self.assertEqual(self.check("core_05.000_charters.md", core(body)), [])

    def test_claim_only_in_widget_fails(self):
        body = "*In plain terms: x*\n\n### 1. A\n"
        text = core(body, widget_claim="Chapter Five is the constitutional owner of **X**.")
        self.assertTrue(any("needs a visible" in f for f in self.check("core_05.000_charters.md", text)))

    def test_claim_after_gloss_fails(self):
        body = "*In plain terms: x*\n\nChapter Seven is the constitutional owner of **X**.\n"
        self.assertTrue(any("before the first gloss" in f for f in self.check("core_05.000_charters.md", core(body))))

    def test_wrong_chapter_fails(self):
        body = "Chapter Six is the constitutional owner of **X**.\n\n*In plain terms: x*\n"
        self.assertTrue(any("must start 'Chapter Five'" in f for f in self.check("core_05.000_charters.md", core(body))))

    def test_part_letter_required(self):
        body = "Chapter Two is the constitutional owner of **X**.\n\n*In plain terms: x*\n"
        name = "core_02.000_values_principles.md"
        self.assertTrue(any("name 'Part A'" in f for f in self.check(name, core(body))))
        ok = "Chapter Two, **Part A**, is the constitutional owner of **X**.\n\n*In plain terms: x*\n"
        self.assertEqual(self.check(name, core(ok)), [])

    def test_live_heading_part_overrides_historical_registry(self):
        name = "core_02.040_stewardship_capacity_principles.md"
        body = "Chapter Two, Part E, is the constitutional owner of **X**.\n\n### 15. Stewardship\n"
        text = core(body).replace("# CHAPTER\n", "# CHAPTER 02, PART E: STEWARDSHIP\n", 1)
        self.assertEqual(self.check(name, text), [])
        self.assertTrue(any("name 'Part E'" in f for f in self.check(name, text.replace("Chapter Two, Part E,", "Chapter Two, Part C,"))))

    def test_chapter_six_part_a_may_omit_part(self):
        body = "Chapter Four is the constitutional owner of **Rights Floors**.\n\n### 1. A\n"
        self.assertEqual(self.check("core_04.000_rights_part_a.md", core(body)), [])
        self.assertTrue(self.check("core_04.010_rights_part_b.md", core(body)))

    def test_part_heading_before_claim_is_allowed(self):
        body = "### Part B: Personhood\n\nChapter Four, Part B, is the constitutional owner of **X**.\n\n*In plain terms: x*\n"
        self.assertEqual(self.check("core_04.010_rights_part_b.md", core(body)), [])

    def test_where_material_and_unbolded_domain_fail(self):
        a = "Chapter Five is the constitutional owner of **X** where material.\n\n*In plain terms: x*\n"
        self.assertTrue(any("where material" in f for f in self.check("core_05.000_charters.md", core(a))))
        b = "Chapter Five is the constitutional owner of X.\n\n*In plain terms: x*\n"
        self.assertTrue(any("in bold" in f for f in self.check("core_05.000_charters.md", core(b))))

    def test_bold_in_list_under_the_line_counts(self):
        body = "Chapter Nine is the constitutional owner of these parts:\n\n- **Phase III:** review\n\n*In plain terms: x*\n"
        name = "subcore_08.040_system_alignment_certification_forum_process_outcomes.md"
        self.assertEqual(self.check(name, core(body)), [])

    def test_stray_bold_marker_after_chapter_name_fails(self):
        # Leftover from a removed "**Part X**" label: "Chapter Nine**, is the ..."
        body = "Chapter Nine**, is the constitutional owner of these parts:\n\n- **Phase III:** review\n\n*In plain terms: x*\n"
        name = "subcore_08.040_system_alignment_certification_forum_process_outcomes.md"
        findings = self.check(name, core(body))
        self.assertTrue(any("unbalanced" in f for f in findings), findings)
        self.assertTrue(any("stray comma" in f for f in findings), findings)

    def test_stray_comma_without_bold_fails(self):
        body = "Chapter Five, is the constitutional owner of **System Charters**.\n\n*In plain terms: x*\n"
        findings = self.check("core_05.000_charters.md", core(body))
        self.assertTrue(any("stray comma" in f for f in findings), findings)

    def test_part_qualified_line_with_balanced_bold_passes(self):
        body = "Chapter Four, **Part B**, is the constitutional owner of **Rights B**.\n\n*In plain terms: x*\n"
        self.assertEqual(self.check("core_04.010_rights_part_b.md", core(body)), [])

    def test_preamble_form(self):
        ok = "The Preamble is the constitutional owner of **the Model**.\n\n*In plain terms: x*\n"
        self.assertEqual(self.check("core_00.000_preamble.md", core(ok)), [])
        bad = "Chapter Zero is the constitutional owner of **the Model**.\n\n*In plain terms: x*\n"
        self.assertTrue(self.check("core_00.000_preamble.md", core(bad)))

    def test_non_owner_files_must_say_so(self):
        name = "core_99.999_example_non_owner.md"
        ok = "These pages are illustrative and own no rule.\n\n*In plain terms: x*\n"
        with mock.patch.object(ola, "CORE_NON_OWNER", {name}):
            self.assertEqual(self.check(name, core(ok)), [])
            self.assertTrue(self.check(name, core("*In plain terms: x*\n")))

    def test_two_claims_before_the_first_section_fail(self):
        body = ("Chapter Five is the constitutional owner of **X**.\n\n"
                "Chapter Five is the constitutional owner of **Y**.\n\n### 1. A\n")
        self.assertTrue(any("once" in f for f in self.check("core_05.000_charters.md", core(body))))


class PreSectionOneTests(unittest.TestCase):
    """OWNER-OPENING-02: only ownership/front matter before section 1."""

    OWNER = "Chapter Five is the constitutional owner of **System Charters**.\n\n"

    def check(self, name: str, body: str) -> list[str]:
        return ola.check_pre_s1(name, core(body))

    def test_owner_line_then_section_one_passes(self):
        self.assertEqual(self.check("core_05.000_charters.md", self.OWNER + "### 1. A\n\n*In plain terms: x*\n"), [])

    def test_gloss_before_section_one_fails(self):
        findings = self.check("core_05.000_charters.md", self.OWNER + "*In plain terms: x*\n\n### 1. A\n")
        self.assertTrue(any("OWNER-OPENING-02" in f and "gloss" in f for f in findings), findings)

    def test_orientation_prose_before_section_one_fails_once_per_file(self):
        body = self.OWNER + "Three chapters work as one chain:\n\n- one\n- two\n\n### 1. A\n"
        findings = self.check("core_05.000_charters.md", body)
        self.assertEqual(len(findings), 1, findings)
        self.assertIn("+2 more", findings[0])

    def test_owner_paragraph_pointer_and_domain_list_pass(self):
        body = ("Chapter Two, Part A, is the constitutional owner of **X**. Collisions are in **Part C**.\n\n"
                "- **Y:** detail\n\n### 1. A\n")
        self.assertEqual(self.check("core_02.000_values_principles.md", body), [])

    def test_front_matter_passes(self):
        body = ('<a id="x"></a>\n### Part B: Thing\n\n<!-- note -->\n\n' + self.OWNER + "---\n\n### 1. A\n")
        self.assertEqual(self.check("core_04.010_rights_part_b.md", body), [])

    def test_chart_before_section_one_fails(self):
        body = self.OWNER + "```mermaid\nflowchart TB\n```\n\n### 1. A\n"
        self.assertTrue(any("code or chart" in f for f in self.check("core_05.000_charters.md", body)))

    def test_text_in_widget_is_ignored(self):
        body = self.OWNER + "<details>\n<summary>Guide</summary>\n\n> *In plain terms: x*\n\n</details>\n\n### 1. A\n"
        self.assertEqual(self.check("core_05.000_charters.md", body), [])

    def test_subcore_files_are_checked(self):
        body = "Subcore 3-A is the constitutional owner of **X**.\n\n*In plain terms: x*\n\n### 1. A\n"
        self.assertTrue(self.check("subcore_03.010_definition_structure.md", body))

    def test_files_without_section_one_and_preamble_are_skipped(self):
        body = self.OWNER + "*In plain terms: x*\n\n### 8. Later part\n"
        self.assertEqual(self.check("core_02.010_values_principles_continuity_aim.md", body), [])
        self.assertEqual(self.check("core_00.000_preamble.md", "Prose.\n\n### 1. The Model\n"), [])


class ImplTests(unittest.TestCase):
    def check(self, rel: str, text: str):
        return ola.check_impl(rel, text)

    def test_standard_sentence_passes(self):
        text = impl("This file is the systems implementation home for **CS-21.305** (*Critical system stewardship*).")
        findings, keys = self.check("corpus_systems/cs_04_x.md", text)
        self.assertEqual(findings, [])
        self.assertEqual(keys, [("CS-21.305", None)])

    def test_missing_sentence_fails(self):
        findings, _ = self.check("corpus_systems/cs_04_x.md", impl("Some prose."))
        self.assertTrue(any("needs a visible" in f for f in findings))

    def test_sentence_only_in_widget_fails(self):
        text = ("# CS-21.305: X\n\n<details>\n<summary>p</summary>\n\n"
                "This file is the systems implementation home for **CS-21.305**.\n\n</details>\n\n## CS-21.305 §1 A\n")
        findings, _ = self.check("corpus_systems/cs_04_x.md", text)
        self.assertTrue(any("needs a visible" in f for f in findings))

    def test_after_first_heading_fails(self):
        text = "# CS-21.305: X\n\n## CS-21.305 §1 A\n\nThis file is the systems implementation home for **CS-21.305**.\n"
        findings, _ = self.check("corpus_systems/cs_04_x.md", text)
        self.assertTrue(any("before the first '##'" in f for f in findings))

    def test_wrong_layer_and_prefix_fail(self):
        text = impl("This file is the forum implementation home for **CF-16.410** (*X*).")
        findings, _ = self.check("corpus_systems/cs_04_x.md", text)
        self.assertTrue(any("layer word" in f for f in findings))
        self.assertTrue(any("not a CS ID" in f for f in findings))

    def test_claimed_id_must_be_a_heading(self):
        text = impl("This file is the systems implementation home for **CS-4.345** (*X*).")
        findings, _ = self.check("corpus_systems/cs_04_x.md", text)
        self.assertTrue(any("not a heading in this file" in f for f in findings))

    def test_ids_after_the_first_sentence_are_pointers_not_claims(self):
        text = impl("This file is the systems implementation home for **CS-21.305** (*X*). The rest is in [f.md](f.md), **CS-4.335** (*Y*).")
        findings, keys = self.check("corpus_systems/cs_04_x.md", text)
        self.assertEqual(findings, [])
        self.assertEqual(keys, [("CS-21.305", None)])

    def test_part_letter_is_part_of_the_claim(self):
        text = ("# CS-4.305: X\n\n" + WIDGET +
                "This file is the systems implementation home for **CS-4.305** (*X*), **Part A**. It owns **y**.\n\n## CS-4.305 §1 A\n")
        findings, keys = self.check("corpus_systems/cs_02_a_x.md", text)
        self.assertEqual(findings, [])
        self.assertEqual(keys, [("CS-4.305", "A")])

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
                impl("This file is the systems implementation home for **CS-21.305** (*X*)."), encoding="utf-8")
        found = ola.audit(root)
        self.assertTrue(any("CS-21.305 is claimed by 2 files" in f for f in found))

    def test_copy_artifacts_are_ignored(self):
        root = Path(tempfile.mkdtemp())
        (root / "core_05.000_charters 2.md").write_text("junk\n", encoding="utf-8")
        self.assertEqual(ola.core_files(root), [])


if __name__ == "__main__":
    unittest.main()
