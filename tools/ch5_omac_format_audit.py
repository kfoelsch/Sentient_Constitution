#!/usr/bin/env python3
"""Report Chapter Five O/M/A/C entry-format remaining work.

Two accepted shapes (see ``doc_architecture.md`` Measurement-informed O/M/A/C):

1. **Aim / leg heads** (Flourishing, Continuity aim, Tetrad leg heads) —
   either precise letter markers or the reader-facing guidepost form:

       - O: … / - M: … / - A: … / - C: …
         (with **In scope:** / Out of scope under O)

       or

       - **What it is** / **How to measure and assess** / **What must hold**
         (same sublabels as leaf definitions)

2. **Leaf definitions** (band ``####`` / ``#####`` entries) — guidepost form:

       - **What it is**
         - **In scope:** …
         - **Out of scope:** …
       - **How to measure and assess**
         - **Primary measure:** …
           **Primary assessment:** …
       - **What must hold**
         - **Primary failure:** …

This audit inventories gaps so operators can chip away at residual format
work. By default it **fails only on aim/leg-head violations** (those must be
precise). Leaf residuals print as ``REMAINING`` and do not fail unless
``--strict`` is set.

Run:

    make ch5-omac-format-audit
    python3 tools/ch5_omac_format_audit.py --root . --strict
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_AIMS, CH5_BANDS, CH5_LEGS  # noqa: E402

# Files whose file-head O/M/A/C (before the first ####) must use letter form.
LEG_HEAD_FILES = frozenset(CH5_LEGS)

HEADING_RE = re.compile(r"^(#{4,5})\s+(.+)$")
LETTER_O_RE = re.compile(r"(?m)^- O:")
LETTER_M_RE = re.compile(r"(?m)^- M:")
LETTER_A_RE = re.compile(r"(?m)^- A:")
LETTER_C_RE = re.compile(r"(?m)^- C:")
GUIDE_O_RE = re.compile(r"(?m)^- \*\*What it is\*\*\s*$")
GUIDE_MA_RE = re.compile(r"(?m)^- \*\*How to measure and assess\*\*\s*$")
GUIDE_C_RE = re.compile(r"(?m)^- \*\*What must hold\*\*\s*$")
IN_SCOPE_RE = re.compile(r"\*\*In scope(?:\s*—[^:]+)?:\*\*")
OUT_SCOPE_RE = re.compile(
    r"\*\*Out of scope:\*\*|^  - Out of scope:",
    re.MULTILINE,
)
PRIMARY_MEASURE_RE = re.compile(r"\*\*Primary measure:\*\*")
PRIMARY_ASSESSMENT_RE = re.compile(r"\*\*Primary assessment:\*\*")
PRIMARY_FAILURE_RE = re.compile(r"\*\*Primary failure[.:]\*\*")
MEASUREMENTS_STUB_RE = re.compile(r"(?m)^\*?Measurements:\*?")


@dataclass
class Finding:
    path: str
    title: str
    kind: str  # head | leaf
    issues: list[str] = field(default_factory=list)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument(
        "--strict",
        action="store_true",
        help="Fail on leaf residuals as well as aim/leg-head violations.",
    )
    p.add_argument(
        "--file",
        action="append",
        default=[],
        help="Limit to one or more relative paths (repeatable).",
    )
    return p.parse_args()


def _split_entries(text: str) -> list[tuple[str, str]]:
    """Return (title, body) pairs; first pair may be ('__FILE_HEAD__', preamble)."""
    parts = re.split(r"(?m)^(#{4,5} .+)$", text)
    entries: list[tuple[str, str]] = [("__FILE_HEAD__", parts[0])]
    i = 1
    while i < len(parts) - 1:
        entries.append((parts[i].strip(), parts[i + 1]))
        i += 2
    return entries


def _is_cluster_shell(title: str, body: str) -> bool:
    if re.match(r"^#{4}\s+Def\.[OPACI]\d+", title):
        return True
    head = body[:800]
    if (
        "**Cluster context:**" in head or "**Semi-independent context**" in head
    ) and not GUIDE_O_RE.search(head) and not LETTER_O_RE.search(head):
        return True
    if title.startswith("### ") or "Independent terms" in title or "Semi-independent" in title:
        return True
    return False


def _check_letter_omac(body: str) -> list[str]:
    issues: list[str] = []
    if not LETTER_O_RE.search(body):
        issues.append("missing - O:")
    if not LETTER_M_RE.search(body):
        issues.append("missing - M:")
    if not LETTER_A_RE.search(body):
        issues.append("missing - A:")
    if not LETTER_C_RE.search(body):
        issues.append("missing - C:")
    if LETTER_O_RE.search(body):
        o_block = body
        m = LETTER_O_RE.search(body)
        if m:
            rest = body[m.end() :]
            next_comp = re.search(r"(?m)^- [MAC]:", rest)
            o_block = rest[: next_comp.start()] if next_comp else rest
        if "**In scope:**" not in o_block:
            issues.append("O missing **In scope:**")
        if not OUT_SCOPE_RE.search(o_block):
            issues.append("O missing Out of scope")
    return issues


def _check_guidepost_omac(body: str) -> list[str]:
    issues: list[str] = []
    if not GUIDE_O_RE.search(body):
        issues.append("missing **What it is**")
    else:
        if not IN_SCOPE_RE.search(body):
            issues.append("O missing **In scope:**")
        if not OUT_SCOPE_RE.search(body):
            issues.append("O missing **Out of scope:**")
    if not GUIDE_MA_RE.search(body):
        issues.append("missing **How to measure and assess**")
    else:
        if not PRIMARY_MEASURE_RE.search(body):
            issues.append("M missing **Primary measure:**")
        if not PRIMARY_ASSESSMENT_RE.search(body):
            issues.append("A missing **Primary assessment:**")
    if not GUIDE_C_RE.search(body):
        issues.append("missing **What must hold**")
    elif not PRIMARY_FAILURE_RE.search(body):
        # Allow unlabelled single-line C only when Primary failure absent and
        # body uses "Non-compliant" prose — still flag for precise rollout.
        issues.append("C missing **Primary failure:**")
    if MEASUREMENTS_STUB_RE.search(body):
        issues.append("legacy *Measurements:* stub (migrate into M/A)")
    if LETTER_O_RE.search(body) and GUIDE_O_RE.search(body):
        issues.append("mixed letter and guidepost O markers")
    elif LETTER_O_RE.search(body) and not GUIDE_O_RE.search(body):
        issues.append("legacy letter-marker leaf (migrate to guidepost)")
        issues.extend(
            x for x in _check_letter_omac(body) if x.startswith("missing - M:")
        )
    return issues


def _file_head_body(preamble: str) -> str:
    """Slice file-head O/M/A/C: after first Trace close, before ### decomposition/measuring."""
    # Prefer content after the Trace widget.
    trace_close = preamble.find("</details>")
    if trace_close == -1:
        body = preamble
    else:
        # May have corpus placement details first; take from last Trace-ish block
        # that precedes an - O: or **What it is**.
        body = preamble
        for m in re.finditer(r"</details>", preamble):
            after = preamble[m.end() :]
            if LETTER_O_RE.search(after) or GUIDE_O_RE.search(after):
                body = after
                break
    cut = re.search(
        r"(?m)^### (?:Constitutional Aim|Aim|Leg|Tetrad Leg) decomposition|^### Measuring |^### \w+: Independent|^## Timeliness",
        body,
    )
    if cut:
        body = body[: cut.start()]
    return body


def audit_file(path: Path, rel: str) -> list[Finding]:
    text = path.read_text(encoding="utf-8")
    findings: list[Finding] = []
    entries = _split_entries(text)

    if rel in CH5_AIMS or rel in LEG_HEAD_FILES:
        head_body = _file_head_body(entries[0][1])
        if GUIDE_O_RE.search(head_body):
            issues = _check_guidepost_omac(head_body)
            # Aim/leg heads are not leaves; drop the leaf-migration residual.
            issues = [
                i for i in issues if i != "legacy letter-marker leaf (migrate to guidepost)"
            ]
        else:
            issues = _check_letter_omac(head_body)
        if issues:
            findings.append(
                Finding(rel, "__FILE_HEAD__", "head", issues)
            )

    if rel in CH5_AIMS or rel in LEG_HEAD_FILES:
        return findings

    for title, body in entries[1:]:
        if _is_cluster_shell(title, body):
            continue
        # Only score bodies that look like definition entries.
        if not (
            GUIDE_O_RE.search(body)
            or LETTER_O_RE.search(body)
            or GUIDE_MA_RE.search(body)
            or MEASUREMENTS_STUB_RE.search(body)
        ):
            continue
        issues = _check_guidepost_omac(body)
        if issues:
            findings.append(Finding(rel, title, "leaf", issues))
    return findings


def main() -> int:
    args = parse_args()
    root = Path(args.root)
    targets = args.file or [*CH5_AIMS, *CH5_LEGS, *CH5_BANDS]
    findings: list[Finding] = []
    for rel in targets:
        path = root / rel
        if not path.exists():
            print(f"MISSING: {rel}", file=sys.stderr)
            return 2
        findings.extend(audit_file(path, rel))

    head_findings = [f for f in findings if f.kind == "head"]
    leaf_findings = [f for f in findings if f.kind == "leaf"]

    if head_findings:
        print("FAIL — aim/leg heads (letter O/M/A/C or guidepost form):\n")
        for f in head_findings:
            print(f"  {f.path} [{f.title}]")
            for issue in f.issues:
                print(f"    - {issue}")
            print()

    if leaf_findings:
        print(
            f"REMAINING — leaf guidepost O/M/A/C gaps "
            f"({len(leaf_findings)} entries):\n"
        )
        by_file: dict[str, list[Finding]] = {}
        for f in leaf_findings:
            by_file.setdefault(f.path, []).append(f)
        for path, items in by_file.items():
            print(f"  {path} ({len(items)})")
            for f in items:
                print(f"    {f.title}")
                for issue in f.issues:
                    print(f"      - {issue}")
            print()

    if not findings:
        print("ch5-omac-format-audit: PASS — no O/M/A/C format gaps found")
        return 0

    print(
        f"ch5-omac-format-audit: {len(head_findings)} head issue(s), "
        f"{len(leaf_findings)} leaf residual(s)"
    )
    if head_findings:
        return 1
    if args.strict and leaf_findings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
