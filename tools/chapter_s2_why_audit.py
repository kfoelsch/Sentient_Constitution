#!/usr/bin/env python3
"""Check that every chapter lead file and every subcore file has a section 2 *why*.

Each core chapter lead file (``core_NN.000_*.md``) and each subcore file
(``subcore_*.md``) must carry, as its section 2:

- a ``### 2. Why …`` heading (the section explains why the chapter or file
  exists); and
- inside that section, a ``**Grounded in:**`` label on its own line, followed by
  a bulleted list.

Exempt: the Preamble (not a chapter) and Chapter Two, whose §2 is principle text
(custodian's review of the section 2 drafts, 2026-11-20).

Rule ID: CHAPTER-S2-WHY-01 (blocking; part of ``make preflight``).
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
RULE = "CHAPTER-S2-WHY-01"

EXEMPT = {
    "core_00.000_preamble.md",
    "core_02.000_values_principles.md",
}
LEAD_RE = re.compile(r"^core_\d\d\.000_.+\.md$")
SUBCORE_RE = re.compile(r"^subcore_.+\.md$")
TOP_RE = re.compile(r"^###\s+(\d+)\.\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^(```|~~~)")
GROUNDED_RE = re.compile(r"^\*\*Grounded in:\*\*\s*$")
LIST_ITEM_RE = re.compile(r"^-\s+\S")


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    message: str


def in_scope(rel_path: str) -> bool:
    name = Path(rel_path).name
    if name != rel_path or name in EXEMPT:
        return False
    return bool(LEAD_RE.match(name) or SUBCORE_RE.match(name))


def scan_text(rel_path: str, text: str) -> list[Finding]:
    lines = text.splitlines()
    in_fence = False
    start = None
    title = ""
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
        if start is None and m.group(1) == "2":
            start, title = i, m.group(2)
        elif start is not None:
            end = i
            break
    if start is None:
        return [Finding(rel_path, 1, "no `### 2.` section")]
    findings: list[Finding] = []
    if not title.startswith("Why "):
        findings.append(
            Finding(rel_path, start + 1, f"§2 heading does not start with 'Why': '{title}'")
        )
    body = lines[start + 1 : end]
    label = next((j for j, line in enumerate(body) if GROUNDED_RE.match(line.strip())), None)
    if label is None:
        findings.append(Finding(rel_path, start + 1, "§2 has no `**Grounded in:**` label"))
        return findings
    following = next((line for line in body[label + 1 :] if line.strip()), "")
    if not LIST_ITEM_RE.match(following):
        findings.append(
            Finding(
                rel_path,
                start + label + 2,
                "`**Grounded in:**` is not followed by a bulleted list",
            )
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
            f"PASS: {RULE} — {len(scope)} chapter lead and subcore files have a "
            "§2 'Why …' with a Grounded in list."
        )
        return 0
    print(f"FAIL: {RULE} — {len(findings)} finding(s) in the section 2 standard.")
    for f in findings:
        print(f"  {f.file}:{f.line}: {RULE}: {f.message}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
