#!/usr/bin/env python3
"""Generate a compact section manifest for AI navigation."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from corpus_paths import source_markdown_files


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")
ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')

# Prefer canonical Preamble measurement anchors over legacy aliases when
# multiple <a id> tags precede the same heading.
CH00_CANONICAL_ANCHORS: frozenset[str] = frozenset(
    {
        "2-the-measurements",
        "measurements-overview",
        "major-measurement-aspects",
        "measuring-threshold-and-scaling",
        "measuring-flourishing",
        "measuring-continuity",
        "measuring-participation",
        "measuring-oversight",
        "measuring-accountability",
        "measuring-timeliness",
        "measuring-constitutional-performance",
        "from-measurement-to-evidence-and-remedy",
    }
)


def pick_section_anchor(pending_anchors: list[str]) -> str | None:
    if not pending_anchors:
        return None
    canonical = [a for a in pending_anchors if a.lstrip("#") in CH00_CANONICAL_ANCHORS]
    if canonical:
        return canonical[-1]
    return pending_anchors[-1]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument("--output", required=True, help="Output JSON path.")
    return p.parse_args()


def manifest_for(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    sections: list[dict] = []
    pending_anchors: list[str] = []
    consumed_anchor_lines: set[int] = set()
    for idx, line in enumerate(lines, start=1):
        if idx in consumed_anchor_lines:
            continue
        anchor = ANCHOR_RE.match(line.strip())
        if anchor:
            pending_anchors.append(f"#{anchor.group(1)}")
            continue
        heading = HEADING_RE.match(line.strip())
        if not heading:
            continue
        section_anchor = pick_section_anchor(pending_anchors)
        for lookahead_idx in range(idx + 1, len(lines) + 1):
            lookahead_line = lines[lookahead_idx - 1].strip()
            if not lookahead_line:
                continue
            following_anchor = ANCHOR_RE.match(lookahead_line)
            if following_anchor:
                following_id = f"#{following_anchor.group(1)}"
                if following_id.lstrip("#") in CH00_CANONICAL_ANCHORS:
                    section_anchor = following_id
                elif section_anchor is None:
                    section_anchor = following_id
                consumed_anchor_lines.add(lookahead_idx)
            break
        sections.append(
            {
                "header": heading.group(2).strip(),
                "level": len(heading.group(1)),
                "line_start": idx,
                "line_end": len(lines),
                "anchor": section_anchor,
            }
        )
        pending_anchors = []
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
        "files": {path.relative_to(root).as_posix(): manifest_for(path) for path in source_markdown_files(root)},
    }
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote section manifest to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
