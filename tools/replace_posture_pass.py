#!/usr/bin/env python3
"""One-off helper: replace 'posture' wording across corpus markdown. Run from repo root."""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {".git", ".cursor", "archive", "evidence", "agent-transcripts", "__pycache__"}

# (path_glob, pattern, repl, flags)
RULES: list[tuple[str, str, str, int]] = [
    # Anchor renames (apply before phrase replacements that might duplicate)
    ("**/*.md", r"#4-posture-limit-and-layer-discipline", "#4-scope-limit-and-layer-discipline", 0),
    ("**/*.md", r"#12-posture-limit-and-layer-discipline", "#12-scope-limit-and-layer-discipline", 0),
    ("**/*.md", r"#4-adoption-posture-and-scope-of-authority", "#4-adoption-framing-and-scope-of-authority", 0),
    ("**/*.md", r"#722-stewardship-and-operator-incentive-posture", "#822-stewardship-and-operator-incentive-alignment", 0),
    ("**/*.md", r"#24-disqualifying-evidence-uncertainty-default-posture", "#24-disqualifying-evidence-uncertainty-default-rule", 0),
]


def iter_md_files() -> list[pathlib.Path]:
    out: list[pathlib.Path] = []
    for p in ROOT.rglob("*.md"):
        if any(x in p.parts for x in EXCLUDE_DIRS):
            continue
        if p.name.endswith(".bak"):
            continue
        out.append(p)
    return sorted(out)


def main() -> None:
    files = iter_md_files()
    for glob_pat, pattern, repl, flags in RULES:
        rx = re.compile(pattern, flags)
        for path in files:
            text = path.read_text(encoding="utf-8")
            new_text, n = rx.subn(repl, text)
            if n:
                path.write_text(new_text, encoding="utf-8")
                print(f"{path.relative_to(ROOT)}: {n} anchor replace(s)")


if __name__ == "__main__":
    main()
