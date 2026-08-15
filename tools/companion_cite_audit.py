#!/usr/bin/env python3
"""Flag wrapper-only companion family cites that should point at subfiles.

REF-FAMILY: when a family file exists, cite the subfile (and optional anchor),
not the layer wrapper. ``oDef.*n*`` remains an alias of **CJS-3.*n***.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402
from family_map_lib import load_family_map, resolve_section_file  # noqa: E402
from rewrite_companion_cites import WRAPPER_BOLD_RE, WRAPPER_LINK_RE, family_token  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    data = load_family_map(root)
    findings: list[str] = []
    for rel in binding_corpus_scope(root):
        path = root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for match in WRAPPER_BOLD_RE.finditer(text):
            token = family_token(match.group(2))
            if token and resolve_section_file(data, token):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    f"{rel}:{line}: wrapper-only family cite {match.group(0)!r} "
                    f"— use the subfile for {token}"
                )
        for match in WRAPPER_LINK_RE.finditer(text):
            token = family_token(match.group(1))
            if token and resolve_section_file(data, token):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    f"{rel}:{line}: wrapper link {match.group(0)!r} "
                    f"— use the subfile for {token}"
                )
    if findings:
        print("Companion cite audit failures:", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        return 1
    print("Companion cite audit OK (no wrapper-only family cites).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
