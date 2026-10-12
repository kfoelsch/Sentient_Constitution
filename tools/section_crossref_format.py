#!/usr/bin/env python3
"""Compact "interned" format for ai_corpus/indexes/section_crossref.json.

The original format wrote every edge as a six-field object, repeating the same
119 file names and ~1,300 section/target anchors 17,000 times (5.5 MB). The
interned format stores each distinct file, source section, and target once and
writes each edge as three integers (about 0.3 MB). Nothing is lost: expand_edges()
returns exactly the original edge objects, in the original order.

Layout (format "interned-v1"):
  files    [file, ...]                          sorted file names
  sources  [[file_index, anchor, header], ...]  distinct source sections
  targets  [[file_index, anchor], ...]          distinct target file#anchor pairs
  edges    [[source_index, target_index, count], ...]

anchor and header may be null. Index values point into the lists above.
"""

from __future__ import annotations

import json
from typing import Any

FORMAT = "interned-v1"
LAYOUT = {
    "sources": "[file_index, anchor, header]",
    "targets": "[file_index, anchor]",
    "edges": "[source_index, target_index, count]",
}
LIST_KEYS = ("files", "sources", "targets", "edges")


def intern_edges(edges: list[dict[str, Any]]) -> dict[str, Any]:
    """Convert original edge objects to the interned tables (order preserved)."""
    files = sorted({e["source_file"] for e in edges} | {e["target_file"] for e in edges})
    file_index = {name: i for i, name in enumerate(files)}
    sources: dict[tuple, int] = {}
    targets: dict[tuple, int] = {}
    rows: list[list[int]] = []
    for e in edges:
        s = (file_index[e["source_file"]], e.get("source_anchor"), e.get("source_header"))
        t = (file_index[e["target_file"]], e.get("target_anchor"))
        si = sources.setdefault(s, len(sources))
        ti = targets.setdefault(t, len(targets))
        rows.append([si, ti, e["count"]])
    return {
        "files": files,
        "sources": [list(k) for k in sources],
        "targets": [list(k) for k in targets],
        "edges": rows,
    }


def is_interned(payload: dict[str, Any]) -> bool:
    return payload.get("format") == FORMAT


def expand_edges(payload: dict[str, Any]) -> list[dict[str, Any]]:
    """Return the original edge objects from either format."""
    if not is_interned(payload):
        return list(payload.get("edges", []))
    files, sources, targets = payload["files"], payload["sources"], payload["targets"]
    out = []
    for si, ti, count in payload["edges"]:
        sf, s_anchor, s_header = sources[si]
        tf, t_anchor = targets[ti]
        out.append(
            {
                "source_file": files[sf],
                "source_header": s_header,
                "source_anchor": s_anchor,
                "target_file": files[tf],
                "target_anchor": t_anchor,
                "count": count,
            }
        )
    return out


def build_payload_from_edges(edges: list[dict[str, Any]], generated_at: str) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "$schema": "../schemas/section_crossref.schema.json",
        "generated_at": generated_at,
        "status": "process_support_not_binding",
        "cannot_narrow_core": True,
        "description": "Source-derived section-to-section Markdown reference graph.",
        "format": FORMAT,
        "layout": LAYOUT,
        "edge_count": len(edges),
    }
    payload.update(intern_edges(edges))
    return payload


def dumps_payload(payload: dict[str, Any], list_keys: tuple[str, ...] = LIST_KEYS) -> str:
    """Serialize with one table row per line: small file, clean line-based diffs.

    Keys named in list_keys are written one row per line; everything else inline.
    Shared with crossref_matrix_format.
    """
    lines = ["{"]
    keys = list(payload)
    for n, key in enumerate(keys):
        comma = "," if n < len(keys) - 1 else ""
        value = payload[key]
        if key in list_keys and isinstance(value, list):
            lines.append(f"  {json.dumps(key)}: [")
            for i, item in enumerate(value):
                tail = "," if i < len(value) - 1 else ""
                lines.append("    " + json.dumps(item, ensure_ascii=False, separators=(",", ":")) + tail)
            lines.append("  ]" + comma)
        else:
            lines.append(f"  {json.dumps(key)}: {json.dumps(value, ensure_ascii=False)}{comma}")
    lines.append("}")
    return "\n".join(lines) + "\n"


def validation_errors(payload: dict[str, Any]) -> list[str]:
    """Structural problems in an interned payload (empty list means valid)."""
    errs: list[str] = []
    if not is_interned(payload):
        return ["format is not " + FORMAT]
    files, sources, targets, edges = (payload.get(k) for k in LIST_KEYS)
    for key, val in zip(LIST_KEYS, (files, sources, targets, edges)):
        if not isinstance(val, list):
            errs.append(f"{key} must be a list")
    if errs:
        return errs
    if payload.get("edge_count") not in (None, len(edges)):
        errs.append("edge_count does not match edges")
    if not all(isinstance(f, str) for f in files):
        errs.append("files must be strings")
    for name, rows, width in (("sources", sources, 3), ("targets", targets, 2)):
        for row in rows:
            ok = (
                isinstance(row, list)
                and len(row) == width
                and isinstance(row[0], int)
                and 0 <= row[0] < len(files)
                and all(v is None or isinstance(v, str) for v in row[1:])
            )
            if not ok:
                errs.append(f"{name} row malformed: {row!r}")
                break
    for row in edges:
        ok = (
            isinstance(row, list)
            and len(row) == 3
            and all(isinstance(v, int) and not isinstance(v, bool) for v in row)
            and 0 <= row[0] < len(sources)
            and 0 <= row[1] < len(targets)
            and row[2] > 0
        )
        if not ok:
            errs.append(f"edges row malformed: {row!r}")
            break
    return errs
