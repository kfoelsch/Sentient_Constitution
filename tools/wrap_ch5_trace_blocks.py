#!/usr/bin/env python3
"""Wrap plain **Trace** blocks in Chapter Five band files with NAV-DEC Trace widgets."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TRACE_HEADING_RE = re.compile(r"^\*\*Trace\*\*\s*$")
CORPUS_HEADING_RE = re.compile(
    r"^\*\*Corpus placement \(non-operative\): file structure and reading rules\*\*\s*$"
)
TRACE_OPEN = (
    '<details>\n'
    '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>\n'
)
CORPUS_OPEN = (
    '<details>\n'
    '<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>\n'
)
TRACE_CLOSE = "</details>\n\n<br>\n"
CORPUS_CLOSE = "</details>\n\n<br>\n"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument("--file", required=True, help="Chapter Five band file to repair.")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def collect_block(lines: list[str], start: int) -> tuple[list[str], int]:
    body: list[str] = []
    idx = start
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    while idx < len(lines):
        stripped = lines[idx].strip()
        if stripped.startswith("- "):
            body.append(lines[idx])
            idx += 1
            continue
        if stripped.startswith("> "):
            body.append(lines[idx])
            idx += 1
            continue
        if not stripped:
            if body and idx + 1 < len(lines) and (
                lines[idx + 1].strip().startswith("- ")
                or lines[idx + 1].strip().startswith("> ")
            ):
                body.append(lines[idx])
                idx += 1
                continue
            break
        break
    return body, idx


def wrap_plain_blocks(text: str, heading_re: re.Pattern[str], open_tag: str, close_tag: str) -> tuple[str, int]:
    lines = text.splitlines()
    out: list[str] = []
    idx = 0
    changes = 0
    while idx < len(lines):
        line = lines[idx]
        if heading_re.match(line.strip()):
            if idx > 0 and lines[idx - 1].strip() == "<details>":
                out.append(line)
                idx += 1
                continue
            body, end = collect_block(lines, idx + 1)
            if not body:
                out.append(line)
                idx += 1
                continue
            out.append(open_tag.rstrip("\n"))
            out.extend(body)
            out.append(close_tag.rstrip("\n"))
            idx = end
            changes += 1
            continue
        out.append(line)
        idx += 1
    return "\n".join(out) + ("\n" if text.endswith("\n") else ""), changes


def main() -> int:
    args = parse_args()
    path = Path(args.root).resolve() / args.file
    text = path.read_text(encoding="utf-8")
    text, corpus_changes = wrap_plain_blocks(text, CORPUS_HEADING_RE, CORPUS_OPEN, CORPUS_CLOSE)
    text, trace_changes = wrap_plain_blocks(text, TRACE_HEADING_RE, TRACE_OPEN, TRACE_CLOSE)
    total = corpus_changes + trace_changes
    if total == 0:
        print(f"No plain Trace/Corpus blocks to wrap in {args.file}")
        return 0
    if args.dry_run:
        print(f"Would wrap {total} block(s) in {args.file}")
        return 0
    path.write_text(text, encoding="utf-8")
    print(f"Wrapped {total} block(s) in {args.file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
