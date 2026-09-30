#!/usr/bin/env python3
"""Fail if any tracked text file contains unresolved merge-conflict markers.

Root cause this guards against: merge commit 71f6416 was committed with
unresolved conflicts, which then rendered as literal text in the chapters.
A conflict start marker is seven "<" characters followed by a space or end of
line; an end marker is seven ">" characters followed by a space or end of line.
Both are matched only at the start of a line. Bare "=======" lines are ignored
because they are valid Markdown (setext headings).

Usage:
  conflict_marker_audit.py --root .            # scan every tracked file
  conflict_marker_audit.py --root . --staged   # scan the staged versions (pre-commit)
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

START = re.compile(r"^" + "<" * 7 + r"(?: |$)")
END = re.compile(r"^" + ">" * 7 + r"(?: |$)")
BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".ico", ".woff", ".woff2", ".zip", ".pyc"}


def git(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True).stdout


def scan(name: str, data: bytes) -> list[str]:
    if b"\0" in data[:8192]:
        return []
    findings = []
    for i, line in enumerate(data.decode("utf-8", "replace").splitlines(), 1):
        if START.match(line) or END.match(line):
            findings.append(f"{name}:{i}: unresolved merge-conflict marker: {line[:80]!r}")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--staged", action="store_true", help="scan staged blobs instead of the working tree")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    findings: list[str] = []
    if args.staged:
        names = git(root, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z").decode().split("\0")
        for name in filter(None, names):
            if Path(name).suffix.lower() in BINARY_SUFFIXES:
                continue
            findings += scan(name, git(root, "show", f":{name}"))
    else:
        names = git(root, "ls-files", "-z").decode().split("\0")
        for name in filter(None, names):
            p = root / name
            if Path(name).suffix.lower() in BINARY_SUFFIXES or not p.is_file():
                continue
            findings += scan(name, p.read_bytes())

    if findings:
        print(f"conflict-marker audit: FAIL ({len(findings)} marker line(s))")
        for f in findings[:200]:
            print("  " + f)
        return 1
    print("conflict-marker audit: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
