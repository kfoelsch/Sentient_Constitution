#!/usr/bin/env python3
"""Tests for crossref_matrix_format (lossless round trip and validation)."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crossref_matrix_format import (  # noqa: E402
    FORMAT,
    build_payload,
    dumps_payload,
    expand_graph,
    validation_errors,
)

NODES = [
    {"id": "a.md", "type": "core"},
    {"id": "b.md", "type": "adopted-implementation"},
    {"id": "c.md", "type": "core"},
]
EDGES = [
    {"source": "a.md", "targets": [
        {"file": "b.md", "count": 3, "anchors": ["#x", "#y"]},
        {"file": "c.md", "count": 1, "anchors": []},
    ]},
    {"source": "c.md", "targets": [
        {"file": "a.md", "count": 2, "anchors": ["#y", "#ü"]},
    ]},
]
GRAPH = {"nodes": NODES, "edges": EDGES}


class RoundTripTests(unittest.TestCase):
    def test_expand_of_build_is_identity_including_key_order(self) -> None:
        out = expand_graph(build_payload(NODES, EDGES, "t"))
        self.assertEqual(out, GRAPH)
        self.assertEqual(list(out["edges"][0]), ["source", "targets"])
        self.assertEqual(list(out["edges"][0]["targets"][0]), ["file", "count", "anchors"])

    def test_anchors_are_deduplicated(self) -> None:
        p = build_payload(NODES, EDGES, "t")
        self.assertEqual(p["anchors"], ["#x", "#y", "#ü"])

    def test_source_without_edges_and_order_are_preserved(self) -> None:
        graph = {"nodes": NODES, "edges": [EDGES[1]]}  # only c.md has edges; b.md absent
        self.assertEqual(expand_graph(build_payload(graph["nodes"], graph["edges"], "t")), graph)

    def test_serialized_form_parses_back(self) -> None:
        p = build_payload(NODES, EDGES, "t")
        text = dumps_payload(p)
        self.assertEqual(json.loads(text), p)
        self.assertEqual(expand_graph(json.loads(text)), GRAPH)

    def test_legacy_format_passes_through(self) -> None:
        self.assertEqual(expand_graph({"graph": GRAPH}), GRAPH)

    def test_empty(self) -> None:
        p = build_payload([], [], "t")
        self.assertEqual(expand_graph(p), {"nodes": [], "edges": []})
        self.assertEqual(validation_errors(p), [])


class ValidationTests(unittest.TestCase):
    def good(self) -> dict:
        return build_payload(NODES, EDGES, "t")

    def test_valid_payload(self) -> None:
        self.assertEqual(validation_errors(self.good()), [])
        self.assertEqual(self.good()["format"], FORMAT)

    def test_bad_indexes_counts_and_ids_are_caught(self) -> None:
        for mutate in (
            lambda p: p["edges"][0].__setitem__(0, 99),
            lambda p: p["edges"][0][1][0].__setitem__(0, 99),
            lambda p: p["edges"][0][1][0].__setitem__(1, 0),
            lambda p: p["edges"][0][1][0][2].append(99),
            lambda p: p["nodes"].append(["a.md", "core"]),
        ):
            p = self.good()
            mutate(p)
            self.assertTrue(validation_errors(p), p)

    def test_non_interned_is_rejected(self) -> None:
        self.assertTrue(validation_errors({"graph": GRAPH}))


if __name__ == "__main__":
    unittest.main()
