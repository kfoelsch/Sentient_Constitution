#!/usr/bin/env python3
"""Generate a compact section manifest for AI navigation."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")
ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument("--output", required=True, help="Output JSON path.")
    return p.parse_args()


def core_files(root: Path) -> list[Path]:
    return sorted(root.glob("core_*.md")) + sorted(root.glob("corpus_*.md"))


def manifest_for(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    sections: list[dict] = []
    pending_anchor: str | None = None
    for idx, line in enumerate(lines, start=1):
        anchor = ANCHOR_RE.match(line.strip())
        if anchor:
            pending_anchor = f"#{anchor.group(1)}"
            continue
        heading = HEADING_RE.match(line.strip())
        if not heading:
            continue
        sections.append(
            {
                "header": heading.group(2).strip(),
                "level": len(heading.group(1)),
                "line_start": idx,
                "line_end": len(lines),
                "anchor": pending_anchor,
            }
        )
        pending_anchor = None
    for idx, section in enumerate(sections):
        for later in sections[idx + 1 :]:
            if later["level"] <= section["level"]:
                section["line_end"] = later["line_start"] - 1
                break
    return {"total_lines": len(lines), "sections": sections}


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "$schema": "../schemas/section_manifest.schema.json",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "files": {path.name: manifest_for(path) for path in core_files(root)},
    }
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote section manifest to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
