#!/usr/bin/env python3
"""Keep Chapter Three §6 worked examples identical to their canonical homes.

Chapter Three §6 shows two complete definitions (one independent definition,
one dependent cluster) as reader examples. Each example sits between marker
comments naming its canonical home:

    <!-- ch3-example:start FILE#ANCHOR HEADING -->
    ...copy...
    <!-- ch3-example:end -->

The copy opens with a separator line and is the canonical text with anchor tags removed, headings demoted one
level, and same-file fragment links pointed at the canonical file.

Usage:
    python3 tools/ch3_worked_examples.py --root .          # rewrite the copies
    python3 tools/ch3_worked_examples.py --root . --check  # fail if any copy drifted
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CHAPTER = "core_03.000_definitions_home.md"
BLOCK_RE = re.compile(
    r"(<!-- ch3-example:start (?P<file>[^#\s]+)#(?P<anchor>\S+) (?P<heading>.+?) -->\n)"
    r"(?P<body>.*?)"
    r"(<!-- ch3-example:end -->)",
    re.S,
)
ANCHOR_LINE_RE = re.compile(r'^\s*<a id="[^"]+"></a>\s*$')
INLINE_ANCHOR_RE = re.compile(r'<a id="[^"]+"></a>')
HEADING_RE = re.compile(r"^(#{1,6}) ")
LOCAL_LINK_RE = re.compile(r"\]\(#([^)\s]+)\)")


def extract(root: Path, src: str, heading: str) -> str:
    lines = (root / src).read_text(encoding="utf-8").split("\n")
    start = next((i for i, l in enumerate(lines) if l.rstrip() == heading), None)
    if start is None:
        raise SystemExit(f"ch3-worked-examples: heading {heading!r} not found in {src}")
    level = len(HEADING_RE.match(heading).group(1))
    end = start + 1
    while end < len(lines):
        m = HEADING_RE.match(lines[end])
        if m and len(m.group(1)) <= level:
            break
        end += 1
    body = lines[start:end]
    # Drop trailing separators, anchors, and blanks that belong to the next entry.
    while body and (not body[-1].strip() or body[-1].strip() == "---" or ANCHOR_LINE_RE.match(body[-1])):
        body.pop()
    out = []
    for line in body:
        if ANCHOR_LINE_RE.match(line):
            continue
        line = INLINE_ANCHOR_RE.sub("", line)
        m = HEADING_RE.match(line)
        if m:
            line = "#" + line
        line = LOCAL_LINK_RE.sub(lambda mm: f"]({src}#{mm.group(1)})", line)
        out.append(line)
    # Collapse blank runs left by removed anchors.
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip("\n")
    return "\n---\n\n" + text + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=".")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    path = root / CHAPTER
    text = path.read_text(encoding="utf-8")
    blocks = list(BLOCK_RE.finditer(text))
    if not blocks:
        print(f"ch3-worked-examples: FAIL (no example blocks in {CHAPTER})")
        return 1
    drift = []

    def repl(m: re.Match) -> str:
        want = extract(root, m.group("file"), m.group("heading"))
        if m.group("body") != want:
            drift.append(f"{m.group('file')}#{m.group('anchor')}")
        return m.group(1) + want + m.group(6)

    new = BLOCK_RE.sub(repl, text)
    if args.check:
        if drift:
            print(f"ch3-worked-examples: FAIL ({len(drift)} example(s) differ from their canonical homes)")
            for d in drift:
                print(f"  {CHAPTER} — copy of {d} is stale; run make ch3-worked-examples")
            return 1
        print(f"ch3-worked-examples: PASS ({len(blocks)} example(s) match their canonical homes)")
        return 0
    if new != text:
        path.write_text(new, encoding="utf-8")
    print(f"ch3-worked-examples: wrote {len(blocks)} example(s); {len(drift)} refreshed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
