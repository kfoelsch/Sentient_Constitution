#!/usr/bin/env python3
"""Write JSON with one record per line instead of 2-space indentation.

Same JSON, same structure, same key order: every loader and consumer is
unchanged. Containers above a chosen depth are written one entry per line;
containers at that depth and below are written inline with compact separators.
This cuts the generated indexes by 15-35% (indentation was most of the
whitespace), and a changed record is a one-line diff.

  top-level object              depth 1   always expanded
  its values (dict / list)      depth 2   expanded (one entry per line)
  the entries inside them       depth 3   inline  <- default row depth

Pass overrides={"key": depth} to expand one top-level key deeper or shallower.
"""

from __future__ import annotations

import json
from typing import Any

DEFAULT_ROW_DEPTH = 3


def _inline(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def _render(value: Any, depth: int, indent: int, row_depth: int) -> str:
    if not isinstance(value, (dict, list)) or not value or depth >= row_depth:
        return _inline(value)
    pad = "  " * (indent + 1)
    end = "  " * indent
    if isinstance(value, dict):
        rows = [f"{pad}{json.dumps(k, ensure_ascii=False)}: {_render(v, depth + 1, indent + 1, row_depth)}" for k, v in value.items()]
        return "{\n" + ",\n".join(rows) + "\n" + end + "}"
    rows = [f"{pad}{_render(v, depth + 1, indent + 1, row_depth)}" for v in value]
    return "[\n" + ",\n".join(rows) + "\n" + end + "]"


def dumps_rows(payload: dict[str, Any], row_depth: int = DEFAULT_ROW_DEPTH, overrides: dict[str, int] | None = None) -> str:
    """Serialize a top-level object one record per line (see module docstring)."""
    overrides = overrides or {}
    if not payload:
        return "{}\n"
    rows = []
    for key, value in payload.items():
        depth = overrides.get(key, row_depth)
        rows.append(f"  {json.dumps(key, ensure_ascii=False)}: {_render(value, 2, 1, depth)}")
    return "{\n" + ",\n".join(rows) + "\n}\n"
