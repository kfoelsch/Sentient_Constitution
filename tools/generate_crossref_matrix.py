#!/usr/bin/env python3
"""Generate a compact Markdown cross-reference matrix."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from corpus_paths import source_markdown_files


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
            "type": "core" if path.name.startswith("core_") else "companion",
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
    payload = {
        "$schema": "../schemas/crossref_matrix.schema.json",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "description": "Source-derived file-to-file Markdown reference graph.",
        "graph": {"nodes": nodes, "edges": edges},
    }
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote cross-reference matrix to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
