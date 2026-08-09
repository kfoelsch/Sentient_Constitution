#!/usr/bin/env python3
"""Turn the bold run-in labels in the CS protocol files into real headings.

Eight CS files carry their whole body under a single title, with sections
marked only by a bold lead-in such as ``**3. Partition-safe decision
constraints.** During Degraded-Partitioned modes ...``. A reader gets no table
of contents, no anchors, and no way to link to a section.

This promotes those labels to ``## 3. Partition-safe decision constraints``,
matching the pattern already working in
``cs_02_a_information_types_and_handling.md``, and leaves the sentence that
followed the label as the section's opening paragraph.

Only labels that begin a line and read as ``<number or letter>. <Title>.`` are
promoted. Sub-labels such as ``**Systems-layer profile:**`` keep their bold
run-in styling, because they qualify the section rather than divide it.
Headings are additive, so no inbound reference breaks.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# **3. Title.** rest  /  **A. Title.** rest
LABEL_RE = re.compile(r"^\*\*(?P<label>(?:\d+|[A-Z]))\.\s+(?P<title>[^*]+?)\.\*\*(?P<rest>.*)$")

TARGETS = (
    "cs_04_critical_system_stewardship.md",
    "cs_protocol_a_system_design_testing_verification_deployment.md",
    "cs_protocol_b_system_comprehensibility_complexity_stewardship.md",
    "cs_protocol_d_decentralized_constitutional_continuity_partition_resilience.md",
    "cs_protocol_r_subversion_response_replacement_reconstitution.md",
    "cs_protocol_s4_adaptive_sustainability_ecosystem_resilience.md",
    "cs_protocol_s5_resource_allocation_funding_stewardship.md",
    "cs_protocol_t_transition_constitution_migration_governance.md",
)


def promote(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out: list[str] = []
    count = 0
    fenced = False
    depth = 0
    for line in lines:
        if line.startswith("```"):
            fenced = not fenced
        stripped = line.strip()
        if "<details>" in stripped:
            depth += 1
        elif "</details>" in stripped:
            depth = max(0, depth - 1)

        match = None if (fenced or depth) else LABEL_RE.match(line)
        if not match:
            out.append(line)
            continue

        title = match.group("title").strip()
        rest = match.group("rest").strip()
        if out and out[-1].strip():
            out.append("")
        out.append(f"## {match.group('label')}. {title}")
        count += 1
        if rest:
            out.append("")
            out.append(rest)
    result = "\n".join(out)
    result = re.sub(r"\n{3,}", "\n\n", result)
    if not result.endswith("\n"):
        result += "\n"
    return result, count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--file", help="Restrict to one file name.")
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    names = [args.file] if args.file else list(TARGETS)
    total = 0
    for name in names:
        path = root / "corpus_systems" / name
        if not path.is_file():
            print(f"missing: {name}", file=sys.stderr)
            return 2
        text = path.read_text(encoding="utf-8")
        new_text, count = promote(text)
        if not count:
            print(f"  no labels: {name}")
            continue
        total += count
        print(f"{'wrote' if args.write else 'would promote'} {name}: {count} headings")
        if args.write:
            path.write_text(new_text, encoding="utf-8")
    print(f"\n{total} headings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
