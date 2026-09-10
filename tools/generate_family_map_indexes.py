#!/usr/bin/env python3
"""Generate grouped companion-wrapper family indexes from family_map.json.

The four landing wrappers are the human TOCs. This tool patches the region
between BEGIN/END GENERATED FAMILY INDEX markers. ``--check`` is the audit
mode used by ``make family-map-audit``.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAMILY_MAP_PATH = ROOT / "tools" / "architecture" / "family_map.json"
BEGIN = "<!-- BEGIN GENERATED FAMILY INDEX -->"
END = "<!-- END GENERATED FAMILY INDEX -->"


def load_family_map(root: Path) -> dict:
    path = root / "tools" / "architecture" / "family_map.json"
    return json.loads(path.read_text(encoding="utf-8"))


def entry_href(entry: dict, wrapper: str) -> str:
    rel = entry["file"]
    anchor = entry.get("anchor")
    href = rel
    if wrapper and "/" not in wrapper:
        # Wrapper is at repo root; subfile paths are already repo-relative.
        href = rel
    if anchor:
        href = f"{href}#{anchor}"
    return href


def render_layer_index(layer: dict) -> str:
    wrapper = layer["wrapper"]
    heading = layer["index_heading"]
    lines = [f"## {heading}", ""]
    for group in layer["groups"]:
        lines.append(f"### {group['title']}")
        lines.append("")
        lines.append("| Stable family | Authoritative subfile |")
        lines.append("|---|---|")
        for entry in group["entries"]:
            href = entry_href(entry, wrapper)
            label = entry["label"]
            if entry.get("status") == "reserved":
                note = entry.get("note", "Reserved family ID.")
                cell = f"{note} See [{Path(entry['file']).name}]({href})."
                lines.append(f"| {label} | {cell} |")
            else:
                name = Path(entry["file"]).name
                lines.append(f"| {label} | [{name}]({href}) |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def patch_region(text: str, body: str) -> str:
    if BEGIN not in text or END not in text:
        raise ValueError("missing generated-index markers")
    before, rest = text.split(BEGIN, 1)
    _, after = rest.split(END, 1)
    return f"{before}{BEGIN}\n{body}{END}{after}"


def expected_wrapper_text(root: Path, layer: dict) -> str:
    wrapper = root / layer["wrapper"]
    current = wrapper.read_text(encoding="utf-8")
    body = render_layer_index(layer)
    return patch_region(current, body)


def validate_map(root: Path, data: dict) -> list[str]:
    errors: list[str] = []
    for layer_id, layer in data["layers"].items():
        wrapper = root / layer["wrapper"]
        if not wrapper.is_file():
            errors.append(f"{layer_id}: missing wrapper {layer['wrapper']}")
            continue
        text = wrapper.read_text(encoding="utf-8")
        if BEGIN not in text or END not in text:
            errors.append(f"{layer['wrapper']}: missing {BEGIN} / {END} markers")
        for group in layer["groups"]:
            for entry in group["entries"]:
                path = root / entry["file"]
                if not path.is_file():
                    errors.append(f"{entry['id']}: missing file {entry['file']}")
    for cluster, rel in data.get("cjs3_cluster_homes", {}).items():
        path = root / rel
        if not path.is_file():
            errors.append(f"cjs3 cluster {cluster}: missing {rel}")
    for section, rel in data.get("cjs12_section_homes", {}).items():
        path = root / rel
        if not path.is_file():
            errors.append(f"cjs12 section {section}: missing {rel}")
    for section, rel in data.get("cs_section_homes", {}).items():
        path = root / rel
        if not path.is_file():
            errors.append(f"cs section {section}: missing {rel}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Patch wrapper indexes from family_map.json.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if wrapper indexes drift from family_map.json.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    data = load_family_map(root)
    errors = validate_map(root, data)
    if errors:
        print("Family map validation failures:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    drift: list[str] = []
    for layer_id, layer in data["layers"].items():
        wrapper = root / layer["wrapper"]
        current = wrapper.read_text(encoding="utf-8")
        try:
            expected = expected_wrapper_text(root, layer)
        except ValueError as exc:
            print(f"{layer['wrapper']}: {exc}", file=sys.stderr)
            return 1
        if current != expected:
            if args.write:
                wrapper.write_text(expected, encoding="utf-8")
            else:
                drift.append(layer["wrapper"])

    if args.write:
        print("Wrote grouped family indexes into the four companion wrappers.")
        return 0
    if drift:
        print("Family-map index drift:", file=sys.stderr)
        for rel in drift:
            print(f"  - {rel} (run: make family-map-indexes)", file=sys.stderr)
        return 1
    print("Family-map indexes match family_map.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
