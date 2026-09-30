#!/usr/bin/env python3
"""Fail when binding corpus depends on a support document for routing or meaning.

Binding corpus text must not depend on ``doc_architecture.md`` or
``doc_architecture/`` generated artifacts for owner homes, definition placement,
routing, or formatting. Allowed exceptions:

1. Explicit classification of doc_architecture as non-binding / process-and-map
   support / non-operative orientation (unless validly adopted).
2. Reading-chain navigation footers (``**Next file:**`` / ``**Previous file:**``)
   that terminate at ``doc_architecture.md``.

``README.md`` is the same layer — the README classifies itself as process / map
support — so binding text must not route *through* it either. A deep link into a
README section (``README.md#…``) sends a reader to the support map to learn where
a constitutional step lives; cite the owner chapter, or the Preamble chain map at
``core_00_preamble.md#62-how-the-full-chain-fits-together``, instead. A bare
``README.md`` link stays allowed: reading order, the binding/support split, edition
and document-control identifiers, and the reading-chain footer are what the README
is for.

Rule ID: SUPPORT-DOC-POINTER-01
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope

DOC_ARCH = re.compile(r"doc_architecture", re.I)
# A link whose target is a section *inside* the README: ](README.md#…) or ](../README.md#…).
README_DEEP_LINK = re.compile(r"\]\(\s*(?:\.\./)*README\.md#[^)\s]+\)", re.I)
FOOTER = re.compile(
    r"^\*\*(?:Next|Previous) file:\*\*.*doc_architecture\.md",
    re.I,
)
ALLOW_MARKERS = (
    "non-binding",
    "non-operative",
    "process and map support",
    "unless expressly adopted",
    "unless adopted",
    "unless a valid adopting instrument",
    "unless a valid adopting",
)


def _allowed(line: str) -> bool:
    if FOOTER.search(line):
        return True
    lower = line.lower()
    if not DOC_ARCH.search(line):
        return True
    return any(marker in lower for marker in ALLOW_MARKERS)


def audit(root: Path) -> list[str]:
    errors: list[str] = []
    for rel in binding_corpus_scope(root):
        path = root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), start=1):
            if README_DEEP_LINK.search(line):
                errors.append(
                    f"{rel}:{lineno}: binding corpus routes through a README section; "
                    f"cite the owner chapter or the Preamble chain map "
                    f"(core_00_preamble.md#62-how-the-full-chain-fits-together) "
                    f"(SUPPORT-DOC-POINTER-01): {line.strip()[:160]}"
                )
            if not DOC_ARCH.search(line):
                continue
            if _allowed(line):
                continue
            errors.append(
                f"{rel}:{lineno}: binding corpus cites doc_architecture "
                f"without non-binding/support classification "
                f"(SUPPORT-DOC-POINTER-01): {line.strip()[:160]}"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    root = args.root.resolve()
    errors = audit(root)
    if errors:
        print(f"FAIL: {len(errors)} support-doc pointer finding(s)")
        for err in errors:
            print(err)
        return 1
    print("PASS: no improper doc_architecture or README-section pointers in binding corpus.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
