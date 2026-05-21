#!/usr/bin/env python3
"""Generate a compact Markdown cross-reference matrix."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


LINK_RE = re.compile(r"\]\(([^)#]+\.md)(#[^)]+)?\)")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument("--output", required=True, help="Output JSON path.")
    return p.parse_args()


def source_files(root: Path) -> list[Path]:
    return sorted(root.glob("core_*.md")) + sorted(root.glob("corpus_*.md"))


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    nodes = [{"id": path.name, "type": "core" if path.name.startswith("core_") else "companion"} for path in source_files(root)]
    edges = []
    for path in source_files(root):
        text = path.read_text(encoding="utf-8")
        counts: Counter[str] = Counter()
        anchors: dict[str, set[str]] = defaultdict(set)
        for target, anchor in LINK_RE.findall(text):
            if not (root / target).exists():
                continue
            counts[target] += 1
            if anchor:
                anchors[target].add(anchor)
        if counts:
            edges.append(
                {
                    "source": path.name,
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
