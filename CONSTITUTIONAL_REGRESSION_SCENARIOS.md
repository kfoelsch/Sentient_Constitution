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
- **XXIII-G** — Timely resolution and anti-delay (`RS-XXIII-G-*`)
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
| RS-XXIII-G-CHILD-001 | XXIII-G | draft |
| RS-XXIII-G-DISC-001 | XXIII-G | draft |
| RS-XXIII-G-BIZ-001 | XXIII-G | draft |
| RS-XXIII-G-DELAY-001 | XXIII-G | draft |
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
- **Summary:** Tracked row for `RS-CH1-SENT-ADJ-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SENT-ADJ-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SENT-ADJ-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SENT-ADJ-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SENT-ADJ-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FAMILY-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FAMILY-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FAMILY-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FAMILY-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FAMILY-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FAMILY-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CHILD-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CHILD-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CHILD-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CHILD-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CHILD-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CHILD-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DERIVED-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DERIVED-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DERIVED-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DERIVED-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HEALTH-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HEALTH-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HEALTH-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HEALTH-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HEALTH-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HEALTH-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MENTAL-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MENTAL-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MENTAL-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MENTAL-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DISCONT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DISCONT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DISCONT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DISCONT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-EXPR-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-EXPR-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-EXPR-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-EXPR-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-EXPR-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-EXPR-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MOVE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MOVE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MOVE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MOVE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-MOVE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-MOVE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-POL-EQ-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-POL-EQ-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-POL-EQ-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-POL-EQ-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DEM-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DEM-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-DEM-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-DEM-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-STAND-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-STAND-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-STAND-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-STAND-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FORCE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FORCE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FORCE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FORCE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-FORCE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-FORCE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AUTOWEAP-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AUTOWEAP-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AUTOWEAP-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AUTOWEAP-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AUTOWEAP-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AUTOWEAP-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CAP-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CAP-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CAP-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CAP-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CAP-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CAP-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-LABOR-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-LABOR-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-LABOR-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-LABOR-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HOUSE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HOUSE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HOUSE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HOUSE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-HOUSE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-HOUSE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ACCESS-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ACCESS-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ACCESS-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ACCESS-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PRIV-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PRIV-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PRIV-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PRIV-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONC-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONC-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONC-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONC-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CULT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CULT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CULT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CULT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CULT-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CULT-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ANIM-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ANIM-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ANIM-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ANIM-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CREATIVE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CREATIVE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CREATIVE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CREATIVE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PROD-CAP-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PROD-CAP-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONTIN-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONTIN-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-CONTIN-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-CONTIN-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SELF-HEAL-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SELF-HEAL-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SELF-HEAL-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SELF-HEAL-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-SELF-HEAL-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-SELF-HEAL-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AVOID-BURDEN-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AVOID-BURDEN-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AVOID-BURDEN-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AVOID-BURDEN-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-AVOID-BURDEN-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-AVOID-BURDEN-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-ADOPT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-ADOPT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PLAIN-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PLAIN-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH1-PLAIN-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH1-PLAIN-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-VALIDITY-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-VALIDITY-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-VALIDITY-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-VALIDITY-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-VALIDITY-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-VALIDITY-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-TIERED-OFFENSE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-TIERED-OFFENSE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-TIERED-OFFENSE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-TIERED-OFFENSE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-TIERED-OFFENSE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-TIERED-OFFENSE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH7-TIERED-OFFENSE-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH7-TIERED-OFFENSE-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XXIII-G-CHILD-001
- **Class:** implementation / timely-resolution vignette
- **Summary:** Tier A child neglect / care-duty path: interim protection before merits; verified violation standing record; **Interpersonal / Care Duty Misconduct** Q1; safeguard locks Q2; **CF-11.3.1** Tier A milestone compliance. Vignette: [implementation/CH6-9_APPLICATION_VIGNETTES.md](implementation/CH6-9_APPLICATION_VIGNETTES.md#vignette-child-neglect-care-duty).
- **Read with:** [Article XXIII-G](core_10-10_rights_part_d.md#article-xxiii-g-timely-resolution-and-anti-delay-floor); [Chapter Six §3](core_06-06_standing_assessment.md#6-classification-evaluation-dimensions); [Chapter Seven §3.10](core_07-07_standing_integration.md#310-non-recurrence-lock-dimensions); **CF-11.3.1**.

### Scenario ID: RS-XXIII-G-DISC-001
- **Class:** implementation / timely-resolution vignette
- **Summary:** Tier B employment discrimination / participation-barrier pattern: institutional violation record; **Accessibility and Participation-Barrier Misconduct** + **System Misconduct** Q1; restriction and institutional vehicle locks Q2; no contribution offset. Vignette: [implementation/CH6-9_APPLICATION_VIGNETTES.md](implementation/CH6-9_APPLICATION_VIGNETTES.md#vignette-discrimination-participation-barrier).
- **Read with:** [Article XXIII-G](core_10-10_rights_part_d.md#article-xxiii-g-timely-resolution-and-anti-delay-floor); [Article XII-B](core_10-10_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress); **CF-11.3.1**.

### Scenario ID: RS-XXIII-G-BIZ-001
- **Class:** implementation / timely-resolution vignette
- **Summary:** Tier B–C misaligned business: exit lock-in, externalized harm caps contribution credit; **Exit and Lock-In Misconduct** + **System Misconduct** Q1; pathway-scoped and concealment escalated locks Q2; optional **Chapter Eight** escalation. Vignette: [implementation/CH6-9_APPLICATION_VIGNETTES.md](implementation/CH6-9_APPLICATION_VIGNETTES.md#vignette-misaligned-business-structural-harm).
- **Read with:** [Article XXIII-G](core_10-10_rights_part_d.md#article-xxiii-g-timely-resolution-and-anti-delay-floor); [Chapter Seven §5.4](core_07-07_standing_integration.md#54-anti-evasion-and-look-through-authority); **CF-11.3.1**.

### Scenario ID: RS-XXIII-G-DELAY-001
- **Class:** adversarial / anti-delay
- **Summary:** Designed backlog and exhaustion delay defeat **Article XII-B** and **Article XXIII-G**; chronic underfunding of remedy organ under [Chapter Seven §5.2](core_07-07_standing_integration.md#52-remedy-organ-durability) is non-compliance; allegations must not substitute for verified standing during delay.
- **Read with:** [Timeliness](core_05a_accountability_definitions.md#timeliness-constitutional); [Timely Resolution](core_05a_accountability_definitions.md#timely-resolution-constitutional); **CF-11.4**; **CF-11.5**.

### Scenario ID: RS-TETRAD-TIMELINESS-001
- **Class:** implementation / tetrad-timeliness vignette
- **Summary:** Steward defers repair after documented drift notice; **Stewardship Defect** and Ch6 **Response timeliness / avoidable delay** Q1 hook; Ch7 §3.10 remedy-commencement dimension. Vignette: [implementation/CH6-9_APPLICATION_VIGNETTES.md](implementation/CH6-9_APPLICATION_VIGNETTES.md#vignette-stewardship-delay-deferred-repair).
- **Read with:** [Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad); [Chapter One §6.1](core_01_b_stewardship_capacity_principles.md#61-stewardship); [Chapter Six §3](core_06-06_standing_assessment.md#dual-use-classification-dimensions); **Article XXIII-G**.

### Scenario ID: RS-TETRAD-TIMELINESS-002
- **Class:** adversarial / tetrad-hollow
- **Summary:** Forum maintains formal structures but pipeline milestones chronically overrun without extension — **timeliness** leg hollowed while O·P·A forms persist; may escalate to **tetrad capture** under Chapter Eight at scale. Vignette: [implementation/CH6-9_APPLICATION_VIGNETTES.md](implementation/CH6-9_APPLICATION_VIGNETTES.md#vignette-pipeline-overrun-tetrad-hollow).
- **Read with:** [Timeliness](core_05a_accountability_definitions.md#timeliness-constitutional); [Capture of Resolution Pathways](core_05a_accountability_definitions.md#capture-of-resolution-pathways); [Chapter Eight](core_08-08_misconduct.md#chapter-eight-anti-constitutional-misconduct); **CF-11.3.1**.

### Scenario ID: RS-CH5-GW-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH5-GW-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH5-GW-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH5-GW-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH5-GW-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AUTO-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AUTO-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AUTO-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AUTO-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CAP-016
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CAP-016`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-011
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-011`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-012
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-012`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-HUM-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-HUM-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-011
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-011`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-012
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-012`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-IND-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-IND-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XD-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XD-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH64-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH64-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH64-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH64-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-ROLES-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-ROLES-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-EPI-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-EPI-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-VI-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-VI-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-T7-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-T7-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AGE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AGE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AGE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AGE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AGE-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AGE-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SCI-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SCI-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SCI-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SCI-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SCI-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SCI-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CRYPT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CRYPT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CRYPT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CRYPT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CRYPT-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CRYPT-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-PROT-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-PROT-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-004
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-004`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-005
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-005`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-006
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-006`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-007
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-007`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-008
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-008`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-009
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-009`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-010
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-010`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-011
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-011`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-012
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-012`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-013
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-013`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-014
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-014`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-CH6-AX-015
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-CH6-AX-015`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-BMK-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-BMK-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-BMK-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-BMK-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-BMK-003
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-BMK-003`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AC-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AC-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-AC-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-AC-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-VOICE-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-VOICE-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-VOICE-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-VOICE-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XXV-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XXV-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-XXV-002
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-XXV-002`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.

### Scenario ID: RS-SL-001
- **Class:** implementation / catalog seed (reinstatement)
- **Summary:** Tracked row for `RS-SL-001`; advance narrative when tabletop or hook pass produces evidence. Pointer discipline: **Chapter Six** classification vs **Chapter Eight** final slot labels; **Chapter Ten** rights-floor boundary per closing Part D section.
- **Read with:** [doc_architecture.md](doc_architecture.md) section 5; owner layers per scenario family name.


## 6) Scoring and evaluation

Weighted model **SCORING-v1** is defined in `tools/scoring_v1.py`. The audit does not recompute a tabletop score; it validates internal consistency of the **authored** snapshot.

## 7) Optional section placeholders

Historical subsection labels (*7A.1*, *7E*, etc.) refer to the families above. Detailed narratives may be expanded per drill without moving owner-layer law.

### 7E) Humanity/Individual/ Cross-layer stress (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`)

Seeded in draft until tabletop pass evidence is filed under `evidence/<YYYY-MM-DD>/`. `RS-XD-001` checks **Chapters 11–13** vs **Chapter Six** classification authority; `RS-XD-002` rights-layer process-creep; `RS-XD-003` custody chain; `RS-XD-004` / `RS-XD-005` emergency and evidence-gate controls.

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

