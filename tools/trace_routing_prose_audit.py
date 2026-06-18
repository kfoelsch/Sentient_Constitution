#!/usr/bin/env python3
"""Audit routing labels that belong in Trace widgets, not operative prose.

Per ``doc_architecture.md`` rule 10 (Trace contents), ``Read with:`` routing
belongs inside the owning unit's Trace block. Operative prose must not carry
parallel ``**Also read**`` (or equivalent) routing sections with bullet lists,
nor standalone ``Read it with:`` headers followed by routing bullets.

This gate flags those routing headers outside ``<details>`` blocks in the
binding corpus scope.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from corpus_paths import binding_corpus_scope

ROOT = Path(__file__).resolve().parents[1]

# Operative-prose routing headers that should be Trace ``Read with:`` instead.
FORBIDDEN_ROUTING_HEADER_RES = (
    re.compile(r"^\*\*Also read\*\*:?\s*$", re.IGNORECASE),
    re.compile(r"^\*\*See also\*\*:?\s*$", re.IGNORECASE),
    re.compile(r"^\*\*Related reading\*\*:?\s*$", re.IGNORECASE),
    re.compile(r"^Read it with:\s*$", re.IGNORECASE),
    re.compile(r"^Read with:\s*$", re.IGNORECASE),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args()


def audit_file(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    lines = path.read_text(encoding="utf-8").splitlines()
    findings: list[str] = []

    in_details = 0
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if stripped.startswith("<details>"):
            in_details += 1
            continue
        if stripped == "</details>":
            in_details = max(0, in_details - 1)
            continue

        if in_details:
            continue
        if stripped.startswith(">"):
            continue

        for pattern in FORBIDDEN_ROUTING_HEADER_RES:
            if pattern.match(stripped):
                findings.append(
                    f"{rel}:{idx}: move routing to Trace ``Read with:`` "
                    f"(operative prose must not use {stripped!r})"
                )
                break

    return findings


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    findings: list[str] = []

    for rel in binding_corpus_scope(root):
        path = root / rel
        if path.is_file() and path.suffix == ".md":
            findings.extend(audit_file(path, root))

    if findings:
        print("Trace routing prose audit failures:", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        print(f"Total: {len(findings)}", file=sys.stderr)
        return 1

    print("Trace routing prose audit OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
