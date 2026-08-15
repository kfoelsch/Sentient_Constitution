#!/usr/bin/env python3
"""Rewrite wrapper-only companion family cites to subfile links (REF-FAMILY)."""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402
from family_map_lib import load_family_map, resolve_section_file  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

WRAPPER_BOLD_RE = re.compile(
    r"`corpus_(forum|institutions|systems|joint_structure)\.md`\s+\*\*((?:CF|CI|CS|CJS)-[^*]+)\*\*"
)
WRAPPER_LINK_RE = re.compile(
    r"\[(`?(?:CJS|CS|CI|CF)-[^\]`]+)`?\]\(((?:\.\./)*corpus_(?:forum|institutions|systems|joint_structure)\.md)(?:#[^)]*)?\)"
)
FAMILY_TOKEN_RE = re.compile(r"(CJS|CS|CI|CF)-\d+(?:\.\d+){0,2}", re.I)


def rel_link(source: Path, dest: Path) -> str:
    return Path(os.path.relpath(dest, start=source.parent)).as_posix()


def family_token(bold: str) -> str | None:
    match = FAMILY_TOKEN_RE.search(bold)
    return match.group(0) if match else None


def rewrite_text(text: str, source: Path, root: Path, data: dict) -> str:
    def bold_sub(match: re.Match[str]) -> str:
        bold = match.group(2)
        token = family_token(bold)
        if not token:
            return match.group(0)
        rel = resolve_section_file(data, token)
        if not rel:
            return match.group(0)
        href = rel_link(source, root / rel)
        return f"[**{token}**]({href})"

    def link_sub(match: re.Match[str]) -> str:
        label = match.group(1).strip("`")
        token = family_token(label)
        if not token:
            return match.group(0)
        rel = resolve_section_file(data, token)
        if not rel:
            return match.group(0)
        href = rel_link(source, root / rel)
        return f"[**{token}**]({href})"

    text = WRAPPER_BOLD_RE.sub(bold_sub, text)
    text = WRAPPER_LINK_RE.sub(link_sub, text)
    text = re.sub(
        r"\*\*\[\*\*((?:CJS|CS|CI|CF)-[^*]+)\*\*\]\(([^)]+)\)\*\*",
        r"[**\1**](\2)",
        text,
    )
    return text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    data = load_family_map(root)
    changed = 0
    for rel in binding_corpus_scope(root):
        path = root / rel
        if not path.is_file():
            continue
        original = path.read_text(encoding="utf-8")
        updated = rewrite_text(original, path, root, data)
        if updated == original:
            continue
        changed += 1
        if args.write:
            path.write_text(updated, encoding="utf-8")
            print(f"updated {rel}")
        else:
            print(f"would update {rel}")
    print(f"{'Wrote' if args.write else 'Would update'} {changed} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
