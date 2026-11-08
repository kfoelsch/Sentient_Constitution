#!/usr/bin/env python3
"""Bring a local checkout up to date with origin/main and tidy merged branches (GIT-LOCAL-SYNC-01).

    python3 tools/sync_local.py            # fetch, fast-forward main, leave a merged branch, list the rest
    python3 tools/sync_local.py --dry-run  # say what would happen, change nothing
    python3 tools/sync_local.py --delete-merged   # also delete every merged branch whose remote is gone
    python3 tools/sync_local.py --no-fetch # work from the refs already fetched (offline)

What it does, in order:

1. ``git fetch origin --prune`` (a public repository needs no login to fetch).
2. Fast-forwards ``main`` to ``origin/main``. It never resets, never merges, and never moves ``main`` anywhere else.
3. If the checkout is on a branch whose remote is gone and every commit on it is already in
   ``origin/main``, and tracked files are clean, it switches to ``main`` and deletes that branch.
4. Lists every other local branch whose remote is gone, as merged (safe to delete) or as holding
   commits that are not in ``main`` (kept; it prints how many).

It never deletes a branch that holds a commit missing from ``origin/main``, never switches with
uncommitted changes to tracked files, and never touches untracked files. "In ``origin/main``" is
decided by patch identity (``git cherry``), so a branch whose commits were replayed under new hashes
still counts as merged.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def git(root: Path, *args: str, check: bool = False) -> subprocess.CompletedProcess:
    proc = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    if check and proc.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed: {(proc.stderr or proc.stdout).strip()}")
    return proc


def current_branch(root: Path) -> str:
    return git(root, "branch", "--show-current").stdout.strip()


def tracked_changes(root: Path) -> list[str]:
    out = git(root, "status", "--porcelain", "--untracked-files=no").stdout
    return [line for line in out.splitlines() if line.strip()]


def local_branches(root: Path) -> list[dict]:
    fmt = "%(refname:short)\t%(upstream:track)"
    out = git(root, "for-each-ref", f"--format={fmt}", "refs/heads").stdout
    rows = []
    for line in out.splitlines():
        name, _, track = line.partition("\t")
        rows.append({"name": name, "gone": track.strip() == "[gone]"})
    return rows


def unmerged_commits(root: Path, branch: str, base: str = "origin/main") -> int:
    """Commits on ``branch`` whose change is not in ``base`` (``git cherry`` lines starting with ``+``)."""
    out = git(root, "cherry", base, branch).stdout
    return sum(1 for line in out.splitlines() if line.startswith("+"))


def sync(root: Path, *, fetch: bool = True, dry_run: bool = False, delete_merged: bool = False) -> list[str]:
    say: list[str] = []
    if git(root, "rev-parse", "--git-dir").returncode:
        return [f"not a git checkout: {root}"]
    if fetch:
        proc = git(root, "fetch", "origin", "--prune")
        if proc.returncode:
            return [f"fetch failed, nothing changed: {(proc.stderr or proc.stdout).strip().splitlines()[-1]}"]
    if git(root, "rev-parse", "--verify", "-q", "origin/main").returncode:
        return ["no origin/main to sync with"]
    head = git(root, "rev-parse", "--short", "origin/main").stdout.strip()
    here = current_branch(root)
    dirty = tracked_changes(root)
    verb = "would " if dry_run else ""

    # 3. leave a merged branch we are standing on (done first so main can then be fast-forwarded in place)
    if here and here != "main":
        info = next((b for b in local_branches(root) if b["name"] == here), None)
        if info and info["gone"]:
            n = unmerged_commits(root, here)
            if n:
                say.append(f"stayed on {here}: its remote is gone but {n} commit(s) are not in origin/main")
            elif dirty:
                say.append(f"stayed on {here}: merged, but {len(dirty)} tracked file(s) have uncommitted changes")
            else:
                say.append(f"{verb}switched from merged branch {here} to main and deleted {here}")
                if not dry_run:
                    git(root, "switch", "main", check=True)
                    git(root, "branch", "-D", here, check=True)
                here = "main"

    # 2. fast-forward main
    if git(root, "rev-parse", "--verify", "-q", "main").returncode:
        say.append("no local main branch")
    else:
        behind = git(root, "rev-list", "--count", "main..origin/main").stdout.strip()
        ahead = git(root, "rev-list", "--count", "origin/main..main").stdout.strip()
        if ahead != "0":
            say.append(f"main has {ahead} commit(s) that origin/main lacks; left alone (main should mirror origin/main)")
        elif behind == "0":
            say.append(f"main is up to date with origin/main ({head})")
        elif here == "main":
            if dirty:
                say.append(f"main is {behind} behind origin/main but {len(dirty)} tracked file(s) have uncommitted changes; not updated")
            else:
                say.append(f"{verb}fast-forwarded main by {behind} commit(s) to {head}")
                if not dry_run:
                    git(root, "merge", "--ff-only", "origin/main", check=True)
        else:
            say.append(f"{verb}fast-forwarded main by {behind} commit(s) to {head}")
            if not dry_run:
                git(root, "fetch", "origin", "main:main", check=True)

    # 4. the other branches whose remote is gone
    here = current_branch(root) if not dry_run else here
    for b in local_branches(root):
        if not b["gone"] or b["name"] in {here, "main"}:
            continue
        n = unmerged_commits(root, b["name"])
        if n:
            say.append(f"kept {b['name']}: remote gone, {n} commit(s) not in origin/main")
        elif delete_merged:
            say.append(f"{verb}deleted merged branch {b['name']}")
            if not dry_run:
                git(root, "branch", "-D", b["name"], check=True)
        else:
            say.append(f"merged, safe to delete: {b['name']}  (git branch -D {b['name']}, or rerun with --delete-merged)")
    return say


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--no-fetch", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--delete-merged", action="store_true", help="delete every merged branch whose remote is gone")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()
    try:
        lines = sync(root, fetch=not args.no_fetch, dry_run=args.dry_run, delete_merged=args.delete_merged)
    except RuntimeError as exc:
        print(f"sync-local stopped: {exc}", file=sys.stderr)
        return 1
    for line in lines:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
