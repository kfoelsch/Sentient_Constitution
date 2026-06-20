#!/usr/bin/env python3
"""Audit routing labels that belong in Trace widgets, not operative prose.

Per ``doc_architecture.md`` rule 10 (Trace contents), ``Read with:`` routing
belongs inside the owning unit's Trace block. Operative prose must not carry
parallel ``**Also read**`` (or equivalent) routing sections with bullet lists,
standalone ``Read it with:`` headers followed by routing bullets, nor
line-initial ``Read with`` / ``**Read with**`` routing (with or without a
colon) outside Trace.

Disguised read-with routing in operative prose is also forbidden — for example
``Read them with …``, ``… must be read with …``, or ``… also read **§…**``
when the line's purpose is cross-section navigation rather than operative
substance.

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

# Operative-prose routing that should be Trace ``Read with:`` instead.
FORBIDDEN_ROUTING_PROSE_RES = (
    re.compile(r"^\*\*Also read\*\*:?\s*$", re.IGNORECASE),
    re.compile(r"^\*\*See also\*\*:?\s*$", re.IGNORECASE),
    re.compile(r"^\*\*Related reading\*\*:?\s*$", re.IGNORECASE),
    re.compile(r"^Read it with:\s*$", re.IGNORECASE),
    re.compile(r"^Read with:\s*$", re.IGNORECASE),
    re.compile(r"^\*\*Read with", re.IGNORECASE),
    re.compile(r"^Read it with\b", re.IGNORECASE),
    re.compile(r"^Read with\b", re.IGNORECASE),
    re.compile(r"^- Read with:", re.IGNORECASE),
)

# Disguised read-with navigation outside Trace blocks.
DISGUISED_READ_WITH_LINE_RES = (
    re.compile(r"^Read them with\b", re.IGNORECASE),
    re.compile(r"^Each .+\bmust be read with\b", re.IGNORECASE),
    re.compile(r";\s*where .+\balso read \*\*", re.IGNORECASE),
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

        for pattern in FORBIDDEN_ROUTING_PROSE_RES:
            if pattern.match(stripped):
                findings.append(
                    f"{rel}:{idx}: move routing to Trace ``Read with:`` "
                    f"(operative prose must not use {stripped!r})"
                )
                break
        else:
            for pattern in DISGUISED_READ_WITH_LINE_RES:
                if pattern.search(stripped):
                    findings.append(
                        f"{rel}:{idx}: move disguised read-with routing to Trace "
                        f"``Read with:`` (operative prose must not use {stripped!r})"
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
