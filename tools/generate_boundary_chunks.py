#!/usr/bin/env python3
"""Pre-chunk numbered core_* files at safe split points.

Never splits inside ``<details>`` widgets or O/M/A/C definition blocks.
Chunks are locators (file, anchor, line range), not a second constitution.
Vector embeddings over these spans are postponed indefinitely
(doc_architecture.md#retrieval-no-vector-embeddings).

Usage (from the repo root)::

    python3 tools/generate_boundary_chunks.py --root . --write
    python3 tools/generate_boundary_chunks.py --root . --check
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import CORE_FILES  # noqa: E402
from generate_plain_terms_edition import (  # noqa: E402
    ANCHOR_RE,
    HEADING_RE,
    FENCE_RE,
    auto_slug,
    clean_title,
    read_edition,
)

OUT_REL = "doc_architecture/generated/boundary_chunks.json"
OMAC_START = re.compile(r"^- (?:[OMAC]:|\*\*(?:What it is|How to measure|What must hold)\*\*)")


def chunk_file(root: Path, rel: str) -> list[dict]:
    lines = (root / rel).read_text(encoding="utf-8").splitlines()
    details_depth = 0
    in_fence = False
    pending_anchor: str | None = None
    seen_slugs: dict[str, int] = {}
    splits: list[tuple[int, str, str]] = []  # 1-based line, title, anchor
    omac_open = False

    for idx, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if FENCE_RE.match(stripped):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        anchor_match = ANCHOR_RE.match(stripped)
        if anchor_match and stripped == anchor_match.group(0):
            if pending_anchor is None:
                pending_anchor = anchor_match.group(1)
            continue

        opens = stripped.count("<details")
        closes = stripped.count("</details>")
        heading = HEADING_RE.match(raw)

        if heading and details_depth == 0 and not omac_open:
            title = clean_title(heading.group(2))
            anchor = pending_anchor
            if not anchor:
                base = auto_slug(title)
                n = seen_slugs.get(base, 0)
                seen_slugs[base] = n + 1
                anchor = base if n == 0 else f"{base}-{n}"
            splits.append((idx, title, anchor))
            pending_anchor = None
            details_depth += opens - closes
            omac_open = False
            continue

        if stripped and not heading:
            pending_anchor = None

        details_depth += opens - closes
        if details_depth < 0:
            details_depth = 0

        if details_depth == 0:
            if OMAC_START.match(stripped):
                omac_open = True
            if stripped == "---":
                omac_open = False

    chunks: list[dict] = []
    for i, (start, title, anchor) in enumerate(splits):
        end = (splits[i + 1][0] - 1) if i + 1 < len(splits) else len(lines)
        chunks.append(
            {
                "file": rel,
                "heading": title,
                "anchor": f"#{anchor}",
                "line_start": start,
                "line_end": end,
            }
        )
    return chunks


def build(root: Path) -> dict:
    edition, effective = read_edition(root)
    chunks: list[dict] = []
    for rel in CORE_FILES:
        if (root / rel).is_file():
            chunks.extend(chunk_file(root, rel))
    return {
        "edition": edition,
        "effective_date": effective,
        "status": "process_support_not_binding",
        "cannot_narrow_core": True,
        "split_rule": "headings outside details; never inside O/M/A/C blocks",
        "embeddings": "postponed_indefinitely",
        "chunk_count": len(chunks),
        "chunks": chunks,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=".")
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    payload = json.dumps(build(root), indent=2, ensure_ascii=False) + "\n"
    out = root / OUT_REL
    if args.check:
        if not out.is_file() or out.read_text(encoding="utf-8") != payload:
            print(f"boundary chunks are stale; run `make boundary-chunks` ({OUT_REL})")
            return 1
        print("boundary chunks are current.")
        return 0
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(payload, encoding="utf-8")
    print(f"Wrote {OUT_REL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
