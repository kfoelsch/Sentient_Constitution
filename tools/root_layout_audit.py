#!/usr/bin/env python3
"""Fail if working files (plain-language drafts, WIP/draft files, git bundles) sit in the repo root.

Root cause this guards against: per-Article plain-language companions
(`Article_XIX_plain_language.md` and friends) and other work-in-progress files
were created, and committed, directly in the repository root, which is the
public door (README, START_HERE, the numbered `core_*` files). Working files
belong under `project/`.

Rules (repo-root files only; subdirectories are not checked):
  RL-BUNDLE-01 name ends in ".bundle" (git bundle patch-transfer file)
               -> delete once its commits are pushed; never keep in the repo (report only)
  RL-PLAIN-01  name contains "plain_language" / "plain-language"
               -> belongs in project/plain_language/   (auto-fixable with --fix)
  RL-WIP-01    name has a standalone "wip" or "draft" token (e.g. foo_wip.md,
               DRAFT_notes.md) -> belongs somewhere under project/ (report only)

A file counts if git tracks it OR it is untracked and not ignored, so strays are
caught before they are first committed.

Usage:
  root_layout_audit.py --root .            # audit the root; exit 1 on findings
  root_layout_audit.py --root . --staged   # audit staged additions (pre-commit)
  root_layout_audit.py --root . --fix      # move RL-PLAIN-01 files and fix their links
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    rule_id: str
    pattern: re.Pattern[str]
    dest: str  # repo-relative directory the file should live in
    fixable: bool
    why: str
    advice: str = ""  # overrides the default "move to <dest>/" hint


RULES: tuple[Rule, ...] = (
    Rule(
        "RL-BUNDLE-01",
        re.compile(r"\.bundle$", re.I),
        "",
        False,
        "git bundles are throwaway patch-transfer files, not repo content",
        "delete it once its commits are pushed (check with `git bundle verify`), or keep it outside the repo",
    ),
    Rule(
        "RL-PLAIN-01",
        re.compile(r"plain[_-]?language", re.I),
        "project/plain_language",
        True,
        "plain-language companion files are working files",
    ),
    Rule(
        "RL-WIP-01",
        re.compile(r"(?<![a-z0-9])(?:wip|draft)(?![a-z0-9])", re.I),
        "project",
        False,
        "work-in-progress/draft files are working files",
    ),
)

# Matches a Markdown inline link target: ](target) or ](target#frag) or ](target "title")
LINK_RE = re.compile(r"(\]\()([^)\s#?]+)([^)]*\))")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "../", "/")


@dataclass(frozen=True)
class Finding:
    name: str
    rule: Rule

    def render(self) -> str:
        hint = self.rule.advice or f"move to {self.rule.dest}/"
        return f"{self.name}: {self.rule.rule_id}: {self.rule.why}; {hint}"


def classify(name: str) -> Rule | None:
    """Return the first rule that a repo-root filename violates, else None."""
    for rule in RULES:
        if rule.pattern.search(name):
            return rule
    return None


def find_strays(names: list[str]) -> list[Finding]:
    """Check repo-relative paths; only names with no directory component are root files."""
    out = []
    for name in sorted(set(names)):
        if "/" in name:
            continue
        rule = classify(name)
        if rule:
            out.append(Finding(name, rule))
    return out


def git(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True).stdout


def root_candidates(root: Path, staged: bool) -> list[str]:
    try:
        if staged:
            raw = git(root, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
            names = raw.decode().split("\0")
        else:
            raw = git(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z")
            names = [n for n in raw.decode().split("\0") if n and (root / n).is_file()]
    except (subprocess.CalledProcessError, FileNotFoundError):
        if staged:
            raise
        names = [p.name for p in root.iterdir() if p.is_file()]
    return [n for n in names if n]


def rewrite_links(text: str, old_dir: Path, new_dir: Path) -> str:
    """Re-point relative links in a file that moved from old_dir to new_dir.

    A target that already resolves from new_dir (e.g. a sibling that moved too)
    is left alone; one that resolves from old_dir is re-expressed from new_dir.
    """

    def sub(m: re.Match[str]) -> str:
        target = m.group(2)
        if target.startswith(SKIP_PREFIXES) or (new_dir / target).exists():
            return m.group(0)
        resolved = old_dir / target
        if not resolved.exists():
            return m.group(0)
        rel = Path(*([".."] * len(new_dir.relative_to(old_dir).parts))) / target
        return f"{m.group(1)}{rel.as_posix()}{m.group(3)}"

    return LINK_RE.sub(sub, text)


def fix(root: Path, findings: list[Finding]) -> int:
    moved, skipped = [], []
    for f in findings:
        if not f.rule.fixable:
            skipped.append(f"{f.name}: {f.rule.rule_id} is report-only; move it by hand")
            continue
        dest_dir = root / f.rule.dest
        dest = dest_dir / f.name
        if dest.exists():
            skipped.append(f"{f.name}: {f.rule.dest}/{f.name} already exists; resolve by hand")
            continue
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(root / f.name), str(dest))
        moved.append(f)
    # Rewrite links only after every move, so sibling links resolve correctly.
    for f in moved:
        dest = root / f.rule.dest / f.name
        text = dest.read_text(encoding="utf-8")
        new = rewrite_links(text, root, dest.parent)
        if new != text:
            dest.write_text(new, encoding="utf-8")
        print(f"moved {f.name} -> {f.rule.dest}/{f.name}")
    for s in skipped:
        print("skipped " + s)
    if moved:
        names = {f.name for f in moved}
        hits = []
        for name in git(root, "ls-files", "-z", "*.md").decode().split("\0"):
            p = root / name
            if not name or not p.is_file() or p.parent == root / "project" / "plain_language":
                continue
            body = p.read_text(encoding="utf-8", errors="replace")
            if any(n in body for n in names):
                hits.append(name)
        if hits:
            print("note: these files still mention a moved filename; update the paths by hand:")
            for h in hits:
                print("  " + h)
    return 1 if skipped else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".")
    ap.add_argument("--staged", action="store_true", help="audit staged additions instead of the working tree")
    ap.add_argument("--fix", action="store_true", help="move auto-fixable files (RL-PLAIN-01) and fix their links")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    findings = find_strays(root_candidates(root, args.staged))
    if args.fix and not args.staged:
        if not findings:
            print("root-layout audit: nothing to fix")
            return 0
        return fix(root, findings)

    if findings:
        print(f"root-layout audit: FAIL ({len(findings)} stray file(s) in the repo root)")
        for f in findings:
            print("  " + f.render())
        print("  fix: python3 tools/root_layout_audit.py --root . --fix   (RL-PLAIN-01 only; delete bundles by hand)")
        return 1
    print("root-layout audit: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
