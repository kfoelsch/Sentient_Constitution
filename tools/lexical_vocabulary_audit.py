#!/usr/bin/env python3
"""Regression gate: lexical vocabulary (e.g. cloud; bare ``charter`` in binding corpus scope)."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys
from dataclasses import dataclass

from corpus_paths import binding_corpus_scope

# Enforce **breach**-family ban only where the chapter-six pass has landed; expand as other scoped files are scrubbed.
_BREACH_FAMILY_SCOPE = frozenset({"core_06-06_standing_assessment.md", "core_07-07_standing_integration.md"})

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
_COURT_FAMILY = re.compile(r"\bcourts?\b", re.IGNORECASE)

_RIGHTS_FLOOR_CASING = re.compile(r"\b(?:rights floor|rights floors|rights-floor)\b")
_FOUNDATIONAL_RIGHTS_CASING = re.compile(r"\b(?:Foundational rights|foundational rights)\b")

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
        default=None,
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


def run_internal_regression_checks() -> None:
    """Fail closed if core lexical regexes stop catching known bad phrasing."""
    sample = (
        "User agency and control\n\n"
        "- OP-O: People must have practical control over ranking and presentation "
        "when that control is appropriate, including chronological or lightly processed views where feasible.\n"
    )
    findings = scan_prefer_sentients_not_people_phrasing("internal-regression.md", sample)
    if not findings:
        raise RuntimeError(
            "Internal regression failed: capitalized standalone 'People' was not flagged.",
        )


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


def scan_avoid_court_family(rel_path: str, text: str) -> list[Finding]:
    """Reject **court** / **courts** in institutional senses; prefer **forum** / **forums**."""
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if rel_path == "doc_architecture.md" and "`court" in raw:
            continue

        if _COURT_FAMILY.search(raw):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="avoid-court-family",
                    text=raw.strip(),
                ),
            )

    return findings


def _mask_inline_code_and_link_targets(line: str) -> str:
    """Hide inline code and Markdown link destinations while preserving link text."""
    chars = list(line)
    idx = 0
    while idx < len(chars):
        if chars[idx] == "`":
            end = line.find("`", idx + 1)
            if end == -1:
                for mask_idx in range(idx, len(chars)):
                    chars[mask_idx] = " "
                break
            for mask_idx in range(idx, end + 1):
                chars[mask_idx] = " "
            idx = end + 1
            continue
        if chars[idx] == "]" and idx + 1 < len(chars) and chars[idx + 1] == "(":
            end = line.find(")", idx + 2)
            if end == -1:
                for mask_idx in range(idx + 1, len(chars)):
                    chars[mask_idx] = " "
                break
            for mask_idx in range(idx + 1, end + 1):
                chars[mask_idx] = " "
            idx = end + 1
            continue
        idx += 1
    return "".join(chars)


def scan_load_bearing_capitalization(rel_path: str, text: str) -> list[Finding]:
    """Require load-bearing **Rights Floor** / **Foundational Rights** casing outside links and code."""
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        check_line = _mask_inline_code_and_link_targets(raw)
        if _RIGHTS_FLOOR_CASING.search(check_line):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="load-bearing-rights-floor-casing",
                    text=raw.strip(),
                ),
            )
        if _FOUNDATIONAL_RIGHTS_CASING.search(check_line):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="load-bearing-foundational-rights-casing",
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
        "- **`avoid-court-family`:** reject **court** / **courts** in institutional senses → prefer **forum** / **forums**, **forum family**, or **adjudicative body**.",
        "- **`load-bearing-rights-floor-casing`:** reject lowercase **rights floor**, **rights floors**, and **rights-floor** outside Markdown link targets and inline code → use **Rights Floor**, **Rights Floors**, or **Rights-Floor** for the named Chapter Ten layer.",
        "- **`load-bearing-foundational-rights-casing`:** reject **Foundational rights** / **foundational rights** outside Markdown link targets and inline code → use **Foundational Rights** when naming the Chapter Ten title or layer.",
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
    run_internal_regression_checks()

    root = pathlib.Path(args.root).resolve()
    scope = args.scope or binding_corpus_scope(root, include_support_docs=True)
    if args.scope is None and (root / "architecture_primer.md").is_file():
        scope.append("architecture_primer.md")

    findings: list[Finding] = []
    for rel_path in scope:
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
        findings.extend(scan_avoid_court_family(rel_path, text))
        findings.extend(scan_load_bearing_capitalization(rel_path, text))
        if rel_path in _BREACH_FAMILY_SCOPE:
            findings.extend(scan_avoid_breach_family(rel_path, text))

    report = report_markdown(args.date, scope, findings)
    if args.write_evidence:
        evidence_path = write_evidence(root, args.date, report)
        print(f"Wrote evidence report: {evidence_path}")
    else:
        print(report)

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
