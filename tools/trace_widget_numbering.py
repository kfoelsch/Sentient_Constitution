#!/usr/bin/env python3
"""Apply D13 and D14 to Trace widgets from the chapter-number registry."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
TRACE_RE = re.compile(
    r'(<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>\s*\n)(.*?)(\n</details>)',
    re.S,
)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
CORE_TARGET_RE = re.compile(r"^core_\d{2}\.\d{3}_[^/]+\.md$")
NAMED_CHAPTER_RE = re.compile(r"\b(?:Chapter\s+(?:One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve|Thirteen|Fourteen|Fifteen|Sixteen|Seventeen|Eighteen|\d+)|Part\s+[A-E])\b", re.I)
REFERENCE_RE = re.compile(
    r"\[[^\]]+\]\([^)]+\)|\*\*(?:Chapter\s+[A-Za-z0-9]+|(?:CF|CI|CJS|CS)-\d+(?:\.\d+)?(?:\s+§\s*\d+(?:\.\d+)*)?)\*\*",
    re.I,
)


def source_files(root: Path) -> list[Path]:
    paths = list(root.glob("core_*.md"))
    for folder in ("corpus_joint_structure", "corpus_systems", "corpus_institutions", "corpus_forum"):
        paths.extend((root / folder).glob("*.md"))
    return sorted(p for p in paths if p.is_file())


def registry_numbers(root: Path) -> dict[str, str]:
    data = json.loads((root / "tools/architecture/chapter_numbers.json").read_text(encoding="utf-8"))
    return {
        row["destination_file"]: row["display_id"]
        for row in data["chapters"]
        if row.get("layer") == "CORE" and row.get("status") == "active"
    }


def number_core_links(body: str, source: Path, root: Path, numbers: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        label, target = match.groups()
        target_path = target.split("#", 1)[0]
        if not target_path or not CORE_TARGET_RE.match(PurePosixPath(target_path).name):
            return match.group(0)
        resolved = (source.parent / target_path).resolve()
        try:
            rel = resolved.relative_to(root).as_posix()
        except ValueError:
            return match.group(0)
        number = numbers.get(PurePosixPath(rel).name)
        if not number or not NAMED_CHAPTER_RE.search(label):
            return match.group(0)
        section = re.search(r"§+\s*(\d+(?:\.\d+)*)", label)
        marker = f"({number}{f' §{section.group(1)}' if section else ''})"
        suffix = match.string[match.end() : match.end() + len(marker) + 2]
        if suffix.lstrip().startswith(marker):
            return match.group(0)
        return f"[{label}]({target}) {marker}"

    return LINK_RE.sub(replace, body)


def nested_long_lines(body: str) -> str:
    out: list[str] = []
    for raw_line in body.splitlines(keepends=True):
        ending = "\r\n" if raw_line.endswith("\r\n") else raw_line[-1:] if raw_line.endswith(("\n", "\r")) else ""
        line = raw_line[:-len(ending)] if ending else raw_line
        stripped = line.lstrip()
        indent = line[: len(line) - len(stripped)]
        if not stripped.startswith("- ") or len(REFERENCE_RE.findall(stripped)) < 4:
            out.append(raw_line)
            continue
        content = stripped[2:]
        references = list(REFERENCE_RE.finditer(content))
        if len(references) < 4:
            out.append(raw_line)
            continue
        # Keep the category or explanatory lead on the parent, then give each
        # recognized citation its own child bullet. Splitting at citations
        # rather than punctuation also makes repeated application idempotent.
        lead = content[: references[0].start()].strip()
        separator = ending or "\n"
        out.append(f"{indent}- {lead or 'References:'}{separator}")
        for index, reference in enumerate(references):
            end = references[index + 1].start() if index + 1 < len(references) else len(content)
            piece = content[reference.start() : end].strip()
            child_ending = ending if index == len(references) - 1 else separator
            out.append(f"{indent}  - {piece}{child_ending}")
    return "".join(out)


def transform(
    text: str,
    source: Path,
    root: Path,
    numbers: dict[str, str],
    *,
    add_numbers: bool = True,
    nest_references: bool = True,
) -> str:
    def apply(match: re.Match[str]) -> str:
        body = match.group(2)
        if add_numbers:
            body = number_core_links(body, source, root, numbers)
        if nest_references:
            body = nested_long_lines(body)
        return match.group(1) + body + match.group(3)

    return TRACE_RE.sub(apply, text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--apply", action="store_true", help="Write changes (default is a report).")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--numbers-only", action="store_true", help="Apply D13 only.")
    mode.add_argument("--nested-only", action="store_true", help="Apply D14 only.")
    args = parser.parse_args()
    root = args.root.resolve()
    numbers = registry_numbers(root)
    changes: list[tuple[Path, str, str]] = []
    for path in source_files(root):
        original = path.read_text(encoding="utf-8")
        updated = transform(
            original,
            path,
            root,
            numbers,
            add_numbers=not args.nested_only,
            nest_references=not args.numbers_only,
        )
        if updated != original:
            changes.append((path, original, updated))
    if args.apply:
        for path, _old, updated in changes:
            path.write_text(updated, encoding="utf-8")
    mode = "Updated" if args.apply else "Would update"
    print(f"{mode} {len(changes)} file(s) in Trace widgets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
