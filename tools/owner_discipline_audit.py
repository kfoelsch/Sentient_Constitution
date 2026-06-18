#!/usr/bin/env python3
"""Heuristic single-home discipline audit (advisory by default).

Flags O/E/C-shaped definition gloss blocks outside Chapter Five owner files.
Rule: OWNER-SINGLE-HOME in tools/architecture/rule_registry.json.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402

CH5_OWNERS = {
    "core_05-05_definitions_a_independent.md",
    "core_05-05_definitions_a_independent.md",
    "core_05o_oversight_definitions.md",
    "core_05p_participation_definitions.md",
    "core_05a_accountability_definitions.md",
    "core_05c_continuity_definitions.md",
    "core_05i_integrative_definitions.md",
}

OEC_BLOCK_RE = re.compile(
    r"^\s*(?:-\s*)?(?:\*\*)?O(?:bjective)?(?:\*\*)?\s*[:.]",
    re.I,
)
NEXT_OEC_RE = re.compile(r"^\s*(?:-\s*)?(?:\*\*)?[EC](?:\*\*)?\s*[:.]", re.I)


def scan_file(root: Path, path: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    if any(rel.endswith(name) or rel == name for name in CH5_OWNERS):
        return []
    if rel in {"doc_architecture.md", "README.md"}:
        return []

    lines = path.read_text(encoding="utf-8").splitlines()
    findings: list[str] = []
    i = 0
    while i < len(lines):
        if not OEC_BLOCK_RE.match(lines[i]):
            i += 1
            continue
        block_start = i + 1
        j = i + 1
        e_seen = c_seen = False
        while j < len(lines) and j < i + 12:
            if NEXT_OEC_RE.match(lines[j]):
                label = lines[j].strip()[:1].upper()
                if label == "E":
                    e_seen = True
                if label == "C":
                    c_seen = True
            if lines[j].startswith("#") and j > i:
                break
            if OEC_BLOCK_RE.match(lines[j]) and j > i:
                break
            j += 1
        if e_seen and c_seen:
            snippet = " / ".join(lines[i : min(j, i + 3)])
            findings.append(
                f"{rel}:{block_start}: possible competing O/E/C gloss outside Chapter Five — {snippet[:120]}"
            )
        i = j if j > i else i + 1
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero when findings exist (default: report only)",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()

    findings: list[str] = []
    for rel in binding_corpus_scope(root):
        path = root / rel
        if path.is_file():
            findings.extend(scan_file(root, path))

    print("Owner discipline audit (O/E/C gloss heuristic):")
    if findings:
        print("- Result: FAIL" if args.strict else "- Result: ADVISORY")
        for item in findings[:50]:
            print(f"  - {item}")
        if len(findings) > 50:
            print(f"  - … and {len(findings) - 50} more")
        return 1 if args.strict else 0

    print("- Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
