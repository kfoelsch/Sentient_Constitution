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
_BREACH_FAMILY_SCOPE = frozenset({"core_08-08_standing_assessment.md", "core_09-09_standing_integration.md"})

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
    re.compile(r"supervise,\s+charter,\s+license,\s+or", re.IGNORECASE),
]

# Mechanical ``charter`` → ``constitutional`` passes can leave ``this constitutional.`` or ``the constitutional requires``; catch known bad compounds.
# Normative corpus uses **sentients** for bearers of standing/agency; avoid **person** / **persons**, **people**, and the split phrase **people and agents**.
_PEOPLE_AND_AGENTS = re.compile(r"\bpeople and agents\b", re.IGNORECASE)
_PEOPLE_STANDALONE = re.compile(r"(?<![A-Za-z0-9])people(?![A-Za-z0-9])", re.IGNORECASE)
_PERSON_STANDALONE = re.compile(
    r"(?<![A-Za-z0-9-])persons?(?:['’]s|['’])?(?![A-Za-z0-9-])",
    re.IGNORECASE,
)

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
_TRIBUNAL_FAMILY = re.compile(r"\btribunals?\b", re.IGNORECASE)
_TRIBUNAL_ALLOWED_EXTERNAL = re.compile(
    r"\b(external|historical|international|foreign|arbitral|competent external)\s+tribunals?\b",
    re.IGNORECASE,
)
_STANDING_CALCULUS = re.compile(r"\bstanding[- ]calculus\b", re.IGNORECASE)

_RIGHTS_FLOOR_CASING = re.compile(r"\b(?:rights floor|rights floors|rights-floor)\b")
_FOUNDATIONAL_RIGHTS_CASING = re.compile(r"\b(?:Foundational rights|foundational rights)\b")
_SHOULD_NOT_PROHIBITION = re.compile(r"\bshould\s+not\b", re.IGNORECASE)
_DEFINITION_MAP_LABEL = re.compile(r"\*\*Definition map\.\*\*|\bDefinition map\.", re.IGNORECASE)
_ROUTER_READ_LABEL = re.compile(r"^\*\*Router read:\*\*", re.IGNORECASE)
_IMPLEMENTATION_CORPUS_PREFIXES = (
    "corpus_institutions/",
    "corpus_joint_structure/",
    "corpus_forum/",
)

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
    """Reject standalone **person** / **persons**, **people**, and **people and agents**; prefer **sentients** in normative scoped text."""
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
        if (
            _PEOPLE_AND_AGENTS.search(check_line)
            or _PEOPLE_STANDALONE.search(check_line)
            or _PERSON_STANDALONE.search(check_line)
        ):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="prefer-sentients-not-person-people-phrasing",
                    text=raw.strip(),
                ),
            )

    return findings


def run_internal_regression_checks() -> None:
    """Fail closed if core lexical regexes stop catching known bad phrasing."""
    banned_word = "Peo" + "ple"
    sample = (
        "User agency and control\n\n"
        f"- OP-O: {banned_word} must have practical control over ranking and presentation "
        "when that control is appropriate, including chronological or lightly processed views where feasible.\n"
        "- OP-C: Systems must not misrepresent a person's real options.\n"
    )
    findings = scan_prefer_sentients_not_people_phrasing("internal-regression.md", sample)
    if len(findings) < 2:
        raise RuntimeError(
            "Internal regression failed: capitalized standalone 'People' or possessive 'person' was not flagged.",
        )
    tribunal_findings = scan_avoid_tribunal_family(
        "internal-regression.md",
        "The lead tribunal must publish reasons.\nExternal tribunals remain preserved.\n",
    )
    if len(tribunal_findings) != 1:
        raise RuntimeError(
            "Internal regression failed: internal 'tribunal' was not flagged or external tribunal exception broke.",
        )
    should_not_findings = scan_avoid_should_not_prohibitions(
        "internal-regression.md",
        "Technical forums should not become the routine merits forum.\n"
        "`should not` inside code is not prose.\n",
    )
    if len(should_not_findings) != 1:
        raise RuntimeError(
            "Internal regression failed: prose 'should not' prohibition was not flagged or code masking broke.",
        )
    standing_calculus_findings = scan_avoid_standing_calculus(
        "internal-regression.md",
        "Forums must not run standing calculus.\n"
        "Use standing-record classification under Chapter Eight instead.\n"
        "`standing calculus` inside backticks is documentation only.\n",
    )
    if len(standing_calculus_findings) != 1:
        raise RuntimeError(
            "Internal regression failed: 'standing calculus' was not flagged or backtick masking broke.",
        )


def scan_avoid_standing_calculus(rel_path: str, text: str) -> list[Finding]:
    """Reject undefined **standing calculus** jargon; prefer Chapter Eight standing-record classification wording."""
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if rel_path == "doc_architecture.md" and "`standing calculus" in raw:
            continue
        if rel_path == "doc_architecture.md" and "`standing-calculus" in raw:
            continue

        check_line = _mask_inline_code_and_link_targets(raw)
        if _STANDING_CALCULUS.search(check_line):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="avoid-standing-calculus",
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


def _mask_allowed_tribunal_spans(line: str) -> str:
    masked = line
    masked = _TRIBUNAL_ALLOWED_EXTERNAL.sub(lambda m: " " * len(m.group(0)), masked)
    return masked


def scan_avoid_tribunal_family(rel_path: str, text: str) -> list[Finding]:
    """Reject internal **tribunal** / **tribunals**; prefer **forum**, **bench**, **panel**, or **adjudicative body**."""
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if rel_path == "doc_architecture.md" and "`tribunal" in raw:
            continue

        check_line = _mask_allowed_tribunal_spans(_mask_inline_code_and_link_targets(raw))
        if _TRIBUNAL_FAMILY.search(check_line):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="avoid-tribunal-family",
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


def scan_avoid_should_not_prohibitions(rel_path: str, text: str) -> list[Finding]:
    """Reject **should not** prohibitions; use **must not** for binding negative constraints."""
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
        if _SHOULD_NOT_PROHIBITION.search(check_line):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="avoid-should-not-prohibitions",
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


def scan_avoid_definition_map_label(rel_path: str, text: str) -> list[Finding]:
    """Reject **Definition map.** meta-labels; integrate term relationships in plain prose."""
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if _DEFINITION_MAP_LABEL.search(raw):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="avoid-definition-map-label",
                    text=raw.strip(),
                ),
            )

    return findings


def scan_avoid_router_read_label(rel_path: str, text: str) -> list[Finding]:
    """Reject **Router read:** body labels; CJS-2.1 routing belongs in Trace bullets."""
    if not rel_path.startswith(_IMPLEMENTATION_CORPUS_PREFIXES):
        return []
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if _ROUTER_READ_LABEL.search(raw):
            findings.append(
                Finding(
                    file=rel_path,
                    line=idx,
                    rule="avoid-router-read-label",
                    text=raw.strip(),
                ),
            )

    return findings


def report_markdown(run_date: str, scope: list[str], findings: list[Finding]) -> str:
    lines: list[str] = [
        f"# Lexical vocabulary audit — {run_date}",
        "",
        "Rules:",
        "- **`forbidden-cloud`:** standalone **cloud** → use **info-sphere** (and related) terminology.",
        "- **`corpus-no-bare-charter`:** in scoped files, standalone **charter** → prefer **constitutional** / **this Constitution** for Corpus sense. **Allowed:** `corporate charter`, `treaty, compact, or charter`, `adoption, federation, or charter`, and the verb list `supervise, charter, or …`.",
        "- **`malformed-constitutional-*`:** reject **this constitutional.** / **implement this constitutional.** / **the constitutional requires** / **under the constitutional.** (line-end) / **with this constitutional when** / **constitutional-free**, and hyphen glitches **constitutional-valid**, **constitutional-bounded**, **constitutional-governed**, **constitutional-scaled**, **constitutional-compatible**, **constitutional-applicable**, **constitutional-material**, **constitutional-hook** (use *constitutionally …* or **this Constitution** / **constitutional hook** as appropriate).",
        "- **`prefer-sentients-not-person-people-phrasing`:** reject standalone **person** / **persons** (including possessives), **people**, and **people and agents** → use **sentient** / **sentients** (or another defined corpus term). Exceptions are preserved by boundary rules for compounds and lemmas such as **in-person**, **personal**, **personnel**, **persona**, **personalized**, and **non-personal data**.",
        "- **`avoid-accession-jargon`:** reject **accede**, **acceding**, and **accession** → prefer **join** / **joining** / **additional parties** adoption wording.",
        "- **`avoid-undefined-breach-family`:** reject standalone **breach** / **breaches** / **breached** / **breaching**, **duty breach**, and **duty-breaching** → prefer **violation**, **non-compliance**, **unmet duties**, or defined Chapter Eight typing (see `.cursor/rules/clarity.mdc`). *Currently enforced only on files in `_BREACH_FAMILY_SCOPE` inside `tools/lexical_vocabulary_audit.py`.*",
        "- **`avoid-minima`:** reject **minima** → prefer **requirements**, **floors**, **conditions**, or another context-specific term.",
        "- **`avoid-court-family`:** reject **court** / **courts** in institutional senses → prefer **forum** / **forums**, **forum family**, or **adjudicative body**.",
        "- **`avoid-tribunal-family`:** reject internal Chapter Eleven / forum-governance **tribunal** / **tribunals** → prefer **forum** / **forums**, **forum family**, **panel**, **bench**, or **adjudicative body**. **Allowed:** external or historical tribunal wording where source fidelity or external legal-order references require it.",
        "- **`avoid-standing-calculus`:** reject **standing calculus** / **standing-calculus** (undefined jargon) → prefer **standing-record classification under Chapter Eight**, **classify standing records** on the Contribution and Violation axes, or other explicit Chapter Eight wording.",
        "- **`load-bearing-rights-floor-casing`:** reject lowercase **rights floor**, **rights floors**, and **rights-floor** outside Markdown link targets and inline code → use **Rights Floor**, **Rights Floors**, or **Rights-Floor** for the named Chapter Six layer.",
        "- **`load-bearing-foundational-rights-casing`:** reject **Foundational rights** / **foundational rights** outside Markdown link targets and inline code → use **Foundational Rights** when naming the Chapter Six title or layer.",
        "- **`avoid-should-not-prohibitions`:** reject **should not** in corpus prose → use **must not** for binding negative constraints.",
        "- **`avoid-definition-map-label`:** reject **Definition map.** → integrate term relationships in plain prose; use *In plain terms* for reader orientation.",
        "- **`avoid-router-read-label`:** reject **Router read:** in implementation-corpus body prose → use `- Topic routing (primary owner):` or `- Topic routing (mandatory read-with):` bullets inside the Trace `<details>` block.",
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
        findings.extend(scan_avoid_tribunal_family(rel_path, text))
        findings.extend(scan_avoid_standing_calculus(rel_path, text))
        findings.extend(scan_load_bearing_capitalization(rel_path, text))
        findings.extend(scan_avoid_should_not_prohibitions(rel_path, text))
        findings.extend(scan_avoid_definition_map_label(rel_path, text))
        findings.extend(scan_avoid_router_read_label(rel_path, text))
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
