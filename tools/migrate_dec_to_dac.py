#!/usr/bin/env python3
"""Rename D/A/C widget infrastructure to D/A/C (prerelease, 2026-07).

- Visible title: Definitions · Assessment · Compliance → Definitions · Assessment · Compliance
- Infrastructure prose: D/A/C → D/A/C, NAV-DAC- → NAV-DAC-

Does not rename Python module filenames or Makefile targets (handled separately).
"""
import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INCLUDE_GLOBS = [
    "core_*.md",
    "corpus_*.md",
    "corpus_joint_structure/**/*.md",
    "corpus_systems/**/*.md",
    "corpus_forum/**/*.md",
    "corpus_institutions/**/*.md",
    "ai_corpus/**/*.md",
    "implementation/**/*.md",
    "plans/**/*.md",
    "doc_architecture.md",
    "tools/README.md",
    "tools/**/*.py",
    "tools/architecture/*.json",
]

EXCLUDE_SUBSTR = ["/archive/", "/evidence/", "/doc_architecture/generated/"]

REPLACEMENTS = [
    (
        "Definitions · Assessment · Compliance",
        "Definitions · Assessment · Compliance",
    ),
    ("NAV-DAC-", "NAV-DAC-"),
    ("D/A/C", "D/A/C"),
]


def discover_files():
    seen = set()
    out = []
    for g in INCLUDE_GLOBS:
        for p in glob.glob(os.path.join(ROOT, g), recursive=True):
            rp = os.path.abspath(p)
            norm = rp.replace(os.sep, "/")
            if any(s in norm for s in EXCLUDE_SUBSTR):
                continue
            if rp in seen:
                continue
            seen.add(rp)
            out.append(rp)
    return sorted(out)


def main():
    apply = "--apply" in sys.argv
    files = discover_files()
    total = 0
    touched = 0
    for path in files:
        try:
            with open(path, encoding="utf-8") as fh:
                orig = fh.read()
        except UnicodeDecodeError:
            continue
        new = orig
        changes = 0
        for old, repl in REPLACEMENTS:
            c = new.count(old)
            if c:
                new = new.replace(old, repl)
                changes += c
        if changes and new != orig:
            touched += 1
            total += changes
            print(f"  {changes:5d}  {os.path.relpath(path, ROOT)}")
            if apply:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)
    print(f"\nTotal edits: {total} across {touched} files.")
    if not apply:
        print("Dry-run only. Re-run with --apply to write.")


if __name__ == "__main__":
    main()
