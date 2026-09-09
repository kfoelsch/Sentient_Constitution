# CS-2 data types coverage audit

**Date:** 2026-08-31  
**Status:** Process / evidence support. This file does **not** bind. Indexes point; source binds.  
**Companion spreadsheet:** [cs2_data_types_coverage_matrix.csv](cs2_data_types_coverage_matrix.csv)

## What this is

A coverage matrix, not a taxonomy rewrite. CS-2 already owns the seven types (**E, G, O, H, I, N, S**) in [CS-2 Part B](../../corpus_systems/cs_02_b_data_classifications.md). This audit asks: for every **named data kind** the Constitution talks about, can we point to **at least one** of those types — and does the **source** already say so?

**Out of this pass:** corpus edits, new types, and `make regression`. Gaps stay findings.

Typing rule used for auditor mappings: [CS-2.2](../../corpus_systems/cs_02_a_information_types_and_handling.md#cs-2-2-determination-of-classification) — type by functional effect, not format or pipeline stage; where more than one type fits, the most-restrictive applicable protections govern.

## Scope

| Included | Excluded |
|---|---|
| Numbered `core_*` files | `archive/` |
| Incorporated companions (CS, CJS, CF, CI) where they name records or data kinds | Process support (`implementation/` notes, steward cards) except as they instantiate a named constitutional artifact |
| Chapter Five Definitions A–Z as the priority walk | `ai_corpus/` locators and gloss |

Chapter Five directory size: **224** entries in [core_05__definitions_home.md](../../core_05__definitions_home.md) Definitions A–Z.

A definition is **data-relevant** if it is itself a record, disclosure, or published instrument, or if its in-scope text names kinds of information. Mentioning “data” in passing does not qualify. **186** directory entries are N/A on that test (duties, aims, statuses, and similar). **38** Chapter Five definitions are data-relevant.

## Type legend

| Type | Name | Access-posture band |
|---|---|---|
| **E** | Environmental, emergency, and survival-coordination data | Open / accessible by default |
| **O** | Open public oversight baseline disclosure data | Open / accessible by default |
| **G** | Governance and operational source data | Audit-accessible, not public |
| **H** | Historical, relational, transactional, and participation data | Restricted by default |
| **I** | Identity and attribution data | Restricted by default |
| **S** | Safety, security, and restricted investigation data | Restricted by default (time-bound, review-bound) |
| **N** | Neurocognitive and internal data | Non-accessible by default |

Public-view versus source split is recorded where source already states it (Type O instruments under Public Oversight Baseline Disclosure). For the named constitutional records below, **operator-directed inference** is **Type O by default** for the record itself — not Type G for the “source file” and Type O only for a public extract. Portions retype to **G**, **H**, or **I** only for justified security or privacy hold-backs under [CS-2.2](../../corpus_systems/cs_02_a_information_types_and_handling.md#cs-2-2-determination-of-classification) (most-restrictive) and [CS-2.7](../../corpus_systems/cs_02_a_information_types_and_handling.md#cs-2-7-type-o-baseline-for-class-a-b-c-systems) / [Part A §5.3](../../corpus_systems/cs_02_a_information_types_and_handling.md#53-tiered-transparency-and-audit-access). **S** still applies where exploit- or investigation-sensitive material is in the packet. That default does not rewrite CS-2 Type G’s general “not public by default” band for other governance source.

## Assignment statuses

| Status | Meaning |
|---|---|
| **Explicit** | Source names Type E/G/O/H/I/N/S on that kind |
| **Example-covered** | Named in a CS-2 Part B example list (or an equivalent CS-2 example elsewhere in CS-2) |
| **Inferred** | Auditor mapping from functional effect under CS-2.2; **not** yet in the definition or article home |
| **Gap** | Named data kind with no defensible type under the seven-letter taxonomy |
| **N/A** | Not a data kind (Chapter Five directory count only) |

Inferred is **not** a taxonomy hole. It means operators can type the kind under CS-2.2, but the Chapter Five or article home does not yet assign a letter. Those rows are the **source-assignment gaps** in the register below.

## Counts

| Bucket | Count |
|---|---:|
| Named data-kind rows in the matrix | **136** |
| Explicit | 18 |
| Example-covered | 56 |
| Inferred | 62 |
| Gap (no defensible CS-2 type) | **0** |
| Chapter Five directory entries | 224 |
| Chapter Five data-relevant definitions | 38 |
| Chapter Five N/A definitions | 186 |
| Chapter Five matrix rows (artifact + category) | 60 |
| CS-2 Part B example rows (not already a Chapter Five kind) | 45 |
| Rights-floor rows | 5 |
| Companion rows (CJS / CS-4 / CF-15) | 26 |

Every inventoried kind has **at least one** type. No taxonomy hole was found. The remaining work is **source assignment**: 62 inferred rows, including 35 Chapter Five rows, still lack a type letter on the home that names the kind.

Type hits across rows (a row may count more than once): I 59, G 56, H 33, O 27, S 22, N 19, E 9. Named constitutional records now count **O** as the default type, with G/H/I listed as hold-back types on the same row.

---

## Chapter Five matrix

Priority table. Full cites and notes are in the CSV.

### Artifacts (the definition is a record, disclosure, or instrument)

| Definition | Data kind | Type(s) | Status | Source |
|---|---|---|---|---|
| [Public Oversight Baseline Disclosure](../../core_05_band_oversight.md#public-oversight-baseline-disclosure) | Public Oversight Baseline Disclosure floor | **O** | Explicit | Home: typed and handled as Type O |
| [Transparency](../../core_05_band_oversight.md#transparency) | Public baseline transparency disclosures | **O** | Explicit | Read-with names Type O |
| [Charter](../../core_05_band_continuity.md#charter) | Published Charter / usable public view | **O** | Explicit | Class A/B/C Type O instruments |
| Charter | Charter source instrument (full file) | **O** (default); **G / H / I** hold-back | Inferred | Operator default Type O. Unpublished working papers that are not yet the Charter may remain G |
| [System Certification Record](../../core_05_band_continuity.md#system-certification-record-constitutional) | Usable public view | **O** | Explicit | Type O instruments list |
| System Certification Record | Full source case file | **O** (default); **G / H / I** hold-back | Inferred | Home has no type letter |
| [System Classification Record](../../core_05_band_continuity.md#system-classification-record-constitutional) | Usable public view | **O** | Explicit | Type O instruments list |
| System Classification Record | Full source file | **O** (default); **G / H / I** hold-back | Inferred | Home has no type letter |
| [System Data Types Record](../../core_05_band_continuity.md#system-data-types-record-constitutional) | Usable public view | **O** | Explicit | Type O instruments; CS-2 §8 disclosure |
| System Data Types Record | Source file as material audited information | **O** (default); **G / H / I** hold-back | Inferred | Home has no type letter for the source file |
| [Risk Disclosure](../../core_05_band_oversight.md#risk-disclosure) | Needed-audience / baseline communication; full-fidelity analyses | **O; G** | Explicit | Type O topic satisfaction; Type G examples include full-fidelity risk analyses |
| [Forum Case Record](../../core_05_band_accountability.md#forum-case-record) | Case file | **O** (default); **G / H / I** hold-back; **S** if restricted evidence | Inferred | Identity-bearing fields may be I |
| [Standing Record](../../core_05_band_accountability.md#standing-record-chapter-six) | Axis-pure contribution or violation record | **O** (default); **G / H / I** hold-back | Inferred | Subject-identifying fields may be I |
| [Unified Incident Record](../../core_05_band_accountability.md#unified-incident-record) | Combined incident evidence and reasoning | **O** (default); **G / H / I** hold-back; **S** if investigation- or exploit-sensitive | Inferred | |
| [Sentience-Status Adjudication Record](../../core_05_band_participation.md#sentience-status-adjudication-record-constitutional) | Status determination file | **O** (default); **G / H / I** hold-back | Inferred | Subject identity fields may be I |
| [Stakeholder Rights-Collision Record](../../core_05_band_participation.md#stakeholder-rights-collision-record-binding-stakeholder-choice) | Binding-choice collision record | **O** (default); **G / H / I** hold-back | Inferred | Same named-record default |
| [Non-Compliance Finding Profile](../../core_05_band_accountability.md#non-compliance-finding-profile) | Routing metadata on a finding | **G** | Inferred | |

### Data-category definitions (in-scope names kinds of information)

| Definition | Data kind | Type(s) | Status | Source |
|---|---|---|---|---|
| [Privacy (Informational)](../../core_05_band_continuity.md#privacy-informational) | Personal information | **I; H** | Inferred | I if it identifies a sentient |
| Privacy (Informational) | Relational information | **H** | Example-covered | Type H relational/association patterns |
| Privacy (Informational) | Experiential information | **H; N** | Inferred | N when it reconstructs inner states ([Article VIII-B](../../core_06-06_rights_part_b.md#article-viii-b-experiential-and-derived-data-rights) Explicit N) |
| Privacy (Informational) | Behavioral information | **H; N** | Inferred | Same reconstruction rule |
| Privacy (Informational) | Likeness | **I** | Inferred | Identity-bearing depiction |
| Privacy (Informational) | Metadata | **H** | Example-covered | Type H communication/interaction metadata |
| Privacy (Informational) | Internal-state-adjacent information | **N** | Explicit | [Protected Internal-State Boundary](../../core_05_band_continuity.md#protected-internal-state-boundary-constitutional) |
| Protected Internal-State Boundary | Internal states and reconstructions | **N** | Explicit | Home assessment + Type N definition |
| [Identity Data Protection](../../core_05_band_continuity.md#identity-data-protection) | Identity and attribution data | **H; I** | Explicit | Home names Type H, I |
| Identity Data Protection | Identity-linked reconstruction of internal states | **N** | Explicit | H/I → N ban |
| [Surveillance Boundary](../../core_05_band_continuity.md#surveillance-boundary) | Ordinary security logging / measurement | **H** | Inferred | Type H operational logs |
| Surveillance Boundary | Monitoring that reconstructs protected internal state | **N** | Explicit | Via Protected Internal-State Boundary |
| [Training-Data Use](../../core_05_band_continuity.md#training-data-use-constitutional) | Identifiable sentient-produced work used as training data | **H; I** | Inferred | N if it reconstructs inner states |
| [Likeness and Documentary Depiction Interface](../../core_05_band_continuity.md#likeness-and-documentary-depiction-interface-constitutional) | Recognizably identifiable likeness, voice, synthetic depiction | **I** | Inferred | |
| [Creative Work Attribution](../../core_05_band_continuity.md#creative-work-attribution-constitutional) | Authorship / ownership / attribution records | **I** | Example-covered | Type I authorship examples |
| [Protected Data and Internal-State Publication Constraint](../../core_05_band_oversight.md#protected-data-and-internal-state-publication-constraint) | Restricted data and protected internal-state content at publication | **N** | Explicit | Assessment names Type N; other restricted types follow most-restrictive |
| [Security-Sensitive Disclosure Balance](../../core_05_band_oversight.md#security-sensitive-disclosure-balance) | Exploit-enabling detail (deferred) | **S** | Explicit | Then Type O summaries |
| Security-Sensitive Disclosure Balance | Post-mitigation public summary | **O** | Explicit | |
| [High-Impact and Systemic Harm Publication Constraint](../../core_05_band_oversight.md#high-impact-and-systemic-harm-publication-constraint) | Publication that would enable targeting, exploitation, or safeguard evasion | **S** | Inferred | Functional overlap with Type S; home has no letter |
| [Protected Intimate-Signal Gating](../../core_05_band_participation.md#protected-intimate-signal-gating-and-article-x-c-status-circumvention) | Intimate media, sexual-history signals, intimate-status inferences | **I; N** | Inferred | Most-restrictive wins |
| [Consent](../../core_05_band_participation.md#consent-constitutional) | Consent receipts and revocation events | **H** | Example-covered | Type H examples |
| Consent | Identity-sensitive participation and consent records | **I** | Example-covered | Type I examples |
| [Consent, Sexual](../../core_05_band_participation.md#consent-sexual) | Sexual-consent documentation | **I; N** | Inferred | |
| [Instantiation Consent](../../core_05_band_participation.md#instantiation-consent-constitutional) | Instantiation-consent documentation | **H; I** | Inferred | |
| [Ecological Footprint](../../core_05_band_continuity.md#ecological-footprint) | Energy, materials, emissions, land-use, related burden data | **E** | Example-covered | Published baseline artifacts are Type O |
| [Environmental Preconditions](../../core_05_band_continuity.md#environmental-preconditions-constitutional) | Biophysical condition data | **E** | Example-covered | |
| [Emergency and Contingency](../../core_05_band_continuity.md#emergency-and-contingency-constitutional) | Emergency/hazard coordination streams | **E** | Example-covered | |
| Emergency and Contingency | Published emergency notices | **O** | Example-covered | Type O examples |
| [Evidence Preservation](../../core_05_band_oversight.md#evidence-preservation) | Records; artifacts; provenance; testimony; system states; custody; exculpatory material | **G** (logs **H; G**) | Inferred / Example-covered | Logs are Type H / Type G examples; other evidence kinds inferred. Restricted evidence may be **S** |
| [Protected Reporting (Whistleblowing)](../../core_05_band_accountability.md#protected-reporting-whistleblowing) | Protected reports and reporter-identifying material | **G; I; S** | Inferred | |
| [Verified Inputs for Standing](../../core_05_band_accountability.md#verified-inputs-for-standing) | Verified contribution records and violation findings | **O** (default); **G / H / I** hold-back | Inferred | Same packet as the Standing Record basis |
| [Protected Characteristics](../../core_05_band_participation.md#protected-characteristics-constitutional) | Stored protected-characteristic attributes | **I** | Inferred | Intimate-characteristic inferences may also be N |
| [Competency Clearance](../../core_05_band_accountability.md#competency-clearance) | Clearance status records | **G; I** | Inferred | Definition is a status; the durable file is typed |
| [Standing Lock](../../core_05_band_accountability.md#standing-lock) | Lock status records | **G; I** | Inferred | |
| [Attributable Action](../../core_05_band_accountability.md#attributable-action-constitutional) | Reconstructable action traces | **G; I; H** | Inferred | Systems-layer artifact: [CS-4 §10](../../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) |
| [Attribution Integrity](../../core_05_band_accountability.md#attribution-integrity-constitutional) | Identity fields and logs relied on for attribution | **I; H; G** | Inferred | |

---

## Rest-of-corpus matrix

### Rights floor

| Home | Data kind | Type(s) | Status |
|---|---|---|---|
| [Article VII-B](../../core_06-06_rights_part_b.md#article-vii-b-internal-state-boundary-and-type-n-protection) | Outputs that functionally approximate internal states | **N** | Explicit |
| [Article VIII-A](../../core_06-06_rights_part_b.md#article-viii-a-self-ownership-of-likeness-and-reputation) | Recognizably identifiable likeness, voice, reputation-bearing depictions | **I** | Inferred (article points at CS-2 generally) |
| [Article VIII-B](../../core_06-06_rights_part_b.md#article-viii-b-experiential-and-derived-data-rights) | A sentient's own experiential and interaction-derived data | **H; N** | Inferred for the experience object; Explicit N for reconstructing another sentient's inner states |
| [Article VIII-D](../../core_06-06_rights_part_b.md#article-viii-d-creative-work-training-data-use-and-anti-displacement) | Creative work used as training data | **H; I** | Inferred |
| [Article I-B](../../core_06-06_rights_part_a.md#article-i-b-ecological-footprint-and-transparency) | Ecological-footprint disclosure data | **E; O** | Example-covered |

### CS-2 Part B examples

Forty-five example kinds that are not already a Chapter Five row are listed in the CSV under `layer=cs2-example`. All are **Example-covered**. Grouped:

- **Type E:** ecological/environmental condition streams; infrastructure health; resource availability; system health/degradation; environmental-harm load.
- **Type G:** internal governance records; full deliberation/voting records; audit trails and workpapers; operational telemetry at source fidelity; full-fidelity risk analyses; challenge/review dockets.
- **Type O:** published procedural rules; aggregated/de-identified/summary/delayed substitutes; public eligibility rules for Type G audit; versioned public change/status/performance/failure summaries.
- **Type H:** transaction/transfer records; access and usage events; participation records; dependency/interoperability events; resource-usage records.
- **Type I:** credentials/keys/signatures; identifiers; persistent pseudonyms in health/wellbeing context; health/clinical/genomic records; biometric/substrate health measurements (also **N** where they reconstruct inner states); identifying financial records.
- **Type N:** thoughts/intentions/beliefs; subjective experiences and internal perception; private cognitive processes and internal memory; non-public emotional/psychological states; physical or behavioral data that could reconstruct the above; derived inferences about beliefs, intent, or cognition ([CS-2.6](../../corpus_systems/cs_02_a_information_types_and_handling.md#cs-2-6-data-separation-and-attribution)).
- **Type S:** exploit surfaces; sensitive topology; de-anonymization/privileged-access mechanisms; containment credentials and cryptographic material; unpatched-exploit materials; abuse-detection methods; detection signatures/thresholds/scoring models; adversary tooling; incident-response procedures; active-incident containment; active investigation data; protected-party/witness/location data; restricted evidence.

### Incorporated companions

| Home | Data kind | Type(s) | Status |
|---|---|---|---|
| [CJS-3.3](../../corpus_joint_structure/cjs_03u_audit_process.md) / CJS-3.4 | Audit-process findings, reports, eligibility rules (Type O where feasible, then qualified Type G) | **O; G** | Explicit |
| [CS-4 §10](../../corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) | Inspectable attributable-action log (five-element set). Not a Standing Record | **G; I; H** | Inferred |
| CS-4 §10 | Model weights, private deliberation, protected internal states (not required as the standing record; residual rule if internals are the only attribution path) | **N** | Explicit |
| [CF-15.1](../../corpus_forum/cf_15_standard_records_forms_evidence_artifacts.md#cf-151-minimum-record-set) | Minimum forum templates (intake through post-incident review; 21 named templates). Plus **S** for forensic/investigative/restricted-evidence; **O** for publication-delay logs. CF-15.3 access classes are access tags, not a second type taxonomy | **G; I** | Inferred |
| CF-15.1 | Sentience-Status Adjudication Record (dedicated CF format; same mapping as the Chapter Five home) | **O** (default); **G / H / I** hold-back | Inferred |
| [CF-15.4](../../corpus_forum/cf_15_standard_records_forms_evidence_artifacts.md#cf-154-evidence-artifact-handling) | Forum evidence artifacts (typed by content under CS-2.2) | **G; H; S** | Inferred |

CF-15.3 does not create types. It tags who may see a record. Under the operator-directed default, a Forum Case Record (and CF-15 templates that instantiate it) is Type O unless a justified security or privacy hold-back retypes a portion to G, H, or I — or to S for restricted evidence. The public-facing tag is then ordinary Type O posture, not a special extract from a Type G file.

---

## Gap register

**Taxonomy gaps (no defensible type): none.** Every named kind in this inventory received at least one of E, G, O, H, I, N, S.

**Source-assignment gaps:** the home that names the kind does not yet assign a letter. Later corpus edits, if any, should live on the Chapter Five (or article) home, with a CS-2 Part B example only where the kind is a systems-layer illustration rather than a constitutional record.

Recommended placement for a later pass (not done here):

### Named records — add type letter on the Chapter Five home

| Kind | Suggested type(s) | Where to edit later |
|---|---|---|
| Charter source instrument | **O** default; **G / H / I** hold-back. Unpublished papers that are not yet the Charter may remain **G** | [Charter](../../core_05_band_continuity.md#charter) |
| System Certification Record source | **O** default; **G / H / I** hold-back (public view already Explicit **O**) | Chapter Five home |
| System Classification Record source | **O** default; **G / H / I** hold-back | Chapter Five home |
| System Data Types Record source | **O** default; **G / H / I** hold-back | Chapter Five home; CS-2 §8 already owns the file |
| Forum Case Record | **O** default; **G / H / I** hold-back; **S** if restricted evidence | Chapter Five home; CF-15 may point, not redefine |
| Standing Record | **O** default; **G / H / I** hold-back | Chapter Five home |
| Unified Incident Record | **O** default; **G / H / I** hold-back; **S** if investigation- or exploit-sensitive | Chapter Five home |
| Sentience-Status Adjudication Record | **O** default; **G / H / I** hold-back | Chapter Five home; CF protocol implements |
| Stakeholder Rights-Collision Record | **O** default; **G / H / I** hold-back | Chapter Five home |
| Non-Compliance Finding Profile | **G** | Chapter Five home (routing metadata; not retargeted to O-default) |
| Competency Clearance / Standing Lock files | **G; I** | Chapter Five homes (status files; not in the O-default named-record set) |
| Verified Inputs for Standing | Same as Standing Record: **O** default; **G / H / I** hold-back | Do not create a second type |
| CS-4 inspectable-action log | **G; I; H** | CS-4 §10 (systems-layer); Chapter Five Attributable Action may point |
| CF-15.1 templates that instantiate the named records above | Follow the Chapter Five home (**O** default) | CF-15 should point at CS-2, not invent types |

### Privacy and rights-floor kinds — type the category list

| Kind | Suggested type(s) | Where to edit later |
|---|---|---|
| Privacy: personal | **I** if identifying, else **H** | [Privacy (Informational)](../../core_05_band_continuity.md#privacy-informational) in-scope list |
| Privacy: experiential / behavioral | **H**; **N** if reconstruction | Privacy home; Article VIII-B already Explicit N for the back-door |
| Privacy: likeness | **I** | Privacy home and/or Likeness interface |
| Training-Data Use | **H; I** | Chapter Five Training-Data Use; Article VIII-D may point |
| Article VIII-A likeness as a kind | **I** | Article VIII-A (currently CS-2 generally) |
| Intimate-signal / sexual-consent documentation | **I; N** | Protected Intimate-Signal Gating; Consent, Sexual |
| Protected Characteristics as stored attributes | **I** | Protected Characteristics home |
| High-Impact publication that enables exploitation | **S** | High-Impact constraint home (Security-Sensitive already Explicit S for exploit detail) |
| Evidence Preservation named kinds other than logs | **G** (S if restricted) | Evidence Preservation home |
| Protected reporting packets | **G; I; S** | Protected Reporting home |
| Ordinary surveillance-boundary logging | **H** | Surveillance Boundary (out-of-scope ordinary logging still produces data) |

Do **not** add a new type letter. CS-2.2 already covers mixed and reconstructed data. The missing piece is an on-home assignment so operators are not left to infer from Part B examples alone.

---

## Method notes

1. Walked Chapter Five Definitions A–Z (224). Tagged each as data artifact, data-category, or N/A.
2. Split Privacy (Informational) and Evidence Preservation into the kinds their in-scope lists name.
3. Harvested CS-2 Part B example bullets; omitted duplicates of Chapter Five kinds.
4. Added rights-floor data kinds (Articles VII-B, VIII-A/B/D, I-B) and incorporated companion records (CJS-3.3/3.4, CS-4 §10, CF-15.1/15.4).
5. Assigned at least one type per kind. Multi-type rows follow CS-2.2 most-restrictive.
6. Operator correction (2026-08-31): named constitutional records listed in the artifact table default to Type O; G, H, or I only as justified security/privacy hold-backs. That replaces the first-pass inference that treated the full source file as Type G with Type O only as a public extract.
7. Did not open `ai_corpus/indexes/id_resolver.json` for meaning.

Hydration was from source files cited in the `cite` column of the CSV. If this audit and a source file disagree, the source wins.
