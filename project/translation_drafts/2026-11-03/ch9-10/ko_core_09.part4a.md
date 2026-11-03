##### 5.3.4 지도 및 기록 무결성

의존 지도와 자원 흐름 기록에 의존하기 전에, 인증은 그것들이 **제V-A조**(*의존 지도화 및 자원 흐름 투명성*)를 충족하는지 확인해야 합니다. 다음 조건을 갖춰야 합니다.

- **완전성:** 중요한 경우, 중대한 상류·하류 의존과 자원 흐름 및 숨겨져 있거나 일방적인 관계를 포괄해야 합니다.
- **최신성:** 변화 속도와 시스템의 중요성( [§2 시스템 등급 평가](#2-system-class-evaluation)에 따른 시스템 등급 포함)에 비추어 충분히 자주 갱신되어야 합니다. 마지막 인증 당시가 아니라 현재 운영 중인 시스템을 보여야 합니다.
- **감사 가능성:** **제XVI-A조**(*감사가능성 및 관찰 가능한 증거*)에 따라 감사에 열려 있어야 합니다.

이 기준 중 하나라도 충족하지 못하는 지도나 기록으로는 시스템이 충분히 되돌려 준다고 판단할 수 없습니다. 그 공백을 문서화하고 아래 *결함 및 정렬 불일치*에 따라 처리해야 합니다.

<a id="535-system-class-scaling-and-escalation"></a>
##### 5.3.5 시스템 등급별 조정 및 상향

시스템 등급은 검토 깊이와 충분성 판단의 엄격성을 정합니다. 그렇다고 공유 자원 추출을 중요하지 않은 것으로 취급할 수는 없습니다. 여러 주체·기록·기간에 걸쳐 나뉜 추출은 [제1장 §15.1.1 분할 방지 원칙](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle)에 따라 하나로 판단합니다. 중요성 발동 요건이 충족되면 다음을 적용합니다.

- 공유 유역이나 지역 전력망의 중추 등 감지자가 생존을 위해 필요한 공유 기반을 이용하는 시스템은 의존 지도와 반환 흐름에 대한 가장 강력한 증거를 기록에 남겨야 합니다. 이러한 공유 시스템의 지속적인 역량은 [제1장 §9 공유 시스템 역량](core_01.000_values_principles.md#9-shared-system-capacity)이 보호하며, **제III-A조**(*생존*) 때문에 여기서 가장 강력한 입증이 요구됩니다.
- 공유 인증·보건 정보기술 또는 유사 인프라에 의존하는 시스템은 무엇을 가져가고 지원이 충분한지를 운영의 중요도에 맞는 깊이로 문서화해야 합니다. 「상호운용성」에 대한 막연한 구호는 증거가 아닙니다. [제1장 §18.5 모듈형 구조 및 의존 원칙](core_01.010_stewardship_capacity_principles.md#185-modular-architecture-and-dependency-discipline)이 요구하듯 의존은 지도와 기록에서 드러나야 합니다.
- 현실적으로 전환할 수 없는 기관들을 대상으로 지급·신원·인력 배치의 병목 지점이 되면서도 시스템 간 검토를 조용히 회피해서는 안 됩니다.
  - **전환할 수 없는 대상:** [§5.3.3 평가 요건](#533-evaluation-requirement)의 대체 가능성 요소에 따라 판단합니다.
  - **중요성:** 이는 [제1장 §11.4 자원 및 의존 집중](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)이 설명하는 집중의 유형입니다. 예를 들어 실질적인 대안 없이 단일 제공자에게 의존하는 감지자나 시스템의 수, 공유 인프라의 인터페이스와 접근 지점을 누가 통제하는지에 대해 채택자가 기준을 설정하도록 합니다. 인증은 검토를 강화하기 전에 채택자의 기준이 초과되기를 기다리지 않습니다(아래 참조).
  - **인증의 조치:** [§2.2 모든 평가에 적용되는 시스템 등급 조정](#22-how-system-class-scales-every-evaluation)에 따라 검토를 강화하고 시스템 등급을 재고합니다. 시스템이 생존 필수 조정의 접근을 통제하는 경우 **A등급**까지 상향합니다.

상향 조치는 [제1장 §11.4 자원 및 의존 집중](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)에 따라 설정한 집중 임계치를 기다리지 않습니다. 채택자가 정하고 시스템이 초과한 임계치는 추가 증거가 됩니다. 임계치를 정하지 않았거나 너무 높게 정했다고 상향 조치를 늦출 수 없으며, 임계치 초과만으로 위법 행위가 확인되는 것도 아닙니다.

<a id="536-defects-and-misalignment"></a>
##### 5.3.6 결함 및 정렬 불일치

[§5](#5-rights-floor-and-domain-evaluations)(*권리 바닥 및 분야별 평가*)의 결함은 시스템이 공개해야 하는 **제V-A조**(*의존 지도화 및 자원 흐름 투명성*)상의 의존 또는 자원 흐름 정보까지 포함하여 이 평가에도 적용됩니다. 또한 다음 각 항목은 인증 결함입니다.

- 다음 중 어느 하나를 [비례적 시스템 간 지원](core_05.040_band_continuity.md#proportionate-cross-system-support)을 충족하기에 충분한 것으로 취급함:
  - 상징적·불투명한·지도에 없는·일회성 이전;
  - 시스템이 **제III-A조**(*생존*)의 생존 하한을 충족한다는 사실; 또는
  - 시스템이 [제1장 §11 시장 구조](core_01.000_values_principles.md#11-market-structure)의 시장 집중 한계 안에 있다는 사실;
- 중요성 발동 요건이 적용되는데도 비례적인 반환 없이 공유 기반에서 반복해서 추출함;
- 주로 포획 또는 집중을 고착하는 지원; 및
- **제V-A조**(*의존 지도화 및 자원 흐름 투명성*)가 요구하는 투명성을 무력화하는 조건부 지원.

문서화된 지원 공백은 [제1장 §6 신뢰와 신뢰 가능성](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)에 따라 산입됩니다.

<a id="54-nondiscrimination-evaluation"></a>

#### 5.4 차별 금지 평가

<details>
<summary><strong><span style="color: #2563eb;">추적 경로</span></strong></summary>

- 상위 규범:
  - [C부분 §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record)(9.010 §8)(*기록 내용*);
  - [§2](#2-system-class-evaluation)(*시스템 등급 평가*); 참여 측정 계열(*헌법상 측정으로서의 실질적 공정성, 보호 특성 대리 지표화 및 차등 영향*); **제VI-C조**(*차별 금지*);
  - [실질적 공정성](core_05.055_band_participation.md#substantive-fairness),
  - [보호 특성](core_05.055_band_participation.md#protected-characteristics),
  - [보호 특성 대리 지표화 및 차등 영향](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact),
  - [언어·문화·유산](core_05.040_band_continuity.md#language-culture-and-heritage),
  - [필요성](core_05.035_band_accountability.md#necessity), 및
  - [비례성](core_05.035_band_accountability.md#proportionality)(제5장).
- 상위 규범: 원칙 — 제1장
  - [§3.1 공정성](core_01.000_values_principles.md#31-fairness)(특히 [§3.1.2 혜택과 부담](core_01.000_values_principles.md#312-benefits-and-burdens)) 및
  - [§11.4 자원 및 의존 집중](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)(*관문 통제; §5.4.2의 상향 단계*).
- 하위 규범:
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class)(*시스템 등급별 차별 금지 적용 예시*);
  - [C부분 §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record)(9.010 §8.2)(*기록 무결성*);
  - [C부분 §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate)(9.010 §11.3)(*검증 입력 관문*);
  - [B부분 §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)(9.005 §7)(*차별 패턴에 따른 정렬 불일치 및 대리 지표 회피*).
- 인증이 포럼·행정·집행에 대한 접근을 제한하는 경우 **제VI-C조**(*차별 금지*)의 판정 및 운영 의무와 함께 읽기; [*차별 금지, 보호 특성, 존엄성, 친밀 신호 제한, **제VII-E조**(*성인 간 합의된 상업적 성 서비스 및 성 착취*) 지위*](core_05.055_band_participation.md#fairness-protected-characteristics-and-nondiscrimination)와 함께 읽기.
- 하위 절:
  - [§5.4.1](#541-evaluation-requirement)(*평가 요건*);
  - [§5.4.2](#542-system-class-scaling-and-escalation)(*시스템 등급별 조정 및 상향*);
  - [§5.4.3](#543-defects-and-misalignment)(*결함 및 정렬 불일치*);
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class)(*시스템 등급별 차별 금지 적용 예시*).

</details>

<br>

*쉬운 말로: 어떤 시스템은 누가 들어갈 수 있는지 결정합니다. 어떤 시스템은 누가 더 많이 내는지 정합니다. 또 어떤 시스템은 누구를 낮게 평가하거나 더 큰 부담을 지울지 결정합니다. 시스템이 중요한 방식으로 이런 결정을 내릴 때 인증은 한 가지를 묻습니다. 피해가 주로 보호 특성이 있는 감지자에게, 또는 그 특성을 대신하는 특성에 떨어지는가? 규칙이 중립적이라는 운영자의 말만으로는 답이 되지 않습니다. 적용 예시는 [CS-9.320 §9 시스템 등급별 차별 금지 적용 예시](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class)에 있습니다.*

이 절은 실질적 영향을 미치는 시스템이 자격 규칙·모델 특성·순위 논리·플랫폼 정책 또는 이에 준하는 결정 경로를 통해 감지자 사이의 부담과 혜택을 실질적으로 분류·순위화·가격 책정·제한·배제·배분하는 경우 적용됩니다.

시스템 정렬 인증은 중요성 발동 요건이 적용되는 경우 **제VI-C조**(*차별 금지*), [실질적 공정성](core_05.055_band_participation.md#substantive-fairness), [보호 특성 대리 지표화 및 차등 영향](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact)에 따라 **차별 금지**를 평가해야 합니다.

<a id="541-evaluation-requirement"></a>
##### 5.4.1 평가 요건

*쉬운 말로: 이 장은 포용 할당량을 정하지 않습니다. 공정성 공식을 고르지도 않습니다. 다른 문서가 이를 다룰 수 있고, 코퍼스에 나중에 추가되거나 채택자가 작성하는 문서도 마찬가지입니다. 인증은 누가 혜택을 받고 누가 부담을 지는지, 보호 특성을 대신하는 지표가 작동하는지 실제로 살펴보았는지만 확인합니다. 발동 요건이 적용되는 모든 경우에 이 평가를 합니다.*

인증 절차는 시스템이 실질적으로 의존하는 결정 경로가 다음 중 어느 하나를 근거로 감지자에게 실질적 부담·배제·피해를 부과하는지 판단해야 합니다.

- [보호 특성](core_05.055_band_participation.md#protected-characteristics);
- 그 대리 지표; 또는
- [언어·문화·유산](core_05.040_band_continuity.md#language-culture-and-heritage)에 따른 전문화 등 기능상 대체물로 사용되는 자의적 집단 구분.

평가는 [실질 이해관계](core_00.000_preamble.md#material-stake)에 비례하여 다음을 수행해야 합니다.

- [실질적 공정성](core_05.055_band_participation.md#substantive-fairness)에 따른 부담·혜택 패턴을 시험합니다. 그리고
- [보호 특성 대리 지표화 및 차등 영향](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact)에 따른 대리 지표 또는 차등 영향 위험을 시험합니다.

차등 대우는 문서화된 [필요성](core_05.035_band_accountability.md#necessity), [비례성](core_05.035_band_accountability.md#proportionality) 및 실질적 공정성이 정당화하는 경우에만 허용됩니다. 평가는 표면상의 중립성·선언된 의도·표지가 아니라 기능상 효과를 반영해야 합니다.

<a id="542-system-class-scaling-and-escalation"></a>
##### 5.4.2 시스템 등급별 조정 및 상향

시스템 등급은 평가 깊이를 정합니다. 순위화나 부담 전가를 중요하지 않은 것으로 취급할 수는 없습니다. 중요성 발동 요건이 충족되면 다음을 적용합니다.

- **중단·통지 또는 이에 준하는 규칙으로 생존 필수 요소를 차단할 수 있는 시스템:**
  - 일반적인 모범 사례 문구가 아니라 부담·혜택 및 대리 지표에 관한 가장 강력한 분석을 기록에 남겨야 합니다. 그리고
  - 숨겨진 비용 전가는 [제1장 §3.1.2 혜택과 부담](core_01.000_values_principles.md#312-benefits-and-burdens)을 충족하지 못합니다.
- **매칭 또는 경로 지정 논리가 응급 치료·혜택·자격 접근에 영향을 주는 시스템:**
  - 기록에는 운영상 중요도에 맞춘 차등 영향 및 실질적 공정성 판단이 있어야 합니다. 그리고
  - [제1장 §3.1 공정성](core_01.000_values_principles.md#31-fairness)의 공정성이란 감지자를 설명되지 않은 규칙으로 대하지 않고, 다른 이들이 피하는 비용을 떠안게 하지 않는다는 뜻이기 때문입니다.
- **교대·공급업체·예약 논리가 참여자를 실질적으로 순위화하거나 배제하는 시스템:**
  - 형식적인 공정성 문단을 실제 분석 대신 유지해서는 안 됩니다.
  - 조정이 생존 필수가 되면 인증은 [§2.2 모든 평가에 적용되는 시스템 등급 조정](#22-how-system-class-scales-every-evaluation)에 따라 검토와 재분류를 상향해야 합니다. 시스템이 인력 배치나 응급 경로 지정을 제한하는 경우 **A등급**으로 재분류하는 것도 포함됩니다. 그리고
  - 이런 관문 통제는 [제1장 §11.4 자원 및 의존 집중](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)에 따른 집중 지표입니다. 많은 감지자나 시스템이 실질적인 대안 없이 단일 제공자에게 의존하기 때문이며, 따라서 인증은 여기서 검토를 강화합니다.

<a id="543-defects-and-misalignment"></a>
##### 5.4.3 결함 및 정렬 불일치

이 평가에는 두 가지 결함 묶음이 적용됩니다.

- **절 전체에 적용되는 결함:**
  - [§5](#5-rights-floor-and-domain-evaluations)(*권리 바닥 및 분야별 평가*)의 결함이 이 평가에도 적용됩니다. 그리고
  - **제VI-C조**(*차별 금지*)가 검토를 요구하는 실질적인 분류·순위화·부담 배분 논리에도 적용됩니다.
- **차별 금지 결함:** 다음 각 항목도 인증 결함으로 처리해야 합니다.
  - 평가 가능한 부담·혜택 분석 없이 표면상 중립성, 집계된 편의 지표 또는 운영자의 자기 보고만으로 충분하다고 취급함; 및
  - **제VI-C조**(*차별 금지*)의 **필요성** 및 **비례성** 시험을 충족하지 않은 채 균질화·상호운용성·효율성이라는 틀을 이용해 언어·문화·유산 보호를 무력화함.

문서화된 대리 지표 차별 또는 실질적 불공정성은 [제1장 §6 신뢰와 신뢰 가능성](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)에 따라 산입됩니다.

<a id="55-accessibility-evaluation"></a>
