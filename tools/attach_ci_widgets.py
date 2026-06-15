"""Attach Trace and D/E/C widgets to CI Markdown sections.

The CI folder is one level below the core files, so generated definition links
use ``../core_*`` paths. The pass is conservative: it only inserts widgets
under CI headings that do not already have a local Trace or
Definitions/Evaluation/Compliance widget before their first child heading.

Run from the repository root:

    python3 tools/attach_ci_widgets.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CI_DIR = ROOT / "corpus_institutions"
REGISTRY_PATH = ROOT / "ai_corpus" / "indexes" / "definition_registry.json"

TRACE_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">'
    "Trace</span></strong></summary>"
)
DEC_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">'
    "Definitions · Evaluation · Compliance</span></strong></summary>"
)
DEC_INLINE_PREFIX = (
    '<strong><span style="color: #2563eb;">Definition:</span></strong>'
)

SHARED_CONTRACT = (
    "[CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md"
    "#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract"
)
TOPIC_ROUTER = (
    "[CJS-2.2](../corpus_joint_structure/cjs_02_implementation_integration_map.md"
    "#cjs-22-topic-router-stable-ids) topic router"
)
CORE_READ_WITH = (
    "[Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) "
    "incorporation discipline; "
    "[Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) "
    "canonical definitions; and "
    "[Chapter Ten](../core_10-10_rights_part_a.md#chapter-ten-foundational-rights) rights architecture where rights interfaces are invoked."
)

DEFAULT_TERMS = [
    "Governance",
    "Accountability",
    "Procedural Fairness",
]

TERM_HINTS = {
    "accessibility": "Accessibility",
    "accountability": "Accountability",
    "addiction": "Stakeholder Emergency and Contingency",
    "anti-capture": "System Capture",
    "anti-corruption": "System Capture",
    "anti-domination": "Coercion and Manipulation",
    "appointment": "Governance",
    "assurance": "Oversight",
    "audit": "Auditability",
    "authority": "Authority Stack and Internal Hierarchy",
    "billing": "Transparency",
    "capture": "System Capture",
    "care": "Family and Care Relationships",
    "classification": "Classification-Scaled Governance",
    "commons": "Collective Organization",
    "compliance": "Constitutional Constraint Violation",
    "concentration": "Concentration Threshold",
    "conflict": "System Capture",
    "consultation": "Stakeholder Participation Weight",
    "contest": "Contestability",
    "continuity": "Emergency and Contingency",
    "cooperative": "Collective Organization",
    "coordination": "Governance",
    "corruption": "System Capture",
    "delegation": "Authority Stack and Internal Hierarchy",
    "dependency": "Dependency",
    "disability": "Accessibility",
    "disclosure": "Transparency",
    "dissolution": "Accountability",
    "ecological": "Ecological Integrity",
    "emergency": "Emergency and Contingency",
    "end-of-life": "Dignity and Equal Moral Standing",
    "epidemic": "Emergency and Contingency",
    "evidence": "Evidence Preservation",
    "failure": "Collective Accountability Failure",
    "fee": "Avoidable Burden",
    "fees": "Avoidable Burden",
    "fraud": "Truth (Constitutional Constraint)",
    "governance": "Governance",
    "indigenous": "Indigenous Continuity",
    "innovation": "Innovation Reward and Anti-Enclosure",
    "integrity": "Epistemic Integrity",
    "labor": "Compensation, Organization, Safe Conditions, Leisure, and Creative Work",
    "markets": "Voluntary Exchange",
    "memorial": "Dignity and Equal Moral Standing",
    "neurodiversity": "Accessibility",
    "oversight": "Oversight",
    "participation": "Stakeholder Participation Weight",
    "procedure": "Procedural Fairness",
    "proportionality": "Proportionality",
    "publication": "Transparency",
    "recurring": "Transparency",
    "redress": "Redress and Remediation",
    "removal": "Accountability",
    "respite": "Family and Care Relationships",
    "revenue": "Avoidable Burden",
    "review": "Review and Correction Duty",
    "risk": "Risk",
    "sanctions": "Accountability",
    "scientific": "Epistemic Integrity",
    "self-service": "Accessibility",
    "stakeholder": "Stakeholder",
    "stewardship": "Strategic Stewardship Obligation",
    "transitional": "Reversibility",
    "transparency": "Transparency",
    "trauma": "Procedural Fairness",
    "vulnerable": "Protected Characteristics",
}

LABEL_HINTS = {
    "CI-1": ["Corpus", "Authority Stack and Internal Hierarchy", "Supremacy and Enforceability"],
    "CI-2": ["Governance", "Authority Stack and Internal Hierarchy", "System Capture"],
    "CI-3": ["Authority Stack and Internal Hierarchy", "Governance", "Risk"],
    "CI-4": ["Governance", "Accountability", "Procedural Fairness"],
    "CI-5": ["System Capture", "Incentive Alignment", "Accountability"],
    "CI-6": ["Procedural Fairness", "Contestability", "Adjudication and Dispute Resolution"],
    "CI-7": ["Oversight", "Auditability", "Evidence Preservation"],
    "CI-8": ["Governance", "Emergency and Contingency", "Accountability"],
    "CI-9": ["Classification-Scaled Governance", "Proportionality", "Risk"],
    "CI-10": ["Avoidable Burden", "Transparency", "Voluntary Exchange"],
    "CI-11": ["Strategic Stewardship Obligation", "Incentive Alignment", "Risk"],
    "CI-12": ["Transparency", "Accessibility", "Stakeholder Participation Weight"],
    "CI-13": ["Collective Accountability Failure", "Accountability", "Redress and Remediation"],
    "CI-14": ["Reversibility", "Emergency and Contingency", "Accountability"],
    "CI-15": ["Protected Commercial Sexual Services Status and Article X-C Circumvention", "Coercion and Manipulation", "Protected Characteristics"],
    "CI-16": ["Innovation Reward and Anti-Enclosure", "Transparency", "Incentive Alignment"],
    "CI-17": ["Epistemic Integrity", "Truth (Constitutional Constraint)", "Verifiability"],
    "CI-18": ["Assembly", "Collective Organization", "Meaningful Agency"],
    "CI-19": ["Dignity and Equal Moral Standing", "Privacy (Informational)", "Family and Care Relationships"],
    "CI-20": ["Family and Care Relationships", "Dependency", "Compensation, Organization, Safe Conditions, Leisure, and Creative Work"],
    "CI-21": ["Coercion and Manipulation", "Meaningful Agency", "Procedural Fairness"],
    "CI-22": ["Collective Organization", "Governance", "Incentive Alignment"],
    "CI-23": ["Indigenous Continuity", "Natural Systems Standing", "Stakeholder Participation Weight"],
    "CI-24": ["Accessibility", "Procedural Fairness", "Protected Characteristics"],
    "CI-25": ["Emergency and Contingency", "Wellbeing", "Stakeholder"],
    "CI-26": ["Corpus", "Auditability", "Verifiability"],
}

TERM_ALIASES = {
    "Authority Stack": "Authority Stack and Internal Hierarchy",
}


def load_definitions() -> dict[str, dict[str, str]]:
    data = json.loads(REGISTRY_PATH.read_text())
    by_term: dict[str, dict[str, str]] = {}
    for item in data["definitions"]:
        by_term[item["term"]] = {
            "file": "../" + item["source_file"],
            "anchor": item["anchor"],
        }
    for alias, canonical in TERM_ALIASES.items():
        if canonical in by_term:
            by_term[alias] = by_term[canonical]
    return by_term


DEFINITIONS = load_definitions()


def heading_level(line: str) -> int:
    return len(line) - len(line.lstrip("#"))


def is_ci_heading(line: str) -> bool:
    return bool(re.match(r"^#{2,5}\s+CI-\d+(?:\.\d+)*", line))


def anchor_for_heading(text: str) -> str:
    label = re.sub(r"^#+\s*", "", text).strip().lower()
    label = re.sub(r"[^\w\s.-]", "", label)
    label = label.replace(".", "")
    label = re.sub(r"\s+", "-", label)
    return label


def split_sections(lines: list[str]) -> list[tuple[int, int, int]]:
    starts = [i for i, line in enumerate(lines) if is_ci_heading(line)]
    sections = []
    for pos, start in enumerate(starts):
        level = heading_level(lines[start])
        end = len(lines)
        for nxt in starts[pos + 1 :]:
            if heading_level(lines[nxt]) <= level:
                end = nxt
                break
        sections.append((start, end, level))
    return sections


def local_widget_present(lines: list[str], start: int, end: int) -> bool:
    first_child = end
    for idx in range(start + 1, end):
        if is_ci_heading(lines[idx]):
            first_child = idx
            break
    window = "\n".join(lines[start + 1 : first_child])
    return TRACE_SUMMARY in window or DEC_SUMMARY in window or DEC_INLINE_PREFIX in window


def child_links(lines: list[str], start: int, end: int, level: int) -> list[str]:
    links = []
    for line in lines[start + 1 : end]:
        if is_ci_heading(line) and heading_level(line) == level + 1:
            title = re.sub(r"^#+\s*", "", line).strip()
            links.append(f"[{title}](#{anchor_for_heading(line)})")
    return links[:6]


def sibling_summary(lines: list[str], start: int, end: int) -> str:
    children = child_links(lines, start, end, heading_level(lines[start]))
    if children:
        rest = " and related local subsections" if len(children) == 6 else ""
        return "; ".join(children) + rest
    title = re.sub(r"^#+\s*", "", lines[start]).strip()
    return f"this section's local operational requirements for **{title}**"


def mentioned_links(section_text: str) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    patterns = (
        r"\bCI-\d+(?:\.\d+)*\b",
        r"\bCJS-\d+[A-Z]?(?:\.\d+)?\b",
        r"\bINST-PROTO-\d+\b",
    )
    for pattern in patterns:
        for match in re.findall(pattern, section_text):
            if match in seen:
                continue
            seen.add(match)
            if match == "CJS-1.2":
                out.append(SHARED_CONTRACT)
            elif match == "CJS-2.2":
                out.append(TOPIC_ROUTER)
            else:
                out.append(f"**{match}**")
    return out[:7]


def trace_block(lines: list[str], start: int, end: int) -> list[str]:
    section_text = "\n".join(lines[start:end])
    read_with = mentioned_links(section_text)
    read_with_text = "; ".join(read_with) if read_with else f"{SHARED_CONTRACT}; {TOPIC_ROUTER}"
    return [
        "<details>",
        TRACE_SUMMARY,
        "",
        f"- Upstream: {SHARED_CONTRACT}; {TOPIC_ROUTER}; {CORE_READ_WITH}",
        f"- Downstream: {sibling_summary(lines, start, end)}.",
        f"- Read with: {read_with_text}.",
        "",
        "</details>",
        "",
    ]


def exact_term_matches(text: str) -> list[str]:
    found = []
    for term in sorted(DEFINITIONS, key=len, reverse=True):
        if len(term) < 5:
            continue
        pattern = r"(?<![A-Za-z])" + re.escape(term) + r"(?![A-Za-z])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            found.append(term)
    return found


def ci_label(line: str) -> str | None:
    match = re.search(r"\bCI-\d+(?:\.\d+)*\b", line)
    return match.group(0) if match else None


def concept_terms(lines: list[str], start: int, end: int) -> list[str]:
    text = "\n".join(lines[start:end])
    candidates = exact_term_matches(text)
    lower = text.lower()
    label = ci_label(lines[start])
    if label:
        parts = label.split(".")
        while parts:
            key = ".".join(parts)
            if key in LABEL_HINTS:
                candidates.extend(LABEL_HINTS[key])
            parts.pop()
    for hint, term in TERM_HINTS.items():
        if hint in lower:
            candidates.append(term)
    out: list[str] = []
    seen: set[str] = set()
    for term in candidates:
        canonical = TERM_ALIASES.get(term, term)
        if canonical in DEFINITIONS and canonical not in seen:
            seen.add(canonical)
            out.append(canonical)
    if not out:
        out = [term for term in DEFAULT_TERMS if term in DEFINITIONS]
    return out[:7]


def dec_row(term: str) -> str:
    meta = DEFINITIONS[term]
    base = f"{meta['file']}{meta['anchor']}"
    return f"- [{term}]({base}) · [O]({base}) · [E]({base}-e) · [C]({base}-c)"


def dec_block(terms: list[str]) -> list[str]:
    if len(terms) == 1:
        term = terms[0]
        meta = DEFINITIONS[term]
        base = f"{meta['file']}{meta['anchor']}"
        return [
            f"{DEC_INLINE_PREFIX} [{term}]({base}) · [O]({base}) · [E]({base}-e) · [C]({base}-c)",
            "",
        ]
    return ["<details>", DEC_SUMMARY, "", *[dec_row(term) for term in terms], "", "</details>", "", "<br>", ""]


def attach(path: Path) -> int:
    lines = path.read_text().splitlines()
    inserted = 0
    for start, end, _level in reversed(split_sections(lines)):
        if local_widget_present(lines, start, end):
            continue
        widgets = trace_block(lines, start, end) + dec_block(concept_terms(lines, start, end))
        lines[start + 1 : start + 1] = widgets
        inserted += 1
    if inserted:
        path.write_text("\n".join(lines) + "\n")
    return inserted


def main() -> None:
    total = 0
    for path in sorted(CI_DIR.glob("ci_*.md")):
        count = attach(path)
        total += count
        print(f"{path.relative_to(ROOT)}: inserted widgets under {count} headings")
    print(f"Total inserted: {total}")


if __name__ == "__main__":
    main()
