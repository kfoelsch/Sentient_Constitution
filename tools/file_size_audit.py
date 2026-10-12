#!/usr/bin/env python3
"""Fail if any file in the repository is larger than 1 MB.

Policy (custodian decision, 2026-10-12): no file in this repository should exceed
1 MB (1,000,000 bytes, the figure Finder and GitHub show). Large files slow
clones and diffs, hide review, and usually mean a throwaway artifact (a git
bundle, a data dump, a build output) slipped in. Split the file, compact it, or
keep it out of the repository.

A file counts if git tracks it OR it is untracked and not ignored, so oversize
files are caught before they are first committed.

Known exceptions live in SIZE_EXEMPT below, each with a reason. An exemption
whose file is gone or is now under the limit fails the audit as stale, so remove
it. Never add an exemption to get a check to pass; fix the file. Dated evidence
snapshots (evidence/YYYY-MM-DD/) are never exempt: delete them if they grow too
large.

Usage:
  file_size_audit.py --root .            # audit the working tree; exit 1 on findings
  file_size_audit.py --root . --staged   # audit staged blobs (pre-commit)
  file_size_audit.py --root . --no-exemptions   # strict view: list every oversize file
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

LIMIT_BYTES = 1_000_000

# path (repo-relative, POSIX) -> why it is exempt for now. Ratchet: shrink only.
SIZE_EXEMPT: dict[str, str] = {}


def git(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True).stdout


def sizes(root: Path, staged: bool) -> dict[str, int]:
    """Map repo-relative path -> size in bytes for the files to audit."""
    out: dict[str, int] = {}
    if staged:
        names = git(root, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z").decode().split("\0")
        for name in filter(None, names):
            out[name] = int(git(root, "cat-file", "-s", f":{name}").decode().strip())
        return out
    try:
        names = git(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z").decode().split("\0")
        paths = [n for n in names if n]
    except (subprocess.CalledProcessError, FileNotFoundError):
        paths = [str(p.relative_to(root).as_posix()) for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]
    for name in paths:
        p = root / name
        if p.is_file():
            out[name] = p.stat().st_size
    return out


def audit(file_sizes: dict[str, int], exempt: dict[str, str], limit: int = LIMIT_BYTES, check_stale: bool = True):
    """Return (violations, stale_exemptions, active_exemptions); each entry is a message string."""
    violations, stale, active = [], [], []
    for name in sorted(file_sizes):
        size = file_sizes[name]
        if size <= limit:
            continue
        if name in exempt:
            active.append(f"{name}: {size:,} bytes (exempt: {exempt[name]})")
        else:
            violations.append(f"{name}: {size:,} bytes exceeds the {limit:,}-byte limit")
    if check_stale:
        for name in sorted(exempt):
            if file_sizes.get(name, 0) <= limit:
                stale.append(f"{name}: exemption is stale (file is missing or within the limit); remove it from SIZE_EXEMPT")
    return violations, stale, active


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--staged", action="store_true", help="audit staged blobs instead of the working tree")
    ap.add_argument("--no-exemptions", action="store_true", help="ignore SIZE_EXEMPT (strict view; also used by tests)")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    exempt = {} if args.no_exemptions else SIZE_EXEMPT
    violations, stale, active = audit(sizes(root, args.staged), exempt, check_stale=not args.staged)
    problems = violations + stale
    if problems:
        print(f"file-size audit: FAIL ({len(problems)} problem(s); limit {LIMIT_BYTES:,} bytes)")
        for p in problems:
            print("  " + p)
        for a in active:
            print("  known exception: " + a)
        return 1
    print(f"file-size audit: clean (limit {LIMIT_BYTES:,} bytes; {len(active)} known exception(s))")
    for a in active:
        print("  known exception: " + a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
