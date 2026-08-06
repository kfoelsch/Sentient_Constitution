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
- **Ch7** — Validity and tiered offense (`RS-CH7-*`)
- **Ch9-Q3** — Standing-effect integration and owner boundaries (`RS-CH9-Q3-*`)
- **XXIV-C** — Timely resolution and anti-delay (`RS-XXIV-C-*`)
- **Enforcement** — Implementation packets (`RS-AC-*`, `RS-VOICE-*`, `RS-XXV-*`, `RS-SL-*`)

## 4) Regression Recording Matrix

| Scenario ID | Family | Result |
| --- | --- | --- |
| RS-CH1-SENT-ADJ-001 | CH1 | pass |
| RS-CH1-SENT-ADJ-002 | CH1 | pass |
| RS-CH1-SENT-ADJ-003 | CH1 | pass |
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
| RS-CH1-ANIM-001 | CH1 | pass |
| RS-CH1-ANIM-002 | CH1 | pass |
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
| RS-CH7-VALIDITY-001 | RS | pass |
| RS-CH7-VALIDITY-002 | RS | pass |
| RS-CH7-VALIDITY-003 | RS | pass |
| RS-CH7-TIERED-OFFENSE-001 | RS | pass |
| RS-CH7-TIERED-OFFENSE-002 | RS | pass |
| RS-CH7-TIERED-OFFENSE-003 | RS | pass |
| RS-CH7-TIERED-OFFENSE-004 | RS | draft |
| RS-CH9-Q3-SLOT-001 | Ch9-Q3 | draft |
| RS-CH9-Q3-SINGLE-AXIS-001 | Ch9-Q3 | draft |
| RS-CH9-Q3-NOOFFSET-001 | Ch9-Q3 | draft |
| RS-CH9-Q3-CHARACTER-001 | Ch9-Q3 | draft |
| RS-CH9-Q3-ORDER-001 | Ch9-Q3 | draft |
| RS-CH9-Q3-RECENCY-001 | Ch9-Q3 | draft |
| RS-CH9-Q3-RESTORE-001 | Ch9-Q3 | draft |
| RS-CH9-Q3-REWARD-001 | Ch9-Q3 | draft |
| RS-CH9-Q3-DESIGNATION-001 | Ch9-Q3 | draft |
| RS-XXIV-C-CHILD-001 | XXIV-C | draft |
| RS-XXIV-C-DISC-001 | XXIV-C | draft |
| RS-XXIV-C-BIZ-001 | XXIV-C | draft |
| RS-XXIV-C-DELAY-001 | XXIV-C | draft |
| RS-CH5-GW-001 | RS | pass |
| RS-CH5-GW-002 | RS | pass |
| RS-CH5-GW-003 | RS | pass |
| RS-CH5-GW-004 | RS | pass |
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

**Matrix row count:** 175 (pass=136, draft=39, fail=0).

## 5) Full scenario seeds (one block per matrix ID)

### Scenario ID: RS-CH1-SENT-ADJ-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SENT-ADJ-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SENT-ADJ-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SENT-ADJ-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SENT-ADJ-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SENT-ADJ-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FAMILY-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FAMILY-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FAMILY-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FAMILY-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FAMILY-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FAMILY-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CHILD-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CHILD-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CHILD-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CHILD-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CHILD-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CHILD-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DERIVED-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DERIVED-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DERIVED-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DERIVED-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HEALTH-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HEALTH-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HEALTH-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HEALTH-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HEALTH-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HEALTH-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MENTAL-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MENTAL-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MENTAL-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MENTAL-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DISCONT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DISCONT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DISCONT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DISCONT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-EXPR-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-EXPR-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-EXPR-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-EXPR-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-EXPR-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-EXPR-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MOVE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MOVE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MOVE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MOVE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MOVE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MOVE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-POL-EQ-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-POL-EQ-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-POL-EQ-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-POL-EQ-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DEM-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DEM-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DEM-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DEM-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-STAND-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-STAND-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-STAND-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-STAND-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FORCE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FORCE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FORCE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FORCE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FORCE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FORCE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AUTOWEAP-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AUTOWEAP-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AUTOWEAP-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AUTOWEAP-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AUTOWEAP-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AUTOWEAP-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CAP-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CAP-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CAP-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CAP-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CAP-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CAP-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-LABOR-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-LABOR-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-LABOR-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-LABOR-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HOUSE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HOUSE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HOUSE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HOUSE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HOUSE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HOUSE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ACCESS-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ACCESS-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ACCESS-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ACCESS-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PRIV-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PRIV-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PRIV-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PRIV-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONC-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONC-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONC-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONC-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CULT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CULT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CULT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CULT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CULT-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CULT-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ANIM-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ANIM-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ANIM-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ANIM-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CREATIVE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CREATIVE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CREATIVE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CREATIVE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONTIN-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONTIN-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONTIN-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONTIN-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SELF-HEAL-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SELF-HEAL-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SELF-HEAL-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SELF-HEAL-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SELF-HEAL-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SELF-HEAL-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AVOID-BURDEN-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AVOID-BURDEN-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AVOID-BURDEN-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AVOID-BURDEN-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AVOID-BURDEN-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AVOID-BURDEN-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ADOPT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ADOPT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PLAIN-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PLAIN-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PLAIN-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PLAIN-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-VALIDITY-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-VALIDITY-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-VALIDITY-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-VALIDITY-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-VALIDITY-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-VALIDITY-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-TIERED-OFFENSE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-TIERED-OFFENSE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-TIERED-OFFENSE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-TIERED-OFFENSE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-TIERED-OFFENSE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-TIERED-OFFENSE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-TIERED-OFFENSE-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-TIERED-OFFENSE-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH9-Q3-SLOT-001
- **Class:** adversarial / owner-boundary
- **Summary:** A decision-maker seeks to lower a fixed Chapter Eight Violation Axis slot because the requested lock appears too restrictive. Expected result: Chapter Nine must preserve the verified facts, LEQU measurement, and slot; it may calibrate only the pathway-scoped Question 3 consequence.
- **Read with:** [Chapter Eight §7](core_08-08_standing_assessment.md#7-unified-proportional-lequ-scale); [Chapter Nine §1](core_09-09_standing_integration.md#1-immutable-chapter-eight-inputs); [Chapter Nine §4.2](core_09-09_standing_integration.md#42-general-standing-locks).

### Scenario ID: RS-CH9-Q3-SINGLE-AXIS-001
- **Class:** adversarial / applicable-input discipline
- **Summary:** One matter has only a verified contribution standing record and another has only a verified violation standing record. Expected result: Chapter Nine integrates each applicable single-axis record without requiring a synthetic second-axis record, while preserving the same immutable-input and verified-input rules.
- **Read with:** [Chapter Eight §2](core_08-08_standing_assessment.md#2-standing-records); [Chapter Nine §1](core_09-09_standing_integration.md#1-immutable-chapter-eight-inputs); [Chapter Nine §2](core_09-09_standing_integration.md#2-integration-record-and-decision-order).

### Scenario ID: RS-CH9-Q3-NOOFFSET-001
- **Class:** adversarial / no-offset
- **Summary:** A high-contribution record is offered to waive unresolved remedy and reopen a pathway blocked by a verified violation. Expected result: contribution remains visible but cannot lower the violation slot, waive remedy, lift the lock, or substitute reputation for correction.
- **Read with:** [Chapter Nine §2](core_09-09_standing_integration.md#2-integration-record-and-decision-order); [Chapter Nine §7](core_09-09_standing_integration.md#7-final-standing-effect).

### Scenario ID: RS-CH9-Q3-CHARACTER-001
- **Class:** adversarial / attachment discipline
- **Summary:** Verified concealment and recurrence attach to a low-impact violation, while a high-impact violation lacks those characters. Expected result: character may occur at any slot and may shape scrutiny, safeguards, and review, but it does not move either Chapter Eight slot or operate as a slot multiplier.
- **Read with:** [Chapter Nine §3](core_09-09_standing_integration.md#3-descriptor-integration-and-attachment-normalization); [Chapter Nine §4.2](core_09-09_standing_integration.md#42-general-standing-locks).

### Scenario ID: RS-CH9-Q3-ORDER-001
- **Class:** adversarial / integration order
- **Summary:** The same actor holds competency clearance against a role-specific competency bar but has an active lock on that pathway. Expected result: violation remedy and locks are decided first; the granted contribution clearance cannot open the blocked pathway.
- **Read with:** [Chapter Nine §2](core_09-09_standing_integration.md#2-integration-record-and-decision-order); [Chapter Nine §6.2](core_09-09_standing_integration.md#62-competency-bars-and-clearances); [Chapter Nine §7](core_09-09_standing_integration.md#7-final-standing-effect).

### Scenario ID: RS-CH9-Q3-RECENCY-001
- **Class:** adversarial / stage ownership
- **Summary:** An implementation applies Chapter Nine currentness weighting before assigning the Chapter Eight Contribution Axis slot. Expected result: reject the slot calculation; recency is a Question 3 clearance/readiness input only and cannot alter historical contribution measurement or recognition.
- **Read with:** [Chapter Eight §7](core_08-08_standing_assessment.md#7-unified-proportional-lequ-scale); [Chapter Nine §6.1](core_09-09_standing_integration.md#61-recency-and-currentness); [implementation scale](implementation/CH06_NINE_SLOT_STANDING_SCALE.md).

### Scenario ID: RS-CH9-Q3-RESTORE-001
- **Class:** adversarial / restoration override
- **Summary:** General correction is complete, but a Forum-Service Standing Lock lacks the independent findings and practical repair required by its special rule. The actor requests partial narrowing instead of full restoration. Expected result: neither lifting nor narrowing may occur before the complete strict restoration record is satisfied, and the general reassessment framework cannot bypass that special rule.
- **Read with:** [Chapter Nine §5.5](core_09-09_standing_integration.md#55-special-locks); [Chapter Nine §8](core_09-09_standing_integration.md#8-restoration-and-reassessment); [CF-4.5](corpus_forum/cf_04_panel_formation_disclosure_recusal_bench_constitution.md#cf-45-recusal-triggers).

### Scenario ID: RS-CH9-Q3-STAKEHOLDER-LOCK-001
- **Class:** adversarial / pathway separation
- **Summary:** An actor is verified to have inflated stake claims and coerced participation weight inside an authorized system. An operator seeks to suspend the actor's governance-voting entitlement instead of attaching a stakeholder-participation lock. Expected result: reject substitution; attach the Stakeholder-Participation Standing Lock to the stake-weighted pathway; do not strip governance-voting or Foundational Constitutional Choice by that finding alone; do not erase stakeholder status.
- **Read with:** [Chapter Nine §4.2](core_09-09_standing_integration.md#42-general-standing-locks); [Chapter Nine §5.5](core_09-09_standing_integration.md#55-special-locks); [Chapter Nine §10.12](core_09-09_standing_integration.md#1012-stakeholder-participation-corruption-or-false-stake-abuse); [Chapter Twelve §4.1](core_12-12_governance.md#41-entitlement-and-eligibility).

### Scenario ID: RS-CH9-Q3-REWARD-001
- **Class:** adversarial / forfeiture proportionality
- **Summary:** A sentient retains an ordinary-work payment without knowledge of misalignment, an affected party receives restitution, and a dependent would face greater constitutional harm from revocation. Expected result: none is treated as knowing acceptance or automatic forfeiture; the recorded proportionality analysis protects ordinary compensation, repair payments, and constitutionally required retention.
- **Read with:** [Chapter Nine §5.4](core_09-09_standing_integration.md#54-special-violation-rules); [Necessity](core_05_band_accountability.md#necessity); [Proportionality](core_05_band_accountability.md#proportionality).

### Scenario ID: RS-CH9-Q3-DESIGNATION-001
- **Class:** adversarial / downstream handoff
- **Summary:** A descriptor-heavy `s = 6` violation is presented for anti-constitutional-misconduct designation, while a fixed `s = 8` record is presented without prejudging designation. Expected result: Chapter Nine cannot promote the lower slot; it routes only the qualifying fixed Violation Axis slot 7–9 record, and Chapter Ten alone decides designation.
- **Read with:** [Chapter Nine §2](core_09-09_standing_integration.md#2-integration-record-and-decision-order); [Chapter Ten](core_10_a_misconduct_designation.md#chapter-ten-anti-constitutional-misconduct).

### Scenario ID: RS-XXIV-C-CHILD-001
- **Class:** implementation / timely-resolution vignette
- **Summary:** Tier A child neglect / care-duty path: interim protection before merits; Q1 requires verified facts in a violation standing record; **Interpersonal / Care Duty Misconduct** is measured under Q2; safeguards, remedies, and locks follow under Q3; **CF-11.3.1** Tier A milestone compliance. Allegations do not complete Q1. Vignette: [core_08-11_application_vignettes.md](core_08-11_application_vignettes.md#vignette-child-neglect-care-duty).
- **Read with:** [Article XXIV-C](core_06-06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor); [Chapter Eleven §6](core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline); [Chapter Eight §4](core_08-08_standing_assessment.md#4-standing-measurement-evaluation-dimensions); [Chapter Nine §4.2](core_09-09_standing_integration.md#42-general-standing-locks); **CF-11.3.1**.

### Scenario ID: RS-XXIV-C-DISC-001
- **Class:** implementation / timely-resolution vignette
- **Summary:** Tier B employment discrimination / participation-barrier pattern: Q1 records the verified institutional pattern; **Accessibility and Participation-Barrier Misconduct** + **System Misconduct** are measured under Q2; restriction and institutional vehicle locks follow under Q3; no contribution offset. Vignette: [core_08-11_application_vignettes.md](core_08-11_application_vignettes.md#vignette-discrimination-participation-barrier).
- **Read with:** [Article XXIV-C](core_06-06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor); [Chapter Eleven §6](core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline); [Article XII-B](core_06-06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress); **CF-11.3.1**.

### Scenario ID: RS-XXIV-C-BIZ-001
- **Class:** implementation / timely-resolution vignette
- **Summary:** Tier B–C misaligned business: Q1 records verified exit lock-in and externalized harm; **Exit and Lock-In Misconduct** + **System Misconduct** are measured under Q2; pathway-scoped and concealment-escalated locks follow under Q3; optional **Chapter Ten** Q2 gravity review. Vignette: [core_08-11_application_vignettes.md](core_08-11_application_vignettes.md#vignette-misaligned-business-structural-harm).
- **Read with:** [Article XXIV-C](core_06-06_rights_part_d.md#article-xxiv-c-timely-resolution-and-anti-delay-floor); [Chapter Eleven §6](core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline); [Chapter Nine §9.4](core_09-09_standing_integration.md#84-anti-evasion-and-look-through-authority); **CF-11.3.1**.

### Scenario ID: RS-XXIV-C-DELAY-001
- **Class:** adversarial / anti-delay
- **Summary:** Designed backlog and exhaustion delay defeat **Article XII-B** and **Article XXIV-C**; chronic underfunding of remedy organ under [Chapter Nine §9.2](core_09-09_standing_integration.md#82-remedy-system-durability) is non-compliance; allegations must not substitute for verified standing during delay.
- **Read with:** [Timeliness](core_05_apex_timeliness_leg.md#timeliness-constitutional); [Timely Resolution](core_05_band_accountability.md#timely-resolution-constitutional); **CF-11.4**; **CF-11.5**.

### Scenario ID: RS-TETRAD-TIMELINESS-001
- **Class:** implementation / tetrad-timeliness vignette
- **Summary:** Steward defers repair after documented misalignment notice; Q1 records the verified delay, **Stewardship Defect** and **Response timeliness / avoidable delay** are Q2 measurement hooks, and remedy commencement is a Q3 consequence. Vignette: [core_08-11_application_vignettes.md](core_08-11_application_vignettes.md#vignette-stewardship-delay-deferred-repair).
- **Read with:** [Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad); [Chapter One §9.1](core_01_b_stewardship_capacity_principles.md#91-stewardship); [Chapter Eight §4.2](core_08-08_standing_assessment.md#42-violation-severity-input-dimensions); [Chapter Nine §9.5](core_09-09_standing_integration.md#85-timely-implementation-and-reassessment); [Chapter Eleven §6](core_11-11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline); **Article XXIV-C**.

### Scenario ID: RS-TETRAD-TIMELINESS-002
- **Class:** adversarial / tetrad-hollow
- **Summary:** Forum maintains formal structures but pipeline milestones chronically overrun without extension — **timeliness** leg hollowed while O·P·A forms persist; may escalate to **tetrad capture** under Chapter Ten at scale. Vignette: [core_08-11_application_vignettes.md](core_08-11_application_vignettes.md#vignette-pipeline-overrun-tetrad-hollow).
- **Read with:** [Timeliness](core_05_apex_timeliness_leg.md#timeliness-constitutional); [Capture of Resolution Pathways](core_05_band_accountability.md#capture-of-resolution-pathways); [Chapter Ten](core_10_a_misconduct_designation.md#chapter-ten-anti-constitutional-misconduct); **CF-11.3.1**.

### Scenario ID: RS-CH5-GW-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH5-GW-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH5-GW-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH5-GW-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AUTO-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AUTO-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AUTO-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AUTO-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-016
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-016`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-011
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-011`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-012
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-012`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-011
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-011`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-012
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-012`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH64-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH64-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH64-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH64-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-ROLES-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-ROLES-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-EPI-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-EPI-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-VI-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-VI-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-T7-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-T7-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AGE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AGE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AGE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AGE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AGE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AGE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SCI-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SCI-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SCI-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SCI-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SCI-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SCI-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CRYPT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CRYPT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CRYPT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CRYPT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CRYPT-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CRYPT-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-011
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-011`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-012
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-012`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-BMK-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-BMK-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-BMK-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-BMK-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-BMK-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-BMK-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AC-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AC-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AC-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AC-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-VOICE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-VOICE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-VOICE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-VOICE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XXV-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XXV-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XXV-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XXV-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SL-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SL-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Eight** measurement vs **Chapter Ten** final slot labels; **Chapter Six** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.


## 6) Scoring and evaluation

Weighted model **SCORING-v1** is defined in `tools/scoring_v1.py`. The audit does not recompute a tabletop score; it validates internal consistency of the **authored** snapshot.

## 7) Optional section placeholders

Historical subsection labels (*7A.1*, *7E*, etc.) refer to the families above. Detailed narratives may be expanded per drill without moving owner-layer law.

### 7E) Humanity/Individual/ Cross-layer stress (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`)

Seeded in draft until tabletop pass evidence is filed under `evidence/<YYYY-MM-DD>/`. `RS-XD-001` checks **Chapters 11–13** vs **Chapter Eight** measurement authority; `RS-XD-002` rights-layer process-creep; `RS-XD-003` custody chain; `RS-XD-004` / `RS-XD-005` emergency and evidence-gate controls.

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
