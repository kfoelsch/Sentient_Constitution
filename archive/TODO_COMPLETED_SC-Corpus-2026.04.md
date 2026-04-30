# Archived TODO — External framework & embedding (edition closure)

**Edition:** `SC-Corpus-2026.04`  
**Effective date:** 2026-04-08  
**Archived:** 2026-04-08 (corpus edition cut; narratives frozen for assurance readers).  
**Active checklist:** [`TODO.md`](../TODO.md).

This file is **process history only**. Authoritative rules live in [`core_constitution.md`](../core_constitution.md), [`corpus_primitives.md`](../corpus_primitives.md), and [`corpus_systems.md`](../corpus_systems.md).

**Regression / tabletop IDs** remain authoritative in [`CONSTITUTIONAL_REGRESSION_SCENARIOS.md`](../CONSTITUTIONAL_REGRESSION_SCENARIOS.md) and [`evidence/`](../evidence/).

---

## External Framework and Embedding Gaps (gap-analysis follow-up)

Follow-up from external benchmark review: ISO 37000 / OECD (residual), NIST AI RMF, ISO/IEC 42001, EU AI Act (governance slice), and constitutional-political embedding. **Editorial** crosswalks and non-normative notes belong in `doc_architecture.md` unless you deliberately amend Sentient Constitution / CP / CS.

### Legal embedding and ISO-style completeness

- [x] **Ratification and external law:** Procedural bridge for adoption, amendment in practice, supremacy against conflicting municipal or regulatory law, and dispute resolution with external legal orders (aligns architecture checklist **9**; candidates: `core_constitution.md` tail, new interpretive block, or dedicated transition/ratification subsection). *(Done 2026-04-08: **core_constitution.md** **Chapter Nine** (*Constitutional Change*) ratification/external-law subsections; Ch 3 Supremacy O-component; regression **RS-EMBED-001**, **RS-EMBED-002** — scenarios validated; tabletop **v2026-04-08-tabletop-embed-01** in `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` §8. **Renumber note:** adoption machinery is **Ch 7** after **Ch 6** legitimacy insert.)*
- [x] **Capital markets and intermediaries (OECD Principle III analog):** Record explicit **in-scope** vs **out-of-scope** decision; if in-scope, add steward- or class-scaled rules for listed entities, institutional investors, and market intermediaries (`corpus_systems.md` and/or architecture doc only). *(Done 2026-04-08: **corpus_systems.md** — Interpretation — Capital markets…; **doc_architecture.md** §15.2 row III + **§15.3** scope log; regression **RS-EMBED-003**, tabletop **v2026-04-08-tabletop-embed-02**.)*
- [x] **Strategy and value generation (ISO 37000 partials):** Add a concise governing-body **strategy cycle** and ecosystem-scale **value** narrative (not shareholder-value corporate framing)—candidates: `core_constitution.md` Chapter One or Five, or `corpus_systems.md` Chapter S3 leadership / oversight effectiveness hooks. *(Done 2026-04-08: **core_constitution.md** **Ch 6 §3** (formerly Ch 1 §11); architecture **§15.1** Strategy/Value rows; **RS-EMBED-004**, tabletop **v2026-04-08-tabletop-embed-03**.)*

### AI regulatory and assurance crosswalks (architecture doc)

- [x] **NIST AI RMF crosswalk:** New table: Govern / Map / Measure / Manage → Sentient Constitution / CP / CS pointers; mark **not addressed** where the corpus lacks explicit lifecycle hooks (e.g. system/model cards, evaluation cadence, post-deployment monitoring tied to deployment class). *(Done 2026-04-08: **doc_architecture.md** §15.4.)*
- [x] **ISO/IEC 42001 crosswalk:** Clause-style mapping (context, leadership, planning, support, operation, performance evaluation, improvement) → corpus pointers; flag **presentation gap** where principles exist but MS structure is implicit. *(Done 2026-04-08: **doc_architecture.md** §15.5.)*
- [x] **EU AI Act (high-risk lifecycle) crosswalk:** Map technical documentation, QMS, logging, serious-incident reporting, conformity assessment → pointers or **not addressed**; optional `implementation/` note for adopters subject to EU law. *(Done 2026-04-08: **doc_architecture.md** §15.6.)*
- [x] **Consolidated AI + organizational governance crosswalk:** Single architecture section (or subsection series) unifying NIST AI RMF, ISO 42001, and EU Act tables with shared legend, version column, and pointer to authoritative corpus edition (extends section **15** pattern). *(Done 2026-04-08: **doc_architecture.md** §15 header + §15.7; §16 Purpose cross-link.)*

### Legitimacy and enforcement realism (substantive deepening)

- [x] **Theory of authorization:** Make the **legitimacy mechanism** explicit (e.g. elections, sortition, federated ratification, treaty-of-parties) with scope, constraints, and failure handling; tie to existing participation and standing language (`core_constitution.md` Chapters Three–Four; `corpus_primitives.md` PROT1 as needed). *(Done 2026-04-08: **core_constitution.md** **Chapter Six** §1 *Authorization and Legitimacy of Governance*; former Ch 1 §§10–11 relocated to Ch 6 §§2–3; Ch 3 Supremacy and Art XXI bounded mandate updated; **Chapter Nine** adoption; **Chapter Ten** meta; cross-corpus Ch Seven→Eight meta refs; regression **RS-AUTH-001**.)*
- [x] **Remedy capacity:** Deepen **financing and capacity** for remedies (pools, insurance/indemnity patterns, cross-border judgment recognition, sustained enforcement organs) without assuming a single nation-state; align with enforcement realism and funding protocols (`core_constitution.md`, `corpus_primitives.md` PROT3/PROT6, `corpus_systems.md` Protocol S5 and cross-jurisdiction language). *(Done 2026-04-08: **core_constitution.md** Ch 4 §7 *Enforcement Realism Anchors* (remedy financing mechanisms, remedy-organ durability, cross-border playbooks); **corpus_primitives.md** **PROT3** *Capacity for Remedy and Enforcement*; **PROT6** *Remedy Accessibility and Financing*; **corpus_systems.md** **Protocol C** §8 bullets; **Protocol S5** *Remedy, Restitution, and Systemic Harm Response* allocation category; regression **RS-REMEDY-001**, tabletop **v2026-04-08-tabletop-remedy-01**.)*

### Corpus publication and assurance readiness

- [x] **Editioning and release closure:** Corpus-wide **edition identifier** and **effective date**; narrow or remove blanket work-in-progress notices when release criteria are met; regenerate TOC/page structure if published outputs depend on it (`doc_architecture.md` section **17**, checklist **8**). *(Done 2026-04-08: headers **SC-Corpus-2026.04** / **2026-04-08** on Sentient Constitution / CP / CS; architecture **§17** *Current corpus edition*; checklist **8** closure note.)*
- [x] **Embedding boundary note (optional):** Short **non-normative** architecture subsection: what requires an **adopting polity** or **separate legal instrument** (legitimacy, coercion, courts)—so assurance readers do not over-read the corpus as a complete legal order. *(Done 2026-04-08: **doc_architecture.md** **section 18**.)*
