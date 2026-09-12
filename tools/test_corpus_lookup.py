#!/usr/bin/env python3
"""Tests for tools/corpus_lookup.py."""

from __future__ import annotations

import io
import json
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import corpus_lookup

ROOT = Path(__file__).resolve().parents[1]
CF10 = "corpus_forum/cf_10_technical_specialist_forums_specialist_chambers.md"
CF10_ANCHOR = "#cf-10-technical-specialist-forums-and-specialist-chambers"
GLOSS_NEEDLE = "unaccountable parallel judiciary"


def run_cli(*args: str) -> tuple[int, dict]:
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = corpus_lookup.main(["--root", str(ROOT), *args])
    text = buf.getvalue()
    payload = json.loads(text)
    corpus_lookup.assert_no_gloss(payload)
    return code, payload


class CorpusLookupTests(unittest.TestCase):
    def test_edition_matches_readme(self) -> None:
        code, payload = run_cli("edition")
        self.assertEqual(code, 0)
        self.assertEqual(payload["status"], "process_support_not_binding")
        self.assertTrue(payload["cannot_narrow_core"])
        self.assertEqual(payload["result"]["edition"], "SC-Corpus-2026.08.09")
        self.assertEqual(payload["result"]["effective_date"], "2026-08-09")
        self.assertEqual(payload["edition"], "SC-Corpus-2026.08.09")

    def test_resolve_def_p1(self) -> None:
        code, payload = run_cli("resolve", "Def.P1")
        self.assertEqual(code, 0)
        result = payload["result"]
        self.assertEqual(result["file"], "core_05_band_participation.md")
        self.assertEqual(result["id"], "Def.P1")
        self.assertNotIn("gloss", result)

    def test_hydrate_def_p1_cluster_hits_file_via_definition_term(self) -> None:
        code, resolved = run_cli("resolve", "Def.P1")
        self.assertEqual(code, 0)
        self.assertEqual(resolved["result"]["file"], "core_05_band_participation.md")
        code, hydrated = run_cli("hydrate", "Animal Life")
        self.assertEqual(code, 0)
        result = hydrated["result"]
        self.assertEqual(result["file"], "core_05_band_participation.md")
        self.assertIn("Animal Life", result["text"])
        self.assertLessEqual(
            result["line_end"] - result["line_start"] + 1,
            corpus_lookup.HYDRATE_CAP,
        )

    def test_hydrate_def_p1_over_cap_hints_smaller_range(self) -> None:
        code, payload = run_cli("hydrate", "Def.P1")
        self.assertEqual(code, 1)
        self.assertIn("error", payload)
        self.assertIn("cap", payload["error"])
        self.assertIn("Animal Life", payload["error"])

    def test_hydrate_cf10_source_not_resolver_gloss(self) -> None:
        resolver = json.loads(
            (ROOT / "ai_corpus/indexes/id_resolver.json").read_text(encoding="utf-8")
        )
        gloss = resolver["ids"]["CF-10"]["gloss"]
        self.assertIn(GLOSS_NEEDLE, gloss)
        code, resolved = run_cli("resolve", "CF-10")
        self.assertEqual(code, 0)
        self.assertNotIn("gloss", resolved["result"])
        self.assertNotIn('"gloss"', json.dumps(resolved))
        code, payload = run_cli("hydrate", "CF-10")
        self.assertEqual(code, 0)
        text = payload["result"]["text"]
        self.assertTrue(text.startswith("# CF-10:"))
        self.assertNotEqual(text.strip(), gloss.strip())
        self.assertEqual(payload["result"]["file"], CF10)
        self.assertNotIn("gloss", payload["result"])

    def test_unknown_id_exits_nonzero(self) -> None:
        code, payload = run_cli("resolve", "NOT-A-REAL-ID")
        self.assertEqual(code, 1)
        self.assertIn("unknown", payload["error"])

    def test_topic_route_cjs_r09(self) -> None:
        code, payload = run_cli("topic-route", "CJS-R09")
        self.assertEqual(code, 0)
        result = payload["result"]
        owners = [item["id"] for item in result["primary_owners"]]
        self.assertIn("CF-10", owners)
        self.assertTrue(result["read_with"])

    def test_validity_current_anchor(self) -> None:
        code, payload = run_cli(
            "validity",
            "--file",
            CF10,
            "--anchor",
            CF10_ANCHOR,
        )
        self.assertEqual(code, 0)
        self.assertEqual(payload["result"]["status"], "current")

    def test_door_omits_conflict_prose(self) -> None:
        code, payload = run_cli("door", "standing_record")
        self.assertEqual(code, 0)
        result = payload["result"]
        self.assertIn("operative_box", result)
        self.assertIn("owners", result)
        self.assertNotIn("conflict_rule", result)
        self.assertNotIn("forbidden_move", result)
        dumped = json.dumps(result)
        self.assertNotIn("conflict_rule", dumped)
        self.assertNotIn("forbidden_move", dumped)

    def test_citator_is_capped(self) -> None:
        code, payload = run_cli("citator", "--file", CF10)
        self.assertEqual(code, 0)
        result = payload["result"]
        self.assertLessEqual(len(result["outbound"]), corpus_lookup.CITATOR_CAP)
        self.assertLessEqual(len(result["inbound"]), corpus_lookup.CITATOR_CAP)
        self.assertGreater(result["outbound_count"] + result["inbound_count"], 0)

    def test_resolve_prefix_lists_ids_not_text(self) -> None:
        code, payload = run_cli("resolve", "--prefix", "CF-10")
        self.assertEqual(code, 0)
        ids = [item["id"] for item in payload["result"]["ids"]]
        self.assertIn("CF-10", ids)
        self.assertIn("CF-10.1", ids)
        for item in payload["result"]["ids"]:
            self.assertNotIn("text", item)
            self.assertNotIn("gloss", item)

    def test_route_challenge_hits_contest_door(self) -> None:
        code, payload = run_cli("route", "they barred challenge, review, and redress")
        self.assertEqual(code, 0)
        result = payload["result"]
        self.assertEqual(result["kind"], "natural_language")
        self.assertEqual(result["door"]["id"], "contest")
        self.assertNotIn("fact_pattern", result["door"])
        self.assertNotIn("gloss", result)
        dumped = json.dumps(result)
        self.assertNotIn("gloss", dumped)
        self.assertNotIn("conflict_rule", dumped)
        self.assertIn("citation", result)
        self.assertEqual(result["citation"]["edition"], "SC-Corpus-2026.08.09")

    def test_route_unknown_exits_nonzero(self) -> None:
        code, payload = run_cli("route", "zzzz-not-a-real-constitutional-query")
        self.assertEqual(code, 1)
        self.assertIn("no route", payload["error"])

    def test_route_exact_id_still_resolves(self) -> None:
        code, payload = run_cli("route", "CJS-R09")
        self.assertEqual(code, 0)
        result = payload["result"]
        self.assertEqual(result["kind"], "exact")
        self.assertEqual(result["topic"]["id"], "CJS-R09")
        owners = [item["id"] for item in result["owners"]]
        self.assertIn("CF-10", owners)
        self.assertTrue(result["read_with"])

    def test_apply_pack_hydrates_owner_and_read_with(self) -> None:
        code, payload = run_cli("apply-pack", "CJS-R09")
        self.assertEqual(code, 0)
        result = payload["result"]
        roles = [span["role"] for span in result["spans"]]
        self.assertIn("primary_owner", roles)
        self.assertIn("read_with", roles)
        dumped = json.dumps(result)
        self.assertNotIn('"gloss"', dumped)
        for span in result["spans"]:
            self.assertNotIn("gloss", span)
            if span.get("hydrated"):
                self.assertIn("citation", span)
                self.assertEqual(span["citation"]["edition"], "SC-Corpus-2026.08.09")
                self.assertIn("text", span)
                self.assertLessEqual(
                    span["line_end"] - span["line_start"] + 1,
                    corpus_lookup.HYDRATE_CAP,
                )

    def test_apply_pack_contest_query_hydrates_operative_box(self) -> None:
        code, payload = run_cli(
            "apply-pack", "they barred challenge, review, and redress"
        )
        self.assertEqual(code, 0)
        result = payload["result"]
        self.assertEqual(result["route"]["door"]["id"], "contest")
        roles = [span["role"] for span in result["spans"]]
        self.assertIn("operative_box", roles)
        box = next(span for span in result["spans"] if span["role"] == "operative_box")
        self.assertTrue(box["hydrated"])
        self.assertIn("Operative steward statement", box["text"])
        self.assertEqual(box["citation"]["edition"], "SC-Corpus-2026.08.09")

    def test_cite_pins_edition_and_validity(self) -> None:
        code, payload = run_cli("cite", "--file", CF10, "--anchor", CF10_ANCHOR)
        self.assertEqual(code, 0)
        result = payload["result"]
        self.assertEqual(result["file"], CF10)
        self.assertEqual(result["anchor"], CF10_ANCHOR)
        self.assertEqual(result["edition"], "SC-Corpus-2026.08.09")
        self.assertEqual(result["validity"], "current")
        self.assertIn(CF10, result["citation"])
        self.assertIn("SC-Corpus-2026.08.09", result["citation"])
        self.assertNotIn("gloss", result)

    def test_classes_are_not_gold_key(self) -> None:
        code, payload = run_cli("classes")
        self.assertEqual(code, 0)
        result = payload["result"]
        self.assertTrue(result["not_operator_gold_key"])
        ids = {row["id"] for row in result["classes"]}
        self.assertIn("contest", ids)
        self.assertTrue(all("fact_pattern" not in row for row in result["classes"]))
        contest = next(row for row in result["classes"] if row["id"] == "contest")
        self.assertEqual(
            contest["next_step_class"],
            "invalidate_or_narrow_companion_against_core",
        )

    def test_retrieve_returns_locators_not_gloss(self) -> None:
        code, payload = run_cli("retrieve", "survival challenge review")
        self.assertEqual(code, 0)
        result = payload["result"]
        self.assertTrue(result["not_embeddings"])
        self.assertEqual(result["embeddings"], "postponed_indefinitely")
        self.assertIn("boundary_chunks.json", result["embed_over"])
        self.assertNotIn("gloss", result)
        self.assertGreaterEqual(result["hit_count"], 1)
        hit = result["hits"][0]
        self.assertIn("file", hit)
        self.assertTrue(str(hit["file"]).startswith("core_"))
        self.assertIn("line_start", hit)
        self.assertIn("line_end", hit)
        self.assertNotIn("text", hit)
        self.assertNotIn("gloss", hit)

    def test_retrieve_scores_source_spans(self) -> None:
        code, payload = run_cli("retrieve", "healthcare occupancy shelter")
        self.assertEqual(code, 0)
        result = payload["result"]
        self.assertTrue(result["not_embeddings"])
        self.assertEqual(result["embeddings"], "postponed_indefinitely")
        self.assertGreaterEqual(result["hit_count"], 1)
        files = {str(hit["file"]) for hit in result["hits"]}
        self.assertTrue(
            any(
                name.endswith("core_05_band_continuity.md")
                or name.endswith("core_06_rights_part_a.md")
                for name in files
            ),
            files,
        )
        for hit in result["hits"]:
            self.assertNotIn("text", hit)
            self.assertNotIn("gloss", hit)

    def test_http_handler_route_matches_cli(self) -> None:
        indexes = corpus_lookup.load_indexes(ROOT)
        result = corpus_lookup.handle_http_command(
            indexes, "cite", {"file": CF10, "anchor": CF10_ANCHOR}
        )
        self.assertEqual(result["validity"], "current")
        self.assertNotIn("gloss", result)


if __name__ == "__main__":
    unittest.main()
