#!/usr/bin/env python3
"""Insert missing NAV-DAC-12 entry / E / C anchor tags on Chapter Five definitions."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_dac_widget_audit import (  # noqa: E402
    ANCHOR_TAG_RE,
    CLUSTERED_HEADS,
    H4_RE,
    H5_RE,
    MISSING_C,
    STRUCTURAL_HEADINGS,
    resolve_entry_slug,
    scan_entry_body,
)
from ch5_paths import CH5_ALL, CH5_BANDS  # noqa: E402
from ch5_single_definition_audit import DIR_ROW_RE, parse_directory  # noqa: E402

ANCHOR_LINE_RE = re.compile(r'^<a id="([^"]+)"></a>\s*$')


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument(
        "--file",
        action="append",
        help="Limit repair to one or more Chapter Five band files.",
    )
    p.add_argument("--dry-run", action="store_true", help="Report changes without writing.")
    return p.parse_args()


def directory_anchor_map(root: Path) -> dict[tuple[str, str], str]:
    rows, _ = parse_directory(root)
    out: dict[tuple[str, str], str] = {}
    for row in rows:
        if row.list_name != "Definitions A-Z":
            continue
        if "#" not in row.href:
            continue
        file_name, fragment = row.href.split("#", 1)
        out[(file_name, row.label)] = fragment
    return out


def entry_end(lines: list[str], heading_idx: int) -> int:
    depth = len(lines[heading_idx].strip()) - len(lines[heading_idx].strip().lstrip("#"))
    for idx in range(heading_idx + 1, len(lines)):
        match = H4_RE.match(lines[idx])
        if match and len(lines[idx].strip()) - len(lines[idx].strip().lstrip("#")) <= depth:
            return idx
    return len(lines)


def has_explicit_entry_anchor(lines: list[str], heading_idx: int) -> str | None:
    j = heading_idx - 1
    while j >= 0 and lines[j].strip() == "":
        j -= 1
    while j >= 0 and lines[j].strip() == "---":
        j -= 1
        while j >= 0 and lines[j].strip() == "":
            j -= 1
    if j >= 0:
        match = ANCHOR_TAG_RE.match(lines[j])
        if match:
            return match.group(1)
    return None


def repair_file(
    path: Path,
    directory_map: dict[tuple[str, str], str],
    dry_run: bool,
) -> int:
    rel = path.name
    lines = path.read_text(encoding="utf-8").splitlines()
    inserts: list[tuple[int, list[str]]] = []
    repairs = 0

    for idx, line in enumerate(lines):
        match = H4_RE.match(line) or H5_RE.match(line)
        if not match:
            continue
        label = match.group(1).strip()
        is_h5 = bool(H5_RE.match(line))
        slug = resolve_entry_slug(lines, idx)
        if slug in STRUCTURAL_HEADINGS or slug in CLUSTERED_HEADS:
            continue

        body = scan_entry_body(lines, idx)
        if not body["has_o"]:
            continue

        expected = directory_map.get((rel, label))
        explicit = has_explicit_entry_anchor(lines, idx)
        canonical = expected or slug

        if expected and explicit != expected:
            anchor_line = f'<a id="{expected}"></a>'
            if explicit is None:
                inserts.append((idx, [anchor_line, ""]))
                repairs += 1
            canonical = expected

        if is_h5:
            continue

        end = entry_end(lines, idx)
        inline = body["inline_anchors"]

        for j in range(idx + 1, end):
            stripped = lines[j].strip()
            match = ANCHOR_LINE_RE.match(stripped)
            if match and match.group(1) in {f"{slug}-e", f"{canonical}-e"}:
                if match.group(1) != f"{canonical}-e":
                    lines[j] = f'<a id="{canonical}-e"></a>'
                    repairs += 1
                inline.add(f"{canonical}-e")
                break
            if stripped.startswith("- E:") and f"{canonical}-e" not in inline:
                inserts.append((j, [f'<a id="{canonical}-e"></a>']))
                inline.add(f"{canonical}-e")
                repairs += 1
                break

        if canonical not in MISSING_C:
            for j in range(idx + 1, end):
                stripped = lines[j].strip()
                match = ANCHOR_LINE_RE.match(stripped)
                if match and match.group(1) in {f"{slug}-c", f"{canonical}-c"}:
                    if match.group(1) != f"{canonical}-c":
                        lines[j] = f'<a id="{canonical}-c"></a>'
                        repairs += 1
                    break
                if stripped.startswith("- C:") and f"{canonical}-c" not in inline:
                    inserts.append((j, [f'<a id="{canonical}-c"></a>']))
                    repairs += 1
                    break

    if not repairs:
        return 0

    inserts.sort(key=lambda item: item[0], reverse=True)
    for line_idx, new_lines in inserts:
        lines[line_idx:line_idx] = new_lines

    if dry_run:
        print(f"Would repair {repairs} anchor change(s) in {rel}")
    else:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Repaired {repairs} anchor change(s) in {rel}")
    return repairs


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    targets = args.file or CH5_BANDS
    directory_map = directory_anchor_map(root)
    total = 0
    for rel in targets:
        path = root / rel
        if not path.is_file():
            print(f"Skip missing file: {rel}", file=sys.stderr)
            continue
        total += repair_file(path, directory_map, args.dry_run)
    return 0 if total >= 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
