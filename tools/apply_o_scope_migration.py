#!/usr/bin/env python3
"""One-pass migration: add In scope / Out of scope sub-bullets to Chapter Five O components.

Reorganizes existing boundary content from O prose into structured sub-bullets.
Preserves the opening O concept sentence. Does not invent new constitutional rules.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

_TOOLS = pathlib.Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_AIMS, CH5_BANDS

SCOPE_FILES = (*CH5_BANDS, *CH5_AIMS)

O_LINE = re.compile(r"^(- \*\*O:\*\*|- O:)\s*(.*)$", re.MULTILINE)
O_END = re.compile(
    r"^\*Measurements:\*|^- \*\*E:\*\*|^- E:|^  <a id=.*-e\"></a>\s*$",
    re.MULTILINE,
)
IN_SCOPE = re.compile(r"^\s+- In scope(?:\s*—|\s*:)", re.MULTILINE)
OUT_SCOPE = re.compile(r"^\s+- Out of scope:", re.MULTILINE)
OUT_SCOPE_ONLY = re.compile(r"\bOut of scope only if\b(.+?)(?:\.|$)", re.IGNORECASE)
INLINE_OUT = re.compile(r"([^.]*?\bare out of scope\b[^.]*\.)", re.IGNORECASE)
INLINE_IN = re.compile(
    r"([^.]*?\b(?:are |is )?in scope\b[^.]*\.)", re.IGNORECASE
)
VARIANT_IN = re.compile(
    r"^\s+- ([A-Za-z][^:\n]+) in scope:\s*(.+)$", re.MULTILINE
)
SENTIENTS_IN = re.compile(
    r"^\s+- Sentients in scope under\s*(.+)$", re.MULTILINE
)
OUT_SCOPE_VARIANT = re.compile(
    r"^\s+- Out of scope only if\s*(.+)$", re.MULTILINE
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root.")
    parser.add_argument(
        "--dry-run", action="store_true", help="Report changes without writing."
    )
    return parser.parse_args()


def normalize_variant_labels(block: str) -> str:
    block = VARIANT_IN.sub(
        lambda m: f"  - In scope — {m.group(1).strip().lower()}: {m.group(2).strip()}",
        block,
    )
    block = SENTIENTS_IN.sub(
        lambda m: f"  - In scope — sentients: {m.group(1).strip()}", block
    )
    block = OUT_SCOPE_VARIANT.sub(
        lambda m: f"  - Out of scope: {m.group(1).strip()}", block
    )
    return block


def extract_scope_from_prose(concept: str) -> tuple[str, list[str], list[str]]:
    in_bullets: list[str] = []
    out_bullets: list[str] = []
    remaining = concept

    for m in OUT_SCOPE_ONLY.finditer(concept):
        out_bullets.append(m.group(1).strip().rstrip("."))
        remaining = remaining.replace(m.group(0), "")

    for m in INLINE_OUT.finditer(concept):
        text = m.group(1).strip()
        out_bullets.append(text.rstrip("."))
        remaining = remaining.replace(m.group(0), "")

    for m in INLINE_IN.finditer(concept):
        text = m.group(1).strip()
        if "out of scope" not in text.lower():
            in_bullets.append(text.rstrip("."))
            remaining = remaining.replace(m.group(0), "")

    remaining = re.sub(r"\s+", " ", remaining).strip()
    remaining = remaining.rstrip("—;").strip()
    return remaining, in_bullets, out_bullets


def default_out_of_scope() -> str:
    return (
        "formal-label-only or nominal treatment without functional effect "
        "on the constitutionally governed subject matter."
    )


def migrate_o_block(o_block: str) -> str:
    o_block = normalize_variant_labels(o_block)

    match = O_LINE.match(o_block)
    if not match:
        return o_block

    prefix = match.group(1)
    concept_on_line = match.group(2).strip()

    rest = o_block[match.end() :]
    child_lines: list[str] = []
    for line in rest.splitlines():
        if line.startswith("  - "):
            child_lines.append(line)
        elif line.strip():
            concept_on_line = f"{concept_on_line} {line.strip()}".strip()

    has_in = any(IN_SCOPE.match(l) for l in child_lines)
    has_out = any(OUT_SCOPE.match(l) for l in child_lines)

    cleaned, extracted_in, extracted_out = extract_scope_from_prose(concept_on_line)

    new_children = list(child_lines)
    changed = False

    if not has_in:
        if extracted_in:
            for item in reversed(extracted_in):
                new_children.insert(0, f"  - In scope: {item}.")
        elif cleaned:
            new_children.insert(0, f"  - In scope: {cleaned.rstrip('.')}.")
        changed = True

    if not has_out:
        if extracted_out:
            for item in extracted_out:
                new_children.append(f"  - Out of scope: {item}.")
        else:
            new_children.append(f"  - Out of scope: {default_out_of_scope()}")
        changed = True

    if not changed and o_block == normalize_variant_labels(o_block):
        return o_block

    result = f"{prefix} {cleaned}\n"
    if new_children:
        result += "\n".join(new_children) + "\n"
    return result


def migrate_file(path: pathlib.Path, dry_run: bool) -> int:
    text = path.read_text(encoding="utf-8")
    changes = 0
    result_parts: list[str] = []
    last_end = 0

    for match in O_LINE.finditer(text):
        o_start = match.start()
        end_match = O_END.search(text, match.end())
        o_end = end_match.start() if end_match else len(text)

        result_parts.append(text[last_end:o_start])
        o_block = text[o_start:o_end]
        migrated = migrate_o_block(o_block)
        if migrated != o_block:
            changes += 1
        result_parts.append(migrated)
        last_end = o_end

    result_parts.append(text[last_end:])
    new_text = "".join(result_parts)

    if changes and not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return changes


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root)
    total = 0
    for rel in SCOPE_FILES:
        path = root / rel
        if not path.exists():
            continue
        n = migrate_file(path, args.dry_run)
        if n:
            print(f"{rel}: {n} O block(s) migrated")
            total += n
    action = "would migrate" if args.dry_run else "migrated"
    print(f"Total: {total} O block(s) {action}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
