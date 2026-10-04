#!/usr/bin/env python3
"""Tests for CORPUS-REF-NAME-01 (named, resolving corpus references)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from corpus_ref_name_audit import Section, build_index, scan_line

CS_FILE = "corpus_systems/cs_10_demo.md"
CI_FILE = "corpus_institutions/ci_14_demo.md"
CS_LINK = "../corpus_systems/cs_10_demo.md"


def make_index() -> dict[str, Section]:
    return {
        "CS-10": Section({CS_FILE}, "Transition constitution and migration governance", {"cs-10"}),
        "CS-10.3": Section({CS_FILE}, "Gate criteria and advancement rules", {"cs-10-3-gate"}),
        "CS-11": Section({CS_FILE}, "Escalation and review", {"cs-11"}),
        "CS-11.10": Section({CS_FILE}, "Competency", {"cs-11-10", "10-inspectable-attributable-action"}),
        "CI-14.1": Section(
            {CI_FILE},
            "Interface — Article XXVII-D (Non-Compliant Property) (seizure, incentives)",
            {"ci-141"},
        ),
    }


class CorpusRefNameTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        for rel in (CS_FILE, CI_FILE, "core_06_demo.md"):
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("x\n", encoding="utf-8")
        self.index = make_index()

    def details(self, line: str) -> list[str]:
        return [f.detail for f in scan_line(self.root, "core_06_demo.md", 1, line, self.index)]

    def test_flags_unnamed_link(self) -> None:
        out = self.details("See [**CS-10.3**](corpus_systems/cs_10_demo.md#cs-10-3-gate).")
        self.assertEqual(len(out), 1)
        self.assertIn("no name", out[0])

    def test_accepts_gloss_after_link(self) -> None:
        self.assertEqual(
            self.details(
                "See [**CS-10.3**](corpus_systems/cs_10_demo.md#cs-10-3-gate) "
                "(*Gate criteria and advancement rules*)."
            ),
            [],
        )

    def test_accepts_name_in_link_text(self) -> None:
        self.assertEqual(
            self.details(
                "See [CS-10.3 Gate criteria and advancement rules]"
                "(corpus_systems/cs_10_demo.md#cs-10-3-gate)."
            ),
            [],
        )

    def test_flags_unnamed_bare_reference(self) -> None:
        self.assertEqual(len(self.details("Governed by **CS-10**.")), 1)

    def test_accepts_named_bare_reference(self) -> None:
        self.assertEqual(
            self.details("Governed by **CS-10** (*Transition constitution and migration governance*)."),
            [],
        )

    def test_flags_each_range_endpoint(self) -> None:
        out = self.details("See **CS-10** (*Transition constitution and migration governance*) through **CS-10.3**.")
        self.assertEqual(len(out), 1)

    def test_flags_wrong_name(self) -> None:
        out = self.details("See **CS-10.3** (*Transitional governance*).")
        self.assertIn("does not match", out[0])

    def test_accepts_short_name_for_long_heading(self) -> None:
        self.assertEqual(
            self.details("See **CI-14.1** (*seizure, incentives*)."),
            [],
        )

    def test_flags_unknown_id(self) -> None:
        self.assertIn("no corpus heading", self.details("See **CS-99** (*Whatever*).")[0])

    def test_flags_missing_anchor(self) -> None:
        out = self.details(
            "See [**CS-10.3**](corpus_systems/cs_10_demo.md#nope) (*Gate criteria and advancement rules*)."
        )
        self.assertIn("not an anchor", out[0])

    def test_flags_section_link_without_anchor(self) -> None:
        out = self.details(
            "See [**CS-10.3**](corpus_systems/cs_10_demo.md) (*Gate criteria and advancement rules*)."
        )
        self.assertIn("without its section anchor", out[0])

    def test_flags_wrong_file(self) -> None:
        out = self.details(
            "See [**CS-10.3**](corpus_institutions/ci_14_demo.md#cs-10-3-gate) "
            "(*Gate criteria and advancement rules*)."
        )
        self.assertTrue(any("is defined in" in d for d in out))

    def test_flags_missing_target_file(self) -> None:
        out = self.details("See [**CS-10**](corpus_systems/gone.md) (*Transition constitution and migration governance*).")
        self.assertTrue(any("does not exist" in d for d in out))

    def test_list_label_entry_is_exempt(self) -> None:
        self.assertEqual(self.details("- **CS-10.3** — gate criteria for each phase."), [])

    def test_ignores_code_spans_and_headings(self) -> None:
        self.assertEqual(self.details("Use `CS-10.3` here."), [])
        self.assertEqual(self.details("## CS-10.3 Heading"), [])

    def test_index_reads_heading_after_anchor_and_part_headings(self) -> None:
        d = self.root / "corpus_systems"
        (d / "cs_03_a.md").write_text("# CS-3, Part A: Machinery\n\n## CS-3.1 Purpose\n", encoding="utf-8")
        (d / "cs_03_b.md").write_text(
            "# CS-3, Part B: Impact\n\n## CS-3.8 Impact classes\n<a id=\"cs-3-8-late\"></a>\n",
            encoding="utf-8",
        )
        index = build_index(self.root)
        self.assertEqual(index["CS-3"].files, {"corpus_systems/cs_03_a.md", "corpus_systems/cs_03_b.md"})
        self.assertIn("cs-3-8-late", index["CS-3.8"].anchors)

    def test_accepts_named_subsection_cite_with_section_sign(self) -> None:
        self.assertEqual(
            self.details(
                "See [CS-11 §10 inspectable attributable action]"
                "(corpus_systems/cs_10_demo.md#10-inspectable-attributable-action)."
            ),
            [],
        )

    def test_accepts_part_letter_before_section_sign(self) -> None:
        self.assertEqual(
            self.details(
                "See [CS-11 Part A §10 inspectable attributable action]"
                "(corpus_systems/cs_10_demo.md#10-inspectable-attributable-action)."
            ),
            [],
        )

    def test_accepts_dash_name_after_bold_id(self) -> None:
        self.assertEqual(
            self.details("Scale: **CS-10 — Transition constitution and migration governance** applies."),
            [],
        )

    def test_flags_wrong_dash_name(self) -> None:
        out = self.details("Scale: **CS-10 — Something else entirely** applies.")
        self.assertIn("does not match", out[0])

    def test_placeholder_pattern_is_not_a_cite(self) -> None:
        self.assertEqual(self.details("Clusters are **oDef.*n*** = **CS-10.*n***."), [])

    def test_accepts_registry_or_other_part_name(self) -> None:
        self.index["CS-10"].aliases.add("Transition handling")
        self.assertEqual(self.details("See **CS-10** (*Transition handling*)."), [])

    def test_gloss_after_section_number_link_names_the_subsection(self) -> None:
        self.assertEqual(
            self.details(
                "See [CS-11 §10](corpus_systems/cs_10_demo.md#10-inspectable-attributable-action) "
                "(*Inspectable attributable action*)."
            ),
            [],
        )

    def test_reserved_unused_id_is_allowed(self) -> None:
        self.assertEqual(self.details("**CS-2** (*reserved family ID*) is unused."), [])

    def test_named_subsection_link_by_fragment_is_accepted(self) -> None:
        (self.root / CS_FILE).write_text("# x\n\n### Gate lane map\n", encoding="utf-8")
        self.assertEqual(
            self.details("See [CS-10.3 Gate lane map](corpus_systems/cs_10_demo.md#gate-lane-map)."),
            [],
        )

    def test_flags_subsection_name_that_disagrees_with_fragment(self) -> None:
        (self.root / CS_FILE).write_text("# x\n\n### Gate lane map\n", encoding="utf-8")
        out = self.details("See [CS-10.3 Something else](corpus_systems/cs_10_demo.md#gate-lane-map).")
        self.assertTrue(out)

    def test_flags_unnamed_subsection_cite(self) -> None:
        out = self.details(
            "See [CS-11 §10](corpus_systems/cs_10_demo.md#10-inspectable-attributable-action)."
        )
        self.assertEqual(len(out), 1)
        self.assertIn("has no name", out[0])

    def test_flags_wrong_subsection_name(self) -> None:
        out = self.details(
            "See [CS-11 §10 unrelated thing](corpus_systems/cs_10_demo.md#10-inspectable-attributable-action)."
        )
        self.assertIn("matches neither", out[0])

    def test_index_attaches_deep_body_anchors_to_section(self) -> None:
        d = self.root / "corpus_systems"
        (d / "cs_04_demo.md").write_text(
            "# CS-4: Demo\n\n## CS-4.10 Competency\n\nBody.\n\nMore body.\n\n"
            "<a id=\"10-inspectable-attributable-action\"></a>\n\n**Inspectable.**\n\n"
            "## CS-4.11 Next\n",
            encoding="utf-8",
        )
        index = build_index(self.root)
        self.assertIn("10-inspectable-attributable-action", index["CS-4.10"].anchors)
        self.assertNotIn("10-inspectable-attributable-action", index["CS-4.11"].anchors)


if __name__ == "__main__":
    unittest.main()
