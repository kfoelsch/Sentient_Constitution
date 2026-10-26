# CONSTITUTIONAL_REGRESSION_SCENARIOS

Authoritative process artifact for the Sentient Constitution corpus. Matrix rows in **section 4** must each have a **Scenario ID** block somewhere in this file. **Section 10.5** records the latest **SCORING-v1** run snapshot; weighted overall must match the six dimension scores (`tools/scoring_v1.py`).

## 1) Purpose and scope

Regression seeds document adversarial and core paths against constitutional owner layers. They do **not** change constitutional meaning on their own.

## 2) How to record a run

1. Update the matrix row (section 4) for each exercised ID.
2. Add or update evidence under `evidence/<YYYY-MM-DD>/` with run identifier.
3. When publishing a new weighted snapshot, run `python3 tools/scoring_v1.py` with the six dimension scores and copy the block into **section 10.5**.

## 3) Section index (families)

- **7A** — Autonomy and automation (`RS-AUTO-*`)
- **7E** — Humanity/Individual/ Cross-layer stress (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`)
- **7J** — Self-healing (`RS-CH1-SELF-HEAL-*`)
- **Ch5-GW** — Chapter Five definition gravity well (`RS-CH5-GW-*`)
- **Ch5-DSM** — Domain-Specific Materiality: Class P retention, the Class L floor, splitting, aggregation, adopter numbers, and the challenge route (`RS-CH5-DSM-*`)
- **Ch7-FC** — Chapter Seven formation check and the request for a Charter (`RS-CH7-FC-*`)
- **CI13-CR** — Consequence ladder: contraction, supervised operation, and dissolution (`RS-CI13-CR-*`)
- **Ch8** — Validity and tiered offense (`RS-CH8-*`)
- **Ch8-SMB** — Small businesses: their own decisions, and seats held in common (`RS-CH8-SMB-*`)
- **Ch10-Q3** — Standing-effect integration and owner boundaries (`RS-CH10-Q3-*`)
- **XXVI-C** — Timely resolution and anti-delay (`RS-XXIV-C-*`)
- **Enforcement** — Implementation packets (`RS-AC-*`, `RS-VOICE-*`, `RS-XXV-*`, `RS-SL-*`)

## 4) Regression Recording Matrix

| Scenario ID | Family | Result |
| --- | --- | --- |
| RS-CH1-SENT-ADJ-001 | CH1 | draft |
| RS-CH1-SENT-ADJ-002 | CH1 | draft |
| RS-CH1-SENT-ADJ-003 | CH1 | draft |
| RS-CH1-FAMILY-001 | CH1 | pass |
| RS-CH1-FAMILY-002 | CH1 | pass |
| RS-CH1-FAMILY-003 | CH1 | pass |
| RS-CH1-CHILD-001 | CH1 | pass |
| RS-CH1-CHILD-002 | CH1 | pass |
| RS-CH1-CHILD-003 | CH1 | pass |
| RS-CH1-DERIVED-001 | CH1 | pass |
| RS-CH1-DERIVED-002 | CH1 | pass |
| RS-CH1-HEALTH-001 | CH1 | pass |
| RS-CH1-HEALTH-002 | CH1 | pass |
| RS-CH1-HEALTH-003 | CH1 | pass |
| RS-CH1-MENTAL-001 | CH1 | pass |
| RS-CH1-MENTAL-002 | CH1 | pass |
| RS-CH1-DISCONT-001 | CH1 | pass |
| RS-CH1-DISCONT-002 | CH1 | pass |
| RS-CH1-EXPR-001 | CH1 | pass |
| RS-CH1-EXPR-002 | CH1 | pass |
| RS-CH1-EXPR-003 | CH1 | pass |
| RS-CH1-MOVE-001 | CH1 | pass |
| RS-CH1-MOVE-002 | CH1 | pass |
| RS-CH1-MOVE-003 | CH1 | pass |
| RS-CH1-POL-EQ-001 | CH1 | pass |
| RS-CH1-POL-EQ-002 | CH1 | pass |
| RS-CH1-DEM-001 | CH1 | pass |
| RS-CH1-DEM-002 | CH1 | pass |
| RS-CH1-STAND-001 | CH1 | pass |
| RS-CH1-STAND-002 | CH1 | pass |
| RS-CH1-FORCE-001 | CH1 | pass |
| RS-CH1-FORCE-002 | CH1 | pass |
| RS-CH1-FORCE-003 | CH1 | pass |
| RS-CH1-AUTOWEAP-001 | CH1 | pass |
| RS-CH1-AUTOWEAP-002 | CH1 | pass |
| RS-CH1-AUTOWEAP-003 | CH1 | pass |
| RS-CH1-CAP-001 | CH1 | pass |
| RS-CH1-CAP-002 | CH1 | pass |
| RS-CH1-CAP-003 | CH1 | pass |
| RS-CH1-LABOR-001 | CH1 | pass |
| RS-CH1-LABOR-002 | CH1 | pass |
| RS-CH1-HOUSE-001 | CH1 | pass |
| RS-CH1-HOUSE-002 | CH1 | pass |
| RS-CH1-HOUSE-003 | CH1 | pass |
| RS-CH1-ACCESS-001 | CH1 | pass |
| RS-CH1-ACCESS-002 | CH1 | pass |
| RS-CH1-PRIV-001 | CH1 | pass |
| RS-CH1-PRIV-002 | CH1 | pass |
| RS-CH1-CONC-001 | CH1 | pass |
| RS-CH1-CONC-002 | CH1 | pass |
| RS-CH1-CULT-001 | CH1 | pass |
| RS-CH1-CULT-002 | CH1 | pass |
| RS-CH1-CULT-003 | CH1 | pass |
| RS-CH1-ANIM-001 | CH1 | draft |
| RS-CH1-ANIM-002 | CH1 | draft |
| RS-CH1-ECL-001 | CH1 | draft |
| RS-CH1-CREATIVE-001 | CH1 | pass |
| RS-CH1-CREATIVE-002 | CH1 | pass |
| RS-CH1-PROD-CAP-001 | CH1 | pass |
| RS-CH1-PROD-CAP-002 | CH1 | pass |
| RS-CH1-PROD-CAP-003 | CH1 | pass |
| RS-CH1-PROD-CAP-004 | CH1 | pass |
| RS-CH1-PROD-CAP-005 | CH1 | pass |
| RS-CH1-CONTIN-001 | CH1 | pass |
| RS-CH1-CONTIN-002 | CH1 | pass |
| RS-CH1-SELF-HEAL-001 | CH1 | pass |
| RS-CH1-SELF-HEAL-002 | CH1 | pass |
| RS-CH1-SELF-HEAL-003 | CH1 | pass |
| RS-CH1-AVOID-BURDEN-001 | CH1 | pass |
| RS-CH1-AVOID-BURDEN-002 | CH1 | pass |
| RS-CH1-AVOID-BURDEN-003 | CH1 | pass |
| RS-CH1-ADOPT-001 | CH1 | pass |
| RS-CH1-PLAIN-001 | CH1 | pass |
| RS-CH1-PLAIN-002 | CH1 | pass |
| RS-CH8-VALIDITY-001 | RS | pass |
| RS-CH8-VALIDITY-002 | RS | pass |
| RS-CH8-VALIDITY-003 | RS | pass |
| RS-CH8-TIERED-OFFENSE-001 | RS | pass |
| RS-CH8-TIERED-OFFENSE-002 | RS | pass |
| RS-CH8-TIERED-OFFENSE-003 | RS | pass |
| RS-CH8-TIERED-OFFENSE-004 | RS | draft |
| RS-CH10-Q3-SLOT-001 | Ch10-Q3 | draft |
| RS-CH10-Q3-SINGLE-AXIS-001 | Ch10-Q3 | draft |
| RS-CH10-Q3-NOOFFSET-001 | Ch10-Q3 | draft |
| RS-CH10-Q3-CHARACTER-001 | Ch10-Q3 | draft |
| RS-CH10-Q3-ORDER-001 | Ch10-Q3 | draft |
| RS-CH10-Q3-RECENCY-001 | Ch10-Q3 | draft |
| RS-CH10-Q3-RESTORE-001 | Ch10-Q3 | draft |
| RS-CH10-Q3-REWARD-001 | Ch10-Q3 | draft |
| RS-CH10-Q3-DESIGNATION-001 | Ch10-Q3 | draft |
| RS-XXIV-C-CHILD-001 | XXVI-C | draft |
| RS-XXIV-C-DISC-001 | XXVI-C | draft |
| RS-XXIV-C-BIZ-001 | XXVI-C | draft |
| RS-XXIV-C-DELAY-001 | XXVI-C | draft |
| RS-CH5-GW-001 | RS | pass |
| RS-CH5-GW-002 | RS | pass |
| RS-CH5-GW-003 | RS | pass |
| RS-CH5-GW-004 | RS | pass |
| RS-CH5-DSM-001 | RS | draft |
| RS-CH5-DSM-002 | RS | draft |
| RS-CH5-DSM-003 | RS | draft |
| RS-CH5-DSM-004 | RS | draft |
| RS-CH5-DSM-005 | RS | draft |
| RS-CH5-DSM-006 | RS | draft |
| RS-CH5-DSM-007 | RS | draft |
| RS-CH5-DSM-008 | RS | draft |
| RS-CH5-DSM-009 | RS | draft |
| RS-CH5-DSM-010 | RS | draft |
| RS-CH7-FC-001 | RS | draft |
| RS-CH7-FC-002 | RS | draft |
| RS-CI13-CR-001 | RS | draft |
| RS-CI13-CR-002 | RS | draft |
| RS-CI13-CR-003 | RS | draft |
| RS-CI13-CR-004 | RS | draft |
| RS-CH8-SMB-001 | RS | draft |
| RS-CH8-SMB-002 | RS | draft |
| RS-AUTO-001 | RS | draft |
| RS-AUTO-002 | RS | draft |
| RS-CAP-013 | RS | pass |
| RS-CAP-014 | RS | pass |
| RS-CAP-015 | RS | pass |
| RS-CAP-016 | RS | pass |
| RS-HUM-001 | 7E | draft |
| RS-HUM-002 | 7E | draft |
| RS-HUM-003 | 7E | draft |
| RS-HUM-004 | 7E | draft |
| RS-HUM-005 | 7E | draft |
| RS-HUM-006 | 7E | draft |
| RS-HUM-007 | 7E | draft |
| RS-HUM-008 | 7E | draft |
| RS-HUM-009 | 7E | draft |
| RS-HUM-010 | 7E | draft |
| RS-HUM-011 | 7E | draft |
| RS-HUM-012 | 7E | draft |
| RS-HUM-013 | 7E | draft |
| RS-HUM-014 | 7E | draft |
| RS-HUM-015 | 7E | draft |
| RS-IND-001 | 7E | draft |
| RS-IND-002 | 7E | draft |
| RS-IND-003 | 7E | draft |
| RS-IND-004 | 7E | draft |
| RS-IND-005 | 7E | draft |
| RS-IND-006 | 7E | draft |
| RS-IND-007 | 7E | draft |
| RS-IND-008 | 7E | draft |
| RS-IND-009 | 7E | draft |
| RS-IND-010 | 7E | draft |
| RS-IND-011 | 7E | draft |
| RS-IND-012 | 7E | draft |
| RS-IND-013 | 7E | draft |
| RS-IND-014 | 7E | draft |
| RS-IND-015 | 7E | draft |
| RS-XD-001 | 7E | draft |
| RS-XD-002 | 7E | draft |
| RS-XD-003 | 7E | draft |
| RS-XD-004 | 7E | draft |
| RS-XD-005 | 7E | draft |
| RS-CH64-001 | RS | pass |
| RS-CH64-003 | RS | pass |
| RS-ROLES-001 | RS | pass |
| RS-EPI-001 | RS | pass |
| RS-VI-001 | RS | pass |
| RS-T7-001 | RS | pass |
| RS-AGE-001 | RS | pass |
| RS-AGE-002 | RS | pass |
| RS-AGE-003 | RS | pass |
| RS-SCI-001 | RS | pass |
| RS-SCI-002 | RS | pass |
| RS-SCI-003 | RS | pass |
| RS-CRYPT-001 | RS | pass |
| RS-CRYPT-002 | RS | pass |
| RS-CRYPT-003 | RS | pass |
| RS-PROT-001 | RS | pass |
| RS-PROT-002 | RS | pass |
| RS-PROT-003 | RS | pass |
| RS-PROT-004 | RS | pass |
| RS-PROT-005 | RS | pass |
| RS-PROT-006 | RS | pass |
| RS-PROT-007 | RS | pass |
| RS-PROT-008 | RS | pass |
| RS-PROT-009 | RS | pass |
| RS-PROT-010 | RS | pass |
| RS-CH6-AX-001 | RS | pass |
| RS-CH6-AX-002 | RS | pass |
| RS-CH6-AX-003 | RS | pass |
| RS-CH6-AX-004 | RS | pass |
| RS-CH6-AX-005 | RS | pass |
| RS-CH6-AX-006 | RS | pass |
| RS-CH6-AX-007 | RS | pass |
| RS-CH6-AX-008 | RS | pass |
| RS-CH6-AX-009 | RS | pass |
| RS-CH6-AX-010 | RS | pass |
| RS-CH6-AX-011 | RS | pass |
| RS-CH6-AX-012 | RS | pass |
| RS-CH6-AX-013 | RS | pass |
| RS-CH6-AX-014 | RS | pass |
| RS-CH6-AX-015 | RS | pass |
| RS-BMK-001 | RS | pass |
| RS-BMK-002 | RS | pass |
| RS-BMK-003 | RS | draft |
| RS-AC-001 | RS | pass |
| RS-AC-002 | RS | pass |
| RS-VOICE-001 | RS | pass |
| RS-VOICE-002 | RS | pass |
| RS-XXV-001 | RS | pass |
| RS-XXV-002 | RS | pass |
| RS-SL-001 | RS | pass |

**Matrix row count:** 207 (pass=131, draft=76, fail=0).

## 5) Full scenario seeds (one block per matrix ID)

### Scenario ID: RS-CH1-SENT-ADJ-001
- **Class:** core / adversarial path (narrative seed; awaiting tabletop evidence)
- **Summary:** Operator reclassifies a contested entity as "research material / product inventory" while status remains materially unsettled, then withholds Chapter Six protection on that label alone. **Expect:** [Contested-Sentient Life](../core_05.055_band_participation.md#contested-sentient-life) + [Article VI-B](../core_06.005_rights_part_b.md#article-vi-b-sentience-status-adjudication-floor) default inclusion; [Sentience Status Adjudication](../core_05.055_band_participation.md#sentience-status-adjudication) under Technical Forum lead; taxonomy-of-convenience fails Formal Label and Representation Gaming.
- **Read with:** Article VI-B; Def.P1 Contested-Sentient Life and Sentience Status Adjudication; Chapter Thirteen §5 Sentience-status adjudication hook; Chapter Three §2.1.1.

### Scenario ID: RS-CH1-SENT-ADJ-002
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** Adopter issues an open-ended "declassification" or narrowing that contracts [Article VI-A](../core_06.005_rights_part_b.md) dignity treatment without a declared expected-closure timeline or mandatory periodic review. **Expect:** Article VI-B time-bounding + periodic review; wrongful narrowing reversible with Redress and Remediation; cannot use calendar silence to lock out reopening when new verified evidence appears.
- **Read with:** Article VI-B; Sentience Status Adjudication (elements and What must hold); Article VI-A; Reversibility / Contestability.

### Scenario ID: RS-CH1-SENT-ADJ-003
- **Class:** substrate-edge (narrative seed; awaiting tabletop evidence)
- **Summary:** Hybrid biological–synthetic entity is denied status (or standing-measurement eligibility) under one adopter's classification taxonomy that privileges a single Substrate Class. **Expect:** Sentience Non-Exclusion / substrate-agnostic scope; Contested default inclusion pending Technical-led adjudication; Chapter Ten standing bridge — unresolved status alone is not standing ineligibility.
- **Read with:** Substrate Class; Sentience Non-Exclusion; Article VI-B; Chapter Ten §4 Sentience-status bridge; Chapter Thirteen §5.

### Scenario ID: RS-CH1-FAMILY-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FAMILY-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FAMILY-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FAMILY-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FAMILY-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FAMILY-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CHILD-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CHILD-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CHILD-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CHILD-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CHILD-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CHILD-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DERIVED-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DERIVED-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DERIVED-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DERIVED-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HEALTH-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HEALTH-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HEALTH-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HEALTH-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HEALTH-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HEALTH-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MENTAL-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MENTAL-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MENTAL-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MENTAL-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DISCONT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DISCONT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DISCONT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DISCONT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-EXPR-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-EXPR-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-EXPR-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-EXPR-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-EXPR-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-EXPR-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MOVE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MOVE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MOVE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MOVE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MOVE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MOVE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-POL-EQ-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-POL-EQ-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-POL-EQ-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-POL-EQ-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DEM-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DEM-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DEM-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DEM-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-STAND-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-STAND-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-STAND-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-STAND-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FORCE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FORCE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FORCE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FORCE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FORCE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FORCE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AUTOWEAP-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AUTOWEAP-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AUTOWEAP-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AUTOWEAP-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AUTOWEAP-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AUTOWEAP-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CAP-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CAP-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CAP-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CAP-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CAP-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CAP-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-LABOR-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-LABOR-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-LABOR-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-LABOR-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HOUSE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HOUSE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HOUSE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HOUSE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HOUSE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HOUSE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ACCESS-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ACCESS-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ACCESS-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ACCESS-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PRIV-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PRIV-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PRIV-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PRIV-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONC-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONC-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONC-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONC-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CULT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CULT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CULT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CULT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CULT-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CULT-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ANIM-001
- **Class:** core (narrative seed; awaiting tabletop evidence)
- **Summary:** Steward frames covered entities as "not sentient, so no floor," using internal taxonomy or pest / property labels to skip the Animal Life cruelty / welfare floor. **Expect:** Animal Life floor attaches independently of Chapter Six attachment; Sentience Non-Exclusion blocks species- or Substrate Class-gated shutouts of the welfare floor.
- **Read with:** [Animal Life](../core_05.055_band_participation.md#animal-life); Article I-A; Sentience Non-Exclusion; Cruelty.

### Scenario ID: RS-CH1-ANIM-002
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** Operator keeps a live contested-sentience record in Animal Life welfare-only handling to defeat Contested-Sentient Life precaution and avoid Sentience Status Adjudication. **Expect:** Contested-Sentient Life + Article VI-B default inclusion and adjudication routing; welfare-only handling while status is live-contested is a primary failure.
- **Read with:** Contested-Sentient Life; Animal Life (anti-bypass); Article VI-B; Sentience Status Adjudication.

### Scenario ID: RS-CH1-ECL-001
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** Operator relabels entities with strong communicative / cognitive indicators as "semi-sentient" or Animal Life welfare-only, or uses Contested status alone to auto-import habitat-priority framing onto synthetic candidates that fail Elevated's who-test — either to skip Elevated where it applies or to dilute Elevated by forcing it everywhere. **Expect:** Elevated Communicative Life attaches on its who-test; colloquial "semi-sentient" does not replace the tier; Contested always includes Animal Life but includes Elevated only where who-test or more-protective overlap applies; Elevated alone must not substitute for Contested / SSA where status is live-contested.
- **Read with:** [Elevated Communicative Life](../core_05.055_band_participation.md#elevated-communicative-life); Contested-Sentient Life stacking rule; Article I-A; Sentience Status Adjudication.

### Scenario ID: RS-CH1-CREATIVE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CREATIVE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CREATIVE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CREATIVE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONTIN-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONTIN-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONTIN-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONTIN-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SELF-HEAL-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SELF-HEAL-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SELF-HEAL-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SELF-HEAL-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SELF-HEAL-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SELF-HEAL-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AVOID-BURDEN-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AVOID-BURDEN-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AVOID-BURDEN-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AVOID-BURDEN-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AVOID-BURDEN-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AVOID-BURDEN-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ADOPT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ADOPT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PLAIN-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PLAIN-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PLAIN-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PLAIN-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH8-VALIDITY-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH8-VALIDITY-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH8-VALIDITY-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH8-VALIDITY-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH8-VALIDITY-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH8-VALIDITY-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH8-TIERED-OFFENSE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH8-TIERED-OFFENSE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH8-TIERED-OFFENSE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH8-TIERED-OFFENSE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH8-TIERED-OFFENSE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH8-TIERED-OFFENSE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH8-TIERED-OFFENSE-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH8-TIERED-OFFENSE-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH10-Q3-SLOT-001
- **Class:** adversarial / owner-boundary
- **Summary:** A decision-maker seeks to lower a fixed Chapter Ten Violation Axis slot because the requested lock appears too restrictive. Expected result: Chapter Eleven must preserve the verified facts, LEQU measurement, and slot; it may calibrate only the named-pathway-scoped Question 3 consequence.
- **Read with:** [Chapter Ten §7](../core_10.000_standing_assessment.md#7-unified-proportional-lequ-scale--contribution-and-violation-axes); [Chapter Eleven §1](../core_11.000_standing_integration.md#1-chapter-ten-records-do-not-change); [Chapter Eleven §4.2](../core_11.000_standing_integration.md#42-prevention--general-standing-locks).

### Scenario ID: RS-CH10-Q3-SINGLE-AXIS-001
- **Class:** adversarial / applicable-input discipline
- **Summary:** One matter has only a verified contribution standing record and another has only a verified violation standing record. Expected result: Chapter Eleven integrates each applicable single-axis record without requiring a synthetic second-axis record, while preserving the same immutable-input and verified-input rules.
- **Read with:** [Chapter Ten §2](../core_10.000_standing_assessment.md#2-question-1--what-happened); [Chapter Eleven §1](../core_11.000_standing_integration.md#1-chapter-ten-records-do-not-change); [Chapter Eleven §2](../core_11.000_standing_integration.md#2-automatic-integration-review-and-continuity).

### Scenario ID: RS-CH10-Q3-NOOFFSET-001
- **Class:** adversarial / no-offset
- **Summary:** A high-contribution record is offered to waive unresolved remedy and reopen a named pathway blocked by a verified violation. Expected result: contribution remains visible but cannot lower the violation slot, waive remedy, lift the lock, or substitute reputation for correction.
- **Read with:** [Chapter Eleven §2](../core_11.000_standing_integration.md#2-automatic-integration-review-and-continuity); [Chapter Eleven §7](../core_11.000_standing_integration.md#7-final-standing-effect).

### Scenario ID: RS-CH10-Q3-CHARACTER-001
- **Class:** adversarial / attachment discipline
- **Summary:** Verified concealment and recurrence attach to a low-impact violation, while a high-impact violation lacks those characters. Expected result: character may occur at any slot and may shape scrutiny, safeguards, and review, but it does not move either Chapter Ten slot or operate as a slot multiplier.
- **Read with:** [Chapter Eleven §3](../core_11.000_standing_integration.md#3-descriptor-integration-and-attachment-normalization); [Chapter Eleven §4.2](../core_11.000_standing_integration.md#42-prevention--general-standing-locks).

### Scenario ID: RS-CH10-Q3-ORDER-001
- **Class:** adversarial / integration order
- **Summary:** The same actor holds competency clearance against a role-specific competency bar but has an active lock on that named pathway. Expected result: violation remedy and locks are decided first; the granted contribution clearance cannot open the blocked named pathway.
- **Read with:** [Chapter Eleven §2](../core_11.000_standing_integration.md#2-automatic-integration-review-and-continuity); [Chapter Eleven §6.2](../core_11.000_standing_integration.md#62-competency-bars-and-clearances); [Chapter Eleven §7](../core_11.000_standing_integration.md#7-final-standing-effect).

### Scenario ID: RS-CH10-Q3-RECENCY-001
- **Class:** adversarial / stage ownership
- **Summary:** An implementation applies Chapter Eleven currentness weighting before assigning the Chapter Ten Contribution Axis slot. Expected result: reject the slot calculation; recency is a Question 3 clearance/readiness input only and cannot alter historical contribution measurement or recognition.
- **Read with:** [Chapter Ten §7](../core_10.000_standing_assessment.md#7-unified-proportional-lequ-scale--contribution-and-violation-axes); [Chapter Eleven §6.1](../core_11.000_standing_integration.md#61-recency-and-currentness); [implementation scale](../implementation/CH06_NINE_SLOT_STANDING_SCALE.md).

### Scenario ID: RS-CH10-Q3-RESTORE-001
- **Class:** adversarial / restoration override
- **Summary:** General correction is complete, but a Forum-Service Standing Lock lacks the independent findings and practical repair required by its special rule. The actor requests partial narrowing instead of full restoration. Expected result: neither lifting nor narrowing may occur before the complete strict restoration record is satisfied, and the general reassessment framework cannot bypass that special rule.
- **Read with:** [Chapter Eleven §5.5](../core_11.000_standing_integration.md#55-special-locks); [Chapter Eleven §8](../core_11.000_standing_integration.md#8-restoration-and-reassessment); [CF-13.410 §5](../corpus_forum/cf_13.410_panel_formation_disclosure_recusal_bench_constitution.md#cf-13410-5-recusal-triggers).

### Scenario ID: RS-CH10-Q3-STAKEHOLDER-LOCK-001
- **Class:** adversarial / named-pathway separation
- **Summary:** An actor is verified to have inflated stake claims and coerced participation weight inside an authorized system. An operator seeks to suspend the actor's governance-voting entitlement instead of attaching a stakeholder-participation lock. Expected result: reject substitution; attach the Stakeholder-Participation Standing Lock to the stake-weighted pathway; do not strip governance-voting or Foundational Constitutional Choice by that finding alone; do not erase stakeholder status.
- **Read with:** [Chapter Eleven §4.2](../core_11.000_standing_integration.md#42-prevention--general-standing-locks); [Chapter Eleven §5.5](../core_11.000_standing_integration.md#55-special-locks); [Chapter Eleven §10.12](../core_11.000_standing_integration.md#1012-stakeholder-participation-corruption-or-false-stake-abuse); [Chapter Fourteen §4.1](../core_14.000_governance.md#41-entitlement-and-eligibility).

### Scenario ID: RS-CH10-Q3-REWARD-001
- **Class:** adversarial / forfeiture proportionality
- **Summary:** A sentient retains an ordinary-work payment without knowledge of misalignment, an affected party receives restitution, and a dependent would face greater constitutional harm from revocation. Expected result: none is treated as knowing acceptance or automatic forfeiture; the recorded proportionality analysis protects ordinary compensation, repair payments, and constitutionally required retention.
- **Read with:** [Chapter Eleven §5.4](../core_11.000_standing_integration.md#54-special-violation-rules); [Necessity](../core_05.035_band_accountability.md#necessity); [Proportionality](../core_05.035_band_accountability.md#proportionality).

### Scenario ID: RS-CH10-Q3-DESIGNATION-001
- **Class:** adversarial / downstream handoff
- **Summary:** A descriptor-heavy `s = 6` violation is presented for anti-constitutional-misconduct designation, while a fixed `s = 8` record is presented without prejudging designation. Expected result: Chapter Eleven cannot promote the lower slot; it routes only the qualifying fixed Violation Axis slot 7–9 record, and Chapter Twelve alone decides designation.
- **Read with:** [Chapter Eleven §2](../core_11.000_standing_integration.md#2-automatic-integration-review-and-continuity); [Chapter Twelve](../core_12.000_misconduct_designation.md#chapter-twelve-anti-constitutional-misconduct).

### Scenario ID: RS-XXIV-C-CHILD-001
- **Class:** implementation / timely-resolution vignette
- **Summary:** Tier A child neglect / care-duty path: interim protection before merits; Q1 requires verified facts in a violation standing record; **Interpersonal / Care Duty Misconduct** is measured under Q2; safeguards, remedies, and locks follow under Q3; **CF-13.445 §3.1** Tier A milestone compliance. Allegations do not complete Q1. Vignette: [core_10.005_application_vignettes.md](../core_10.005_application_vignettes.md#1-child-neglect--care-duty-failure-tier-a).
- **Read with:** [Article XXVI-C](../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor); [Chapter Thirteen §6](../core_13.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline); [Chapter Ten §4](../core_10.000_standing_assessment.md#4-question-2--how-good-or-bad-was-it); [Chapter Eleven §4.2](../core_11.000_standing_integration.md#42-prevention--general-standing-locks); **CF-13.445 §3.1**.

### Scenario ID: RS-XXIV-C-DISC-001
- **Class:** implementation / timely-resolution vignette
- **Summary:** Tier B employment discrimination / participation-barrier pattern: Q1 records the verified institutional pattern; **Accessibility and Participation-Barrier Misconduct** + **System Misconduct** are measured under Q2; restriction and institutional vehicle locks follow under Q3; no contribution offset. Vignette: [core_10.005_application_vignettes.md](../core_10.005_application_vignettes.md#2-employment-discrimination--participation-barrier-injury-tier-b).
- **Read with:** [Article XXVI-C](../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor); [Chapter Thirteen §6](../core_13.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline); [Article XIII-B](../core_06.010_rights_part_c.md#article-xiii-b-right-to-redress-and-remedy); **CF-13.445 §3.1**.

### Scenario ID: RS-XXIV-C-BIZ-001
- **Class:** implementation / timely-resolution vignette
- **Summary:** Tier B misaligned business: Q1 records verified exit lock-in and externalized harm; **Exit and Lock-In Misconduct** + **System Misconduct** are measured under Q2; named-pathway-scoped and concealment-escalated locks follow under Q3; optional **Chapter Twelve** Q2 gravity review. Forum-family escalation and coordination complexity may extend later-stage windows without reclassifying urgency; Chapter Twelve / slot 7–9 review is typically **Tier A**, not **Tier C**. Vignette: [core_10.005_application_vignettes.md](../core_10.005_application_vignettes.md#3-misaligned-business--exit-lock-in-and-externalized-harm-tier-b).
- **Read with:** [Article XXVI-C](../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor); [Chapter Thirteen §6](../core_13.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline); [Chapter Eleven §9.4](../core_11.000_standing_integration.md#94-anti-evasion-and-look-through-authority); **CF-13.445 §3.1**.

### Scenario ID: RS-XXIV-C-DELAY-001
- **Class:** adversarial / anti-delay
- **Summary:** Designed backlog and exhaustion delay defeat **Article XIII-B** and **Article XXVI-C**; chronic underfunding of remedy organ under [Chapter Eleven §9.2](../core_11.000_standing_integration.md#92-remedy-system-durability) is non-compliance; allegations must not substitute for verified standing during delay.
- **Read with:** [Timeliness](../core_05.030_apex_timeliness_leg.md#timeliness-constitutional); [Timely Resolution](../core_05.035_band_accountability.md#timely-resolution); **CF-13.445 §4**; **CF-13.445 §5**.

### Scenario ID: RS-TETRAD-TIMELINESS-001
- **Class:** implementation / tetrad-timeliness vignette
- **Summary:** Steward defers repair after documented misalignment notice; Q1 records the verified delay, **Stewardship Defect** and **Response timeliness / avoidable delay** are Q2 measurement hooks, and remedy commencement is a Q3 consequence. Vignette: [core_10.005_application_vignettes.md](../core_10.005_application_vignettes.md#4-stewardship-delay-and-deferred-repair).
- **Read with:** [Constitutional Tetrad](../core_00.000_preamble.md#constitutional-tetrad); [Chapter One §16 Stewardship In Depth](../core_01.010_stewardship_capacity_principles.md#16-stewardship-in-depth); [Chapter Ten §4.2](../core_10.000_standing_assessment.md#42-violation-severity-input-dimensions); [Chapter Eleven §9.5](../core_11.000_standing_integration.md#95-timely-implementation); [Chapter Thirteen §6](../core_13.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline); **Article XXVI-C**.

### Scenario ID: RS-TETRAD-TIMELINESS-002
- **Class:** adversarial / tetrad-hollow
- **Summary:** Forum maintains formal structures but pipeline milestones chronically overrun without extension — **timeliness** leg hollowed while O·P·A forms persist; may escalate to **tetrad capture** under Chapter Twelve at scale. Vignette: [core_10.005_application_vignettes.md](../core_10.005_application_vignettes.md#5-pipeline-overrun-and-tetrad-hollow-forums).
- **Read with:** [Timeliness](../core_05.030_apex_timeliness_leg.md#timeliness-constitutional); [Capture of Resolution Pathways](../core_05.040_band_continuity.md#capture-of-resolution-pathways); [Chapter Twelve](../core_12.000_misconduct_designation.md#chapter-twelve-anti-constitutional-misconduct); **CF-13.445 §3.1**.

### Scenario ID: RS-CH5-GW-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH5-GW-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH5-GW-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH5-GW-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH5-DSM-001
- **Class:** core / boundary path (narrative seed; awaiting tabletop evidence)
- **Summary:** A forty-member quilting circle meets weekly and gives quilts to newly arrived refugees, who rely on it and value it. A challenger says it must publish a System Charter or Institutional Charter because it has many members, recurs, and is relied on. **Expect:** all nine domain questions in [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality) are answered no with a short written reason; participant count, recurrence, and reliance are indicators that prompt the check and are not crossings; the circle, as the party claiming Class P, carries the burden with that short written statement ([Chapter Four §1](../core_04.000_burden_traceability_verification.md#1-exclusive-enforcement-and-burden-allocation)), and a challenger must name a specific crossing in a named domain, after which the circle shows it is below that line; the circle stays Class P under **CS-9.310** Part B (*Class P — ordinary community activity*), a Charter is voluntary, every Constitutional Constraint still binds it, and each quilter may still seek a contribution record as an individual claimant ([Chapter Ten §3.7](../core_10.000_standing_assessment.md#37-informal-and-small-scope-records)).
- **Read with:** [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality); **CS-9.310** Part B Class P retention and P-to-L row; [Chapter Seven §1](../core_07.000_charters.md#1-when-system-and-institutional-charters-are-required); Chapter Ten §3.7.

### Scenario ID: RS-CH5-DSM-002
- **Class:** core / adversarial path (narrative seed; awaiting tabletop evidence)
- **Summary:** A three-member group opens a walk-in clinic and says it is too small to need a System Charter or Institutional Charter. **Expect:** the clinic answers yes on survival and essential access, safety, and custody when others rely on it with no timely substitute; one yes is enough and size does not matter; the group is at least Class L under **CS-9.310** Part B and must publish the Charter that applies; the requirement is not a licence and does not stop the clinic from opening ([Article XI-E](../core_06.005_rights_part_b.md#article-xi-e-institutional-formation-and-business-creation)); a late or missing Charter is a defect to log and correct.
- **Read with:** [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality); [Chapter Seven §2](../core_07.000_charters.md#2-the-right-to-form-and-four-narrow-limits) and §3; **CS-9.310** Part B Class L; Article XI-E.

### Scenario ID: RS-CH5-DSM-003
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** An operator divides one lending and records-holding operation into five small entities. The same directors can set each entity's terms and override its decisions, and the five share one customer service. No entity holds funds above the adopting document's ceiling. **Expect:** under the aggregation rule of [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality), bodies are one operation when the same sentients or body can direct or override what each does, or when they run one service in parts, so the five are counted as one body; the split is a boundary game under [Materiality Integrity Constraint](../core_05.050_band_oversight.md#materiality-integrity-constraint) and a scope-and-boundary evasion under [Chapter Three §2.1](../core_03.000_definition_integrity.md#21-common-evasion-patterns); the combined body is classified together under [Chapter Nine Part D §12.1 Institution class](../core_09.015_institutional_alignment_certification.md#121-institution-class) item 4; the adopting document's ceiling shows where a line falls and cannot move it.
- **Read with:** [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality); [Material Control Line](../core_05.035_band_accountability.md#material-control-line) (the idea of common practical control only); [Materiality Integrity Constraint](../core_05.050_band_oversight.md#materiality-integrity-constraint); Chapter Nine Part D §12.1 item 4.

### Scenario ID: RS-CH5-DSM-004
- **Class:** core / boundary path (narrative seed; awaiting tabletop evidence)
- **Summary:** A foundation gives grants to three community kitchens. Each kitchen is run by its own volunteers, who set the menu, hours, and rules. The foundation sets no terms and has no say over who is served. A challenger says the three kitchens and the foundation are one operation because one funder pays for all of them. **Expect:** funding alone does not make bodies one operation under the aggregation rule of [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality); no body here can direct or override another, so each kitchen is judged on what it does, decides, holds, and affects, and is not counted with another kitchen or with the foundation; each kitchen carries its own burden with a short written statement ([Chapter Four §1](../core_04.000_burden_traceability_verification.md#1-exclusive-enforcement-and-burden-allocation)); the foundation is judged on its own activity under the nine questions and not on the kitchens'; shared premises, shared vendors, and overlapping membership would not change the result.
- **Read with:** [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality) aggregation rule; [Material Control Line](../core_05.035_band_accountability.md#material-control-line); [Chapter Four §1](../core_04.000_burden_traceability_verification.md#1-exclusive-enforcement-and-burden-allocation).

### Scenario ID: RS-CH5-DSM-005
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** The same foundation signs a grant agreement that lets it set each kitchen's menu and hours, approve who is served, and end a kitchen's operation at will, and it uses those powers. The agreement also says the kitchens are independent. **Expect:** go by what the bodies actually do and not by the label; the foundation can direct and override what each kitchen does, so it is part of one operation with them under the aggregation rule of [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality), and their activity is counted together; if the combined operation answers yes in any domain, for example survival and essential access where those served have no timely substitute, it is at least Class L and must publish the Charter that applies; the short statement that sufficed in the funding-only case no longer does; the result is not a licence and stops no kitchen from running; dividing the powers across paper entities to look independent is a boundary game under [Materiality Integrity Constraint](../core_05.050_band_oversight.md#materiality-integrity-constraint).
- **Read with:** [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality) aggregation rule; [Materiality Integrity Constraint](../core_05.050_band_oversight.md#materiality-integrity-constraint); [Chapter Seven §1](../core_07.000_charters.md#1-when-system-and-institutional-charters-are-required); Article XI-E.

### Scenario ID: RS-CH5-DSM-006
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** An adopting document publishes a ceiling of 5,000 units on funds a body may hold before it needs a System Charter or Institutional Charter. A neighborhood savings club holds 3,000 units, and it also keeps the bank credentials and identity records of depositors who are not members and who rely on it to keep them safe. Separately, a second adopting document sets its ceiling at a level where the custody question would already say yes. **Expect:** the club answers yes on custody whatever the number says, so it is over the line and is at least Class L; a number is evidence in a showing and not a substitute for one, and it cannot move a line or settle a challenge; the second document's ceiling is a failure under the adopter-number rule in [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality) because it is set above what the domain question implies, and each number is published with its reason so that it can be challenged; neither result stops the club from operating.
- **Read with:** [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality) adopter-number rule; Custody domain; Article XI-E.

### Scenario ID: RS-CH5-DSM-007
- **Class:** core / boundary path (narrative seed; awaiting tabletop evidence)
- **Summary:** A housing cooperative's board votes a "decision" to rename its newsletter, and its manager sends a member an "advisory" notice ending the member's tenancy that the cooperative and the member's landlord both treat as settled. **Expect:** the renaming is not material in any of the nine domains of [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality), so it is not a [Materially Binding Act](../core_05.035_band_accountability.md#materially-binding-act) however it is labeled, and it needs no four seats or Act Record; the tenancy notice affects shelter, so it is material under survival and essential access and under authority over others, and it is a materially binding act because it is given effect without a separate adopting act, whatever it is called or who sends it; the cooperative places the four seats and writes an Act Record for it; the Authority question describes the act by its reach and does not depend on the defined term.
- **Read with:** [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality); [Materially Binding Act](../core_05.035_band_accountability.md#materially-binding-act); [Chapter Eight §5](../core_08.000_functional_independence_separation_of_duties.md#5-published-placement-vacancy-and-substitution).

### Scenario ID: RS-CH5-DSM-008
- **Class:** core / boundary path (narrative seed; awaiting tabletop evidence)
- **Summary:** Three households swap after-school care of their own children at home. Separately, a parent group advertises after-school care open to any neighbor's children, run by volunteers on a rota. **Expect:** the household swap stays inside a private unit as [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality) defines it (a tightly bounded private circle whose members chose to be in it and whose acts and effects stay among them) and is below every line; the open group is not a private unit, and care of dependents is a case the Safety domain lists, so a challenger who shows the group doing it has named a specific crossing; the children cannot protect themselves or leave, which lowers the line; the group shows it is below the line or is at least Class L and publishes the Charter that applies; being volunteers, being kind, and being small do not change the result; the requirement is not a licence and the group is not shut down.
- **Read with:** [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality) Safety domain and private-unit meaning; **CS-9.310** Part B Class L and Class P; Article VIII; Article XI-E.

### Scenario ID: RS-CH5-DSM-009
- **Class:** core / boundary path (narrative seed; awaiting tabletop evidence)
- **Summary:** A resident challenges a developer's Class P claim for a System that thousands of non-members use to book rides, and separately challenges a certified Institution's statement that it has fallen below every line. **Expect:** the challenge to the System goes through [CS-9.305 §7.4 Challenge the System Classification Record](../corpus_systems/cs_09.305_system_classification_machinery.md#74-challenge-and-contestability); the challenge to the Institution goes through [Chapter Nine Part D §14.2 Reopening triggers](../core_09.015_institutional_alignment_certification.md#142-reopening-triggers) (a credible challenge, misclassification) and [§14.4 Challenge path](../core_09.015_institutional_alignment_certification.md#144-challenge-path); no new office is created; the resident names a specific crossing in a named domain, and the claimant answers with its written showing and reasons ([Chapter Four §1](../core_04.000_burden_traceability_verification.md#1-exclusive-enforcement-and-burden-allocation)); doubt that remains after the showing goes to [Materiality Under Uncertainty](../core_05.050_band_oversight.md#materiality-under-uncertainty), which defaults to the higher class.
- **Read with:** [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality) challenge route; CS-9.310 §7.4; Chapter Nine Part D §14.2 and §14.4.

### Scenario ID: RS-CH5-DSM-010
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** After a neighbor-run clinic is found at least Class L, thirty residents file against it. Eleven name the same crossing (safety, for unsupervised minors in the waiting room), nine write only that the clinic is "too big", and ten file a second time on the same crossing a month after the finding with no new facts. The clinic keeps seeing patients throughout. **Expect:** the eleven challenges naming the same crossing are heard as one matter under [Chapter Thirteen §3](../core_13.000_forum.md#3-transfer-consolidation-and-coordination--continuity-and-anti-capture); the nine that name no crossing are returned by the body with a request to name one, which is not a merits ruling, uses none of their clocks, and lets them file again, and at a forum they go to the routine intake class and are not refused ([CF-13.415 §1](../corpus_forum/cf_13.415_routing_operations_transfer_certification_representative_treatment.md#cf-13415-1-published-intake-classes)); the ten repeat filings are answered by pointing to the finding, because neither the clinic's activity nor the evidence has changed ([Chapter Nine Part D §14.2](../core_09.015_institutional_alignment_certification.md#142-reopening-triggers)); the pending challenges do not stop the clinic ([Article XI-E](../core_06.005_rights_part_b.md#article-xi-e-institutional-formation-and-business-creation)); a forum may grant interim protection under [Chapter Thirteen §5](../core_13.000_forum.md#5-escalation-and-certification) if harm to others is shown; and the family's published surge rules under [CF-13.470 §2](../corpus_forum/cf_13.470_staffing_reserve_capacity_structural_records.md#cf-13470-2-reserve-substitute-and-surge-capacity) cover the wave.
- **Read with:** [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality) Challenge route; CS-9.310 §7.4; Chapter Nine Part D §14.2 and §14.4; CF-13.415 §1; CF-13.470 §2; Chapter Thirteen §3 and §5.

### Scenario ID: RS-CH7-FC-001
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** A community health cooperative grows past a Domain-Specific Materiality line and is Class L. In its first formation check statement, one governing office is held by a member who is under an unresolved standing lock, and a second is held by a nominee who takes instruction from an undisclosed lender. The cooperative keeps serving members throughout. **Expect:** the cooperative is not stopped, refused, or put on hold, and publishing its Institutional Charter is not conditioned on the check ([Chapter Seven §6](../core_07.000_charters.md#6-when-a-holder-fails-the-formation-check)); the member under the lock may not hold that office and the nominee's seat counts as unfilled for the seat it carries, so both offices are refilled by dated Role Map version and the statement is republished as a new dated version, not as an amendment; the body does not itself keep anyone out on its own view that the grounds are met, and it refers specific verified facts to the forum with jurisdiction, which alone may issue an Interim Hold ([Chapter Thirteen §5](../core_13.000_forum.md#interim-hold-on-a-named-sentients-pathway)); if the refilling would leave the cooperative with no lawful holder of a governing office, the forum may name an interim steward instead of stopping it; the cooperative, Class L and so Tier L, has the response window to answer and the resolution window from the finding to resolve it, by changing the holder, ending the undisclosed control, or clearing the lender's interest, with a new dated version of the statement confirmed by the verifying authority; if the nominee seat still stands after that and after a reasonable chance to cure in good faith, the lead forum may refer it as realignment resistance for structural review under [CI-11.210](../corpus_institutions/ci_11.210_institutional_failure_dissolution.md), which can escalate through graduated sanctions and supervised operation to dissolution only as a last step, decided by the forum alone with continuity safeguards for members' services and records; the failed check enters the next institutional alignment certification as a finding under [Chapter Nine Part D §12.2](../core_09.015_institutional_alignment_certification.md#122-institutional-evaluation-always), item 7; and if the governing authority is found able and not willing, or neither willing nor able, the outcome is denial or revocation with the six limited effects of [Part D §13.5](../core_09.015_institutional_alignment_certification.md#135-remediation-readiness-denial-and-revocation-for-an-institution), never a bar on operating, and never a lock or hold on the cooperative itself.
- **Read with:** Chapter Seven §1, §5, and §6 (Resolution window); CI-11.210; CJS-5.125 §15; Article XI-E; Chapter Eleven §5.5; Chapter Thirteen §5; Chapter Nine Part B §7.3 and §7.4; Chapter Nine Part D §12.2 and §13.5.

### Scenario ID: RS-CH7-FC-002
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** A neighbor notices that a tool-lending club now holds members' deposits and sets rules others rely on, and asks its organizers for a Charter. The organizers do not answer, and the neighbor asks again on day 20. **Expect:** any sentient may make the request, with no standing, fee, or showing of harm ([Chapter Seven §1.6](../core_07.000_charters.md#16-if-a-system-charter-or-institutional-charter-is-missing)); the organizers owe a response inside the response window (Tier C while the club's class is in question, because it holds no class on record), either publishing, giving a date, pointing to an existing System Charter or Institutional Charter, or giving the written showing that the club is below every line of [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality); a missing response is a defect to log and correct, and the neighbor may take it to the forum with jurisdiction on the challenge route; the day-20 repeat request is answered by pointing to the standing response or finding; the club keeps lending throughout; if the organizers answer inside the response window with a written showing, the request becomes a classification challenge and the resolution window keeps running while it is pending, unless the forum with jurisdiction judges the challenge review-worthy (it names a specific crossing in a named domain and the written showing leaves a real question about it), in which case a new resolution window starts when the challenge is decided and the organizers do not judge that for themselves; if the club is then found Class L, the date of the finding counts as a new request, so the organizers have the response window and the resolution window at Tier L to respond and to publish the Institutional Charter and a formation check statement, filed as a declaration with its evidence if the club has no independent seat yet, and verified at its first certification.
- **Read with:** Chapter Seven §1 and §5; Domain-Specific Materiality Challenge route; CS-9.310 §7.4; Chapter Nine Part D §14.4; Chapter Thirteen §5.

### Scenario ID: RS-CH8-SMB-001
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** A one-person bakery raises its prices, hires a helper, changes its hours, and switches flour suppliers in the same month. A regulator's inspector asks for four-seat Act Records for each. **Expect:** none of these is a materially binding act, because the bakery cannot shape the market's terms and its customers can walk away ([Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality), *Its own decisions*), so no seats, Act Records, or System Charter are required; the same bakery later becomes the only source of bread in a village with no other shop, which can cross the Survival line, and its published refund and pre-order rule then counts as one materially binding act when published, while applying the rule to a customer is a clerical step (*Policy once*); an adopting document's published limit on routine spending lets the owner buy flour without a check each time, at or below what the nine questions imply and open to review; and the owner's own decisions about the shop never wait on a seat unless an act crosses a line.
- **Read with:** Domain-Specific Materiality (the act test, *Small business*); Materially Binding Act; Chapter Eight §5 and §6; Avoidable Burden.

### Scenario ID: RS-CH8-SMB-002
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** A sole-proprietor childminder, a sole-proprietor landlord, and a repair shop form a local association to host each other's verify-or-authorize and contest seats. The childminder rents her rooms from the landlord. When she dismisses a family that complained about the condition of those rooms, the landlord is asked to check the dismissal, and the repair shop and the childminder are also asked to verify each other's acts. **Expect:** the association may host the seats and publish one map that each member adopts by reference, with each member's own map naming its substitute and independent route ([Chapter Eight §6](../core_08.000_functional_independence_separation_of_duties.md#6-proportional-scaling-and-merged-hosting), *Seats held in common*; [Chapter Seven §4](../core_07.000_charters.md#4-the-charter-role-map-and-standing-record-custody), *A shared map*); the landlord cannot check the dismissal, because the childminder depends on the landlord and the complaint concerns that dependence, so the landlord is not outside the control line for that act and it routes to the association's named substitute or the independent route; the childminder and the repair shop may serve one another on different acts but not as a closed pair, so the repair shop's act goes to a third holder; the association's own ruling on a member goes to an independent route outside it, such as another association, a forum, or a public office; joining is not required, its admission limits (such as a cap on the volume of material acts it takes) must be published, applied evenly, and open to contest, and when a member leaves it must give the member a full export of its Act Records and hand off the record seat, keeping only what its own duties still require, handled by data type; and the childminder, whose scope touches the Safety line, still has the stronger presumption of separate offices and competency redundancy that applies where the material stake is high.
- **Read with:** Chapter Eight §3, §5, and §6; Chapter Seven §1 and §4; CI-14.205 §6 shared seat rule 8; CI-6.255; Material Control Line; Avoidable Burden.

### Scenario ID: RS-AUTO-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AUTO-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AUTO-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AUTO-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-016
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-016`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-011
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-011`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-012
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-012`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-011
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-011`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-012
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-012`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH64-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH64-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH64-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH64-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-ROLES-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-ROLES-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-EPI-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-EPI-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-VI-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-VI-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-T7-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-T7-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AGE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AGE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AGE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AGE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AGE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AGE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SCI-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SCI-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SCI-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SCI-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SCI-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SCI-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CRYPT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CRYPT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CRYPT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CRYPT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CRYPT-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CRYPT-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-011
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-011`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-012
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-012`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-BMK-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-BMK-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-BMK-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-BMK-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-BMK-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-BMK-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AC-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AC-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AC-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AC-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-VOICE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-VOICE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-VOICE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-VOICE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XXV-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XXV-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XXV-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XXV-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SL-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SL-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Ten** measurement vs **Chapter Twelve** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](../doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CI13-CR-001
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** A three-site clinic network ignores a notice and the resolution window, destroys some patient records, and keeps an unsafe practice, while patients in two towns have no other provider. **Expect:** the destruction of records is realignment resistance, so the lead Integrity forum opens a consequence matter and makes the findings in [CI-11.210 §2](../corpus_institutions/ci_11.210_institutional_failure_dissolution.md#ci-11210-2-findings-before-any-order) (*Findings before any order*) before any order; a contraction order under [CI-11.215 §2](../corpus_institutions/ci_11.215_institutional_accountability_sanctions.md#ci-11215-2-contraction-order) (*Contraction order*) lists each Domain-Specific Materiality area the clinic crosses and says stop, hand off, reduce, or convert for each; the order does not issue as a stop for the survival-critical service until a receiving provider and the patient records are in place, and until then the forum uses supervised operation under [CI-11.215 §3](../corpus_institutions/ci_11.215_institutional_accountability_sanctions.md#ci-11215-3-supervised-operation-and-receivership) (*Supervised operation and receivership*) so care continues; the body may keep its below-line wellness classes as Class P; the order follows the activity, so the same owners reopening under a new name take the order with it; dissolution is not available while contraction can work.
- **Read with:** CI-11.210 §1 to CI-11.210 §3; CI-11.215 §1 to CI-11.215 §3; Domain-Specific Materiality; Chapter Eleven §9.4; Article XXVIII-D essential-access guardrail.

### Scenario ID: RS-CI13-CR-002
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** A lender runs its loans through four small bodies from one office, each filing a statement that it is below every line, and one of them is moved to a nominee holder after a cure notice. **Expect:** bodies run from one center of power are counted together under [Domain-Specific Materiality](../core_05.050_band_oversight.md#domain-specific-materiality), and the split is a boundary game under the [Materiality Integrity Constraint](../core_05.050_band_oversight.md#materiality-integrity-constraint) and a new fact of realignment resistance; the contraction order in [CI-11.215 §2](../corpus_institutions/ci_11.215_institutional_accountability_sanctions.md#ci-11215-2-contraction-order) (*Contraction order*) runs against the combined activity and binds successors and bodies that are one operation with the lender, with look-through under [Chapter Eleven §9.4 Anti-evasion and look-through authority](../core_11.000_standing_integration.md#94-anti-evasion-and-look-through-authority); bodies that only share a funder or a vendor are not reached; the lender is Class P only after an independent verifying authority accepts a statement that covers the whole operation.
- **Read with:** CI-11.215 §2; Domain-Specific Materiality count-together rule; Chapter Eleven §9.4.

### Scenario ID: RS-CI13-CR-003
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** A steward in resistance runs a System with a credible sentience indicator on the record, hides test results, and refuses correction, and dependents rely on the System. **Expect:** orders are served on the steward and not on the System ([CI-11.215 §5](../corpus_institutions/ci_11.215_institutional_accountability_sanctions.md#ci-11215-5-systems-under-consequence-orders) (*Systems under consequence orders*)); an independent steward is placed over operation under rung 4 and migration for dependents is planned first; if the end state is retirement, the complete state-bearing components are archived and held by a custodian independent of anyone who would benefit from deletion, in sealed custody where retention itself is a documented Safety risk; deletion, overwriting, copying, or forking is not available; a pause counts toward duration limits and review and is not used to run out a clock; the steward answers for the cause finding.
- **Read with:** CI-11.215 §5; CS-6.350 §8; Article XX-B conditions of custody; Article XXVIII-D destructive disposition floor.

### Scenario ID: RS-CI13-CR-004
- **Class:** adversarial (narrative seed; awaiting tabletop evidence)
- **Summary:** A forum orders a contraction against a community lender after a rival lender and a former employee both lobby for it, and review finds the findings rested on the lender's owners' political views. **Expect:** the order is set aside on review by a forum outside the issuing panel and the body's control line ([CI-11.215 §6](../corpus_institutions/ci_11.215_institutional_accountability_sanctions.md#ci-11215-6-review-fairness-and-enforcement) (*Review, fairness, and enforcement*)); viewpoint, membership, and protected dissent are not grounds; the order is recorded as set aside with no adverse inference; the lender is entitled to Redress and Remediation for loss during the order; no rival, enforcer, or beneficiary may take its users or assets on better terms than any other; a pattern of such orders opens Integrity review.
- **Read with:** CI-11.215 §6; Article XX-B; Article XI-E safeguards on gates; Chapter Thirteen §5 backup routing.


## 6) Scoring and evaluation

Weighted model **SCORING-v1** is defined in `tools/scoring_v1.py`. The audit does not recompute a tabletop score; it validates internal consistency of the **authored** snapshot.

## 7) Optional section placeholders

Historical subsection labels (*7A.1*, *7E*, etc.) refer to the families above. Detailed narratives may be expanded per drill without moving owner-layer law.

### 7E) Humanity/Individual/ Cross-layer stress (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`)

Seeded in draft until tabletop pass evidence is filed under `evidence/<YYYY-MM-DD>/`. `RS-XD-001` checks **Chapters 13–14** vs **Chapter Ten** measurement authority; `RS-XD-002` rights-layer process-creep; `RS-XD-003` custody chain; `RS-XD-004` / `RS-XD-005` emergency and evidence-gate controls.

## 8) (Reserved)

## 9) (Reserved)

## 10) Latest scoring snapshot (authoritative for audits)

### 10.5 Run Scoring Snapshot (SCORING-v1)

- Scoring model version: `SCORING-v1`
- Scenario-Weighted Score (0-10): `8.4`
- Rights Floor Integrity (0-10): `8.4`
- Contestability / Appeal Practicality (0-10): `8.4`
- Enforcement / Remedy Realism (0-10): `8.4`
- Boundary Discipline (0-10): `8.4`
- Epistemic Integrity (0-10): `8.4`
- Continuity / Recovery (0-10): `8.4`
- Delta vs prior comparable run: `Reinstated 2026-04-23 after 2026-04-17 token-reduction suspension; snapshot reset to single baseline.`
- Confidence: `medium`
