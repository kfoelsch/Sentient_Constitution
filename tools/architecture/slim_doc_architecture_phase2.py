#!/usr/bin/env python3
"""Second-pass slim-down for doc_architecture.md (2026-06-15)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "doc_architecture.md"

SECTION_1A_SHORT = """## 1A. Canonical Filename Convention

- Use `snake_case` canonical filenames (no spaces; no `%20` links).
- Numbered core pattern: `core_<start>-<end>_<short_owner_label>.md` (zero-padded chapters; repeat chapter number for single-chapter files).
- Full inventory: [README.md](README.md). Chapter One retains numeric headings (`CHAPTER 00`, `CHAPTER 01`) as the instrument-opening exception.

## 1B. Rename Readiness Gate (Conservative)

Filename renames require a dedicated pass: reference audit, same-change link updates, dated evidence under `evidence/<date>/`, compatibility decision, and edition/custody record. Until the gate passes, candidate names stay planning-only.
"""

SECTION_2_FOOTER_SHORT = """**Footer policy:** corpus files use navigation footers per class (see `make footer-audit`). Template: one `---`, then `**Next file:**` / optional `**Previous file:**`; optional `*Corpus alignment:*` above the block.

**Authority stack (quick reference):** (1) numbered `core_*` constitutional source; (2) incorporated implementation files within adoption scope; (3) this map and process docs unless explicitly incorporated; (4) Sentient Constitution meaning controls operational layers.
"""

SECTION_4_TRIM_START = """## 4. Project-wide definitions protocol (pinned)

This subsection **pins** how definitions work across the corpus. Machine-checkable rules: [tools/architecture/rule_registry.json](tools/architecture/rule_registry.json). Audit catalog: [implementation/AUTOMATED_REFERENCE_CHECKING.md](implementation/AUTOMATED_REFERENCE_CHECKING.md).

### What counts as a “definition” here

- **Hard definitions:** Sentient Constitution Ch 2–4 (`core_02-04_definition_mechanics.md`) for O/E/C structure, integrity, burden, traceability, and verification; Chapter Five §1–§3 for canonical terms (single-home rule below).
- **Values language:** Chapter One, with vocabulary anchor + cluster index at end under **Reference: Chapter Five vocabulary anchor and cluster index**.
- **Contribution / standing:** Chapters Six and Seven (**verified** inputs only); Chapter Nine owns forum process for allegations — not standing calculus.
- **Rights:** Chapter Ten (Articles I–XXV); implementation files cite articles, they do not invent parallel rights.
- **Cross-domain integrity routing:** **CJS-4.3** and **CJS-5**; Chapter Fifteen is the incorporation bridge.
- **Operational taxonomies:** **CS-3**, **CS-4**, **CS-5** and named protocols in `corpus_systems.md`.
- **Joint operational definitions** (cross-implementation interface terms): `corpus_joint_structure.md` only — route via **CJS-2.1** (*Topic router*).

### CJS operational-definition owner rule

Use **CJS** when a term exists only at a cross-implementation interface, regulates how **CJS / CS / CI / CF** interact, and is operational rather than constitutional. Place reusable joint terms in **CJS-5** clusters; **CJS-4** interlocks point to **CJS-5** and the primary owner. Escalate to Chapter Five when constitutional meaning is at stake; relocate to a single implementation file when only one file needs the term.

### Chapter Five admission gate

Keep only constitutional concept + O/E/C boundary in Chapter Five. Do not embed institutional architecture, appointment mechanics, or governance workflow — cite owner homes instead. **`make ch5-definitions-gravity-audit`** (blocking).

### Citing corpus_systems.md from Sentient Constitution

Cite as **[corpus_systems.md](corpus_systems.md), CS-3 — Information types and handling** (same pattern for CS-4, CS-5, protocols). Bare **CS-3** labels are not Sentient Constitution chapter numbers.

"""

SECTION_4_TRIM_END = """
### Order and alphabetization (Chapter Five)

Editorial discipline for maintainers only — not operative Chapter Five text. §1/§2 A–Z; §3 cluster bodies A–Z after fixed §3.1–§3.2; one visible definition per term; trace separators and compound-heading alignment enforced by `make ch5-entry-format-audit`, `make ch5-alphabetical-directory-audit`, `make ch5-cluster-order-audit`, and `make ch5-single-definition-audit`. Historical separator examples: [archive/doc_architecture_decision_log/DEC_WIDGET_AND_NAV_DECISIONS_2026-04-16_2026-06-15.md](archive/doc_architecture_decision_log/DEC_WIDGET_AND_NAV_DECISIONS_2026-04-16_2026-06-15.md).

### Single home rule

For drift-prone concepts: identify the canonical paragraph (**section 2** owner table; **section 13** sweep discipline); elsewhere use pointers only unless amending the canonical home on purpose.

### Precedence (if two passages disagree)

1. Sentient Constitution values and rights over conflicting operational wording.
2. Ch 2–3 over implementation files for term meaning and satisfaction.
3. CS-3/4/5 over Sentient Constitution / CJS for Type/Class/steward assignment.
4. Stricter applicable rule wins where the corpus already says so.

### Adding or changing a term (workflow)

1. Cross-cutting terms → one Chapter Five §1/§2/§3 home aligned with Ch 2–4.
2. Operational-only labels → implementation file or CJS with pointer to Ch 2–3 if needed.
3. Grep competing definitional paragraphs; replace with cross-references.
4. Update **section 2** or this section for new owner classes.
5. Update Chapter One vocabulary anchor / cluster index when traceability terms change.

---
"""

SECTION_5_SHORT = """## 5. Stable IDs — Sentient Constitution

| ID | Status | Content (summary) |
|----|--------|-------------------|
| Sentient Constitution Ch 1–15 | **Present** | Numbered `core_*` files per [README.md](README.md) — values (Ch 1), definition mechanics (Ch 2–4), definitions (Ch 5), standing (Ch 6–7), misconduct (Ch 8), forums (Ch 9), rights Articles I–XXV (Ch 10), governance (Ch 11), amendment block (Ch 12–14 in `core_12-14_amendment.md`), incorporation bridge (Ch 15) |

**Integration note:** [corpus_joint_structure.md](corpus_joint_structure.md) is incorporated by reference as authoritative implementation text. **CJS-4** and **CJS-5** are not Sentient Constitution chapter numbers.

**Authority boundary:** This file is the navigation map; corpus normative text controls on conflict.

### Stable IDs — CJS operational cluster file

| Stable ID | Heading in CJS file |
|-----------|-------------------|
| **CJS-5.2–CJS-5.7** | Authority, constraint, secrecy, and procedure terms |
| **CJS-5.8–CJS-5.11** | Evidence, audit, and claim-integrity terms |
| **CJS-5.12–CJS-5.15** | Participation, comprehension, and disclosure terms |
| **CJS-5.16–CJS-5.18** | Dependency, exit, and lifecycle-integrity terms |
| **CJS-5.19–CJS-5.23** | Failure, robustness, intervention, and correction terms |

### Articles I–XXV (core rights; implementation files implement detail)

Articles **I–XXV** are **present** in [core_10-10_rights_part_a.md](core_10-10_rights_part_a.md) through [core_10-10_rights_part_d.md](core_10-10_rights_part_d.md).

- **Article titles and Roman numerals:** `make reference-audit` / Chapter Ten part files.
- **Implementation routing:** [corpus_joint_structure.md](corpus_joint_structure.md) **CJS-2.1**; `make router-bidirectional-audit`.
- **Generated index:** [doc_architecture/generated/stable_id_index.md](doc_architecture/generated/stable_id_index.md) via `make architecture-index`.

Do not maintain a second hand-edited article-to-implementation map here.

---
"""

SECTION_6_SHORT = """## 6. Stable IDs — corpus_systems.md (CS implementation file)

| Stable ID | Heading in implementation file |
|-----------|------------------------|
| **SYS-CS-3** | CS-3 — Information types and handling |
| **SYS-CS-4** | CS-4 — System classification and handling |
| **SYS-CS-5** | CS-5 — Critical system stewardship |
| **SYS-PROTO-A** | Protocol A: System Design, Testing, Verification, and Deployment |
| **SYS-PROTO-B** | Protocol B: System Comprehensibility and Complexity Stewardship |
| **SYS-PROTO-S4** | Protocol S4 — Adaptive Sustainability and Ecosystem Resilience |
| **SYS-PROTO-S5** | Protocol S5 — Resource Allocation and Funding Stewardship |

[corpus_systems.md](corpus_systems.md) is a compatibility entrypoint; substantive text lives in `corpus_systems/` subfiles (**section 11**). CJS cluster IDs: **section 5**.

---
"""

SECTION_8_SHORT = """## 8. Cross-reference convention

- **Rights:** `Sentient Constitution Ch 10 Art III` or spelled-out article cite.
- **Standing:** `Sentient Constitution Ch 6` / Ch 7; forums in Ch 9 for allegations.
- **Governance / amendment:** Ch 11–14 in `core_12-14_amendment.md` where applicable.
- **Incorporation:** Ch 15 + applicable CJS family.
- **CJS clusters:** cite specific **CJS-5.*n*** heading; router: **CJS-2.1**.
- **CS:** `CS SYS-CS-4` or `[corpus_systems.md](corpus_systems.md), CS-4`.
- **CI / CF:** `corpus_institutions.md` **CI-*n***; `corpus_forum.md` **CF-*n***.

---
"""

SECTION_12_SHORT = """## 12. Known cleanup notes (implementation files and CJS clusters)

- Prefer **CS-3** over legacy “Chapter Two (Information Types…)” wording inside CS text.
- **CJS-4** and **CJS-5** are the live citation grammar; retired implementation-label files are gone (guarded by `make primitive-retirement-audit`).
- Route cross-implementation choreography to `corpus_joint_structure.md`; local doctrine to CS / CI / CF per **section 4**.

---
"""


def main() -> None:
    text = DOC.read_text(encoding="utf-8")

    text = re.sub(
        r"## 1A\. Canonical Filename Convention\n\n.*?(?=## 1B\. Rename Readiness Gate)",
        SECTION_1A_SHORT + "\n",
        text,
        flags=re.S,
    )

    text = re.sub(
        r"\*\*Abbreviations:\*\*.*?(?=---\n\n## 3\. Boundary rules)",
        SECTION_2_FOOTER_SHORT + "\n\n---\n\n",
        text,
        flags=re.S,
    )

    # Keep rule table block; replace surrounding section 4 prose
    rule_table_match = re.search(
        r"(### Editorial rule registry \(machine-checkable\).*?Historical navigation and D/E/C rollout rationale:.*?\n\n)"
        r"(### Plain-Language Vocabulary Guardrails\n\n.*?\n\n\n\n)"
        r"(### Implementation-file source hierarchy block\n\n.*?"
        r"### Adding or changing a term \(workflow\)\n\n.*?"
        r"### Vocabulary anchor vs cluster index \(Chapter One\)\n\n.*?"
        r"### Quick index \(non-exhaustive\)\n\n.*?\n\n---\n\n)",
        text,
        flags=re.S,
    )
    if rule_table_match:
        middle = rule_table_match.group(1) + rule_table_match.group(2)
        text = text[: rule_table_match.start()] + SECTION_4_TRIM_START + middle + SECTION_4_TRIM_END + text[rule_table_match.end() :]
    else:
        print("WARN: section 4 trim pattern not found")

    text = re.sub(
        r"## 5\. Stable IDs — Sentient Constitution\n\n.*?(?=## 6\. Stable IDs — corpus_systems)",
        SECTION_5_SHORT + "\n",
        text,
        flags=re.S,
    )

    text = re.sub(
        r"## 6\. Stable IDs — corpus_systems\.md \(CS implementation file\)\n\n.*?(?=## 7\. Dependency graph)",
        SECTION_6_SHORT + "\n",
        text,
        flags=re.S,
    )

    text = re.sub(
        r"## 8\. Cross-reference convention\n\n.*?(?=## 9\. Dependency order for editing)",
        SECTION_8_SHORT + "\n",
        text,
        flags=re.S,
    )

    text = re.sub(
        r"## 11\. Systems file split \(executed\)\n\n.*?(?=## 13\. Redundancy)",
        SECTION_12_SHORT + "\n",
        text,
        flags=re.S,
    )

    text = re.sub(r"\n---\n\n---\n\n## 14\.", "\n\n---\n\n## 14.", text)

    DOC.write_text(text, encoding="utf-8")
    print(f"Phase-2 slimmed {DOC} to {len(text.splitlines())} lines")


if __name__ == "__main__":
    main()
