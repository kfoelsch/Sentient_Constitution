<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (ko)

## English source (lines 311–335)

This section states what certification must verify:

- **Evaluation requirement:**
  - whether the assigned system class reflects observed and reasonably foreseeable **impact**, **dependency**, and **risk** under CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*), including:
    - aggregate effects;
    - interaction effects;
    - adversarial effects;
    - threshold effects;
  - that classification is determined by actual system behavior and impacts, not from:
    - declared intent;
    - nominal scope;
    - [System Charter](core_05.040_band_continuity.md#system-charter) text alone; or
    - self-description alone;
  - that the system's class was re-checked under the **[CS-9.305 §3.5 reclassification requirement](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** whenever a significant change called for it; and
  - that the [System Classification Record](core_05.040_band_continuity.md#system-classification-record) shows the **highest system class that applies** under current conditions.
- **Assurance and regression testing:**
  - that system-class-scaled assurance, infrastructure robustness, and regression coverage match the assigned system class under:
    - CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*); and
    - CS-6.345 (*System lifecycle*), read with these shared operational terms where materially applicable:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*Continuity: graceful degradation and failure-mode integrity terms*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*Continuity: reversibility and containment terms*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*Continuity: adversarial robustness and abuse-resistance terms*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*Integrative: constrained-secrecy and protected-investigation terms*), where the system's class or function makes it materially applicable; and
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*Integrative: intervention and override integrity terms*), where the system's class or function makes it materially applicable; and
  - that regression testing was run for each recertification, as CS-6.345 (*System lifecycle*) requires, with its results on the record under [§8.1 Minimum record contents](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents).

## Translation draft

이 절은 인증이 무엇을 확인해야 하는지 정한다.

- **평가 요건:**
  - 지정된 시스템 등급이 CS-9.305 (*시스템 분류 체계*) 및 CS-9.310 (*시스템 영향 분류*)에 따라 관찰되었고 합리적으로 예견 가능한 **영향**, **의존성**, **위험**을 반영하는지 여부. 여기에는 다음이 포함된다.
    - 집합 효과;
    - 상호작용 효과;
    - 적대적 효과;
    - 임계값 효과;
  - 분류는 실제 시스템 동작과 영향에 따라 결정되며 다음에 근거하지 않는다는 점:
    - 선언된 의도;
    - 명목상 범위;
    - [시스템 헌장](core_05.040_band_continuity.md#system-charter) 문구만; 또는
    - 자체 설명만;
  - 중대한 변경이 요구하는 경우 **[CS-9.305 §3.5 재분류 요건](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)**에 따라 시스템 등급을 다시 확인했는지 여부; 그리고
  - [시스템 분류 기록](core_05.040_band_continuity.md#system-classification-record)에 현재 조건에서 적용되는 **가장 높은 시스템 등급**이 표시되어 있는지 여부.
- **보증 및 회귀 테스트:**
  - 등급에 맞춘 보증, 기반시설 견고성, 회귀 테스트 범위가 지정된 시스템 등급과 다음 기준에 부합하는지 여부:
    - CS-9.305 (*시스템 분류 체계*) 및 CS-9.310 (*시스템 영향 분류*); 그리고
    - CS-6.345 (*시스템 수명주기*). 실질적으로 적용되는 경우 다음 공동 운영 용어와 함께 읽는다.
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*연속성: 점진적 성능저하 및 실패 모드 무결성 용어*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*연속성: 가역성 및 봉쇄 용어*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*연속성: 적대적 견고성 및 악용 저항 용어*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*통합: 제한된 비밀유지 및 보호된 조사 용어*). 시스템 등급이나 기능상 실질적으로 적용되는 경우; 그리고
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*통합: 개입 및 재정의 무결성 용어*). 시스템 등급이나 기능상 실질적으로 적용되는 경우; 그리고
  - CS-6.345 (*시스템 수명주기*)가 요구하는 대로 재인증마다 회귀 테스트를 수행했고, 그 결과를 [§8.1 최소 기록 내용](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents)에 따라 기록했는지 여부.
