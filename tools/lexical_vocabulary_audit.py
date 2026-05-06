#!/usr/bin/env python3
"""Regression gate: lexical vocabulary (e.g. cloud; bare ``charter`` in binding corpus scope)."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys
from dataclasses import dataclass

# Same binding corpus as reference_audit.py; keeps terminology consistent across normative text.
DEFAULT_SCOPE = [
    "core_00-01_principles.md",
    "core_02-04_definition_mechanics.md",
    "core_05-05_definitions_a_independent.md",
    "core_05-05_definitions_b_semi_independent.md",
    "core_05-05_definitions_c_dependent_clusters.md",
    "core_06-06_standing_classification.md",
    "core_06-06_standing_integration.md",
    "core_07-07_misconduct.md",
    "core_08-08_forum.md",
    "core_09-09_rights_part_a.md",
    "core_09-09_rights_part_b.md",
    "core_09-09_rights_part_c.md",
    "core_09-09_rights_part_d.md",
    "core_10-10_governance.md",
    "core_11-13_amendment.md",
    "core_14-14_incorporation.md",
    "corpus_systems.md",
    "corpus_institutions.md",
    "corpus_forum.md",
    "corpus_joint_structure.md",
    "doc_architecture.md",
    "README.md",
    "architecture_primer.md",
]

# Enforce **breach**-family ban only where the chapter-six pass has landed; expand as other scoped files are scrubbed.
_BREACH_FAMILY_SCOPE = frozenset({"core_06-06_standing_classification.md", "core_06-06_standing_integration.md"})

# Standalone word "cloud" / "Cloud" / "CLOUD", including compounds like cloud-native (still banned).
# Does not match substrings inside unrelated tokens (e.g. "icloud" as one word — no boundary before 'c').
_CLOUD_WORD = re.compile(r"(?<![A-Za-z0-9])cloud(?![A-Za-z0-9])", re.IGNORECASE)

# Prefer **constitutional** / **this Constitution** for Corpus sense; keep **charter** only for legal-instrument senses (allowlisted).
_CHARTER_WORD = re.compile(r"(?<![A-Za-z0-9])charter(?![A-Za-z0-9])", re.IGNORECASE)
_ALLOWLIST_STRIP = [
    re.compile(r"corporate charter(\s+law)?", re.IGNORECASE),
    re.compile(r"treaty,\s+compact,\s+or\s+charter", re.IGNORECASE),
    re.compile(r"adoption,\s+federation,\s+or\s+charter", re.IGNORECASE),
    re.compile(r"supervise,\s+charter,\s+or", re.IGNORECASE),
]

# Mechanical ``charter`` → ``constitutional`` passes can leave ``this constitutional.`` or ``the constitutional requires``; catch known bad compounds.
# Normative corpus uses **sentients** for bearers of standing/agency; avoid **people** and the split phrase **people and agents**.
_PEOPLE_AND_AGENTS = re.compile(r"\bpeople and agents\b", re.IGNORECASE)
_PEOPLE_STANDALONE = re.compile(r"(?<![A-Za-z0-9])people(?![A-Za-z0-9])", re.IGNORECASE)

_ACCESSION_JARGON = re.compile(
    r"\b(accede|acceding|accession)\b",
    re.IGNORECASE,
)

# Undefined in Chapter Five; prefer **violation**, **non-compliance**, **unmet duties** (see `.cursor/rules/clarity.mdc`).
_BREACH_FAMILY = re.compile(
    r"\bduty-breaching\b|\bduty breach\b|\bbreaches\b|\bbreached\b|\bbreaching\b|\bbreach\b",
    re.IGNORECASE,
)

_MINIMA_WORD = re.compile(r"\bminima\b", re.IGNORECASE)

_MALFORMED_CONSTITUTIONAL: list[tuple[str, re.Pattern[str]]] = [
    ("dangling-this-constitutional", re.compile(r"\bthis constitutional\.")),
    ("implement-this-constitutional-period", re.compile(r"\bimplement this constitutional\.")),
    ("the-constitutional-requires", re.compile(r"\bthe constitutional requires\b", re.I)),
    ("under-the-constitutional-period", re.compile(r"\bunder the constitutional\.\s*$")),
    ("with-this-constitutional-when", re.compile(r"\bwith this constitutional when\b", re.I)),
    ("hyphen-constitutional-free", re.compile(r"\bconstitutional-free\b", re.I)),
    (
        "hyphen-constitutional-adjective-glitch",
        re.compile(
            r"\bconstitutional-(valid|bounded|governed|scaled|compatible|applicable|material|hook)\b",
            re.I,
        ),
    ),
]


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    rule: str
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=".",
        help="Workspace root path.",
    )
    parser.add_argument(
        "--scope",
        nargs="+",
        default=DEFAULT_SCOPE,
        help="Markdown files to scan.",
    )
    parser.add_argument(
        "--write-evidence",
        action="store_true",
        help="Write a dated report under evidence/<date>/.",
    )
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Date for evidence path (YYYY-MM-DD).",
    )
    return parser.parse_args()


def load_text(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Missing required file: {path}")


def scan_cloud(rel_path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    for idx, raw_line in enumerate(text.splitlines(), start=1):
        if _CLOUD_WORD.search(raw_line):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="forbidden-cloud",
                    text=raw_line.strip(),
                ),
            )
    return findings


def _mask_allowlisted_charter_spans(line: str) -> str:
    masked = line
    for pat in _ALLOWLIST_STRIP:
        masked = pat.sub(lambda m: " " * len(m.group(0)), masked)
    return masked


def scan_corpus_no_bare_charter(rel_path: str, text: str) -> list[Finding]:
    """Standalone **charter** is reserved for allowlisted legal-instrument phrases; elsewhere use **constitutional** / **this Constitution**."""
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        check_line = _mask_allowlisted_charter_spans(raw)
        if _CHARTER_WORD.search(check_line):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="corpus-no-bare-charter",
                    text=raw.strip(),
                ),
            )

    return findings


def scan_prefer_sentients_not_people_phrasing(rel_path: str, text: str) -> list[Finding]:
    """Reject **people** (standalone) and **people and agents**; prefer **sentients** in normative scoped text."""
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if _PEOPLE_AND_AGENTS.search(raw) or _PEOPLE_STANDALONE.search(raw):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="prefer-sentients-not-people-phrasing",
                    text=raw.strip(),
                ),
            )

    return findings


def scan_avoid_accession_jargon(rel_path: str, text: str) -> list[Finding]:
    """Prefer plain **join** / **joining** (and related adoption wording) over treaty-style **accede** / **accession**."""
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if _ACCESSION_JARGON.search(raw):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="avoid-accession-jargon",
                    text=raw.strip(),
                ),
            )

    return findings


def scan_avoid_breach_family(rel_path: str, text: str) -> list[Finding]:
    """Reject undefined **breach** / **duty breach** / **duty-breaching** (prefer **violation**, **non-compliance**, **unmet duties**)."""
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if _BREACH_FAMILY.search(raw):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="avoid-undefined-breach-family",
                    text=raw.strip(),
                ),
            )

    return findings


def scan_avoid_minima(rel_path: str, text: str) -> list[Finding]:
    """Reject **minima**; prefer **requirements**, **floors**, **conditions**, or a context-specific term."""
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if _MINIMA_WORD.search(raw):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="avoid-minima",
                    text=raw.strip(),
                ),
            )

    return findings


def scan_malformed_constitutional_phrasing(rel_path: str, text: str) -> list[Finding]:
    """Flag grammar glitches from bad ``constitutional`` compounding (prefer **this Constitution** or *constitutionally* …)."""
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        for rule_name, pat in _MALFORMED_CONSTITUTIONAL:
            if pat.search(raw):
                findings.append(
                    Finding(
                        file=rel_path,
                        line=idx,
                        rule=rule_name,
                        text=raw.strip(),
                    ),
                )
                break

    return findings


def report_markdown(run_date: str, scope: list[str], findings: list[Finding]) -> str:
    lines: list[str] = [
        f"# Lexical vocabulary audit — {run_date}",
        "",
        "Rules:",
        "- **`forbidden-cloud`:** standalone **cloud** → use **info-sphere** (and related) terminology.",
        "- **`corpus-no-bare-charter`:** in scoped files, standalone **charter** → prefer **constitutional** / **this Constitution** for Corpus sense. **Allowed:** `corporate charter`, `treaty, compact, or charter`, `adoption, federation, or charter`, and the verb list `supervise, charter, or …`.",
        "- **`malformed-constitutional-*`:** reject **this constitutional.** / **implement this constitutional.** / **the constitutional requires** / **under the constitutional.** (line-end) / **with this constitutional when** / **constitutional-free**, and hyphen glitches **constitutional-valid**, **constitutional-bounded**, **constitutional-governed**, **constitutional-scaled**, **constitutional-compatible**, **constitutional-applicable**, **constitutional-material**, **constitutional-hook** (use *constitutionally …* or **this Constitution** / **constitutional hook** as appropriate).",
        "- **`prefer-sentients-not-people-phrasing`:** reject standalone **people** and **people and agents** → use **sentients** (or another defined corpus term).",
        "- **`avoid-accession-jargon`:** reject **accede**, **acceding**, and **accession** → prefer **join** / **joining** / **additional parties** adoption wording.",
        "- **`avoid-undefined-breach-family`:** reject standalone **breach** / **breaches** / **breached** / **breaching**, **duty breach**, and **duty-breaching** → prefer **violation**, **non-compliance**, **unmet duties**, or defined Chapter Six typing (see `.cursor/rules/clarity.mdc`). *Currently enforced only on files in `_BREACH_FAMILY_SCOPE` inside `tools/lexical_vocabulary_audit.py`.*",
        "- **`avoid-minima`:** reject **minima** → prefer **requirements**, **floors**, **conditions**, or another context-specific term.",
        "",
        "## Scope",
    ]
    for file_path in scope:
        lines.append(f"- `{file_path}`")
    lines.extend(["", "## Findings"])
    if findings:
        lines.append("| File | Line | Rule | Snippet |")
        lines.append("|---:|---:|---|---|")
        for item in findings:
            snippet = item.text.replace("|", "\\|")
            if len(snippet) > 120:
                snippet = snippet[:117] + "..."
            lines.append(
                f"| `{item.file}` | {item.line} | `{item.rule}` | {snippet} |"
            )
        lines.append("")
        lines.append("## Result")
        lines.append("- `FAIL`")
    else:
        lines.append("- No occurrences detected.")
        lines.append("")
        lines.append("## Result")
        lines.append("- `PASS`")
    lines.append("")
    return "\n".join(lines)


def write_evidence(root: pathlib.Path, run_date: str, report: str) -> pathlib.Path:
    evidence_dir = root / "evidence" / run_date
    evidence_dir.mkdir(parents=True, exist_ok=True)
    evidence_file = evidence_dir / f"LEXICAL_VOCABULARY_AUDIT_{run_date}.md"
    evidence_file.write_text(report, encoding="utf-8")
    return evidence_file


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()

    findings: list[Finding] = []
    for rel_path in args.scope:
        file_path = root / rel_path
        if not file_path.is_file():
            print(
                f"lexical_vocabulary_audit: skipping missing scope file: {rel_path}",
                file=sys.stderr,
            )
            continue
        text = load_text(file_path)
        findings.extend(scan_cloud(rel_path, text))
        findings.extend(scan_corpus_no_bare_charter(rel_path, text))
        findings.extend(scan_malformed_constitutional_phrasing(rel_path, text))
        findings.extend(scan_prefer_sentients_not_people_phrasing(rel_path, text))
        findings.extend(scan_avoid_accession_jargon(rel_path, text))
        findings.extend(scan_avoid_minima(rel_path, text))
        if rel_path in _BREACH_FAMILY_SCOPE:
            findings.extend(scan_avoid_breach_family(rel_path, text))

    report = report_markdown(args.date, args.scope, findings)
    if args.write_evidence:
        evidence_path = write_evidence(root, args.date, report)
        print(f"Wrote evidence report: {evidence_path}")
    else:
        print(report)

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
