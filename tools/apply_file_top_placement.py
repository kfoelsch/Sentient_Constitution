#!/usr/bin/env python3
"""One-shot helper: wrap core_* binding banners in Corpus placement widgets."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PLACEMENT_OPEN = """<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other chapters.
>
"""
PLACEMENT_CLOSE = """
</details>

<br>

"""

BINDING_START = re.compile(
    r"^This file is \*\*part of the Sentient Constitution\*\* and is \*\*binding only together\*\*"
)
NAV_LINE = re.compile(r"^\*\*(Upstream|Next|Previous):\*\*")


def transform(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if "Corpus placement (non-operative): file structure and reading rules" in text:
        return False

    try:
        binding_idx = next(
            i for i, line in enumerate(lines) if BINDING_START.match(line.rstrip("\n"))
        )
    except StopIteration:
        return False

    # Collect binding paragraph and optional nav lines until blank or non-nav content.
    end = binding_idx + 1
    while end < len(lines):
        stripped = lines[end].rstrip("\n")
        if stripped == "":
            end += 1
            continue
        if NAV_LINE.match(stripped):
            end += 1
            continue
        break

    inner = "".join(lines[binding_idx:end]).rstrip()
    # Reformat nav lines as blockquote continuation if needed.
    inner_lines = inner.splitlines()
    quoted = []
    for line in inner_lines:
        if line.strip():
            quoted.append(f"> {line}")
        else:
            quoted.append(">")
    inner_quoted = "\n".join(quoted)

    replacement = PLACEMENT_OPEN + inner_quoted + "\n" + PLACEMENT_CLOSE
    new_lines = lines[:binding_idx] + [replacement] + lines[end:]
    new_text = "".join(new_lines)
    new_text = new_text.replace("<br>\n---", "<br>\n\n---")
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for path in sorted(ROOT.glob("core_*.md")):
        if transform(path):
            print(f"updated {path.name}")
            changed += 1
    print(f"Total updated: {changed}")


if __name__ == "__main__":
    main()
