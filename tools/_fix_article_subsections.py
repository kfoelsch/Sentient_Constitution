#!/usr/bin/env python3
"""Align #### Article subsections with preceding ### Article parent (post-migration repair)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Files that use ### / #### Article structure for Chapter Nine parts
TARGETS = [
    ROOT / "core_10-10_rights_part_c.md",
    ROOT / "core_10-10_rights_part_d.md",
]

H3_RE = re.compile(r"^### Article ([IVXLC]+):")
H4_RE = re.compile(r"^(#### Article )([IVXLC]+)(-[A-Z0-9]+:)")


def fix_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    current = None
    out = []
    for line in lines:
        m_h3 = H3_RE.match(line)
        if m_h3:
            current = m_h3.group(1)
        m_h4 = H4_RE.match(line)
        if m_h4 and current is not None:
            prefix, roman, rest = m_h4.group(1), m_h4.group(2), m_h4.group(3)
            if roman != current:
                line = f"{prefix}{current}{rest}{line[m_h4.end():]}"
        out.append(line)
    path.write_text("".join(out), encoding="utf-8")


def main() -> None:
    for p in TARGETS:
        fix_file(p)
    print("OK: fixed #### / ### alignment in part_c and part_d.")


if __name__ == "__main__":
    main()
