"""Attach Trace and D/E/C widgets to CJS Markdown sections.

The CJS folder is one level below the core files, so generated links use
``../core_*`` paths. The pass is intentionally conservative: it only inserts
widgets under headings that do not already have a local Trace or
Definitions/Evaluation/Compliance widget before their first prose block.

Run from the repository root:

    python3 tools/attach_cjs_widgets.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CJS_DIR = ROOT / "corpus_joint_structure"
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

CORE_READ_WITH = (
    "[Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) "
    "incorporation discipline and "
    "[Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) "
    "canonical definitions."
)
SHARED_CONTRACT = (
    "[CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) "
    "shared implementation-corpus contract"
)
TOPIC_ROUTER = (
    "[CJS-2.2](cjs_02_implementation_integration_map.md#cjs-22-topic-router-stable-ids) "
    "topic router"
)

DEFAULT_TERMS = [
    "Corpus",
    "Authority Stack and Internal Hierarchy",
    "Supremacy and Enforceability",
]

TERM_HINTS = {
    "adjudication": "Adjudication and Dispute Resolution",
    "adversarial": "Adversarial, Scaled, and Exploited Conditions",
    "alignment": "Incentive Alignment",
    "anti-capture": "System Capture",
    "audit": "Auditability",
    "auditability": "Auditability",
    "authority": "Authority Stack and Internal Hierarchy",
    "capture": "System Capture",
    "classification": "Classification-Scaled Governance",
    "coercion": "Coercion and Manipulation",
    "compliance": "Constitutional Constraint Violation",
    "contest": "Contestability",
    "dependency": "Dependency",
    "disclosure": "Transparency",
    "ecological": "Ecological Integrity",
    "emergency": "Emergency and Contingency",
    "enforceability": "Supremacy and Enforceability",
    "evidence": "Evidence Preservation",
    "failure": "Cascading Failure",
    "forum": "Adjudication and Dispute Resolution",
    "governance": "Governance",
    "harm": "Harm",
    "integrity": "Epistemic Integrity",
    "interoperability": "Interoperability",
    "intervention": "Oversight",
    "justification": "Accountability",
    "material": "Materiality Determination",
    "mechanism": "Incentive Alignment",
    "oversight": "Oversight",
    "participation": "Stakeholder Participation Weight",
    "procedure": "Procedural Fairness",
    "proportional": "Proportionality",
    "proxy": "Proxy Divergence",
    "reconstruct": "Auditability",
    "recusal": "Procedural Fairness",
    "remediation": "Redress and Remediation",
    "reversibility": "Reversibility",
    "risk": "Risk",
    "safety": "Safety (Constraint)",
    "secrecy": "Transparency",
    "standing": "Participant Standing",
    "supremacy": "Supremacy and Enforceability",
    "transparency": "Transparency",
    "trust": "Trust",
    "trustworthiness": "Trustworthiness",
    "truth": "Truth (Constitutional Constraint)",
    "verification": "Verifiability",
}

LABEL_HINTS = {
    "CJS-5C.3 and CJS-5C.4": ["Risk", "Truth (Constitutional Constraint)", "Transparency"],
    "CJS-5C.2": ["Accessibility", "Meaningful Agency", "Transparency"],
    "CJS-5C.4": ["Transparency", "Disclosure Sufficiency"],
    "CJS-5D.1": ["Dependency", "Risk"],
    "CJS-5E.1": ["Cascading Failure", "Safety (Constraint)"],
    "CJS-5D.2": ["Interoperability", "Dependency"],
    "CJS-5E.2": ["Oversight", "Proportionality", "Redress and Remediation"],
    "CJS-5B.2": ["Auditability", "Verifiability"],
    "CJS-5B.3": ["Transparency", "Auditability"],
    "CJS-5B.4": ["Verifiability", "Truth (Constitutional Constraint)"],
    "CJS-5E.3 and CJS-5D.3": ["Reversibility", "Risk"],
    "CJS-5E.4": ["Adversarial, Scaled, and Exploited Conditions", "Safety (Constraint)"],
    "CJS-5E.5 and CJS-5B.1": ["Reversibility", "Trustworthiness"],
    "CJS-5A.1 and CJS-5C.1": ["Governance", "Proportionality"],
    "CJS-5A.2 and CJS-5E.2": ["Oversight", "Redress and Remediation", "Proportionality"],
    "CJS-5A.3 and CJS-5B.1": ["Transparency", "Accountability"],
    "CJS-5A.4": ["Accountability", "Proportionality", "Necessity"],
    "CJS-5A.5": ["Transparency", "Procedural Fairness"],
    "CJS-5A.6": ["Procedural Fairness", "Adjudication and Dispute Resolution"],
}

TERM_ALIASES = {
    "Authority Stack": "Authority Stack and Internal Hierarchy",
    "Environmental Preconditions": "Environmental Preconditions",
    "Forum Family, Constitutional": "Constitutional Forum Family",
    "Forum Family, Environment": "Environment Forum Family",
    "Forum Family, Institutional": "Institutional Forum Family",
    "Forum Family, Integrity": "Integrity Forum Family",
    "Forum Family, Sentient": "Sentient Forum Family",
    "Forum Family, Technical": "Technical Forum Family",
    "Incentive Alignment": "Incentive Alignment",
    "Oversight": "Oversight",
    "Participant Standing": "Participant Standing",
    "Redress and Remediation": "Redress and Remediation",
    "Reversibility": "Reversibility",
    "Supremacy and Enforceability": "Supremacy and Enforceability",
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


def anchor_for_heading(text: str) -> str:
    label = re.sub(r"^#+\s*", "", text).strip().lower()
    label = re.sub(r"[^\w\s.-]", "", label)
    label = label.replace(".", "")
    label = re.sub(r"\s+", "-", label)
    return label


def split_sections(lines: list[str]) -> list[tuple[int, int, int]]:
    starts = [i for i, line in enumerate(lines) if re.match(r"^#{2,5}\s+", line)]
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
        if re.match(r"^#{2,5}\s+", lines[idx]):
            first_child = idx
            break
    window = "\n".join(lines[start + 1 : first_child])
    return TRACE_SUMMARY in window or DEC_SUMMARY in window or DEC_INLINE_PREFIX in window


def child_links(lines: list[str], start: int, end: int, level: int) -> list[str]:
    links = []
    for line in lines[start + 1 : end]:
        if re.match(rf"^#{{{level + 1}}}\s+", line):
            title = re.sub(r"^#+\s*", "", line).strip()
            links.append(f"[{title}](#{anchor_for_heading(line)})")
    return links[:6]


def sibling_summary(lines: list[str], start: int, end: int) -> str:
    level = heading_level(lines[start])
    children = child_links(lines, start, end, level)
    if children:
        rest = ""
        if len(children) == 6:
            rest = " and related local subsections"
        return "; ".join(children) + rest
    title = re.sub(r"^#+\s*", "", lines[start]).strip()
    return f"this section's local operational requirements for **{title}**"


def mentioned_links(section_text: str) -> list[str]:
    patterns = [
        r"\bCJS-\d+(?:\.\d+)?\b",
    ]
    out: list[str] = []
    seen: set[str] = set()
    for pattern in patterns:
        for match in re.findall(pattern, section_text):
            if match not in seen:
                seen.add(match)
                if match == "CJS-2.2":
                    out.append(
                        "[CJS-2.2](cjs_02_implementation_integration_map.md#cjs-22-topic-router-stable-ids)"
                    )
                elif match == "CJS-1.2":
                    out.append(SHARED_CONTRACT)
                else:
                    out.append(f"**{match}**")
    return out[:6]


def trace_block(lines: list[str], start: int, end: int, level: int) -> list[str]:
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


def inferred_terms(text: str) -> list[str]:
    terms: list[str] = []
    lower = text.lower()
    for label, mapped_terms in LABEL_HINTS.items():
        if label.lower() in lower:
            terms.extend(mapped_terms)
    for hint, term in TERM_HINTS.items():
        if hint in lower:
            terms.append(term)
    return terms


def concept_terms(lines: list[str], start: int, end: int) -> list[str]:
    text = "\n".join(lines[start:end])
    candidates = exact_term_matches(text) + inferred_terms(text)
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
    anchor = meta["anchor"]
    e = f"{meta['file']}{anchor}-e"
    c = f"{meta['file']}{anchor}-c"
    return f"- [{term}]({base}) · [O]({base}) · [E]({e}) · [C]({c})"


def dec_block(terms: list[str]) -> list[str]:
    if len(terms) == 1:
        term = terms[0]
        meta = DEFINITIONS[term]
        base = f"{meta['file']}{meta['anchor']}"
        return [
            f"{DEC_INLINE_PREFIX} [{term}]({base}) · [O]({base}) · "
            f"[E]({base}-e) · [C]({base}-c)",
            "",
        ]
    return ["<details>", DEC_SUMMARY, "", *[dec_row(term) for term in terms], "", "</details>", "", "<br>", ""]


def attach(path: Path) -> int:
    lines = path.read_text().splitlines()
    inserted = 0
    for start, end, level in reversed(split_sections(lines)):
        if local_widget_present(lines, start, end):
            continue
        widgets = trace_block(lines, start, end, level) + dec_block(concept_terms(lines, start, end))
        lines[start + 1 : start + 1] = widgets
        inserted += 1
    if inserted:
        path.write_text("\n".join(lines) + "\n")
    return inserted


def main() -> None:
    total = 0
    for path in sorted(CJS_DIR.glob("*.md")):
        count = attach(path)
        total += count
        print(f"{path.relative_to(ROOT)}: inserted widgets under {count} headings")
    print(f"Total inserted: {total}")


if __name__ == "__main__":
    main()
