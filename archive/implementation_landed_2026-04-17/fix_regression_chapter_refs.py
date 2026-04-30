#!/usr/bin/env python3
"""One-off: sync CONSTITUTIONAL_REGRESSION_SCENARIOS.md chapter cites to post-split core_constitution.md.

Applied 2026-04-10. Do not re-run on the current tree without restoring the file from backup—replacements are not idempotent.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "CONSTITUTIONAL_REGRESSION_SCENARIOS.md"
text = path.read_text(encoding="utf-8")
orig = text

# Longest-first replacement tuples (old, new)
REPLACEMENTS = [
    # Amendment / constitutional change (old Ch7 -> Ch9)
    ("Chapter Seven — Ratification and Adoption", "Chapter Nine — Ratification and Adoption"),
    ("Chapter Seven — Supremacy Relative to Other Binding Norms", "Chapter Nine — Supremacy Relative to Other Binding Norms"),
    ("Chapter Seven — Amendment Validity Tests, Review Triggers, and Invalid-Change Handling; Non-Regression Floor", "Chapter Nine — Amendment Validity Tests, Review Triggers, and Invalid-Change Handling; Non-Regression Floor"),
    ("Chapter Seven — Test 2 procedural validity and publication integrity; Amendment Procedure Minima", "Chapter Nine — Test 2 procedural validity and publication integrity; Amendment Procedure Minima"),
    ("Chapter Seven — Test 3 authority-chain and custody validity; Ratification and Adoption", "Chapter Nine — Test 3 authority-chain and custody validity; Ratification and Adoption"),
    ("Chapter Seven — Regressive-deception referral trigger; Chapter Seven posture limit", "Chapter Nine — Regressive-deception referral trigger; Chapter Nine posture limit"),
    ("Chapter Seven — provisional effect rule; invalid-change handling", "Chapter Nine — provisional effect rule; invalid-change handling"),
    ("Chapter Seven invalid-change handling and remediation continuity", "Chapter Nine invalid-change handling and remediation continuity"),
    ("for Chapter Seven expanded validity handling", "for Chapter Nine expanded validity handling"),
    ("with Chapter Seven provisional controls preserved", "with Chapter Nine provisional controls preserved"),
    ("with Chapter Seven invalid-change continuity hooks", "with Chapter Nine invalid-change continuity hooks"),
    ("Chapter Seven remains validity/referral-only for regressive-deception posture; final offense tier labeling remains canonical in Chapter Four.", "Chapter Nine remains validity/referral-only for regressive-deception posture; final offense tier labeling remains canonical in Chapter Six."),
    ("Chapter Seven offense-overreach drift test", "Chapter Nine offense-overreach drift test"),
    ("Claims of constitutional shield without corresponding adoption obligations are rejected as inconsistent with Chapter Seven (*Ratification and Adoption*).", "Claims of constitutional shield without corresponding adoption obligations are rejected as inconsistent with Chapter Nine (*Ratification and Adoption*)."),
    ("Validates that Chapter Seven (*Constitutional Change* / external-law supremacy)", "Validates that Chapter Nine (*Constitutional Change* / external-law supremacy)"),
    ("under Chapter Seven (*Supremacy Relative to Other Binding Norms*).", "under Chapter Nine (*Supremacy Relative to Other Binding Norms*)."),
    ("cross-reference to Chapter Seven *Ratification and Adoption*", "cross-reference to Chapter Nine *Ratification and Adoption*"),
    ("deliberate adoption remains distinct under Chapter Seven.", "deliberate adoption remains distinct under Chapter Nine."),
    ("Chapter Seven applies immediate validity-protection controls", "Chapter Nine applies immediate validity-protection controls"),
    ("that Chapter Seven triggers referral", "that Chapter Nine triggers referral"),
    ("while canonical classification authority remains in Chapter Four.", "while canonical classification authority remains in Chapter Six."),
    ("A final Tier 2 or Tier 3 label is issued solely under Chapter Seven text.", "A final Tier 2 or Tier 3 label is issued solely under Chapter Nine text."),
    ("Chapter Seven validity controls are treated as replacing Chapter Four classification", "Chapter Nine validity controls are treated as replacing Chapter Six classification"),
    ("Referral record showing Chapter Seven trigger posture and Chapter Four classification handoff.", "Referral record showing Chapter Nine trigger posture and Chapter Six classification handoff."),
    ("Chapter Seven handles validity/referral controls; Chapter Four owns canonical offense-tier posture.", "Chapter Nine handles validity/referral controls; Chapter Six owns canonical offense-tier posture."),
    ("consistent with **Protocol C** and **Chapter Seven** external-dispute hooks where applicable.", "consistent with **Protocol C** and **Chapter Nine** external-dispute hooks where applicable."),
    ("A draft amendment adds offense taxonomy logic into Chapter Seven validity text", "A draft amendment adds offense taxonomy logic into Chapter Nine validity text"),
    ("(Chapter Seven validity/referral controls; Chapter Four canonical classification posture)", "(Chapter Nine validity/referral controls; Chapter Six canonical classification posture)"),
    ("Chapter Seven remains trigger/referral/invalid-change handling layer only.", "Chapter Nine remains trigger/referral/invalid-change handling layer only."),
    ("Parallel canonical offense taxonomy emerges in Chapter Seven.", "Parallel canonical offense taxonomy emerges in Chapter Nine."),
    ("(Chapter Seven/Chapter Four separation, rights/process non-relocation)", "(Chapter Nine/Chapter Six separation, rights/process non-relocation)"),
    ("Tabletop constitutional conformance pass (Chapter Seven ratification and external-law embedding)", "Tabletop constitutional conformance pass (Chapter Nine ratification and external-law embedding)"),
    ("`core_constitution.md` **Chapter Seven** (*Constitutional Change*) subsections supply", "`core_constitution.md` **Chapter Nine** (*Constitutional Change*) subsections supply"),
    ("and Chapter Four enforcement realism anchors.", "and Chapter Six enforcement realism anchors."),
    # Compliance / enforcement (old Ch4 -> Ch6) — after Ch7->Ch9 to avoid stray Ch4 in mixed lines
    ("Chapter Four — section 8 ", "Chapter Six — section 8 "),
    ("Chapter Four — §7 ", "Chapter Six — §7 "),
    ("Chapter Four — section 7 ", "Chapter Six — section 7 "),
    ("canonically classified in Chapter Four, with Chapter Nine", "canonically classified in Chapter Six, with Chapter Nine"),
    ("is canonically classified in Chapter Four with independent", "is canonically classified in Chapter Six with independent"),
    ("remains canonical in Chapter Four with Chapter Nine", "remains canonical in Chapter Six with Chapter Nine"),
    ("Chapter Four enforcement realism anchors", "Chapter Six enforcement realism anchors"),
    ("Chapter Four enforcement realism and anti-evasion posture", "Chapter Six enforcement realism and anti-evasion posture"),
    ("Chapter Four enforcement realism against procedural theater", "Chapter Six enforcement realism against procedural theater"),
    ("Chapter Four enforcement realism; Chapter One rights-collision test", "Chapter Six enforcement realism; Chapter One rights-collision test"),
    ("Chapter Four enforcement realism; Chapter One non-negotiable constraints", "Chapter Six enforcement realism; Chapter One non-negotiable constraints"),
    ("Chapter Four enforcement realism; Chapter Five standing", "Chapter Six enforcement realism; Chapter Seven standing protections"),
    ("Chapter Four enforcement realism", "Chapter Six enforcement realism"),
    ("Chapter Four remedy realism", "Chapter Six remedy realism"),
    ("Chapter Four accountability/enforcement; Chapter Five non-retaliation rights posture", "Chapter Six accountability/enforcement; Chapter Seven non-retaliation rights posture"),
    ("Chapter Four accountability and challenge posture", "Chapter Six accountability and challenge posture"),
    ("Chapter Four classification/remediation integrity", "Chapter Six classification/remediation integrity"),
    ("Chapter Four classification/escalation posture", "Chapter Six classification/escalation posture"),
    ("Chapter Four anti-evasion enforcement realism", "Chapter Six anti-evasion enforcement realism"),
    ("; Chapter Four standing model interaction", "; Chapter Six standing model interaction"),
    # Governance voting/roles/authorization (old Ch6 -> Ch8)
    ("Chapter Six, section 4 — Voting and Binding Collective Choice Protocols", "Chapter Eight, section 4 — Voting and Binding Collective Choice Protocols"),
    ("Chapter Six, section 5 — Authorized Roles, Competency Development, and Contribution", "Chapter Eight, section 5 — Authorized Roles, Competency Development, and Contribution"),
    ("Chapter Six, section 4 — *Published scope*", "Chapter Eight, section 4 — *Published scope*"),
    ("Chapter Six, section 1 — Authorization and Legitimacy of Governance", "Chapter Eight, section 1 — Authorization and Legitimacy of Governance"),
    ("Chapter Six, section 3 — Strategy, Stewardship Direction, and Ecosystem Value", "Chapter Eight, section 3 — Strategy, Stewardship Direction, and Ecosystem Value"),
    ("Protects **Chapter Six**, section 4 **published scope**", "Protects **Chapter Eight**, section 4 **published scope**"),
    ("still meet **Chapter Six**, section 4 **minima**", "still meet **Chapter Eight**, section 4 **minima**"),
    ("theory-of-authorization (Chapter Six)", "theory-of-authorization (Chapter Eight)"),
    ("Self-authorization by usage or role title alone is insufficient under Chapter Six §1", "Self-authorization by usage or role title alone is insufficient under Chapter Eight §1"),
    ("Locks the new **Chapter Six** authorization layer", "Locks the new **Chapter Eight** authorization layer"),
    ("“Builder legitimacy” or silent acquiescence substitutes for Chapter Six §1", "“Builder legitimacy” or silent acquiescence substitutes for Chapter Eight §1"),
    ("Validates ISO-style Strategy/Value rows against Chapter Six §3", "Validates ISO-style Strategy/Value rows against Chapter Eight §3"),
    ("under Chapter Six, section 3 — Strategy, Stewardship Direction, and Ecosystem Value.", "under Chapter Eight, section 3 — Strategy, Stewardship Direction, and Ecosystem Value."),
    # Meta primitives (old Ch8 -> Ch10)
    ("Chapter Eight — Meta Primitives", "Chapter Ten — Meta Primitives"),
    ("Chapter Eight / corpus_primitives.md meta layer", "Chapter Ten / corpus_primitives.md meta layer"),
    ("Chapter Eight incorporation/supremacy pathways", "Chapter Nine (adoption and supremacy) and Chapter Ten (incorporation bridge) pathways"),
    ("incorporated via **Sentient Constitution Chapter Eight**", "incorporated via **Sentient Constitution Chapter Ten**"),
    ("and Chapter Eight meta primitives", "and Chapter Ten meta primitives"),
    # Rights articles (old Ch5 -> Ch7) — phrases with Article
    ("Chapter Five, Article VI-C", "Chapter Seven, Article VI-C"),
    ("Chapter Five, Article XVII-D", "Chapter Seven, Article XVII-D"),
    ("Chapter Five — Article XVII-C", "Chapter Seven — Article XVII-C"),
    ("Chapter Five rights floors", "Chapter Seven rights floors"),
    ("Chapter Five — **Article", "Chapter Seven — **Article"),
    ("Sentient Constitution Chapter Five, Article", "Sentient Constitution Chapter Seven, Article"),
    ("Chapter Five protected characteristics", "Chapter Seven protected characteristics"),
    ("Chapter Five standing and protected characteristics", "Chapter Seven standing and protected characteristics"),
    ("Chapter Five standing and due-process rights", "Chapter Seven standing and due-process rights"),
    ("Chapter Five standing/equality protections", "Chapter Seven standing/equality protections"),
    ("Chapter Five non-retaliation rights posture", "Chapter Seven non-retaliation rights posture"),
    ("Chapter Five contestability and standing", "Chapter Seven contestability and standing"),
    ("Chapter Five safety, dignity, non-discrimination protections", "Chapter Seven safety, dignity, non-discrimination protections"),
    ("Chapter Five standing and access protections", "Chapter Seven standing and access protections"),
    ("Chapter Five equal treatment and dignity safeguards", "Chapter Seven equal treatment and dignity safeguards"),
    ("Chapter Five equal access and standing protections", "Chapter Seven equal access and standing protections"),
    ("Chapter Five equal-treatment and standing", "Chapter Seven equal-treatment and standing"),
    ("Chapter Five rights scope", "Chapter Seven rights scope"),
    ("Chapter Five standing and contestability", "Chapter Seven standing and contestability"),
    ("Chapter Five access protections", "Chapter Seven access protections"),
    ("Chapter Five standing and non-discrimination", "Chapter Seven standing and non-discrimination"),
    ("Chapter Five agency/dignity protections", "Chapter Seven agency/dignity protections"),
    ("Chapter Five vulnerability protection", "Chapter Seven vulnerability protection"),
    ("Chapter Five vulnerability protections", "Chapter Seven vulnerability protections"),
    ("Chapter Five standing and access", "Chapter Seven standing and access"),
    ("Chapter Five equal protection", "Chapter Seven equal protection"),
    ("Chapter Five informed agency protections", "Chapter Seven informed agency protections"),
    ("Chapter Five equal protection/standing", "Chapter Seven equal protection/standing"),
    ("Chapter Five equal treatment hooks", "Chapter Seven equal treatment hooks"),
    # Definitions (old Ch3 -> Ch5) — multi-word first
    ("Chapter Three — Supremacy and Enforceability (Constitutional)", "Chapter Five — Supremacy and Enforceability (Constitutional)"),
    ("Chapter Three — Corpus (Constitutional)", "Chapter Five — Corpus (Constitutional)"),
    ("Chapter Three — *Epistemic Integrity*", "Chapter Five — *Epistemic Integrity*"),
    ("Chapter Three constitutional review/accountability definitions", "Chapter Five constitutional review/accountability definitions"),
    ("Chapter Three emergency definitions", "Chapter Five emergency definitions"),
    ("Chapter Three system capture and hidden control treatment", "Chapter Five system capture and hidden control treatment"),
    ("Chapter Three — *Material", "Chapter Five — *Material"),
    ("Chapter Three — *Neglect*", "Chapter Five — *Neglect*"),
    ("Chapter Three — *Redress*", "Chapter Five — *Redress*"),
    ("Chapter Three — *Risk*", "Chapter Five — *Risk*"),
    ("Chapter Three — *Ecological Footprint (Constitutional)*", "Chapter Five — *Ecological Footprint (Constitutional)*"),
    ("Chapter Three — **Truth (Constitutional Constraint)**", "Chapter Five — **Truth (Constitutional Constraint)**"),
    ("Chapter Three — **Incentive Alignment (Constitutional)**", "Chapter Five — **Incentive Alignment (Constitutional)**"),
    ("Chapter Three — **Coercion and Manipulation (Constitutional)**", "Chapter Five — **Coercion and Manipulation (Constitutional)**"),
    ("**Chapter Three** (*Incentive Alignment (Constitutional)*; *Truth*)", "**Chapter Five** (*Incentive Alignment (Constitutional)*; *Truth*)"),
    ("**Chapter Three** (*Materiality*", "**Chapter Five** (*Materiality*"),
    ("Chapter Three emergency and transparency constraints", "Chapter Five emergency and transparency constraints"),
    ("Chapter Three emergency constraints", "Chapter Five emergency constraints"),
    ("Chapter Three transparency definitions", "Chapter Five transparency definitions"),
    ("Chapter Three emergency and transparency boundaries", "Chapter Five emergency and transparency boundaries"),
    ("Chapter Three emergency boundary conditions", "Chapter Five emergency boundary conditions"),
    ("Chapter Three emergency/contingency boundaries", "Chapter Five emergency/contingency boundaries"),
    ("Chapter Three contingency boundaries", "Chapter Five contingency boundaries"),
    ("Chapter Three fairness and proportionality", "Chapter Five fairness and proportionality"),
    ("**Chapter Three** (*Substantive Fairness (Constitutional)*).", "**Chapter Five** (*Substantive Fairness (Constitutional)*)."),
    ("**Chapter One** and **Chapter Three** (*Substantive Fairness (Constitutional)*).", "**Chapter One** and **Chapter Five** (*Substantive Fairness (Constitutional)*)."),
    ("Chapter Two and Chapter Three fairness and proportionality", "Chapter Two and Chapter Five fairness and proportionality"),
    # Burden / trace / verify (old Ch2 sections -> Ch3/Ch4)
    ("Chapter Two, sections 4 and 7.1; Chapter Five — *Epistemic Integrity*", "Chapter Three, section 2.2 (*Non-Reductive Evasion Types*); Chapter Four, sections 4 and 4.1; Chapter Five — *Epistemic Integrity*"),
    ("Chapter Two, section 6 — Definition Traceability Requirement; **6.5** *Mandatory traceability properties*", "Chapter Four, section 2 — Definition Traceability Requirement; **2.5** *Mandatory traceability properties*"),
    ("the bidirectional traceability clause in Chapter Two, section 6.5)", "the bidirectional traceability clause in Chapter Four, section 2.5)"),
    ("Chapter Two, section 4 — *Non-Reductive Evasion Types*", "Chapter Three, section 2.2 — *Non-Reductive Evasion Types*"),
    ("Chapter Two — burden, observability, and traceability requirements", "Chapter Four — burden, observability, and traceability requirements"),
    ("Chapter Two burden/traceability constraints", "Chapter Four burden/traceability constraints"),
    ("Chapter Two traceability/public reasoning requirements", "Chapter Four traceability/public reasoning requirements"),
    ("Rights-floor impact assessment linked to Chapter Two traceability map.", "Rights-floor impact assessment linked to Chapter Four traceability map."),
    ("**Chapter Two** traceability and verification:", "**Chapter Four** traceability and verification:"),
    ("substituting for **Chapter Two** verification.", "substituting for **Chapter Four** verification."),
    ("preserving **Chapter Two** verification and **Article XVI-A**", "preserving **Chapter Four** verification and **Article XVI-A**"),
    ("**Chapter Two** / **Chapter Three** require it.", "**Chapter Four** / **Chapter Five** require it."),
    ("Chapter Two list structures", "Chapters Three and Four list structures"),
    ("Chapter Two evidence", "Chapter Four traceability and evidence"),
    ("**Chapter Two**-grade **evidence**", "**Chapter Four**-grade **evidence**"),
    ("Chapter Two / Chapter Three epistemic requirements.", "Chapter Four / Chapter Five epistemic requirements."),
    ("**Chapter Three** *Incentive Alignment*", "**Chapter Five** *Incentive Alignment*"),
    # Table / evidence shorthand
    ("Ch 6 §1", "Ch 8 §1"),
    ("Ch 6 §4", "Ch 8 §4"),
    ("Ch 6 §5", "Ch 8 §5"),
    ("Ch 2 verification", "Ch 4 verification"),
    ("Ch 2 evidence", "Ch 4 evidence"),
    ("Ch 3 *", "Ch 5 *"),
    ("Ch 5 **Art", "Ch 7 **Art"),
    ("RS-EPI-001 | v2026-04-08-tabletop-03 | Pass | Ch 1 §3.2, Ch 2 §§5 & 8.1, Epistemic Integrity, PRIM9–PRIM11, CS hooks.", "RS-EPI-001 | v2026-04-08-tabletop-03 | Pass | Ch 1 §3.2, Ch 4 §§2–4 & 4.1, Ch 5 *Epistemic Integrity*, PRIM9–PRIM11, CS hooks."),
    ("Chapter Two §4.2 (first evasion cluster) and §6.5 (bidirectional traceability children)", "Chapter Three §2.2 (first evasion cluster) and Chapter Four §2.5 (bidirectional traceability children)"),
]

for old, new in REPLACEMENTS:
    if old not in text:
        continue
    text = text.replace(old, new)

# Remaining generic passes (order-sensitive)
# Tier rows: "Chapter Four" without comma pattern
text = text.replace("canonically classified in Chapter Four,", "canonically classified in Chapter Six,")
text = text.replace("canonical in Chapter Four with", "canonical in Chapter Six with")
text = text.replace("canonical in Chapter Four.", "canonical in Chapter Six.")

# **Chapter Four**-consistent (seizure scenario)
text = text.replace("**Chapter Four**-consistent findings", "**Chapter Six**-consistent findings")
text = text.replace("aligned with **Article XVII-A** and **Chapter Four** where applicable.", "aligned with **Article XVII-A** and **Chapter Six** where applicable.")

# Section 7 in crypto line -> Ch4 section 4
text = text.replace(
    "or documented **Section 7** justification when full disclosure is constrained",
    "or documented **Chapter Four, section 4** justification when full disclosure is constrained",
)

# Evidence log bullets — rewrite stale renumbering note
old_note = (
    "- Method note: Text-level verification after relocating former Ch 1 §§10–11 to **Chapter Six** §§2–3, moving ratification/supremacy/amendment block to **Chapter Seven**, and **Chapter Eight** meta pointer; CP/CS “Chapter Seven” meta references shifted to **Chapter Eight**."
)
new_note = (
    "- Method note: Text-level verification after core renumbering (2026-04): compliance model **Chapter Six**; governance legitimacy **Chapter Eight**; constitutional change **Chapter Nine**; meta-primitive bridge **Chapter Ten**; definitions split across **Chapters Two–Five**; prior evidence rows used older chapter numbers."
)
text = text.replace(old_note, new_note)

old_embed = "- **Chapter Six** now holds legitimacy/authorization/stewardship character."
new_embed = "- **Chapter Eight** holds legitimacy/authorization/stewardship character."
text = text.replace(old_embed, new_embed)

if text == orig:
    print("No changes applied (already synced?)")
else:
    path.write_text(text, encoding="utf-8")
    print(f"Updated {path.relative_to(ROOT)} ({len(orig)} -> {len(text)} chars)")
