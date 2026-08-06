#!/usr/bin/env python3
"""Audit Chapter Five for redundant legacy measurement stubs.

Flags two MEAS-DEF-01 transition problems:

1. **cluster_head_child_stub** — a `####` cluster head carries a full tier
   routing block (`*Measurements:*` with Primary + Secondary, or
   `*Measurements (family routing):*`) and a `#####` child still carries a
   legacy stub block (`*Measurements:*` + `**Primary:** … supporting measure`
   only). Children should inherit cluster-head routing via guidepost
   `**Primary measure:**` lines instead.

2. **legacy_stub_leaf** — a standalone `####`/`#####` entry uses only the
   Wave-9 placeholder stub (`*Measurements:*` + supporting-measure Primary)
   without a guidepost `**How to measure and assess**` header.

Advisory by default (exit 0). Pass ``--strict`` to fail CI.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL  # noqa: E402

MEAS = re.compile(r"^\s*-?\s*\*Measurements:\*\s*$", re.MULTILINE)
FAMILY_ROUTING = re.compile(r"\*Measurements \(family routing\):\*", re.MULTILINE)
HEAD_TIER = re.compile(
    r"\*Measurements:\*\s*\n\s*- \*\*Primary:\*\*[^\n]+\n\s*- \*\*Secondary:\*\*",
    re.MULTILINE,
)
STUB = re.compile(
    r"\*Measurements:\*\s*\n\s*- \*\*Primary:\*\* [^\n]*supporting measure",
    re.MULTILINE | re.IGNORECASE,
)
GUIDEPOST = re.compile(r"^- \*\*How to measure and assess\*\*", re.MULTILINE)

SCAN_FILES = tuple(f for f in CH5_ALL if f != "core_05__definitions_home.md")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument("--strict", action="store_true", help="Exit non-zero on findings.")
    return p.parse_args()


def audit_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    warnings: list[str] = []
    parts = re.split(r"^(#### .+)$", text, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        title = parts[i].lstrip("#").strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        child_split = re.search(r"^##### ", body, re.MULTILINE)
        if not child_split:
            if STUB.search(body) and not GUIDEPOST.search(body):
                line = text.count("\n", 0, text.find(parts[i])) + 1
                warnings.append(
                    f"{path}:{line}: {title} — legacy_stub_leaf "
                    "(stub *Measurements:* without guidepost M/A)"
                )
            continue
        pre, post = body[: child_split.start()], body[child_split.start() :]
        head_routing = bool(HEAD_TIER.search(pre) or FAMILY_ROUTING.search(pre))
        if not head_routing:
            continue
        for m in STUB.finditer(post):
            line = text.count("\n", 0, text.find(parts[i]) + child_split.start() + m.start()) + 1
            warnings.append(
                f"{path}:{line}: {title} — cluster_head_child_stub "
                "(child still carries legacy supporting-measure stub)"
            )
    return warnings


def main() -> int:
    args = parse_args()
    root = Path(args.root)
    warnings: list[str] = []
    for rel in SCAN_FILES:
        path = root / rel
        if path.is_file():
            warnings.extend(audit_file(path))
    if warnings:
        print("\n".join(sorted(warnings)))
        print(
            f"\n{len(warnings)} measurement-stub issue(s). "
            "Cluster children should inherit head routing via guidepost "
            "**Primary measure:**; legacy leaves need guidepost migration."
        )
        return 1 if args.strict else 0
    print("ch5-measurement-stub-audit: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
