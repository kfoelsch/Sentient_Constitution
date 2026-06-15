#!/usr/bin/env python3
"""One-off: replace ambiguous 'Constitutional Systems' with corpus_systems.md-based references. Run from repo root."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_PREFIXES = ("archive/", "implementation/", ".cursor/")

# Applied in order: longest / most specific first.
REPLACEMENTS: list[tuple[str, str]] = [
    # Long protocol + chapter with em dash
    (
        "**Constitutional Systems, Protocol C — Justice Safeguards, Restitution, and Rehabilitation Implementation**",
        "**[corpus_systems.md](corpus_systems.md), Protocol C — Justice Safeguards, Restitution, and Rehabilitation Implementation**",
    ),
    (
        "**Constitutional Systems, Protocol A — System Design, Testing, Verification, and Deployment**",
        "**[corpus_systems.md](corpus_systems.md), Protocol A — System Design, Testing, Verification, and Deployment**",
    ),
    (
        "**Constitutional Systems, Protocol B — *System Comprehensibility and Complexity Stewardship***",
        "**[corpus_systems.md](corpus_systems.md), Protocol B — *System Comprehensibility and Complexity Stewardship***",
    ),
    (
        "Constitutional Systems, CS-3 — Information types and handling",
        "[corpus_systems.md](corpus_systems.md), CS-3 — Information types and handling",
    ),
    (
        "Constitutional Systems, CS-4 — System classification and handling",
        "[corpus_systems.md](corpus_systems.md), CS-4 — System classification and handling",
    ),
    (
        "Constitutional Systems, CS-3",
        "[corpus_systems.md](corpus_systems.md), CS-3",
    ),
    (
        "Constitutional Systems, CS-4",
        "[corpus_systems.md](corpus_systems.md), CS-4",
    ),
    (
        "Constitutional Systems, CS-5",
        "[corpus_systems.md](corpus_systems.md), CS-5",
    ),
    # Protocols (shorter)
    (
        "**Constitutional Systems, Protocol S5**",
        "**[corpus_systems.md](corpus_systems.md), Protocol S5**",
    ),
    (
        "**Constitutional Systems, Protocol S4**",
        "**[corpus_systems.md](corpus_systems.md), Protocol S4**",
    ),
    (
        "**Constitutional Systems, Protocol D**",
        "**[corpus_systems.md](corpus_systems.md), Protocol D**",
    ),
    (
        "**Constitutional Systems, Protocol C**",
        "**[corpus_systems.md](corpus_systems.md), Protocol C**",
    ),
    (
        "**Constitutional Systems, Protocol A**",
        "**[corpus_systems.md](corpus_systems.md), Protocol A**",
    ),
    (
        "**Constitutional Systems, Protocol B**",
        "**[corpus_systems.md](corpus_systems.md), Protocol B**",
    ),
    # Two-bold merged references (S1, S2, S3 with titles)
    (
        "**Constitutional Systems**, **CS-3 — Information types and handling**",
        "**[corpus_systems.md](corpus_systems.md), CS-3 — Information types and handling**",
    ),
    (
        "**Constitutional Systems**, **CS-4 — System classification and handling**",
        "**[corpus_systems.md](corpus_systems.md), CS-4 — System classification and handling**",
    ),
    (
        "**Constitutional Systems**, **CS-5 — Critical system stewardship**",
        "**[corpus_systems.md](corpus_systems.md), CS-5 — Critical system stewardship**",
    ),
    # Chapter only (second part bold)
    (
        "**Constitutional Systems** **CS-3**",
        "**[corpus_systems.md](corpus_systems.md), CS-3**",
    ),
    (
        "**Constitutional Systems** **Protocol A**",
        "**[corpus_systems.md](corpus_systems.md), Protocol A**",
    ),
    # Parenthetical in incorporation
    (
        "([corpus_systems.md](corpus_systems.md)) (*Constitutional Systems*)",
        "([corpus_systems.md](corpus_systems.md)) (*systems companion*)",
    ),
    # Italic joint
    (
        "*Constitutional Systems, CS-3*",
        "*[corpus_systems.md](corpus_systems.md), CS-3*",
    ),
    (
        "*Constitutional Systems* CS-4",
        "*[corpus_systems.md](corpus_systems.md)*, CS-4",
    ),
    (
        "Under *Constitutional Systems* CS-4,",
        "Under *[corpus_systems.md](corpus_systems.md)*, CS-4,",
    ),
    (
        "including *Constitutional Systems*, CS-4",
        "including *[corpus_systems.md](corpus_systems.md)*, CS-4",
    ),
    # Governance / adoption loose phrasing
    (
        "Constitutional Systems Chapters S2 and S3",
        "[corpus_systems.md](corpus_systems.md) Chapters S2 and S3",
    ),
    (
        "in Constitutional Systems and **section 15.3**",
        "in [corpus_systems.md](corpus_systems.md) and **section 15.3**",
    ),
    # Annex mini heading patterns (doc_architecture)
    (
        "### Citing Constitutional Systems from Sentient Constitution",
        "### Citing corpus_systems.md from Sentient Constitution",
    ),
    (
        "## 6. Stable IDs — Constitutional Systems (CS companion file)",
        "## 6. Stable IDs — corpus_systems.md (CS companion file)",
    ),
    (
        "### Constitutional Systems — opening interpretation (non-chapter anchors)",
        "### corpus_systems.md — opening interpretation (non-chapter anchors)",
    ),
    (
        "  subgraph annex [Constitutional Systems]",
        "  subgraph annex [corpus_systems.md]",
    ),
    # Bare final
    (
        "**Constitutional Systems**",
        "**[corpus_systems.md](corpus_systems.md)**",
    ),
    # Remaining "Constitutional Systems" without ** (e.g. already partially replaced) — run last
]

# Phrases that must become links but were broken by the broad **[corpus_systems...]** if any — handled by order.


def should_process(rel: str) -> bool:
    for p in SKIP_PREFIXES:
        if rel.startswith(p):
            return False
    if rel in ("doc_architecture.md", "architecture_adoption_appendix.md"):
        return True
    if rel.startswith("core_") or rel.startswith("corpus_"):
        return True
    return False


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*.md")):
        rel = str(path.relative_to(ROOT))
        if not should_process(rel):
            continue
        text = path.read_text(encoding="utf-8")
        orig = text
        for a, b in REPLACEMENTS:
            text = text.replace(a, b)
        # `CS` = line in doc — update separately
        if rel == "doc_architecture.md" and "`CS` = Constitutional Systems (companion systems file)" in text:
            text = text.replace(
                "`CS` = Constitutional Systems (companion systems file).",
                "`CS` = [corpus_systems.md](corpus_systems.md) (systems companion; **do not** use the bare phrase *Constitutional Systems* in body text — see *Plain-Language Vocabulary Guardrails*).",
            )
        if text != orig:
            path.write_text(text, encoding="utf-8", newline="\n")
            changed += 1
            print("updated:", rel)
    print("files changed:", changed)


if __name__ == "__main__":
    main()
