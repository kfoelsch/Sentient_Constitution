#!/usr/bin/env python3
"""
Split former Chapter Two into Chapters Two–Four; renumber former Ch3–Ch8 to Ch5–Ch10.
Run from repo root: python3 implementation/migrate_constitution_chapters.py
"""
from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
path = ROOT / "core_constitution.md"
text = path.read_text(encoding="utf-8")
lines = text.splitlines(True)

start = next(i for i, L in enumerate(lines) if L.startswith("## CHAPTER TWO:"))
end = next(i for i, L in enumerate(lines) if L.startswith("## CHAPTER THREE: FOUNDATIONAL DEFINITIONS"))
chunk = "".join(lines[start:end])

# --- Remove Part A / Part B markers ---
chunk = chunk.replace(
    "**Part A — Definition structure, integrity, and observable non-compliance (sections 2–4).**\n\n",
    "",
)
chunk = chunk.replace(
    "**Part B — Burden, tracing, observability, security limits, and practical verification (sections 5–10).**\n\n",
    "",
)

# --- Chapter Two header + purpose ---
old_ch2_open = """## CHAPTER TWO: DEFINITION REQUIREMENTS
### 1. Purpose and Role
This chapter defines semantic, evaluative, and compliance requirements, including how such requirements must be interpreted and applied.

It establishes the conditions under which definitions are considered validly satisfied.

Those conditions include requirements for evaluation scope, evidence, tracing, observability, and verification as necessary to preserve epistemic integrity and binding effect.

Enforceability in the constitutional sense is further specified in Chapter Three Interdependent Definitions (Supremacy and Enforceability (Constitutional)).

This chapter does not define:
"""
new_ch2_open = """## CHAPTER TWO: DEFINITION STRUCTURE AND COMPONENT REQUIREMENTS
### 1. Purpose and Role
This chapter defines how definitions must be decomposed into Ontological (O), Evaluative (E), and Compliance (C) components and how those components must remain internally aligned within each definition.

Anti-evasion interpretation and observable non-compliance are governed by **Chapter Three**. Burden of proof, definition traceability, observability, security-constrained verification, and verification accessibility are governed by **Chapter Four**.

Terminology and definitional refinements for evaluative and compliance work appear in **Chapter Five** Interdependent and Clustered Definitions.

Enforceability in the constitutional sense is further specified in Chapter Five Interdependent Definitions (Supremacy and Enforceability (Constitutional)).

This chapter does not define:
"""
if old_ch2_open not in chunk:
    raise SystemExit("Expected Chapter Two opening not found; abort.")
chunk = chunk.replace(old_ch2_open, new_ch2_open, 1)
chunk = chunk.replace(
    "All such mechanisms must be defined in subsequent chapters and must operate in full compliance with the semantic, evaluative, and compliance constraints established herein.",
    "All such mechanisms must be defined in subsequent chapters and must operate in full compliance with the structural constraints established herein.",
)

chunk = chunk.replace(
    "All uses of “reasonably foreseeable” in this chapter are governed exclusively by the Foreseeability definitions in Chapter Three, section 2 — Clustered Definitions. They must be explicitly traceable where invoked.",
    "All uses of “reasonably foreseeable” in **Chapters Two through Four** are governed exclusively by the Foreseeability definitions in Chapter Five, section 2 — Clustered Definitions. They must be explicitly traceable where invoked.",
)
chunk = chunk.replace(
    "All evaluation requirements defined in this chapter must be enforced through the Compliance Burden of Proof Standard (section 5 of this chapter). They must be applied consistently with all applicable Interdependent Definitions (Chapter Three, section 1 — Interdependent Definitions).",
    "All evaluation requirements defined in **Chapters Two and Three** must be enforced through the Compliance Burden of Proof Standard (**Chapter Four, section 1 — Compliance Burden of Proof Standard**). They must be applied consistently with all applicable Interdependent Definitions (Chapter Five, section 1 — Interdependent Definitions).",
)
chunk = chunk.replace(
    "as defined in Chapter Three, section 2 — Clustered Definitions (Foreseeability)",
    "as defined in Chapter Five, section 2 — Clustered Definitions (Foreseeability)",
)

# --- Split Chapter Three (integrity + observable) ---
split_marker = "### 3. Definition Integrity and Anti-Evasion Constraints\n"
if split_marker not in chunk:
    raise SystemExit("Split marker for old section 3 not found.")
idx = chunk.index(split_marker)
ch2_only = chunk[:idx]
ch3_on = chunk[idx:]
ch3_on = ch3_on.replace(
    "This section does not define evaluation standards, evidence sufficiency, or burden of proof, which are governed exclusively by Sections 2 and 5.",
    "This section does not define evaluation standards, evidence sufficiency, or burden of proof, which are governed exclusively by **Chapter Two, section 2** and **Chapter Four, section 1**.",
)
ch3_on = ch3_on.replace("### 3. Definition Integrity", "### 1. Definition Integrity", 1)
ch3_on = ch3_on.replace(
    "### 4. Non-Compliance from Observable System Behavior",
    "### 2. Non-Compliance from Observable System Behavior",
    1,
)
for n in range(7, 0, -1):
    ch3_on = ch3_on.replace(f"#### 4.{n} ", f"#### 2.{n} ")
ch3_on = (
    "## CHAPTER THREE: DEFINITION INTEGRITY AND OBSERVABLE NON-COMPLIANCE\n\n" + ch3_on
)
chunk = ch2_only + ch3_on

# --- Split Chapter Four (verification pipeline) ---
split2 = "### 5. Compliance Burden of Proof Standard\n"
if split2 not in chunk:
    raise SystemExit("Split marker for old section 5 not found.")
idx2 = chunk.index(split2)
head = chunk[:idx2]
tail = chunk[idx2:]
tail = tail.replace(
    "### 5. Compliance Burden of Proof Standard\n",
    "## CHAPTER FOUR: BURDEN OF PROOF, TRACEABILITY, AND VERIFICATION\n\n### 1. Compliance Burden of Proof Standard\n",
    1,
)
for n in range(6, -1, -1):
    tail = tail.replace(f"#### 5.{n} ", f"#### 1.{n} ")

old_10 = """#### 1.0 Non-overlapping roles (sections 5–9)
Sections 5–9 implement one pipeline; **6.1** states that failure in any of sections 6–9 fails the whole. To limit redundancy and editorial drift, each section’s **primary** job—what **neighboring** sections do not already do—is:

- **Section 5:** **Who must prove compliance** and **what suffices** as evidence (joint O/E/C satisfaction under real conditions, independence where reasonably achievable, scaling, disqualifying evidence, uncertainty defaults). It does **not** specify the trace **artifact** (section 6) or required **instrumentation and access** (section 7).
- **Section 6:** The **structured trace**: explicit mapping from each O/E/C component (and invoked Interdependent Definitions) to observable behavior and effects. It does **not** allocate burden (section 5), supply observability **capability** (section 7), or authorize security **exceptions** (section 8).
- **Section 7:** **Observability enablers**—instrumentation and access so section 6’s mappings can be examined under required conditions. Design-driven opacity is a compliance problem here, not a burden rule (section 5) and not a security carve-out (section 8).
- **Section 8:** **Justified limits** on the manner, scope, timing, or accessibility of disclosure and verification; **pretextual** security claims cannot nullify tracing or independent validation. It does **not** define general evidence sufficiency (section 5) or substitute crypto for sections 6–9 (**8.1**).
- **Section 9:** **Practical achievability** for appropriately authorized or affected parties—cost, delay, complexity, and structural dependence must not make independent verification **practically** illusory. Constraints here remain subject to section 8. It does **not** restate burden allocation (section 5).
"""
new_10 = """#### 1.0 Non-overlapping roles (sections 1–5)
Sections **1** through **5** of this chapter implement one pipeline; **2.1** states that failure in any of sections **2** through **5** fails the whole. To limit redundancy and editorial drift, each section’s **primary** job—what **neighboring** sections do not already do—is:

- **Section 1:** **Who must prove compliance** and **what suffices** as evidence (joint O/E/C satisfaction under real conditions, independence where reasonably achievable, scaling, disqualifying evidence, uncertainty defaults). It does **not** specify the trace **artifact** (section 2) or required **instrumentation and access** (section 3).
- **Section 2:** The **structured trace**: explicit mapping from each O/E/C component (and invoked Interdependent Definitions) to observable behavior and effects. It does **not** allocate burden (section 1), supply observability **capability** (section 3), or authorize security **exceptions** (section 4).
- **Section 3:** **Observability enablers**—instrumentation and access so section 2’s mappings can be examined under required conditions. Design-driven opacity is a compliance problem here, not a burden rule (section 1) and not a security carve-out (section 4).
- **Section 4:** **Justified limits** on the manner, scope, timing, or accessibility of disclosure and verification; **pretextual** security claims cannot nullify tracing or independent validation. It does **not** define general evidence sufficiency (section 1) or substitute crypto for sections **2** through **5** (**4.1**).
- **Section 5:** **Practical achievability** for appropriately authorized or affected parties—cost, delay, complexity, and structural dependence must not make independent verification **practically** illusory. Constraints here remain subject to section **4**. It does **not** restate burden allocation (section **1**).
"""
if old_10 not in tail:
    raise SystemExit("1.0 non-overlapping block not found.")
tail = tail.replace(old_10, new_10, 1)

tail = tail.replace("### 6. Definition Traceability Requirement\n", "### 2. Definition Traceability Requirement\n", 1)
for n in range(6, 0, -1):
    tail = tail.replace(f"#### 6.{n} ", f"#### 2.{n} ")

tail = tail.replace(
    "#### 2.1 Integrated requirement scope (sections 6–9)\nSections 6–9 define a single integrated requirement; failure in any section means failure of the entire observability and verification system.\n",
    "#### 2.1 Integrated requirement scope (sections 2–5)\nSections 2–5 define a single integrated requirement; failure in any section means failure of the entire observability and verification system.\n",
    1,
)

tail = tail.replace(
    "Systems must demonstrate tracing from definition to observable system behavior and effects (direct, indirect, delayed, aggregated). Each definition component must be independently validatable through observations that appropriately authorized or affected parties can independently reproduce. That validation must be consistent with the Compliance Burden of Proof Standard.",
    "Systems must demonstrate tracing from definition to observable system behavior and effects (direct, indirect, delayed, aggregated). Each definition component must be independently validatable through observations that appropriately authorized or affected parties can independently reproduce. That validation must be consistent with the Compliance Burden of Proof Standard (**Chapter Four, section 1**).",
    1,
)

tail = tail.replace(
    "- evaluated in full compliance with sections 3 and 4 of this chapter (Definition Integrity and Anti-Evasion Constraints; Non-Compliance from Observable System Behavior).\n",
    "- evaluated in full compliance with **Chapter Three, sections 1 and 2** (Definition Integrity and Anti-Evasion Constraints; Non-Compliance from Observable System Behavior).\n",
    1,
)

tail = tail.replace(
    "All tracing mappings and their associated verification methods must satisfy the Compliance Burden of Proof Standard defined in section 5 of this chapter. They must be supported by observable, verifiable evidence.\n",
    "All tracing mappings and their associated verification methods must satisfy the Compliance Burden of Proof Standard defined in **section 1** of this chapter. They must be supported by observable, verifiable evidence.\n",
    1,
)

tail = tail.replace(
    "### 7. Observability of Traceability Requirement\n",
    "### 3. Observability of Traceability Requirement\n",
    1,
)
tail = tail.replace(
    "Those capabilities must enable full satisfaction of Definition Traceability requirements (section 6 of this chapter).\n",
    "Those capabilities must enable full satisfaction of Definition Traceability requirements (**section 2** of this chapter).\n",
    1,
)

tail = tail.replace(
    "### 8. Security-Constrained Observability and Verification Rule\n",
    "### 4. Security-Constrained Observability and Verification Rule\n",
    1,
)
tail = tail.replace("#### 8.1 ", "#### 4.1 ", 1)

tail = tail.replace(
    "- **Non-substitution:** Cryptographic controls **do not** satisfy, and **must not** be invoked to replace, **sections 6 through 9** of this chapter. For **materially relevant** compliance facts, **observability**, **definition traceability**, **independent verification**, and **challenge rights** must remain achievable. That achievement must use **qualified** pathways under **section 8** (including **security-constrained** verification). It must also use **corpus_primitives.md** **PRIM9–PRIM11** and **Constitutional Systems**, **Chapter S1 — Information Types and Handling**. Pathways must **not** rely on **permanent** concealment of compliance-relevant evidence. They must **not** rest on **pretextual** claims that encryption makes verification impossible where safer pathways are **reasonably achievable**.\n",
    "- **Non-substitution:** Cryptographic controls **do not** satisfy, and **must not** be invoked to replace, **sections 2 through 5** of this chapter. For **materially relevant** compliance facts, **observability**, **definition traceability**, **independent verification**, and **challenge rights** must remain achievable. That achievement must use **qualified** pathways under **section 4** (including **security-constrained** verification). It must also use **corpus_primitives.md** **PRIM9–PRIM11** and **Constitutional Systems**, **Chapter S1 — Information Types and Handling**. Pathways must **not** rely on **permanent** concealment of compliance-relevant evidence. They must **not** rest on **pretextual** claims that encryption makes verification impossible where safer pathways are **reasonably achievable**.\n",
    1,
)
tail = tail.replace(
    "without defeating **section 8** justification rules",
    "without defeating **section 4** justification rules",
    1,
)
tail = tail.replace(
    "Those requirements are consistent with **Article IX-A** and **Chapter Two** tracing.\n",
    "Those requirements are consistent with **Article IX-A** and **Chapter Four** tracing.\n",
    1,
)

tail = tail.replace(
    "### 9. Verification Accessibility and Feasibility Constraint\n",
    "### 5. Verification Accessibility and Feasibility Constraint\n",
    1,
)
tail = tail.replace(
    "Any constraints on verification imposed for security, safety, or operational reasons must comply with section 8 of this chapter (Security-Constrained Observability and Verification Rule). They must comply with **8.1** (*Cryptographic protection, credentials, and verification*) where cryptographic controls apply. Such constraints must **not** reduce verification below a level sufficient to maintain epistemic integrity and independent validation.\n",
    "Any constraints on verification imposed for security, safety, or operational reasons must comply with **section 4** of this chapter (Security-Constrained Observability and Verification Rule). They must comply with **4.1** (*Cryptographic protection, credentials, and verification*) where cryptographic controls apply. Such constraints must **not** reduce verification below a level sufficient to maintain epistemic integrity and independent validation.\n",
    1,
)

tail = tail.replace(
    "### 10. Compliance and Standing Alignment Pointer\n",
    "### 6. Compliance and Standing Alignment Pointer\n",
    1,
)
tail = tail.replace(
    "That model is defined in **Chapter Four — Compliance, Violation, and Standing Model**.\n",
    "That model is defined in **Chapter Six — Compliance, Violation, and Standing Model**.\n",
    1,
)

tail = tail.replace(
    "- remain consistent with sections 3 and 4 of this chapter. Where constitutional values or constraints interact or conflict in the same evaluation, verification must also remain consistent with Chapter One (Interaction and Conflict Resolution).\n",
    "- remain consistent with **Chapter Three, sections 1 and 2**. Where constitutional values or constraints interact or conflict in the same evaluation, verification must also remain consistent with Chapter One (Interaction and Conflict Resolution).\n",
    1,
)

tail = tail.replace(
    "Failure to satisfy any required definition or definition component invalidates all dependent compliance claims. Any constraints on evidence generation, disclosure, or verification must comply with section 8 of this chapter (Security-Constrained Observability and Verification Rule). They must comply with **8.1** where cryptographic controls apply.\n",
    "Failure to satisfy any required definition or definition component invalidates all dependent compliance claims. Any constraints on evidence generation, disclosure, or verification must comply with **section 4** of this chapter (Security-Constrained Observability and Verification Rule). They must comply with **4.1** where cryptographic controls apply.\n",
    1,
)

tail = tail.replace(
    "  - Outcomes must be assessed under reasonably foreseeable conditions as defined in Chapter Three, section 2 — Clustered Definitions (Foreseeability).\n",
    "  - Outcomes must be assessed under reasonably foreseeable conditions as defined in Chapter Five, section 2 — Clustered Definitions (Foreseeability).\n",
    1,
)

tail = tail.replace(
    "That standard is consistent with **Truth (Constitutional Constraint)**, **Epistemic Integrity** (Chapter Three), and this section. This does not require laboratory science for every decision. It does require **proportional** openness to **disconfirmation** and **independent** validation where this chapter and Chapter Three require verification.\n",
    "That standard is consistent with **Truth (Constitutional Constraint)**, **Epistemic Integrity** (Chapter Five), and this section. This does not require laboratory science for every decision. It does require **proportional** openness to **disconfirmation** and **independent** validation where this chapter and Chapter Five require verification.\n",
    1,
)

chunk = head + tail

# Reassemble file (preserve blank line before Foundational Definitions)
new_text = (
    "".join(lines[:start])
    + chunk
    + "\n## CHAPTER FIVE: FOUNDATIONAL DEFINITIONS\n"
    + "".join(lines[end + 1 :])
)

# --- Rename downstream ## headers (order: avoid collision) ---
new_text = new_text.replace(
    "## CHAPTER EIGHT: META-PRIMITIVES (INCORPORATION BRIDGE)",
    "## CHAPTER TEN: META-PRIMITIVES (INCORPORATION BRIDGE)",
    1,
)
new_text = new_text.replace(
    "## CHAPTER SEVEN: CONSTITUTIONAL CHANGE, NON-REGRESSION, AND EXPANSION OF PROTECTION",
    "## CHAPTER NINE: CONSTITUTIONAL CHANGE, NON-REGRESSION, AND EXPANSION OF PROTECTION",
    1,
)
new_text = new_text.replace(
    "## CHAPTER SIX: GOVERNANCE LEGITIMACY, AUTHORIZATION, AND STEWARDSHIP",
    "## CHAPTER EIGHT: GOVERNANCE LEGITIMACY, AUTHORIZATION, AND STEWARDSHIP",
    1,
)
new_text = new_text.replace(
    "## CHAPTER FIVE: FOUNDATIONAL RIGHTS",
    "## CHAPTER SEVEN: FOUNDATIONAL RIGHTS",
    1,
)
new_text = new_text.replace(
    "## CHAPTER FOUR: COMPLIANCE, VIOLATION, AND STANDING MODEL",
    "## CHAPTER SIX: COMPLIANCE, VIOLATION, AND STANDING MODEL",
    1,
)

# --- Foundational Definitions through EOF: bump prose chapter numbers ---
fd_mark = "## CHAPTER FIVE: FOUNDATIONAL DEFINITIONS"
ix = new_text.index(fd_mark)
pre_fd = new_text[:ix]
post_fd = new_text[ix:]


_PROTECT_TOKENS = (
    ("<<<PRIM14>>>", "Primitive Chapters One through Four"),
    ("<<<PRIM4>>>", "Primitive Chapter Four"),
    ("<<<PRIM1>>>", "Primitive Chapter One"),
)


def bump_line(line: str) -> str:
    if line.startswith("## CHAPTER "):
        return line
    for tok, s in _PROTECT_TOKENS:
        line = line.replace(s, tok)
    line = line.replace("Chapters Four through Eight", "Chapters Six through Ten")
    line = line.replace("Chapters One through Eight", "Chapters One through Ten")
    line = line.replace("Chapter Eight", "Chapter Ten")
    line = line.replace("Chapter Seven", "Chapter Nine")
    line = line.replace("Chapter Six", "Chapter Eight")
    line = line.replace("Chapter Five", "Chapter Seven")
    line = line.replace("Chapter Four", "Chapter Six")
    line = line.replace("Chapter Three", "Chapter Five")
    for tok, s in _PROTECT_TOKENS:
        line = line.replace(tok, s)
    return line


post_lines = post_fd.splitlines(True)
out_post = [post_lines[0]] + [bump_line(L) for L in post_lines[1:]]
new_text = pre_fd + "".join(out_post)

# --- Pre-Foundational fixes (Chapter One + new Ch2–4) ---
pre = new_text[: new_text.index(fd_mark)]

replacements_pre = [
    (
        "as interpreted through Chapters One through Three and rights guarantees in Chapter Five.",
        "as interpreted through Chapters One through Five and rights guarantees in Chapter Seven.",
    ),
    (
        "All terms and constraints in Chapter One are defined and governed by Chapter Two and Three.\n",
        "All terms and constraints in Chapter One are defined and governed by **Chapters Two through Five**.\n",
    ),
    (
        "No interpretation of Chapter One is valid outside the definitions and evaluation constraints established in Chapter Two and Three.\n",
        "No interpretation of Chapter One is valid outside the definitions and evaluation constraints established in **Chapters Two through Five**.\n",
    ),
    (
        "Where ambiguity exists in Chapter One, interpretation must default to the strictest reading consistent with Chapter Three definitions. That reading must also align with evaluation constraints in Chapters Two and Three.\n",
        "Where ambiguity exists in Chapter One, interpretation must default to the strictest reading consistent with **Chapter Five** definitions. That reading must also align with evaluation constraints in **Chapters Two through Four**.\n",
    ),
    (
        "Wellbeing is defined in Chapter Three Interdependent Definitions (Wellbeing).\n",
        "Wellbeing is defined in Chapter Five Interdependent Definitions (Wellbeing).\n",
    ),
    (
        "Wellbeing must be interpreted across direct, indirect, delayed, cumulative, and cross-system effects under Chapter Two evaluative and tracing requirements.\n",
        "Wellbeing must be interpreted across direct, indirect, delayed, cumulative, and cross-system effects under **Chapters Two through Four** evaluative and tracing requirements.\n",
    ),
    (
        "Its definitional, evaluative, and compliance requirements are governed by Chapter Two and Chapter Three Interdependent and Clustered Definitions.\n",
        "Its definitional, evaluative, and compliance requirements are governed by **Chapters Two through Five** Interdependent and Clustered Definitions.\n",
        2,
    ),
    (
        "Compliance state, violation typing, and related determinations for Safety and for Truth are governed by **Chapter Four**, read together with Chapters Two and Three.\n",
        "Compliance state, violation typing, and related determinations for Safety and for Truth are governed by **Chapter Six**, read together with **Chapters Two through Five**.\n",
    ),
    (
        "- **independent scrutiny** proportionate to stakes under **Chapter Two** and **Chapter Three** (*Epistemic Integrity*; *Truth (Constitutional Constraint)*)\n",
        "- **independent scrutiny** proportionate to stakes under **Chapter Four** and **Chapter Five** (*Epistemic Integrity*; *Truth (Constitutional Constraint)*)\n",
    ),
    (
        "Domain-appropriate rigor and **Classification-Scaled Governance** (Chapter Three) govern how formality scales with impact and dependency.\n",
        "Domain-appropriate rigor and **Classification-Scaled Governance** (Chapter Five) govern how formality scales with impact and dependency.\n",
    ),
    (
        "Trust is a constitutional coordination condition grounded in truth and demonstrated trustworthiness over time, as defined in Chapter Three (Trust; Trustworthiness).\n",
        "Trust is a constitutional coordination condition grounded in truth and demonstrated trustworthiness over time, as defined in Chapter Five (Trust; Trustworthiness).\n",
    ),
    (
        "Feasibility claims that limit agency must be demonstrable under Chapter Two burden and tracing requirements. They must also be consistent with Chapter Three definitions (including Feasibility, Necessity, Proportionality, and Harm Minimization (Tradeoff Selection)).\n",
        "Feasibility claims that limit agency must be demonstrable under **Chapter Four** burden and tracing requirements. They must also be consistent with **Chapter Five** definitions (including Feasibility, Necessity, Proportionality, and Harm Minimization (Tradeoff Selection)).\n",
    ),
    (
        "Correction must follow Chapter Two tracing and Chapter Three proxy-related definitions. It must include documented escalation and review.\n",
        "Correction must follow **Chapter Four** tracing and **Chapter Five** proxy-related definitions. It must include documented escalation and review.\n",
    ),
    (
        "**Authorized roles**, **competency development**, and **paths into material responsibility** for stewards and operators appear in **Chapter Six, section 5 — Authorized Roles, Competency Development, and Contribution**.\n",
        "**Authorized roles**, **competency development**, and **paths into material responsibility** for stewards and operators appear in **Chapter Eight, section 5 — Authorized Roles, Competency Development, and Contribution**.\n",
    ),
    (
        "Those pathways must support **Meaningful Agency** (Chapter Three).\n",
        "Those pathways must support **Meaningful Agency** (Chapter Five).\n",
    ),
    (
        "They must be treated as escalation conditions under Chapter Two and Chapter Three.\n",
        "They must be treated as escalation conditions under **Chapters Two through Five**.\n",
    ),
    (
        "### Reference: Chapter Three vocabulary anchor and cluster index\n",
        "### Reference: Chapter Five vocabulary anchor and cluster index\n",
    ),
    (
        "Map this chapter to these Chapter Three Interdependent Definitions where applicable:\n",
        "Map this chapter to these Chapter Five Interdependent Definitions where applicable:\n",
    ),
    (
        "- Core wellbeing and agency terms (Chapter Three), including:\n",
        "- Core wellbeing and agency terms (Chapter Five), including:\n",
    ),
    (
        "- Materiality and system terms (Chapter Three), including:\n",
        "- Materiality and system terms (Chapter Five), including:\n",
    ),
    (
        "- Evaluation and failure terms (Chapter Three), including:\n",
        "- Evaluation and failure terms (Chapter Five), including:\n",
    ),
    (
        "- Transparency, fairness, and corpus terms (Chapter Three), including:\n",
        "- Transparency, fairness, and corpus terms (Chapter Five), including:\n",
    ),
    (
        "- Governance, stakeholders, and oversight (Chapter Three), including:\n",
        "- Governance, stakeholders, and oversight (Chapter Five), including:\n",
    ),
    (
        "- Redress, boundaries, governance, and standing (Chapter Three), including:\n",
        "- Redress, boundaries, governance, and standing (Chapter Five), including:\n",
    ),
    (
        "- Cooperative interaction, fairness, and ecological standing (Chapter Three), including:\n",
        "- Cooperative interaction, fairness, and ecological standing (Chapter Five), including:\n",
    ),
    (
        "- Fairness, emergency, and sustainability terms (Chapter Three), including:\n",
        "- Fairness, emergency, and sustainability terms (Chapter Five), including:\n",
    ),
    (
        "- Supremacy, adjudication, reporting, and collective accountability (Chapter Three), including:\n",
        "- Supremacy, adjudication, reporting, and collective accountability (Chapter Five), including:\n",
    ),
    (
        "Section 6 interaction rules (including proportionality, necessity, and harm minimization) apply through these Interdependent Definitions and the rest of Chapter Three.\n",
        "Section 6 interaction rules (including proportionality, necessity, and harm minimization) apply through these Interdependent Definitions and the rest of Chapter Five.\n",
    ),
    (
        "Chapter Two governs definition structure, tracing, verification, and anti-evasion for the constitution as a whole.\n",
        "**Chapters Two through Four** govern definition structure, integrity under interpretation, observable non-compliance, tracing, verification, and anti-evasion for the constitution as a whole.\n",
    ),
    (
        "Cluster index (Chapter Three, section 2 — Clustered Definitions): For evaluations governed by Chapter Two, materially relevant clustered entries in Chapter Three must also be traced. Major clusters include:\n",
        "Cluster index (Chapter Five, section 2 — Clustered Definitions): For evaluations governed by **Chapters Two through Four**, materially relevant clustered entries in Chapter Five must also be traced. Major clusters include:\n",
    ),
]
for item in replacements_pre:
    old, new = item[0], item[1]
    count = item[2] if len(item) > 2 else None
    if count:
        if pre.count(old) != count:
            raise SystemExit(f"Expected {count} occurrences of pre-replacement fragment, got {pre.count(old)}: {old[:60]}...")
        pre = pre.replace(old, new, count)
    else:
        if old not in pre:
            raise SystemExit(f"Missing pre-replacement fragment: {old[:80]}...")
        pre = pre.replace(old, new, 1)

new_text = pre + "".join(out_post)

# --- Whole-file section remaps from old Chapter Two numbering ---
subs = [
    ("Chapter Two, section 8.1", "Chapter Four, section 4.1"),
    ("Chapter Two, section 8 —", "Chapter Four, section 4 —"),
    ("Chapter Two, section 9", "Chapter Four, section 5"),
    ("Chapter Two, section 7", "Chapter Four, section 3"),
    ("Chapter Two, section 6", "Chapter Four, section 2"),
    ("Chapter Two, section 5", "Chapter Four, section 1"),
    ("Chapter Two, sections 3 and 4", "Chapter Three, sections 1 and 2"),
]
for a, b in subs:
    new_text = new_text.replace(a, b)

# Reading note: Chapter One (values) + Chapter Seven (rights), then this chapter (definitions)
new_text = new_text.replace(
    "Plain-language reading note (non-operative): Read Chapters One and Seven first for constitutional direction, then return to this chapter for term precision in interpretation, audit, and adjudication.\n",
    "Plain-language reading note (non-operative): Read Chapters One and Seven first for constitutional direction (values and rights floors), then return to this chapter for term precision in interpretation, audit, and adjudication.\n",
    1,
)

path.write_text(new_text, encoding="utf-8")
print("Wrote", path)
