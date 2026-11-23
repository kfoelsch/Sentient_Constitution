#!/usr/bin/env python3
"""Check that every chapter lead file opens with a standard section 1.

Each core chapter lead file (``core_NN.000_*.md``) except the Preamble must carry,
as its first numbered section:

- the exact heading ``### 1. Purpose, Role, and Scope``; and
- inside that section, the three lead-ins ``**Purpose:**``, ``**Role:**`` and
  ``**Chapter scope:**``, each opening its own line (an anchor tag may come
  first), in that order.

Exempt: the Preamble, which is not a numbered chapter. Subcore files use their
own opening and are not checked here.

Rule ID: CHAPTER-S1-PURPOSE-01 (blocking; part of ``make regression``).
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "CHAPTER-S1-PURPOSE-01"
HEADING = "### 1. Purpose, Role, and Scope"
LEAD_INS = ("**Purpose:**", "**Role:**", "**Chapter scope:**")

EXEMPT = {"core_00.000_preamble.md"}
LEAD_RE = re.compile(r"^core_\d\d\.000_.+\.md$")
TOP_RE = re.compile(r"^###\s+(\d+)\.\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^(```|~~~)")
ANCHOR_PREFIX_RE = re.compile(r"^(?:<a id=\"[^\"]*\"></a>)+")


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    message: str


def in_scope(rel_path: str) -> bool:
    name = Path(rel_path).name
    if name != rel_path or name in EXEMPT:
        return False
    return bool(LEAD_RE.match(name))


def scan_text(rel_path: str, text: str) -> list[Finding]:
    lines = text.splitlines()
    in_fence = False
    start = None
    end = len(lines)
    for i, line in enumerate(lines):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = TOP_RE.match(line)
        if not m:
            continue
        if start is None:
            if m.group(1) != "1":
                return [Finding(rel_path, i + 1, f"first numbered section is not §1: '{line.strip()}'")]
            start = i
        else:
            end = i
            break
    if start is None:
        return [Finding(rel_path, 1, "no `### 1.` section")]
    findings: list[Finding] = []
    if lines[start].rstrip() != HEADING:
        findings.append(
            Finding(rel_path, start + 1, f"§1 heading is not `{HEADING}`: '{lines[start].strip()}'")
        )
    positions: list[int] = []
    for label in LEAD_INS:
        hit = None
        for j in range(start + 1, end):
            body = ANCHOR_PREFIX_RE.sub("", lines[j].strip())
            if body.startswith(label):
                hit = j
                break
        if hit is None:
            findings.append(Finding(rel_path, start + 1, f"§1 has no `{label}` lead-in"))
        else:
            positions.append(hit)
    if len(positions) == len(LEAD_INS) and positions != sorted(positions):
        findings.append(
            Finding(rel_path, start + 1, "§1 lead-ins are not in the order Purpose, Role, Chapter scope")
        )
    return findings


def scan_file(root: Path, rel_path: str) -> list[Finding]:
    path = root / rel_path
    if not path.is_file():
        return []
    return scan_text(rel_path, path.read_text(encoding="utf-8"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    scope = [rel for rel in binding_corpus_scope(root) if in_scope(rel)]
    findings = [f for rel in scope for f in scan_file(root, rel)]
    if not findings:
        print(
            f"PASS: {RULE} — {len(scope)} chapter lead files open with "
            f"'{HEADING}' and its Purpose, Role, and Chapter scope lead-ins."
        )
        return 0
    print(f"FAIL: {RULE} — {len(findings)} finding(s) in the section 1 standard.")
    for f in findings:
        print(f"  {f.file}:{f.line}: {RULE}: {f.message}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
