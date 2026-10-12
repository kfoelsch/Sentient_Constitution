#!/usr/bin/env python3
"""Tests for section_crossref_format (lossless round trip and validation)."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from section_crossref_format import (  # noqa: E402
    FORMAT,
    build_payload_from_edges,
    dumps_payload,
    expand_edges,
    intern_edges,
    validation_errors,
)

EDGES = [
    {"source_file": "a.md", "source_header": "1. One", "source_anchor": "#1-one",
     "target_file": "b.md", "target_anchor": "#x", "count": 1},
    {"source_file": "a.md", "source_header": "1. One", "source_anchor": "#1-one",
     "target_file": "b.md", "target_anchor": None, "count": 3},
    {"source_file": "a.md", "source_header": None, "source_anchor": None,
     "target_file": "a.md", "target_anchor": "#y", "count": 2},
    {"source_file": "b.md", "source_header": "Ünïcode ☃", "source_anchor": "#u",
     "target_file": "a.md", "target_anchor": "#y", "count": 1},
]


class RoundTripTests(unittest.TestCase):
    def test_expand_of_intern_is_identity_including_key_order_and_nulls(self) -> None:
        payload = build_payload_from_edges(EDGES, "t")
        out = expand_edges(payload)
        self.assertEqual(out, EDGES)
        self.assertEqual([list(e) for e in out], [list(e) for e in EDGES])

    def test_tables_are_deduplicated(self) -> None:
        t = intern_edges(EDGES)
        self.assertEqual(t["files"], ["a.md", "b.md"])
        self.assertEqual(len(t["sources"]), 3)  # the two "1. One" edges share one source
        self.assertEqual(len(t["targets"]), 3)

    def test_serialized_form_parses_back_and_is_one_row_per_line(self) -> None:
        payload = build_payload_from_edges(EDGES, "t")
        text = dumps_payload(payload)
        self.assertEqual(json.loads(text), payload)
        self.assertEqual(expand_edges(json.loads(text)), EDGES)
        self.assertEqual(sum(1 for ln in text.splitlines() if ln.startswith("    [")),
                         len(payload["sources"]) + len(payload["targets"]) + len(payload["edges"]))

    def test_legacy_format_passes_through(self) -> None:
        self.assertEqual(expand_edges({"edges": EDGES}), EDGES)

    def test_empty(self) -> None:
        p = build_payload_from_edges([], "t")
        self.assertEqual(expand_edges(p), [])
        self.assertEqual(validation_errors(p), [])


class ValidationTests(unittest.TestCase):
    def good(self) -> dict:
        return build_payload_from_edges(EDGES, "t")

    def test_valid_payload_has_no_errors(self) -> None:
        self.assertEqual(validation_errors(self.good()), [])
        self.assertEqual(self.good()["format"], FORMAT)

    def test_bad_index_count_and_edge_count_are_caught(self) -> None:
        p = self.good(); p["edges"][0][0] = 99
        self.assertTrue(validation_errors(p))
        p = self.good(); p["edges"][0][2] = 0
        self.assertTrue(validation_errors(p))
        p = self.good(); p["edge_count"] += 1
        self.assertTrue(validation_errors(p))
        p = self.good(); p["sources"][0][0] = 50
        self.assertTrue(validation_errors(p))

    def test_non_interned_is_rejected(self) -> None:
        self.assertTrue(validation_errors({"edges": EDGES}))


if __name__ == "__main__":
    unittest.main()
