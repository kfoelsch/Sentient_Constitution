#!/usr/bin/env python3
"""Generate a compact Markdown cross-reference matrix.

The output uses the compact "interned" format (see crossref_matrix_format.py):
each distinct anchor is listed once and files are referred to by node index. Use
crossref_matrix_format.expand_graph() to read the original nodes/edges objects.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import source_markdown_files  # noqa: E402
from crossref_matrix_format import build_payload, dumps_payload  # noqa: E402


LINK_RE = re.compile(r"\]\(([^)#]+\.md)(#[^)]+)?\)")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument("--output", required=True, help="Output JSON path.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    sources = source_markdown_files(root)
    source_ids = {path.relative_to(root).as_posix() for path in sources}
    nodes = [
        {
            "id": path.relative_to(root).as_posix(),
            "type": "core" if path.name.startswith("core_") else "adopted-implementation",
        }
        for path in sources
    ]
    edges = []
    for path in sources:
        text = path.read_text(encoding="utf-8")
        counts: Counter[str] = Counter()
        anchors: dict[str, set[str]] = defaultdict(set)
        for target, anchor in LINK_RE.findall(text):
            resolved = (path.parent / target).resolve()
            try:
                target_id = resolved.relative_to(root).as_posix()
            except ValueError:
                continue
            if target_id not in source_ids:
                continue
            counts[target_id] += 1
            if anchor:
                anchors[target_id].add(anchor)
        if counts:
            edges.append(
                {
                    "source": path.relative_to(root).as_posix(),
                    "targets": [
                        {
                            "file": target,
                            "count": count,
                            "anchors": sorted(anchors[target]),
                        }
                        for target, count in sorted(counts.items())
                    ],
                }
            )
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    payload = build_payload(nodes, edges, generated_at)
    output.write_text(dumps_payload(payload), encoding="utf-8")
    print(f"Wrote cross-reference matrix to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
