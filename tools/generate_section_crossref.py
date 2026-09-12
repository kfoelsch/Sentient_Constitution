#!/usr/bin/env python3
"""Generate a section-to-section Markdown citation graph.

File-to-file edges remain in crossref_matrix.json. This index keys the same
links by the innermost source heading and the target file#anchor.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import source_markdown_files  # noqa: E402
from generate_section_manifest import manifest_for  # noqa: E402

LINK_RE = re.compile(r"\]\(([^)#]+\.md)(#[^)]+)?\)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--output", required=True, help="Output JSON path.")
    return parser.parse_args()


def innermost_section(sections: list[dict], line_no: int) -> dict | None:
    containing = [
        section
        for section in sections
        if section["line_start"] <= line_no <= section["line_end"]
    ]
    if not containing:
        return None
    return max(containing, key=lambda section: (section["level"], section["line_start"]))


def source_key(file_rel: str, section: dict | None, line_no: int) -> tuple:
    if section is None:
        return (file_rel, "", line_no)
    return (
        file_rel,
        section.get("anchor") or section["header"],
        section["line_start"],
    )


def build_payload(root: Path) -> dict:
    sources = source_markdown_files(root)
    source_ids = {path.relative_to(root).as_posix() for path in sources}
    manifests = {
        path.relative_to(root).as_posix(): manifest_for(path) for path in sources
    }
    counts: Counter[tuple] = Counter()
    meta: dict[tuple, dict] = {}
    for path in sources:
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        sections = manifests[rel]["sections"]
        for line_no, line in enumerate(text.splitlines(), start=1):
            for target, anchor in LINK_RE.findall(line):
                resolved = (path.parent / target).resolve()
                try:
                    target_id = resolved.relative_to(root).as_posix()
                except ValueError:
                    continue
                if target_id not in source_ids:
                    continue
                section = innermost_section(sections, line_no)
                key = (
                    *source_key(rel, section, line_no)[:2],
                    target_id,
                    anchor or "",
                )
                counts[key] += 1
                if key not in meta:
                    meta[key] = {
                        "source_file": rel,
                        "source_header": section["header"] if section else None,
                        "source_anchor": section.get("anchor") if section else None,
                        "target_file": target_id,
                        "target_anchor": anchor or None,
                    }
    edges = []
    for key, count in sorted(counts.items(), key=lambda item: (item[0][0], item[0][1], item[0][2])):
        row = dict(meta[key])
        row["count"] = count
        edges.append(row)
    return {
        "$schema": "../schemas/section_crossref.schema.json",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "status": "process_support_not_binding",
        "cannot_narrow_core": True,
        "description": "Source-derived section-to-section Markdown reference graph.",
        "edge_count": len(edges),
        "edges": edges,
    }


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = build_payload(root)
    output.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Wrote section crossref ({payload['edge_count']} edges) to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
