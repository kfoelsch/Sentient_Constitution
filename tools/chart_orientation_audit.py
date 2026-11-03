#!/usr/bin/env python3
"""Check Mermaid flowchart directions against VIS-CHART-ORIENT-04."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))
from corpus_paths import binding_corpus_scope  # noqa: E402

RULE = "VIS-CHART-ORIENT-04"
OPEN = re.compile(r"^\s*```\s*mermaid\b", re.I)
CLOSE = re.compile(r"^\s*```\s*$")
DIRECTION = re.compile(r"^\s*flowchart\s+(LR|RL|BT)\b", re.I)
EXCEPTION = re.compile(r"^\s*%%\s*VIS-CHART-ORIENT-04 exception:\s*\S.+", re.I)


def scan_text(rel: str, text: str) -> list[str]:
    findings: list[str] = []
    chart = False
    for number, line in enumerate(text.splitlines(), 1):
        if not chart:
            chart = bool(OPEN.match(line))
            continue
        if CLOSE.match(line):
            chart = False
            continue
        match = DIRECTION.match(line)
        if match:
            following = text.splitlines()[number:number + 3]
            if not any(EXCEPTION.match(item) for item in following):
                findings.append(f"{rel}:{number}: {RULE}: flowchart {match.group(1).upper()} needs an explicit exception note")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--paths", nargs="*", help="Repository-relative Markdown paths")
    args = parser.parse_args()
    root = args.root.resolve()
    scope = list(binding_corpus_scope(root, include_support_docs=False))
    for pattern in ("CONTRIBUTING.md", "guides/*.md", "implementation/*.md"):
        scope.extend(p.relative_to(root).as_posix() for p in sorted(root.glob(pattern)) if p.is_file())
    if args.paths:
        allowed = set(scope)
        scope = [p for p in args.paths if p in allowed]
    findings = [finding for rel in scope if (root / rel).is_file()
                for finding in scan_text(rel, (root / rel).read_text(encoding="utf-8"))]
    if findings:
        print(f"FAIL: {RULE} — {len(findings)} non-default chart direction(s) need exception notes.")
        print("\n".join(f"  {item}" for item in findings))
        return 1
    print(f"PASS: {RULE} — flowchart directions follow the default or state an exception.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
