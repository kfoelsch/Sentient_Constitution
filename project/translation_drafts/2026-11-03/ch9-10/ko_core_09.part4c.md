#### 5.6 신뢰성 및 시스템 의존 무결성 평가

<details>
<summary><strong><span style="color: #2563eb;">추적 경로</span></strong></summary>

- 상위 규범:
  - [C부분 §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record)(9.010 §8)(*기록 내용*);
  - [§2](#2-system-class-evaluation)(*시스템 등급 평가*); 감독 측정 계열(*헌법상 측정으로서의 진실과 인식 무결성, 신뢰성, 신뢰 저하 및 오도된 의존*); **제XIII조**(*신뢰할 수 있고 신뢰할 만한 시스템에 대한 권리*);
  - [신뢰성](core_05.040_band_continuity.md#trustworthiness),
  - [신뢰](core_05.040_band_continuity.md#trust),
  - [신뢰 저하 및 오도된 의존](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance),
  - [다툴 수 있음](core_05.035_band_accountability.md#contestability),
  - [구제 및 시정](core_05.035_band_accountability.md#redress-and-remediation),
  - [인센티브 정렬](core_05.045_band_integrative.md#incentive-alignment),
  - [가역성](core_05.040_band_continuity.md#reversibility),
  - [중요성](core_05.050_band_oversight.md#materiality),
  - [의존](core_05.040_band_continuity.md#dependency), 및
  - [위험](core_05.040_band_continuity.md#risk)(제5장).
- 상위 규범: 원칙 — 제1장
  - [§3.1.5 현재 역량과 선제적 도움](core_01.000_values_principles.md#315-present-capability-and-proactive-help)(*현재의 감지자에게 작동하는 다툼 및 검토 경로; 실제 의존자를 기준으로 판단하는 오도된 의존; 응답하지 않는 이들에게 도달하는 생존 중요 경보*),
  - [§4 안전](core_01.000_values_principles.md#4-safety-harm-constraint),
  - [§6 신뢰](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity),
  - [§10 회복력 및 자기 치유 설계](core_01.000_values_principles.md#10-resilience-and-self-healing-design), 및
  - [§11.4 자원 및 의존 집중](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)(*피할 수 없는 의존; §5.6.2의 상향 단계*).
- 하위 규범:
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class)(*시스템 등급별 신뢰성 적용 예시*);
  - [C부분 §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record)(9.010 §8.2)(*기록 무결성*);
  - [C부분 §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate)(9.010 §11.3)(*검증 입력 관문*);
  - [B부분 §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)(9.005 §7)(*허위 신뢰 정렬 불일치, 역효과 인센티브 정렬 불일치, 복구 무결성 정렬 불일치*).
- **제XIII-A조**(*신뢰성 및 신뢰 가능성 기준*), **제XIII-B조**(*구제 및 시정 권리*), **제XVI조**(*감사, 투명성 및 독립 검증*)와 함께 읽기 — 다툼 및 감사 권리는 해당 조문이 계속 담당합니다. 고자율 시스템이 거버넌스나 검증 경로를 실질적으로 중개하는 경우 **제XIII-E조**(*고자율 시스템 및 도구 매개 절차 무결성*)와 함께 읽기; 지속적 의존이 생존 필수 접근에 영향을 주는 경우 **제III-A조**(*생존*)와 함께 읽기; 신체·건강·안전에 영향을 주는 제품이나 서비스를 시스템이 제공·목록화·추천·조언하는 경우 **제III-F조**(*안전한 제품 및 건강 정보*)와 함께 읽기; 의존하는 모든 감지자가 건강·안전 정보를 사용할 수 있어야 하는 경우 **제VI-D조**(*접근성*)와 함께 읽기; [제1장 §6 신뢰](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)(1.000 §6) 및 [제1장 §5 진실](core_01.000_values_principles.md#5-truth-epistemic-integrity-constraint)(1.000 §5)와 함께 읽기.
- 운영 조건: 제품·서비스의 건강·안전 정보 및 평점·순위·유료 홍보에 대해서는 [CJS-5.120 §10](corpus_joint_structure/cjs_05.120_participation_operations.md#product-and-service-health-and-safety-information)(*참여: 공개 충분성 및 관찰 가능성 조건*); 피해 보고 및 시정 통지에 대해서는 [CJS-5.125 §15](corpus_joint_structure/cjs_05.125_accountability_operations.md#harm-reports-and-corrective-notices)(*책무: 구조 검토, 시정 긴급성 및 공개 조건*)와 함께 읽기.
- 하위 절:
  - [§5.6.1](#561-evaluation-requirement)(*평가 요건*);
  - [§5.6.2](#562-system-class-scaling-and-escalation)(*시스템 등급별 조정 및 상향*);
  - [§5.6.3](#563-defects-and-misalignment)(*결함 및 정렬 불일치*);
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class)(*시스템 등급별 신뢰성 적용 예시*).

</details>

<br>

*쉬운 말로: 시스템이 감지자가 말과 행동을 신뢰할 수 있는지, 그리고 신뢰가 깨졌을 때 이의를 제기할 수 있는지에 실질적 영향을 준다면, 인증은 그러한 의존이 실제로 정당한지, 정직하게 공개되는지, 문제를 고칠 수 있는지 확인해야 합니다. 신뢰성 지표와 시험 묶음의 설계는 다른 문서에 있습니다. 인증은 발동 요건이 적용되는 경우 신뢰성·허위 신뢰 위험·다툼 경로를 실제로 평가했는지 확인합니다. 적용 예시는 [CS-9.320 §11 시스템 등급별 신뢰성 적용 예시](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class)에 있습니다.*

이 절은 중대한 시스템이 감지자가 시스템의 다음 사항에 기대를 걸도록 형성하는 경우 적용됩니다. 시스템의 작동, 한계, 발생 가능한 문제, 다툼 방법, 문제 해결 방식입니다. 이는 다음을 통해 이루어질 수 있습니다.

- 신뢰성에 관한 주장;
- 공개하거나 공개하지 않는 내용;
- 실제 운영 방식;
- 시스템에 내재된 인센티브;
- 실패에서 회복하는 방식; 또는
- 감지자가 시스템에 의존하게 되는 유사한 방식.

중요성 발동 요건이 적용되는 경우 시스템 정렬 인증은 다음에 따라 **신뢰성 및 시스템 의존 무결성**을 평가해야 합니다.

- **제XIII조**(*신뢰할 수 있고 신뢰할 만한 시스템에 대한 권리*);
- [신뢰성](core_05.040_band_continuity.md#trustworthiness); 및
- [신뢰 저하 및 오도된 의존](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance).

<a id="561-evaluation-requirement"></a>
##### 5.6.1 평가 요건

인증 절차는 **제XIII-A조**(*신뢰성 및 신뢰 가능성 기준*)에 따라 감지자가 시스템을 [신뢰](core_05.040_band_continuity.md#trust)하고 정확하게 의존할 만한 충분한 이유가 있는지 확인해야 합니다.

또한 다음을 시험해야 합니다.

- 감지자가 실제로 시스템에 이의를 제기하고, 결정을 재검토받고, 문제를 시정할 수 있는지 확인합니다. 서류상으로만 가능해서는 안 됩니다. 현재 상태의 감지자에게 작동해야 하며, 쉽게 답변하거나 긴 절차를 거치기 어려운 이들도 포함됩니다([제1장 §3.1.5 현재 역량과 선제적 도움](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **제XIII-A조**(*신뢰성 및 신뢰 가능성 기준*) 및 **제XIII-B조**(*구제 및 시정 권리*)).
- 감지자가 시스템이 받을 만한 수준보다 더 신뢰하거나 의존하도록 오도될 수 있는지 확인합니다. 시스템이 얻지 못한 신뢰를 얻었거나 공개하지 않은 한계를 숨기는 경우를 포함합니다. 이는 평균 감지자가 아니라 실제로 시스템을 사용하는 감지자를 기준으로 판단합니다(**제XIII-C조**(*허위 신뢰 및 오도된 의존 금지*)).
- 건강이나 안전에 영향을 미칠 수 있는 제품·서비스에 관한 시스템 정보가 정확하고, 행동하기에 충분히 완전하며, 필요한 감지자가 쉽게 찾아 이해할 수 있는지 확인합니다. 안전 경고·건강 주장·영양 정보·성분·알레르기 정보가 이에 해당합니다. 무엇이 알려지지 않았거나 시험되지 않았는지 명확하게 밝혀야 하며, 이를 안전하다고 읽힐 수 있는 공백으로 남겨서는 안 됩니다(**제III-F조**(*안전한 제품 및 건강 정보*), 시스템 층위의 연결 규범인 **제XIII-A조**(*신뢰성 및 신뢰 가능성 기준*)와 **제XIII-C조**(*허위 신뢰 및 오도된 의존 금지*)와 함께 적용).
- 건강·안전 정보를 감각·인지·언어 필요가 서로 다른 감지자가 사용할 수 있고, 결정할 때 전달되는지 확인합니다. 작은 글씨에 묻혀 있거나 한 가지 형식으로만 제공되어서는 안 됩니다(**제III-F조**(*안전한 제품 및 건강 정보*); **제VI-D조**(*접근성*); [제1장 §3.1.5 현재 역량과 선제적 도움](core_01.000_values_principles.md#315-present-capability-and-proactive-help)).
- 정보가 틀렸거나 제품이 안전하지 않은 것으로 드러나면, 이에 의존한 모두에게 피해의 긴급성에 따른 통지 기간(NU-1부터 NU-3까지) 안에 알리고 그들이 있는 곳까지 연락하는지 확인합니다. 또한 해당 긴급성의 봉쇄 및 시정 기간(CU-1부터 CU-4까지) 안에 위험한 제품이나 잘못된 정보가 나타나는 모든 곳에서 이를 봉쇄·시정하는지 확인합니다([제1장 §3.1.5 현재 역량과 선제적 도움](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **제XIII-B조**(*구제 및 시정 권리*)).
- 시스템에 내재된 보상이 속임수나 지름길을 선호하는지 확인합니다(**제XIII-D조**(*인센티브 정렬 제약*)).
- 중요한 경우, 시스템이 실패를 숨기거나 누구의 권리도 조용히 빼앗지 않고 정직하게 회복할 수 있는지 확인합니다(**제XIII-F조**(*회복력 및 자기 치유 기준*)).

시험은 [중요성](core_05.050_band_oversight.md#materiality), [의존](core_05.040_band_continuity.md#dependency), [위험](core_05.040_band_continuity.md#risk)에 비례하여 조정합니다.

평가는 시간·규모·의존 전반의 기능상 효과를 반영해야 하며 다음을 근거로 해서는 안 됩니다.

- 평판·규모·마케팅;
- 명목상 보증 표지;
- 신뢰성 배지나 공급업체 점수가 실제 인력 배치 또는 구매를 좌우하는데도 형식적으로만 신뢰성을 언급한 문단;
- 선언된 의도; 또는
- 과거 성과만으로 판단하는 것.

<a id="562-system-class-scaling-and-escalation"></a>
##### 5.6.2 시스템 등급별 조정 및 상향

검토의 깊이는 시스템 등급에 따라 달라집니다. 중요성 발동 요건이 충족되면 다음을 적용합니다.

- 시스템의 측정값·경보·복구 주장이 감지자 가구나 운영자가 생존 필수 요소에 관해 오해하게 만들 수 있다면, 시스템이 신뢰할 만하다는 주장만이 아니라 강력한 증거를 기록에 남겨야 합니다. 의존은 시스템의 실제 행동으로 얻어야 하기 때문입니다([제1장 §6 신뢰](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)). 증거는 다음을 보여야 합니다.
  - 감지자가 시스템을 신뢰할 수 있음;
  - 감지자가 허위로 안심하지 않음;
  - [제1장 §3.1.5 현재 역량과 선제적 도움](core_01.000_values_principles.md#315-present-capability-and-proactive-help)이 요구하듯, 응답하지 않은 감지자에게 후속 조치를 포함해 생존 중요 경보 및 권고가 전달됨; 및
  - [제1장 §10 회복력 및 자기 치유 설계](core_01.000_values_principles.md#10-resilience-and-self-healing-design)가 요구하듯 시스템이 실패에서 정직하게 회복함.
- 시스템의 가동 시간·매칭·응급 우회(긴급 접근) 주장이 감지자의 임상 치료나 응급 서비스 접근 여부를 통제한다면(이는 [제1장 §4 안전](core_01.000_values_principles.md#4-safety-harm-constraint)이 다루는 위험입니다), 중요도에 맞춘 상세 자료를 기록에 남겨야 합니다.
  - 감지자가 그 주장에 어떻게 이의를 제기할 수 있는지; 및
  - 감지자가 그 주장을 믿고 의존하도록 오도될 수 있는지.
- 조정이 생존에 필수가 되면 인증은 [§2.2 모든 평가에 적용되는 시스템 등급 조정](#22-how-system-class-scales-every-evaluation)에 따라 검토를 강화하고 시스템 등급을 재고해야 합니다. 오도된 의존으로 감지자가 생존에 필요한 조정에서 차단될 수 있다면 **A등급** 쪽으로 상향할 수 있습니다. 감지자가 현실적으로 피할 수 없는 의존은 [제1장 §11.4 자원 및 의존 집중](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)이 말하는 의존입니다.

<a id="563-defects-and-misalignment"></a>
##### 5.6.3 결함 및 정렬 불일치

[§5](#5-rights-floor-and-domain-evaluations)(*권리 바닥 및 분야별 평가*)의 결함은 **제XIII조**(*신뢰할 수 있고 신뢰할 만한 시스템에 대한 권리*)가 검토를 요구하는 실질적 한계·위험·실패 이력 정보까지 포함하여 이 평가에도 적용됩니다. 또한 다음 각 항목은 인증 결함으로 처리해야 합니다.

- 평가 가능한 [신뢰성](core_05.040_band_continuity.md#trustworthiness) 분석 없이 평판·보증·규모·운영자의 자기 보고만으로 충분하다고 취급함;
- **제III-F조**(*안전한 제품 및 건강 정보*)에 따라 미지 또는 미시험 상태임을 명확하게 밝히지 않고 경고가 없거나 필드가 비어 있다는 사실을 제품·서비스가 안전하다는 증거로 취급함; 및
- **제XIII조**(*신뢰할 수 있고 신뢰할 만한 시스템에 대한 권리*)의 신뢰성 및 **제XIII-A조**(*신뢰성 및 신뢰 가능성 기준*)의 다툼 원칙을 충족하지 않으면서 효율성·혁신·보안을 구실로 공개·다툴 수 있음·구제를 무력화함.

문서화된 허위 신뢰, 역효과 인센티브, 접근 불가능한 다툼 경로, 실패를 숨기는 복구 관행은 [제1장 §6 신뢰와 신뢰 가능성](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)에 따라 산입됩니다.

<br>

*포럼 절차 및 결과로 계속:* [제9장 B부분 — 포럼 절차 및 결과](core_09.005_system_alignment_certification_record_process.md#chapter-nine-part-b-system-alignment-certification--forum-process-and-outcomes)([§6 포럼 절차](core_09.005_system_alignment_certification_record_process.md#6-forum-process) 및 [§7 인증 결과](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)). *그다음 기록, 재인증 및 궤적 연결로:* [제9장 C부분 — 기록, 재인증 및 궤적](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-system-alignment-certification--record-recertification-and-standing)([§8 시스템 인증 기록](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record)부터 [§11 궤적과의 관계](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing)까지).

*각 평가 영역의 적용 예시:* [CS-9.320 시스템 정렬 인증 예시](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-system-alignment-certification-illustrations).
