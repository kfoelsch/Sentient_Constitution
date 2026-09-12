#!/usr/bin/env python3
"""Inventory doc_architecture.md and corpus references to its sections."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import defaultdict
from pathlib import Path

_TOOLS = Path(__file__).resolve().parents[1]
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402

SECTION_RE = re.compile(r"^## (.+)$", re.M)
REF_PATTERNS = [
    re.compile(r"doc_architecture\.md(?:\s+)?(?:section|sec\.|§)\s*(\d+[A-Z]?)", re.I),
    re.compile(r"doc_architecture\.md\s+\*\*section\s+(\d+)\*\*", re.I),
    re.compile(r"doc_architecture\.md\s+\*\*section\s+(\d+[A-Z]?)\*\*", re.I),
    re.compile(r"doc_architecture rule\s+(\d+)", re.I),
]


def section_line_counts(text: str) -> list[tuple[str, int]]:
    matches = list(SECTION_RE.finditer(text))
    rows: list[tuple[str, int]] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[start:end]
        rows.append((match.group(1).strip(), body.count("\n")))
    return rows


def scan_references(root: Path) -> dict[str, list[str]]:
    hits: dict[str, list[str]] = defaultdict(list)
    scan_paths = [
        *binding_corpus_scope(root, include_support_docs=True),
        "tools",
        "implementation",
        "Makefile",
    ]
    for rel in scan_paths:
        path = root / rel
        if path.is_dir():
            for file in sorted(path.rglob("*")):
                if file.suffix not in {".md", ".py", ".mdc"} and file.name != "Makefile":
                    continue
                if "archive" in file.parts or "evidence" in file.parts:
                    continue
                _scan_file(root, file, hits)
            continue
        if not path.is_file():
            continue
        _scan_file(root, path, hits)
    return hits


def _scan_file(root: Path, path: Path, hits: dict[str, list[str]]) -> None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return
    if "doc_architecture" not in text and "architecture_primer" not in text:
        return
    rel = path.relative_to(root).as_posix()
    for pat in REF_PATTERNS:
        for match in pat.finditer(text):
            key = match.group(1)
            line = text.count("\n", 0, match.start()) + 1
            hits[key].append(f"{rel}:{line}")
    if "architecture_primer.md" in text and rel.startswith(
        tuple(binding_corpus_scope(root, include_support_docs=True))
    ):
        for idx, line in enumerate(text.splitlines(), start=1):
            if "architecture_primer.md" in line:
                hits["architecture_primer.md"].append(f"{rel}:{idx}")


def render_report(root: Path) -> str:
    doc_path = root / "doc_architecture.md"
    text = doc_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    refs = scan_references(root)
    rows = section_line_counts(text)
    today = dt.date.today().isoformat()
    out: list[str] = [
        f"# doc_architecture inventory ({today})",
        "",
        f"- File: `{doc_path.relative_to(root).as_posix()}`",
        f"- Lines: {len(lines)}",
        f"- Bytes: {doc_path.stat().st_size}",
        "",
        "## Section sizes",
        "",
        "| Section | Lines |",
        "|---------|------:|",
    ]
    for title, count in rows:
        out.append(f"| {title} | {count} |")
    out.extend(["", "## External references", ""])
    for key in sorted(refs, key=lambda k: (k.isdigit(), k)):
        out.append(f"### {key}")
        for item in sorted(set(refs[key]))[:40]:
            out.append(f"- `{item}`")
        if len(set(refs[key])) > 40:
            out.append(f"- … and {len(set(refs[key])) - 40} more")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--write-evidence",
        action="store_true",
        help="Write evidence/<date>/doc_architecture_inventory.md",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    report = render_report(root)
    print(report)
    if args.write_evidence:
        out_dir = root / "evidence" / dt.date.today().isoformat()
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "doc_architecture_inventory.md"
        out_path.write_text(report, encoding="utf-8")
        print(f"Wrote {out_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
