#!/usr/bin/env python3
"""Delete content-free navigation scaffolding from companion implementation files.

Only lines that carry no routing a reader could not already derive are removed:

* ``- Downstream: this section's local operational requirements for **X**.``
  -- restates the heading it sits under.
* ``- Read with: **X**.`` where ``X`` is the enclosing section -- cites itself.
* ``- Upstream: ...`` repeated verbatim from the file-level Trace block.

A Trace block left with no bullets is removed entirely. Its Definitions ·
Assessment · Compliance widget is removed with it only when every row is
already present in the file-level widget, so no Chapter Five jump link is lost.

``- Topic routing (...)`` bullets are never touched: the CJS-0.1 router audit
requires them inside the owning section.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from corpus_paths import COMPANION_SUBDIRS

ROOT = Path(__file__).resolve().parents[1]

TRACE_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>'
)
DAC_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">'
    "Definitions · Assessment · Compliance</span></strong></summary>"
)

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
HEADING_ID_RE = re.compile(r"^((?:CF|CI|CS|CJS)-[0-9]+(?:\.[0-9]+)*[A-Z]?)")
SELF_DOWNSTREAM_RE = re.compile(
    r"^- Downstream: this section's local operational requirements", re.I
)
SELF_READ_WITH_RE = re.compile(r"^- Read with: \*\*((?:CF|CI|CS|CJS)-[\d.]+)\*\*\.\s*$")
UPSTREAM_RE = re.compile(r"^- Upstream:")
BULLET_RE = re.compile(r"^- \S")


class Block:
    """A ``<details>`` widget with its line span and kind."""

    def __init__(self, kind: str, start: int, end: int) -> None:
        self.kind = kind  # "trace" | "dac" | "other"
        self.start = start  # index of the "<details>" line
        self.end = end  # index of the "</details>" line


def find_blocks(lines: list[str]) -> list[Block]:
    blocks: list[Block] = []
    start: int | None = None
    kind = "other"
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "<details>":
            start = idx
            kind = "other"
            continue
        if start is not None:
            if TRACE_SUMMARY in line:
                kind = "trace"
            elif DAC_SUMMARY in line:
                kind = "dac"
            if stripped == "</details>":
                blocks.append(Block(kind, start, idx))
                start = None
                kind = "other"
    return blocks


def enclosing_section_id(lines: list[str], index: int) -> str | None:
    for idx in range(index, -1, -1):
        match = HEADING_RE.match(lines[idx])
        if match:
            ident = HEADING_ID_RE.match(match.group(2).strip())
            return ident.group(1) if ident else None
    return None


def dac_rows(lines: list[str], block: Block) -> set[str]:
    return {
        line.strip()
        for line in lines[block.start : block.end]
        if line.strip().startswith("- [")
    }


def prune_file(path: Path) -> tuple[str, dict[str, int]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    blocks = find_blocks(lines)
    stats = {"downstream": 0, "read_with": 0, "upstream": 0, "trace": 0, "dac": 0}

    traces = [b for b in blocks if b.kind == "trace"]
    dacs = [b for b in blocks if b.kind == "dac"]
    if not traces:
        return text, stats

    file_trace = traces[0]
    file_upstreams = {
        line.strip()
        for line in lines[file_trace.start : file_trace.end]
        if UPSTREAM_RE.match(line.strip())
    }
    file_dac_rows = dac_rows(lines, dacs[0]) if dacs else set()

    drop: set[int] = set()

    for trace in traces:
        section_id = enclosing_section_id(lines, trace.start)
        is_file_level = trace is file_trace
        for idx in range(trace.start + 1, trace.end):
            stripped = lines[idx].strip()
            if SELF_DOWNSTREAM_RE.match(stripped):
                drop.add(idx)
                stats["downstream"] += 1
                continue
            match = SELF_READ_WITH_RE.match(stripped)
            if match and section_id and match.group(1) == section_id:
                drop.add(idx)
                stats["read_with"] += 1
                continue
            if (
                not is_file_level
                and UPSTREAM_RE.match(stripped)
                and stripped in file_upstreams
            ):
                drop.add(idx)
                stats["upstream"] += 1

        # A Trace with no surviving bullets carries nothing.
        survivors = [
            idx
            for idx in range(trace.start + 1, trace.end)
            if idx not in drop and BULLET_RE.match(lines[idx].strip())
        ]
        if survivors or is_file_level:
            continue

        drop.update(range(trace.start, trace.end + 1))
        stats["trace"] += 1

        following = next(
            (b for b in dacs if b.start > trace.end and b.start - trace.end <= 3), None
        )
        if following and dac_rows(lines, following) <= file_dac_rows:
            drop.update(range(following.start, following.end + 1))
            stats["dac"] += 1

    if not drop:
        return text, stats

    kept = [line for idx, line in enumerate(lines) if idx not in drop]
    result = "\n".join(kept)
    result = re.sub(r"\n{3,}", "\n\n", result)
    # A widget spacer with no widget above it is dead markup.
    result = re.sub(r"(^#{1,6} .*\n)\n*<br>\n+", r"\1\n", result, flags=re.M)
    if text.endswith("\n") and not result.endswith("\n"):
        result += "\n"
    return result, stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--layer", help="Restrict to one companion subdirectory.")
    parser.add_argument("--write", action="store_true", help="Apply changes to disk.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    subdirs = [args.layer] if args.layer else list(COMPANION_SUBDIRS)

    totals = {"downstream": 0, "read_with": 0, "upstream": 0, "trace": 0, "dac": 0}
    changed = 0
    for subdir in subdirs:
        base = root / subdir
        if not base.is_dir():
            print(f"No such layer: {subdir}", file=sys.stderr)
            return 2
        for path in sorted(base.glob("*.md")):
            new_text, stats = prune_file(path)
            if not any(stats.values()):
                continue
            changed += 1
            for key, value in stats.items():
                totals[key] += value
            rel = path.relative_to(root).as_posix()
            summary = ", ".join(f"{k}={v}" for k, v in stats.items() if v)
            print(f"{'wrote' if args.write else 'would prune'} {rel}: {summary}")
            if args.write:
                path.write_text(new_text, encoding="utf-8")

    print(
        f"\n{changed} files | Downstream {totals['downstream']}, "
        f"Read-with {totals['read_with']}, Upstream {totals['upstream']}, "
        f"Trace blocks {totals['trace']}, DAC blocks {totals['dac']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
