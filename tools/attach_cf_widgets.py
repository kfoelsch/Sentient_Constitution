"""Attach Trace and D/E/C widgets to CF Markdown sections.

The CF folder is one level below the core files, so generated links use
``../core_*`` paths. The pass is conservative: it only inserts widgets under
headings that do not already have a local Trace or Definitions/Evaluation/
Compliance widget before their first child heading.

Run from the repository root:

    python3 tools/attach_cf_widgets.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CF_DIR = ROOT / "corpus_forum"
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
    "[CJS-2.1](../corpus_joint_structure/cjs_02_implementation_integration_map.md"
    "#cjs-21-topic-router-stable-ids) topic router"
)
CORE_READ_WITH = (
    "[Chapter Nine](../core_09-09_forum.md#chapter-nine-forums-and-jurisdiction) "
    "forum-family routing; "
    "[Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) "
    "incorporation discipline; and "
    "[Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) "
    "canonical definitions."
)

DEFAULT_TERMS = [
    "Adjudication and Dispute Resolution",
    "Procedural Fairness",
    "Contestability",
]

TERM_HINTS = {
    "accessibility": "Accessibility",
    "adjudication": "Adjudication and Dispute Resolution",
    "alignment": "Incentive Alignment",
    "appeal": "Procedural Fairness",
    "audit": "Auditability",
    "backlog": "Procedural Fairness",
    "capture": "System Capture",
    "certification": "Accountability",
    "chain of custody": "Evidence Preservation",
    "chamber": "Forum Family, Technical",
    "contest": "Contestability",
    "continuity": "Emergency and Contingency",
    "disclosure": "Transparency",
    "evidence": "Evidence Preservation",
    "exhaustion": "Procedural Fairness",
    "forensic": "Evidence Preservation",
    "forum": "Adjudication and Dispute Resolution",
    "independence": "Procedural Fairness",
    "intake": "Accessibility",
    "investigative": "Oversight",
    "jurisdiction": "Adjudication and Dispute Resolution",
    "panel": "Procedural Fairness",
    "performance": "Accountability",
    "publication": "Transparency",
    "recusal": "Procedural Fairness",
    "record": "Unified Record",
    "redress": "Redress and Remediation",
    "remediation": "Redress and Remediation",
    "review": "Contestability",
    "routing": "Adjudication and Dispute Resolution",
    "specialist": "Forum Family, Technical",
    "technical": "Forum Family, Technical",
    "timeliness": "Procedural Fairness",
    "transfer": "Adjudication and Dispute Resolution",
    "transparency": "Transparency",
}

LABEL_HINTS = {
    "CF-1": ["Adjudication and Dispute Resolution", "Authority Stack and Internal Hierarchy"],
    "CF-3": ["Forum Family, Constitutional", "Forum Family, Institutional", "Forum Family, Technical"],
    "CF-4": ["Procedural Fairness", "System Capture", "Accountability"],
    "CF-5": ["Adjudication and Dispute Resolution", "Accessibility", "Contestability"],
    "CF-6": ["Contestability", "Procedural Fairness", "Redress and Remediation"],
    "CF-7": ["System Capture", "Incentive Alignment", "Oversight"],
    "CF-8": ["Evidence Preservation", "Verifiability", "Auditability"],
    "CF-9": ["Oversight", "Evidence Preservation", "Accountability"],
    "CF-10": ["Forum Family, Technical", "Epistemic Integrity", "Verifiability"],
    "CF-11": ["Accessibility", "Procedural Fairness", "Accountability"],
    "CF-12": ["Emergency and Contingency", "Evidence Preservation", "Safety (Constraint)"],
    "CF-13": ["Primary-Stakes Routing", "System Capture", "Contestability"],
    "CF-14": ["Emergency and Contingency", "Irreversible Harm", "Contestability"],
    "CF-15": ["Unified Record", "Evidence Preservation", "Transparency"],
    "CF-16": ["Governance", "Accountability", "Procedural Fairness"],
}

TERM_ALIASES = {
    "Authority Stack": "Authority Stack and Internal Hierarchy",
    "Forum Family, Constitutional": "Forum Family, Constitutional",
    "Forum Family, Environment": "Forum Family, Environment",
    "Forum Family, Institutional": "Forum Family, Institutional",
    "Forum Family, Integrity": "Forum Family, Integrity",
    "Forum Family, Sentient": "Forum Family, Sentient",
    "Forum Family, Technical": "Forum Family, Technical",
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
    children = child_links(lines, start, end, heading_level(lines[start]))
    if children:
        rest = " and related local subsections" if len(children) == 6 else ""
        return "; ".join(children) + rest
    title = re.sub(r"^#+\s*", "", lines[start]).strip()
    return f"this section's local operational requirements for **{title}**"


def mentioned_links(section_text: str) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for pattern in (r"\bCF-\d+(?:\.\d+)*(?:[A-Z])?\b", r"\bCJS-\d+(?:\.\d+)?\b"):
        for match in re.findall(pattern, section_text):
            if match in seen:
                continue
            seen.add(match)
            if match == "CJS-1.2":
                out.append(SHARED_CONTRACT)
            elif match == "CJS-2.1":
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


def concept_terms(lines: list[str], start: int, end: int) -> list[str]:
    text = "\n".join(lines[start:end])
    candidates = exact_term_matches(text)
    lower = text.lower()
    for label, terms in LABEL_HINTS.items():
        if label.lower() in lower:
            candidates.extend(terms)
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
    for path in sorted(CF_DIR.glob("*.md")):
        count = attach(path)
        total += count
        print(f"{path.relative_to(ROOT)}: inserted widgets under {count} headings")
    print(f"Total inserted: {total}")


if __name__ == "__main__":
    main()
