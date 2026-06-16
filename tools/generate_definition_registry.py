#!/usr/bin/env python3
"""Generate the AI definition registry from authoritative Chapter Five files."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
import sys

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL, CH5_PART_A, CH5_PART_B, CH5_PART_C  # noqa: E402
from ch5_single_definition_audit import (  # noqa: E402
    HEADING_RE,
    collect_cluster_members,
    href_for,
    owns_oec,
    previous_entry_anchor,
)


@dataclass(frozen=True)
class RegistryEntry:
    term: str
    source_file: str
    anchor: str
    line_start: int
    line_end: int
    category: str
    cluster_membership: dict[str, str | int] | None


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument("--output", required=True, help="Output JSON path.")
    return p.parse_args()


def body_end(lines: list[str], heading_idx: int, max_depth: int) -> int:
    for idx in range(heading_idx + 1, len(lines)):
        stripped = lines[idx].strip()
        match = HEADING_RE.match(stripped)
        if (
            match
            and len(match.group(1)) <= max_depth
            and not match.group(2).strip().startswith("In plain terms:")
        ):
            return idx
    return len(lines)


def body_until_next_heading(lines: list[str], heading_idx: int, max_depth: int) -> str:
    return "\n".join(lines[heading_idx + 1 : body_end(lines, heading_idx, max_depth)])


def category_for(file_name: str) -> str:
    if file_name == CH5_PART_A:
        return "independent"
    if file_name == CH5_PART_B:
        return "semi_independent"
    return "dependent_cluster"


def collect_entries(root: Path) -> list[RegistryEntry]:
    memberships: dict[str, list[dict[str, str | int]]] = defaultdict(list)
    for member in collect_cluster_members(root):
        memberships[member.label].append(
            {
                "cluster": member.owner,
                "cluster_file": CH5_PART_C,
                "line": member.line,
            }
        )

    entries: list[RegistryEntry] = []
    for file_name in CH5_ALL:
        path = root / file_name
        lines = path.read_text(encoding="utf-8").splitlines()
        in_part_a_defs = False
        for idx, raw in enumerate(lines):
            stripped = raw.strip()
            if file_name == CH5_PART_A:
                if stripped == "### 1. Independent Definitions":
                    in_part_a_defs = True
                    continue
                if not in_part_a_defs:
                    continue
            match = HEADING_RE.match(stripped)
            if not match:
                continue
            depth = len(match.group(1))
            label = match.group(2).strip()
            if label.startswith("In plain terms:"):
                continue
            if file_name == CH5_PART_C:
                if depth != 5:
                    continue
                max_depth = 5
            else:
                if depth != 4:
                    continue
                max_depth = 4
            body = body_until_next_heading(lines, idx, max_depth)
            if not owns_oec(body):
                continue
            anchor_href = href_for(file_name, previous_entry_anchor(lines, idx), label)
            anchor = anchor_href.split("#", 1)[1]
            member_entries = memberships.get(label, [])
            if len(member_entries) > 1:
                raise SystemExit(f"Definition {label!r} has multiple cluster memberships")
            entries.append(
                RegistryEntry(
                    term=label,
                    source_file=file_name,
                    anchor=f"#{anchor}",
                    line_start=idx + 1,
                    line_end=body_end(lines, idx, max_depth),
                    category=category_for(file_name),
                    cluster_membership=member_entries[0] if member_entries else None,
                )
            )
    return sorted(entries, key=lambda entry: entry.term.casefold())


def anchor_line(path: Path, anchor: str) -> int:
    anchor_id = anchor.lstrip("#")
    needle = f'id="{anchor_id}"'
    for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if needle in line:
            return idx
    raise SystemExit(f"Missing anchor {anchor} in {path}")


def principle_layer_entries(root: Path) -> list[RegistryEntry]:
    preamble = root / "core_00_preamble.md"
    values = root / "core_01_a_values_principles.md"
    triad_start = anchor_line(preamble, "#constitutional-triad")
    spec: list[tuple[str, Path, str, int | None]] = [
        ("Constitutional Triad", preamble, "#constitutional-triad", triad_start + 4),
        ("material stake", preamble, "#material-stake", None),
        ("Two Constitutional Aims", values, "#two-constitutional-aims", None),
        ("Flourishing", values, "#flourishing", None),
        ("Continuity", values, "#continuity", None),
    ]
    entries: list[RegistryEntry] = []
    for term, path, anchor, line_end in spec:
        line_start = anchor_line(path, anchor)
        entries.append(
            RegistryEntry(
                term=term,
                source_file=path.name,
                anchor=anchor,
                line_start=line_start,
                line_end=line_end if line_end is not None else line_start,
                category="principle_layer",
                cluster_membership=None,
            )
        )
    return entries


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    entries = collect_entries(root) + principle_layer_entries(root)
    entries = sorted(entries, key=lambda entry: entry.term.casefold())
    payload = {
        "$schema": "../schemas/definition_registry.schema.json",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source": "authoritative Chapter Five core files and Chapter One principle-layer anchors (preamble + Part A)",
        "definition_count": len(entries),
        "definitions": [asdict(entry) for entry in entries],
    }
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} definitions to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
