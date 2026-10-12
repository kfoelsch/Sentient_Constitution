#!/usr/bin/env python3
"""Compact "interned" format for ai_corpus/indexes/crossref_matrix.json.

The original format repeated every target file name and every anchor string in
full (7,996 anchor strings, only 1,376 distinct; 746 KB). The interned format
stores each distinct anchor once and refers to files by their node index
(about 0.13 MB). Nothing is lost: expand_graph() returns exactly the original
{"nodes": [...], "edges": [...]} structure, in the original order.

Layout (format "interned-v1"):
  nodes    [[id, type], ...]                        one per corpus file
  anchors  ["#anchor", ...]                         distinct anchors, first-use order
  edges    [[source_index, [[target_index, count, [anchor_index, ...]], ...]], ...]

source_index and target_index point into nodes; anchor_index points into anchors.
"""

from __future__ import annotations

from typing import Any

from section_crossref_format import dumps_payload as _dumps

FORMAT = "interned-v1"
LIST_KEYS = ("nodes", "anchors", "edges")
LAYOUT = {
    "nodes": "[id, type]",
    "anchors": "distinct anchor strings",
    "edges": "[source_index, [[target_index, count, [anchor_index, ...]], ...]]",
}


def is_interned(payload: dict[str, Any]) -> bool:
    return payload.get("format") == FORMAT


def intern_graph(nodes: list[dict[str, Any]], edges: list[dict[str, Any]]) -> dict[str, Any]:
    """Convert the original nodes/edges objects to interned tables (order preserved)."""
    node_index = {n["id"]: i for i, n in enumerate(nodes)}
    anchors: dict[str, int] = {}
    rows = []
    for edge in edges:
        targets = []
        for t in edge["targets"]:
            idx = [anchors.setdefault(a, len(anchors)) for a in t["anchors"]]
            targets.append([node_index[t["file"]], t["count"], idx])
        rows.append([node_index[edge["source"]], targets])
    return {
        "nodes": [[n["id"], n["type"]] for n in nodes],
        "anchors": list(anchors),
        "edges": rows,
    }


def build_payload(nodes: list[dict[str, Any]], edges: list[dict[str, Any]], generated_at: str) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "$schema": "../schemas/crossref_matrix.schema.json",
        "generated_at": generated_at,
        "description": "Source-derived file-to-file Markdown reference graph.",
        "format": FORMAT,
        "layout": LAYOUT,
    }
    payload.update(intern_graph(nodes, edges))
    return payload


def expand_graph(payload: dict[str, Any]) -> dict[str, Any]:
    """Return {"nodes": [...], "edges": [...]} in the original object form (either format)."""
    if not is_interned(payload):
        return payload.get("graph", {})
    nodes = [{"id": nid, "type": ntype} for nid, ntype in payload["nodes"]]
    ids = [n["id"] for n in nodes]
    anchors = payload["anchors"]
    edges = []
    for source_index, targets in payload["edges"]:
        edges.append(
            {
                "source": ids[source_index],
                "targets": [
                    {"file": ids[ti], "count": count, "anchors": [anchors[a] for a in idx]}
                    for ti, count, idx in targets
                ],
            }
        )
    return {"nodes": nodes, "edges": edges}


def dumps_payload(payload: dict[str, Any]) -> str:
    return _dumps(payload, LIST_KEYS)


def _is_int(v: Any) -> bool:
    return isinstance(v, int) and not isinstance(v, bool)


def validation_errors(payload: dict[str, Any]) -> list[str]:
    """Structural problems in an interned payload (empty list means valid)."""
    if not is_interned(payload):
        return ["format is not " + FORMAT]
    nodes, anchors, edges = (payload.get(k) for k in LIST_KEYS)
    for key, val in zip(LIST_KEYS, (nodes, anchors, edges)):
        if not isinstance(val, list):
            return [f"{key} must be a list"]
    errs: list[str] = []
    if not all(isinstance(r, list) and len(r) == 2 and all(isinstance(v, str) for v in r) for r in nodes):
        errs.append("nodes must be [id, type] string pairs")
    if len({r[0] for r in nodes if isinstance(r, list) and r}) != len(nodes):
        errs.append("node ids must be unique")
    if not all(isinstance(a, str) for a in anchors):
        errs.append("anchors must be strings")
    n_nodes, n_anchors = len(nodes), len(anchors)
    for row in edges:
        ok = isinstance(row, list) and len(row) == 2 and _is_int(row[0]) and 0 <= row[0] < n_nodes and isinstance(row[1], list)
        if ok:
            for t in row[1]:
                ok = (
                    isinstance(t, list)
                    and len(t) == 3
                    and _is_int(t[0])
                    and 0 <= t[0] < n_nodes
                    and _is_int(t[1])
                    and t[1] > 0
                    and isinstance(t[2], list)
                    and all(_is_int(a) and 0 <= a < n_anchors for a in t[2])
                )
                if not ok:
                    break
        if not ok:
            errs.append(f"edges row malformed: {str(row)[:80]}")
            break
    return errs
