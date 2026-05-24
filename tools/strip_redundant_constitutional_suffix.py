#!/usr/bin/env python3
"""One-shot sweep: strip redundant ' (Constitutional)' suffix from Chapter Five
defined-term references across the binding corpus.

Codifies the rule already stated in doc_architecture.md §"Order and
alphabetization (Chapter Five)" > Section 1 (entry titles) and enforced for
Chapter Five headings by tools/ch5_entry_format_audit.py. This sweep extends
the same rule to *references* throughout the corpus.

Protected contexts (not changed):
- URL anchor fragments:        ...#foo-constitutional
- HTML anchor tags:            <a id="foo-constitutional"></a>
- Distinct parenthetical:      (Constitutional Constraint)
- Backtick-quoted meta-text:   `(Constitutional)` (the rule itself)

The script operates on an explicit allow-list of files. Run once; safe to rerun
(idempotent). Prints a per-file change count.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TARGETS = [
    # Binding core files
    "core_00-01_principles.md",
    "core_02-04_definition_mechanics.md",
    "core_05-05_definitions_a_independent.md",
    "core_05-05_definitions_b_semi_independent.md",
    "core_05-05_definitions_c_dependent_clusters.md",
    "core_06-06_standing_assessment.md",
    "core_07-07_standing_integration.md",
    "core_08-08_misconduct.md",
    "core_09-09_forum.md",
    "core_10-10_rights_part_a.md",
    "core_10-10_rights_part_b.md",
    "core_10-10_rights_part_c.md",
    "core_10-10_rights_part_d.md",
    "core_11-11_governance.md",
    "core_12-14_amendment.md",
    "core_15-15_incorporation.md",
    # Binding companion corpus
    "corpus_systems.md",
    "corpus_institutions.md",
    "corpus_forum.md",
    "corpus_joint_structure.md",
    # Architectural maps and adoption
    "doc_architecture.md",
    "architecture_primer.md",
    "architecture_adoption_appendix.md",
    "README.md",
    "TRUST_UNDER_ATTACK_DELTA_REPORT.md",
    # Active planning / implementation docs referencing defined terms
    "implementation/ARCHITECTURE_WORKLIST.md",
    "implementation/DEC_CONTENT_GAPS_PLAN_2026-04-16.md",
    "implementation/DEC_INDIGENOUS_CONTINUITY_SCOPE_2026-04-17.md",
    "implementation/DEC_TRACK_7_1_POLICY_2026-04-17.md",
    "implementation/TRANSITION_FRAMEWORK_2026.md",
]

# Strip a literal ' (Constitutional)' sequence, but only where it is NOT:
#   (a) preceded by a backtick-opened meta-reference ``(Constitutional)``
#   (b) extended to '(Constitutional Constraint)'  (regex excludes this by
#       matching the closing paren immediately after 'Constitutional')
#
# The regex matches exactly the string " (Constitutional)" as a standalone
# parenthetical appended to a display term. URL anchors like
# "#foo-constitutional" don't contain parentheses at all and are unaffected.
# HTML anchors like '<a id="foo-constitutional">' likewise don't match.
PATTERN = re.compile(r" \(Constitutional\)")

# Lines that must be preserved verbatim (meta-text about the suffix itself).
# Matched by substring; if a line contains any of these, we skip it.
PRESERVE_LINE_SUBSTRINGS = (
    "`(Constitutional)`",  # backtick-quoted meta reference to the literal suffix
)


def should_preserve_line(line: str) -> bool:
    return any(substr in line for substr in PRESERVE_LINE_SUBSTRINGS)


def strip_line(line: str) -> str:
    if should_preserve_line(line):
        return line
    return PATTERN.sub("", line)


def process_file(path: Path) -> tuple[int, int]:
    """Return (line_changes, total_matches_replaced)."""
    original = path.read_text(encoding="utf-8")
    out_lines: list[str] = []
    line_changes = 0
    total_replacements = 0
    for line in original.splitlines(keepends=True):
        if should_preserve_line(line):
            out_lines.append(line)
            continue
        new_line, n = PATTERN.subn("", line)
        if n:
            line_changes += 1
            total_replacements += n
        out_lines.append(new_line)
    new_text = "".join(out_lines)
    if new_text != original:
        path.write_text(new_text, encoding="utf-8")
    return line_changes, total_replacements


def main() -> int:
    grand_lines = 0
    grand_replacements = 0
    any_missing = False
    for rel in TARGETS:
        p = ROOT / rel
        if not p.exists():
            print(f"MISSING: {rel}")
            any_missing = True
            continue
        line_changes, total = process_file(p)
        if total:
            print(f"{rel}: {line_changes} lines changed, {total} suffixes stripped")
        grand_lines += line_changes
        grand_replacements += total
    print()
    print(f"TOTAL: {grand_lines} lines changed, {grand_replacements} suffixes stripped")
    return 1 if any_missing else 0


if __name__ == "__main__":
    sys.exit(main())
