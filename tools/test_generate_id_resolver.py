#!/usr/bin/env python3
"""Tests for the derived ID resolver and section-to-section crossref."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from generate_id_resolver import build_payload
from generate_section_crossref import build_payload as build_section_crossref

ROOT = Path(__file__).resolve().parents[1]


class IdResolverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = build_payload(ROOT)

    def test_cannot_narrow_core(self) -> None:
        self.assertTrue(self.payload["cannot_narrow_core"])
        self.assertEqual(self.payload["status"], "process_support_not_binding")

    def test_family_and_section_ids_resolve(self) -> None:
        ids = self.payload["ids"]
        self.assertEqual(
            ids["CF-10"]["file"],
            "corpus_forum/cf_10_technical_specialist_forums_specialist_chambers.md",
        )
        self.assertEqual(
            ids["CJS-3.13"]["file"],
            "corpus_joint_structure/cjs_03a_accountability_operations.md",
        )
        self.assertEqual(
            ids["CS-4"]["file"],
            "corpus_systems/cs_04_critical_system_stewardship.md",
        )
        self.assertEqual(
            ids["CI-12"]["file"],
            "corpus_institutions/ci_12_cross_institution_coordination_escalation.md",
        )
        self.assertEqual(
            ids["Def.P1"]["file"],
            "core_05_band_participation.md",
        )
        self.assertEqual(ids["Def.P1"]["kind"], "cluster")

    def test_subsection_does_not_inherit_file_gloss(self) -> None:
        family = self.payload["ids"]["CF-10"]
        subsection = self.payload["ids"]["CF-10.1"]
        self.assertIn("gloss", family)
        if "gloss" in subsection:
            self.assertNotEqual(subsection["gloss"], family["gloss"])

    def test_topic_row_resolves_owner_and_read_with(self) -> None:
        row = next(item for item in self.payload["topics"] if item["id"] == "CJS-R09")
        owners = [item["id"] for item in row["primary_owners"]]
        self.assertIn("CF-10", owners)
        self.assertTrue(any(item.get("file") for item in row["primary_owners"]))
        read_ids = [item["id"] for item in row["read_with"]]
        self.assertTrue(read_ids)

    def test_definition_pointer_has_no_duty_text(self) -> None:
        proportionality = next(
            item for item in self.payload["definitions"] if item["term"] == "Proportionality"
        )
        self.assertTrue(proportionality["file"].startswith("core_05_"))
        self.assertTrue(proportionality["anchor"].startswith("#"))
        self.assertNotIn("must", proportionality)
        self.assertNotIn("components", proportionality)

    def test_steward_doors_are_pointers(self) -> None:
        doors = self.payload["steward_doors"]
        self.assertEqual(doors["index"], "implementation/steward_owner_clock_index.json")
        self.assertIn("standing_record", doors["case_ids"])
        self.assertNotIn("conflict_rule", doors["cases"][0])

    def test_pre_release_has_no_fossil_aliases(self) -> None:
        self.assertEqual(self.payload["aliases"], [])


class SectionCrossrefTests(unittest.TestCase):
    def test_section_edges_are_more_specific_than_files(self) -> None:
        payload = build_section_crossref(ROOT)
        self.assertGreater(payload["edge_count"], 0)
        sample = next(
            edge
            for edge in payload["edges"]
            if edge["source_file"].endswith(
                "cf_10_technical_specialist_forums_specialist_chambers.md"
            )
            and edge.get("target_anchor")
        )
        self.assertTrue(sample["source_header"] or sample["source_anchor"])
        self.assertTrue(sample["target_anchor"].startswith("#"))

    def test_freshness_roundtrip_id_resolver(self) -> None:
        first = build_payload(ROOT)
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / "id_resolver.json"
            out.write_text(json.dumps(first), encoding="utf-8")
            second = build_payload(ROOT)
        first.pop("generated_at", None)
        second.pop("generated_at", None)
        self.assertEqual(first["ids"]["CF-10"], second["ids"]["CF-10"])


if __name__ == "__main__":
    unittest.main()
