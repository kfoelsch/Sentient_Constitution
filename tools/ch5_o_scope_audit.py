#!/usr/bin/env python3
"""Audit Chapter Five O components for mandatory In scope / Out of scope sub-bullets.

Enforces Chapter Two §2.1 and doc_architecture.md MEAS-DEF-01 entry placement step 2b:
every O component must include at least one In scope sub-bullet (consolidated or
dimensional) and at least one Out of scope sub-bullet.
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

O_START = re.compile(r"^(- \*\*O:\*\*|- O:|- \*\*What it is\*\*)", re.MULTILINE)
O_END = re.compile(
    r"^- \*\*E:\*\*|^- E:|^- \*\*How to measure and assess\*\*|^\s*<a id=.*-e\"></a>\s*$",
    re.MULTILINE,
)
IN_SCOPE = re.compile(r"^\s+- \*{0,2}In scope(?:\s*—|\s*:)", re.MULTILINE)
OUT_SCOPE = re.compile(r"^\s+- \*{0,2}Out of scope:", re.MULTILINE)

SCOPE_FILES = (*CH5_BANDS, *CH5_AIMS)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root (default: .).")
    return parser.parse_args()


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def find_title_before(text: str, o_start: int) -> str:
    before = text[:o_start]
    for line in reversed(before.splitlines()):
        stripped = line.strip()
        if stripped.startswith("#### ") or stripped.startswith("##### "):
            return stripped.lstrip("#").strip()
    return "(unknown term)"


def audit_file(path: pathlib.Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    violations: list[str] = []
    for match in O_START.finditer(text):
        o_start = match.start()
        end_match = O_END.search(text, match.end())
        o_block = text[o_start : end_match.start()] if end_match else text[o_start:]
        title = find_title_before(text, o_start)
        lineno = line_number(text, o_start)
        has_in = bool(IN_SCOPE.search(o_block))
        has_out = bool(OUT_SCOPE.search(o_block))
        if not has_in or not has_out:
            missing = []
            if not has_in:
                missing.append("In scope")
            if not has_out:
                missing.append("Out of scope")
            violations.append(
                f"{path}:{lineno}: {title} — missing {' / '.join(missing)} under O"
            )
    return violations


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root)
    violations: list[str] = []
    for rel in SCOPE_FILES:
        path = root / rel
        if path.exists():
            violations.extend(audit_file(path))
    if violations:
        print("\n".join(violations))
        print(f"\n{len(violations)} O-scope violation(s).")
        return 1
    print("ch5-o-scope-audit: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
