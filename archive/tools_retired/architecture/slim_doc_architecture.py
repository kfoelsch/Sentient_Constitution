#!/usr/bin/env python3
"""One-shot slim-down for doc_architecture.md (2026-06-15 migration)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "doc_architecture.md"
ARCHIVE_DIR = ROOT / "archive" / "doc_architecture_decision_log"
DECISION_LOG = ARCHIVE_DIR / "DEC_WIDGET_AND_NAV_DECISIONS_2026-04-16_2026-06-15.md"
OVERLAP_ARCHIVE = ARCHIVE_DIR / "OVERLAP_THEME_TABLE_ARCHIVED_2026-06-15.md"

RULE_TABLE = """### Editorial rule registry (machine-checkable)

Full rule IDs, audit targets, and legacy `doc_architecture` rule numbers live in [tools/architecture/rule_registry.json](tools/architecture/rule_registry.json). Lexical guardrails live in [tools/architecture/lexical_guardrails.json](tools/architecture/lexical_guardrails.json). Audit catalog: [implementation/AUTOMATED_REFERENCE_CHECKING.md](implementation/AUTOMATED_REFERENCE_CHECKING.md).

| Rule ID | Summary | Gate |
|---------|---------|------|
| NAV-TRACE-08–10 | Trace placement and contents | `make ch9-trace-audit`, `make trace-routing-prose-audit` |
| NAV-DEC-12 | D/E/C widget discipline | `make ch5-dec-widget-audit`, `make nav-widget-spacer-audit` |
| NAV-DEC-CH1-ORDER | Chapter One functional D/E/C order | `make ch1-dec-order-audit` |
| LINK-IN-PARA-14 | Load-bearing in-paragraph links | `make in-paragraph-link-audit` |
| CH5-GRAVITY | Chapter Five admission / de-bundling | `make ch5-definitions-gravity-audit` |
| CH5-ORDER-01 | Chapter Five editorial order | `make ch5-cluster-order-audit`, `make ch5-entry-format-audit` |
| CH5-SINGLE-DEF | One visible definition per term | `make ch5-single-definition-audit` |
| LEX-GUARDRAILS | Vocabulary and capitalization | `make lexical-vocabulary-audit` |
| GLOSS-SUBARTICLE | Chapter Ten `*In plain terms:*` on subarticles | `make subarticle-gloss-audit` |
| OWNER-SINGLE-HOME | Competing O/E/C gloss heuristics | `make owner-discipline-audit` |
| REF-ARTICLES | Article titles and Roman numerals | `make reference-audit` |
| ROUTER-CJS21 | Cross-implementation routing | `make router-bidirectional-audit` |

Historical navigation and D/E/C rollout rationale: [archive/doc_architecture_decision_log/DEC_WIDGET_AND_NAV_DECISIONS_2026-04-16_2026-06-15.md](archive/doc_architecture_decision_log/DEC_WIDGET_AND_NAV_DECISIONS_2026-04-16_2026-06-15.md).

### Plain-Language Vocabulary Guardrails

Use for preambles, chapter openings, reader guidance, and summaries. Capitalize **Wellbeing**, **Safety**, **Truth**, **Rights Floor**, and **Foundational Rights** when they name constitutional layers; keep generic wellbeing, safety, truth, and bare `rights` lowercase unless in a formal title. Prefer everyday words when meaning is preserved; keep canonical defined terms where precision requires them.

Full substitution tables, ambiguous-label rules, co-gloss registry, and plain-language gloss placement are in [tools/architecture/lexical_guardrails.json](tools/architecture/lexical_guardrails.json). Enforcement: `make lexical-vocabulary-audit` (blocking), `make plain-language-audit` (advisory), `make subarticle-gloss-audit` (advisory).

Same forum / court / tribunal vocabulary exceptions as [.cursor/rules/sentient-constitution.mdc](.cursor/rules/sentient-constitution.mdc).
"""

ARTICLE_POINTER = """### Articles I–XXV (core rights; implementation files implement detail)

Articles **I–XXV** are **present** in [core_10-10_rights_part_a.md](core_10-10_rights_part_a.md) through [core_10-10_rights_part_d.md](core_10-10_rights_part_d.md). Chapter Ten uses a **planet-first** presentation in **Parts A–D**.

- **Article titles and Roman numerals:** `make reference-audit` / Chapter Ten part files.
- **Implementation routing:** [corpus_joint_structure.md](corpus_joint_structure.md) **CJS-2.1** (*Topic router (stable IDs)*); `make router-bidirectional-audit`.
- **Generated stable-ID index (optional):** [doc_architecture/generated/stable_id_index.md](doc_architecture/generated/stable_id_index.md) via `make architecture-index`.

Do not maintain a second hand-edited article-to-implementation map here; the corpus and router own that routing.

When tightening obligations, edit **Sentient Constitution Chapter Ten** for the right-level statement and implementation corpus files for operational checklists, preserving **single home** discipline in **section 4**.
"""

SECTION_13_SLIM = """## 13. Redundancy, overlap, and attack surface

The **pinned** definitions hierarchy and editing rules are in **section 4**. This section states discipline only; detailed pass logs and overlap theme tables are archived.

**Chapter map:** fifteen Sentient Constitution chapters in numbered `core_*` files (inventory in [README.md](README.md)). Use **section 5** stable IDs when reconciling older notes.

**Definitions-first sweep (center-out):** work from Chapter Five definitions outward per **section 9**. For each touched definition: (a) correct §1/§2/§3 home, (b) O/E/C aligned with Chapters Two through Four, (c) institutional mechanics relocated with pointers. Per-term workflow: locate canonical paragraph → grep across Sentient Constitution / CJS / CS → classify hits as pointer, harmless recap, or competing definition → resolve at the canonical home.

**Why overlap matters:** parallel rules drift and enable forum shopping. Treat unintended duplication as an integrity issue.

**Allowed vs risky redundancy**

- **Safe:** one canonical exposition plus pointers elsewhere (CJS-5 cluster, short recap, explicit deferral).
- **Risky:** two full definitions of the same obligation with different thresholds without declared precedence.

**Precedence (reinforce when editing)**

1. **Sentient Constitution values and rights** beat conflicting operational wording.
2. **Stricter / more specific** applicable rule wins where the corpus already says so.
3. **CS-3** is canonical for Type C–S labels; Sentient Constitution and CJS reference Type N via CS-3.

**Ongoing discipline:** identify single home before adding rules; grep theme across Sentient Constitution, CJS, and CS on major edits; optional `*Corpus alignment:*` footers per **section 17**.

**Historical material:** pass logs in [archive/doc_architecture_section_13_pass_logs_ARCHIVED_2026-04-29.md](archive/doc_architecture_section_13_pass_logs_ARCHIVED_2026-04-29.md); overlap theme table in [archive/doc_architecture_decision_log/OVERLAP_THEME_TABLE_ARCHIVED_2026-06-15.md](archive/doc_architecture_decision_log/OVERLAP_THEME_TABLE_ARCHIVED_2026-06-15.md); adoption document control in [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md) **section 17**.
"""

RETIRED_SECTIONS = """## 14. Retired sections (14–19)

Sections **14–19** previously held the living worklist, external-framework crosswalk, assurance notes, document control, embedding boundary, and rights-layer bridge. That material now lives in:

- Worklist: [archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md) (**section 14**)
- Adopter-facing appendix (**sections 15–19**): [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md)

**Section 17 quick pointer (document control):** authoritative corpus = constitutional and implementation files named in [README.md](README.md); this file remains the core structure map; historical edition and custody narrative is in the archived appendix.

Numbering is preserved so existing references to **sections 14–19** still land on the right concept.
"""


def extract_block(text: str, start_marker: str, end_marker: str) -> str:
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    return text[start:end].strip()


def main() -> None:
    text = DOC.read_text(encoding="utf-8")
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    decision = extract_block(
        text,
        "**Architecture note (2026-04-16, D/E/C split):**",
        "### Plain-Language Vocabulary Guardrails",
    )
    overlap = extract_block(
        text,
        "**Overlap zones (baseline map — revise when you edit)**",
        "**Precedence (already in corpus; reinforce when editing)**",
    )
    DECISION_LOG.write_text(
        "# D/E/C and navigation decision log (archived)\n\n"
        "Moved from `doc_architecture.md` section 4 on 2026-06-15.\n\n"
        + decision
        + "\n",
        encoding="utf-8",
    )
    OVERLAP_ARCHIVE.write_text(
        "# Overlap theme table (archived)\n\n"
        "Moved from `doc_architecture.md` section 13 on 2026-06-15.\n\n"
        + overlap
        + "\n",
        encoding="utf-8",
    )

    # Remove architecture notes before Plain-Language section
    text = re.sub(
        r"\n\*\*Architecture note \(2026-04-16, D/E/C split\):\*\*.*?(?=### Plain-Language Vocabulary Guardrails)",
        "\n",
        text,
        flags=re.S,
    )
    # Remove Ch5 architecture notes under Order and alphabetization
    text = re.sub(
        r"\n\*\*Architecture note \(2026-04-27, Ch 5 §2/§3 section dividers\):\*\*.*?(?=### Single home rule)",
        "\n",
        text,
        flags=re.S,
    )

    # Replace Reader-Guidance block through end of rule 14 regression note
    text = re.sub(
        r"### Reader-Guidance Discipline \(Navigation Load Control\).*?"
        r"`python3 tools/in_paragraph_link_audit.py --strict-companion` when tightening companion pointer-first discipline\.\n",
        RULE_TABLE + "\n",
        text,
        flags=re.S,
    )

    # Replace Plain-Language section (old long form) if still present
    text = re.sub(
        r"### Plain-Language Vocabulary Guardrails\n\nUse this rule for preambles.*?`make regression-full`\. A subarticle-level gate.*?\n",
        "",
        text,
        flags=re.S,
    )

    # Replace Articles I-XXV narrative block
    text = re.sub(
        r"### Articles I–XXV \(core rights; implementation files implement detail\)\n\n.*?"
        r"When tightening obligations, edit \*\*Sentient Constitution Ch 9\*\* for the right-level statement.*?\n",
        ARTICLE_POINTER + "\n",
        text,
        flags=re.S,
    )

    # Replace section 13
    text = re.sub(
        r"## 13\. Redundancy, overlap, and attack surface\n\n.*?(?=---\n\n## 14\.)",
        SECTION_13_SLIM + "\n\n---\n\n",
        text,
        flags=re.S,
    )

    # Replace sections 14-19 with collapsed block
    text = re.sub(
        r"## 14\. Project completion checklist.*?(?=\*Last aligned with corpus filenames:)",
        RETIRED_SECTIONS + "\n\n---\n\n",
        text,
        flags=re.S,
    )

    # Fix section 2 ambiguous label pointer
    text = text.replace(
        "see *Ambiguous implementation labels* under *Plain-Language Vocabulary Guardrails*",
        "see [tools/architecture/lexical_guardrails.json](tools/architecture/lexical_guardrails.json)",
    )

    DOC.write_text(text, encoding="utf-8")
    print(f"Slimmed {DOC} to {len(text.splitlines())} lines")


if __name__ == "__main__":
    main()
