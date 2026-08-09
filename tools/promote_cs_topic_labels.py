#!/usr/bin/env python3
"""Give the remaining wall-of-text CS files real section headings.

``cs_04`` and ``Protocol S5`` carry their whole body under a single title, with
topic changes marked only by a bold run-in such as ``**Dependent systems
map.** Systems must maintain ...``. A reader gets no table of contents, no
anchors, and no way to link to a topic.

This promotes a named list of those labels to numbered ``## N. Title``
headings with explicit anchors, matching the pattern already working in
``cs_02_a_information_types_and_handling.md``, and leaves the sentence that
followed the label as the section's opening paragraph.

Labels are listed per file rather than matched by pattern, because these files
also use bold run-ins for sub-points that qualify a topic rather than start
one. Promoting those would fragment the section they belong to. Headings are
additive, so no inbound reference breaks.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Ordered topic labels, exactly as they appear between the bold markers and
# before the terminating "." or ":".
LABELS: dict[str, tuple[str, ...]] = {
    "cs_04_critical_system_stewardship.md": (
        "Definition",
        "Classification as steward",
        "Stewardship criticality levels",
        "Scaling obligations",
        "Steward responsibilities — systems under control",
        "Steward responsibilities — governance structures",
        "Conduct, conflicts of interest, and independence",
        "Continuity, transfer, and exit integrity",
        "Competency, succession, and oversight effectiveness",
        "Integrated risk governance (Class A/B)",
        "Intervention trigger",
        "Relationship to system classes",
        "Private chokepoints sentients depend on (access continuity and non-capture)",
        "Core characteristics (typical)",
        "Substitutability and dependency reduction",
        "Transparency and auditability",
        "Intervention and cooperation",
        "Governance and incentive integrity",
        "Failure and reclassification",
    ),
    "cs_protocol_s5_resource_allocation_funding_stewardship.md": (
        "Principles of funding",
        "Cross-system resource flows and dependencies",
        "Dependent systems map",
        "Transparency of resource flows",
        "Prevention of funding-based capture",
        "Required allocation categories",
        "Bounded builder returns",
        "Stability of funding agreements",
        "Evolution of funding models",
        "Default funding allocation models",
        "Reference allocation guidance",
        "Substrate system funding",
        "Non-substrate systems",
        "Stakeholder governance of funding",
        "Trigger definitions",
        "Triggering review and challenge",
        "Due process in funding changes",
        "Steward, operator, and governance remuneration (incentive governance)",
        "Conflict-free remuneration processes",
        "Observability of alignment",
    ),
}


def slug(text: str) -> str:
    """GitHub's heading slug: lowercase, punctuation dropped, spaces hyphenated."""
    lowered = text.lower()
    kept = re.sub(r"[^\w\s-]", "", lowered.replace("—", " ").replace("/", " "))
    return re.sub(r"[-\s]+", "-", kept).strip("-")


def promote(text: str, labels: tuple[str, ...], start: int) -> tuple[str, list[str]]:
    lines = text.splitlines()
    out: list[str] = []
    missed = list(labels)
    number = start
    fenced = False
    depth = 0

    pending = {label: re.compile(rf"^\*\*{re.escape(label)}[.:]\*\*(?P<rest>.*)$")
               for label in labels}

    for line in lines:
        if line.startswith("```"):
            fenced = not fenced
        stripped = line.strip()
        if "<details>" in stripped:
            depth += 1
        elif "</details>" in stripped:
            depth = max(0, depth - 1)

        hit = None
        if not fenced and not depth:
            for label in missed:
                match = pending[label].match(line)
                if match:
                    hit = (label, match.group("rest").strip())
                    break

        if not hit:
            out.append(line)
            continue

        label, rest = hit
        missed.remove(label)
        title = f"{number}. {label}"
        number += 1
        if out and out[-1].strip():
            out.append("")
        out.append(f'<a id="{slug(title)}"></a>')
        out.append(f"## {title}")
        if rest:
            out.append("")
            out.append(rest)

    result = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    if not result.endswith("\n"):
        result += "\n"
    return result, missed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--file", help="Restrict to one file name.")
    parser.add_argument("--start", type=int, default=1, help="First section number.")
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    names = [args.file] if args.file else list(LABELS)
    status = 0
    for name in names:
        path = root / "corpus_systems" / name
        if not path.is_file():
            print(f"missing: {name}", file=sys.stderr)
            return 2
        text = path.read_text(encoding="utf-8")
        new_text, missed = promote(text, LABELS[name], args.start)
        found = len(LABELS[name]) - len(missed)
        print(f"{'wrote' if args.write else 'would promote'} {name}: {found} headings")
        for label in missed:
            print(f"  NOT FOUND: {label}", file=sys.stderr)
            status = 1
        if args.write:
            path.write_text(new_text, encoding="utf-8")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
