"""Verify that every D/E/C widget row in the consumer files resolves to a live
anchor in ``core_05-05_definitions_a_independent.md``. Reports any dead
targets on stderr and returns non-zero if any are found.

Run from the repository root:

    python3 tools/verify_dec_anchors.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


CH5 = Path("core_05-05_definitions_a_independent.md")
CONSUMERS = [
    Path("core_00_preamble.md"),
    Path("core_01_a_values_principles.md"),
    Path("core_01_b_stewardship_capacity_principles.md"),
    Path("core_02-04_definition_mechanics.md"),
    Path("core_06-06_standing_assessment.md"),
    Path("core_07-07_standing_integration.md"),
    Path("core_08-08_misconduct.md"),
    Path("core_09-09_forum.md"),
    Path("core_10-10_rights_part_a.md"),
    Path("core_10-10_rights_part_b.md"),
    Path("core_10-10_rights_part_c.md"),
    Path("core_10-10_rights_part_d.md"),
    Path("core_11-11_governance.md"),
    Path("core_12-14_amendment.md"),
    Path("core_15-15_incorporation.md"),
]

LINK_RE = re.compile(r"\]\(core_05-05_definitions_a_independent\.md#([^)]+)\)")
ANCHOR_TAG_RE = re.compile(r'<a id="([^"]+)"></a>')
H2_RE = re.compile(r"^##\s+(.+?)\s*$")
H3_RE = re.compile(r"^###\s+(.+?)\s*$")
H4_RE = re.compile(r"^####\s+(.+?)\s*$")
H5_RE = re.compile(r"^#####\s+(.+?)\s*$")


def collect_ch5_anchors() -> set[str]:
    anchors: set[str] = set()
    for m in ANCHOR_TAG_RE.finditer(CH5.read_text(encoding="utf-8")):
        anchors.add(m.group(1))
    # Also include implicit heading anchors (auto-slug) for headings that do
    # not carry an explicit <a id="..."></a>.
    for line in CH5.read_text(encoding="utf-8").splitlines():
        for pat in (H2_RE, H3_RE, H4_RE, H5_RE):
            m = pat.match(line)
            if m:
                slug = m.group(1).lower()
                slug = re.sub(r"[^\w\s-]", "", slug)
                slug = re.sub(r"\s+", "-", slug)
                slug = re.sub(r"-+", "-", slug).strip("-")
                if slug:
                    anchors.add(slug)
    return anchors


def main() -> int:
    anchors = collect_ch5_anchors()

    missing: list[tuple[str, int, str]] = []
    for consumer in CONSUMERS:
        if not consumer.exists():
            continue
        for lineno, line in enumerate(
            consumer.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for m in LINK_RE.finditer(line):
                slug = m.group(1)
                if slug not in anchors:
                    missing.append((str(consumer), lineno, slug))

    if missing:
        print(
            f"MISSING ANCHORS ({len(missing)} links into Chapter Five have no "
            f"matching anchor):",
            file=sys.stderr,
        )
        for path, lineno, slug in missing:
            print(f"  {path}:{lineno}  #{slug}", file=sys.stderr)
        return 1

    print(f"OK: all Chapter Five links across {len(CONSUMERS)} consumer files resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
