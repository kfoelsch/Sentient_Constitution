### 7. 인증 결과

<details>
<summary><strong><span style="color: #2563eb;">추적</span></strong></summary>

- 상위:
  - [§6](#6-forum-process) (*포럼 절차와 신뢰할 수 있는 이의제기*);
  - [파트 A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2)부터
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*평가에서 발견된 오분류, 부정합, 결함*)까지;
  - [두 가지 헌법적 목적](core_00.000_preamble.md#two-constitutional-aims);
  - [제3장 §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) 및
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*정의 무결성과 회피*);
  - [제3장 §2.1 일반적인 회피 패턴](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*범위와 경계 회피*);
  - [시스템 헌장](core_05.040_band_continuity.md#system-charter) (*시스템 헌장과 행동의 불일치 및 기한이 지난 심사*).
- 하위:
  - [파트 C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*결과는 기록에 명시됨*);
  - [파트 C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*결과와 함께 이의제기 경로가 열림*);
  - [파트 C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*재인증과 재개*);
  - [파트 C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*불리한 소견을 뒷받침하는 사실이 있을 때 검증된 입력 관문*);
  - [제13장](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*포럼 감독*);
  - [제10장](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- 함께 읽기: 예약된 데이터 유형 재평가에 대해서는 **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*재분류와 수명주기 거버넌스*), 시스템 등급 재평가 유발 요인과 SAC 검증에 대해서는 **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*재분류 요건*).
- 하위 절:
  - [§7.1](#71-go-live-gate) (*가동 개시 관문*, 다음을 포함:
  - [§7.1.1 이미 운영 중인 시스템](#711-systems-already-operating) 및
  - [§7.1.2 파일럿](#712-pilots));
  - [§7.2](#72-certification-defects-and-correction) (*인증 결함과 시정*);
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*시정 준비: 시정 의지와 역량*, 다음을 포함:
  - [§7.3.1 의지](#731-willingness),
  - [§7.3.2 역량](#732-capacity),
  - [§7.3.3 입증 단계](#733-proof-step),
  - [§7.3.4 소견](#734-findings), 및
  - [§7.3.5 모든 운영자에게 동일한 조건](#735-same-terms-for-every-operator));
  - [§7.4](#74-denial-and-revocation) (*거부와 취소*, 다음을 포함:
  - [§7.4.1 거부와 취소의 의미](#741-what-denial-and-revocation-are),
  - [§7.4.2 거부 또는 취소가 필요한 경우](#742-when-denial-or-revocation-is-required),
  - [§7.4.3 보호 우선](#743-protection-first),
  - [§7.4.4 절차](#744-process),
  - [§7.4.5 효과](#745-effect), 및
  - [§7.4.6 영구적인 금지가 아님](#746-not-a-permanent-bar)).

</details>

<br>

*쉽게 말해, 모든 인증 심사는 결과를 명시하며 끝난다. 결과는 증거와 그 과정에서 제기된 우려에 근거한다. 인증을 받고, 공개된 결과를 통해 영향을 받는 지각 존재에게 실질적인 이의제기 기회가 주어지며, 가동 개시 전에 필요한 보호 조치를 확인하기 전에는 어떤 시스템도 가동하지 않는다.*

이 절은 [§6 포럼 절차](#6-forum-process) (**제III단계, 심사**) 다음에 오는 **제IV단계, 결정**이다. 포럼이 도달하는 결과를 다룬다. [§7.1 가동 개시 관문](#71-go-live-gate)은 가동 개시 관문을 정하고, [§7.2 인증 결함과 시정](#72-certification-defects-and-correction)은 결함이 발견된 뒤의 조치를 정한다.

인증 결정은 결과를 [파트 C §8.1 기록의 최소 내용](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)에 따라 기록에 명시하고, 그 결과에 이르는 과정에서 제기된 우려도 함께 기록해야 한다. 결과는 다음 중 하나다.

- 잠정 인증;
- 완전 인증;
- 조건부 인증;
- 연기된 인증;
- 미인증;
- 철회;
- 만료; 또는
- 조건 해제.

잠정 인증이나 완전 인증을 보유하지 않은 시스템은 **미인증**이다. 인증이 다음 중 하나인 경우가 이에 해당한다.

- 연기됨;
- 거부됨;
- 철회됨; 또는
- 만료됨.

잠정 인증과 완전 인증은 인증의 두 **상태**다. [파트 C §9.2 잠정 및 완전 인증](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification)은 시스템이 각 상태를 획득하고, 유지하고, 상실하는 방법을 설명한다. 조건부 인증의 조건은 어느 상태에든 부과될 수 있다.

<a id="71-go-live-gate"></a>

