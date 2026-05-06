#!/usr/bin/env python3
"""Audit Chapter Five for stub/pointer entries (violation of 'no stubs' rule).

Per doc_architecture.md "Chapter Five — no stubs (editorial rule)":
- No placeholder headings whose only purpose is alphabetical location
- No "locator only" lines that defer O/E/C without a real definition block
- Do not retain parallel empty shells in §1 or §2

Detection patterns:
1. "paired-entry pointer" or similar in title
2. "alphabetical locator stub" or "alphabetical location" in prose
3. "defined in full in the paired entry" pattern
4. "canonical O/E/C statement for X lives in" pattern
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

_TOOLS = pathlib.Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root (default: .).")
    return parser.parse_args()


# Patterns that indicate a stub or pointer entry
STUB_INDICATORS = [
    "paired-entry pointer",
    "alphabetical locator stub",
    "alphabetical location",
    "defined in full in the paired entry",
    "canonical O/E/C statement",
    r"canonical.*lives in",
    "locator-only",
    "locator only",
]

STUB_PATTERNS = [re.compile(pattern, re.IGNORECASE) for pattern in STUB_INDICATORS]


def find_entries(lines: list[str]) -> list[tuple[int, str, int]]:
    """Find all definition entry headings (#### or #####) and return (line_idx, title, level)."""
    entries: list[tuple[int, str, int]] = []
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("#####"):
            entries.append((idx, stripped[5:].strip(), 5))
        elif stripped.startswith("####"):
            entries.append((idx, stripped[4:].strip(), 4))
    return entries


def get_entry_content(lines: list[str], start_idx: int, next_entry_idx: int | None) -> str:
    """Get all content from start_idx to the next entry heading (or end of lines)."""
    end_idx = next_entry_idx if next_entry_idx is not None else len(lines)
    return "\n".join(lines[start_idx : end_idx])


def is_alphabetical_directory_heading(title: str) -> bool:
    """Check if this is the alphabetical directory heading itself (not a stub)."""
    return "all definitions" in title.lower() and "a–z" in title.lower()


def is_stub_entry(content: str, title: str) -> bool:
    """Check if content matches stub/pointer patterns."""
    # The alphabetical directory heading is not a stub, it's a legitimate section
    if is_alphabetical_directory_heading(title):
        return False
    
    for pattern in STUB_PATTERNS:
        if pattern.search(content):
            return True
    return False


def check_file(path: pathlib.Path) -> list[str]:
    """Check a single Chapter Five file for stub entries."""
    violations: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    
    entries = find_entries(lines)
    
    for idx, (entry_idx, title, level) in enumerate(entries):
        next_entry_idx = entries[idx + 1][0] if idx + 1 < len(entries) else None
        content = get_entry_content(lines, entry_idx, next_entry_idx)
        
        if is_stub_entry(content, title):
            violations.append(
                f"{path}:{entry_idx + 1}: STUB/POINTER ENTRY FOUND:\n"
                f"  Title: {title}\n"
                f"  Content snippet: {content[:200]}...\n"
                f"  (Violates 'Chapter Five — no stubs' rule per doc_architecture.md)"
            )
    
    return violations


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    
    violations: list[str] = []
    
    for file_pattern in CH5_ALL:
        path = root / file_pattern
        if path.exists():
            violations.extend(check_file(path))
    
    if violations:
        for violation in violations:
            print(violation)
        print(f"\n{len(violations)} stub/pointer violations found.")
        return 1
    else:
        print("✓ No stub/pointer entries found in Chapter Five.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
