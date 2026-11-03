#### 3.3 시간적 일관성 제약

예견 가능한 중·장기 위반이 해결되지 않은 경우, 인증은 다음 항목을 충분한 근거로 취급해서는 안 됩니다.

- 단기 지표;
- 국지적 준수; 또는
- 단기 효율성.

단기 성과를 추구하는 행위가 시간이 지나면서 다음 항목을 무너뜨릴 것으로 합리적으로 예상된다면 허용되지 않습니다. 피해가 천천히 쌓이거나 늦게 나타나거나 여러 시스템에 퍼지더라도 마찬가지입니다.

- **안전**;
- **진실**; 또는
- **웰빙**.

<a id="34-data-types-and-handling-evaluation"></a>

#### 3.4 데이터 유형 및 처리 평가

<details>
<summary><strong><span style="color: #2563eb;">추적 경로</span></strong></summary>

- 상위 규범:
  - [§3](#3-whole-system-certification-evaluation)(*전체 시스템 평가 요소*);
  - [CS-9.320 §4](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class)(*시스템 등급별 전체 시스템 적용 예시*);
  - [C부분 §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record)(9.010 §8)(*기록 내용*);
  - [§2](#2-system-class-evaluation)(*시스템 등급 평가*); 감독 측정 계열(*헌법상 측정으로서 진실과 인식의 무결성*);
  - [제XV조: 정보 영역 무결성](core_06.010_rights_part_c.md#article-xv-info-sphere-integrity);
  - [제XVI조: 감사, 투명성 및 독립 검증](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [제VII조: 자기 소유](core_06.005_rights_part_b.md#article-vii-self-ownership).
- 하위 규범:
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class)(*시스템 등급별 데이터 처리 적용 예시*);
  - [§5.1](#51-ecological-footprint-evaluation) 및
  - [CS-9.320 §6](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-6-illustrative-ecological-footprint-application-by-system-class)(*시스템 등급별 생태 발자국 적용 예시*);
  - [C부분 §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record)(9.010 §8.2)(*기록 무결성*);
  - [C부분 §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate)(9.010 §11.3)(*검증 입력 관문*);
  - [B부분 §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)(9.005 §7)(*재분류 및 처리 정렬 불일치*).
- 함께 읽기:
  - **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling)(*정보 유형 및 처리*) 및 [CS-6.310 — 데이터 분류](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**(다음 포함:
  - [CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)(*재분류 및 생애 주기 거버넌스*) 및
  - [CS-6.305 §8](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-8-system-data-types-record-governance)(*시스템 데이터 유형 기록 거버넌스*));
  - [시스템 데이터 유형 기록](core_05.040_band_continuity.md#system-data-types-record);
  - [공공 감독 기준 공개](core_05.050_band_oversight.md#public-oversight-baseline-disclosure);
  - 실질적으로 적용되는 경우 **CJS-5.130 §18**(*데이터 보유 및 생애 주기 무결성 조건*),
  - **CJS-5.130 §21**(*적대적 견고성 및 악용 저항 조건*), 및
  - **CJS-5.130 §17**(*상호운용성, 이동성 및 퇴장 무결성 조건*);
  - 사생활 지점이 관련되는 경우 [§4.1 사생활(정보) 공동 발동](#41-privacy-informational-joint-invocation).
- 하위 절:
  - [§3.4.1](#341-type-o-baseline-disclosure)(*제O유형 기준 공개*);
  - [§3.4.2](#342-privacy-discipline)(*사생활 원칙*);
  - [§3.4.3](#343-protective-storage-and-key-custody)(*보호 저장 및 키 보관*);
  - [§3.4.4](#344-scheduled-data-type-re-evaluation)(*예정된 데이터 유형 재평가*);
  - [§3.4.5](#345-system-class-scaled-infrastructure-assurance)(*시스템 등급별 인프라 보증*);
  - [§3.4.6](#346-infrastructure-robustness-for-data)(*데이터 인프라 견고성*);
  - [§3.4.7](#347-defects-and-misalignment)(*결함 및 정렬 불일치*);
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class)(*시스템 등급별 데이터 처리 적용 예시*).

</details>

<br>

*쉬운 말로: 인증은 시스템이 어떤 종류의 데이터를 다루고 이를 적절히 처리하는지도 살펴야 합니다. 현재 검토 주기에도 유형이 여전히 적절한지, 해당 시스템 등급에서 그 데이터를 처리하기에 기반 인프라가 충분히 견고한지도 포함됩니다. 데이터 유형 규칙과 시스템 데이터 유형 기록은 시스템 코퍼스에 있습니다. 인증은 규칙이 실제로 적용되었는지, 기록이 정직한지 확인합니다.*

시스템 정렬 인증은 실질적 영향을 미치는 모든 시스템 인증 기록의 일부로 **데이터 유형 및 처리**를 평가해야 합니다. 이 절은 인증이 무엇을 검증해야 하는지 명시합니다. 데이터 유형 체계와 처리 방식은 **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling)(*정보 유형 및 처리*) 및 [CS-6.310 — 데이터 분류](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**에 있으며, 다음도 포함됩니다.

- 표준 정보 유형 정의;
- 처리 규칙 및 분리 요건;
- 생애 주기 세부 사항; 및
- 지속적으로 유지되는 [시스템 데이터 유형 기록](core_05.040_band_continuity.md#system-data-types-record).

**평가 요건.** 인증 절차는 시스템이 다음을 수행하는지 확인해야 합니다.

- 실질적으로 범위에 포함되는 데이터 유형을 식별하는지; 그리고
- 변환, 집계, 위임, 저장, 보유 및 분야 간 연계 전반에서 **적용 가능한 가장 제한적인** 분류에 따라 처리하는지.

평가는 표지·형식·처리 파이프라인 단계만이 아니라 기능상의 효과를 반영해야 합니다.

<a id="341-type-o-baseline-disclosure"></a>
##### 3.4.1 제O유형 기준 공개

**[CS-6.305 §7 제O유형 기준](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems)**이 적용되는 경우, 인증은 공개된 [공공 감독 기준 공개](core_05.050_band_oversight.md#public-oversight-baseline-disclosure)(**제O유형**)가 다음을 기준으로 산정한 **인증 범위**를 포괄하는지도 검증해야 합니다.

- 지배적인 [시스템 헌장](core_05.040_band_continuity.md#system-charter);
- 지정된 시스템 등급; 및
- 관찰된 [시스템 경계](core_05.040_band_continuity.md#system-boundaries).

이 범위에는 [§3.1 거버넌스, 인센티브 및 다툴 수 있음의 원칙](#31-governance-incentive-and-contestability-discipline)에 따라 확립된 거버넌스·인센티브·다툴 수 있음 판단과 배정된 역할이 포함되어야 합니다.

인증은 L등급과 P등급을 포함한 모든 시스템 등급에서 시스템 인증 기록이 [CS-6.310 Part B §9.3 제O유형](corpus_systems/cs_06.310_data_classifications.md#93-type-o-open-public-oversight-baseline-disclosure-data)에 따른 **제O유형** 인증 데이터로 공개되는지도 검증해야 합니다. A·B·C등급 이외에는 공개를 위해 완전한 공공 감독 기준 공개가 필요하지 않습니다.

시스템 위험이 관련되는 경우 평가된 위험을 공유하는 것도 이 기준에 포함될 수 있습니다. 대중의 기준상 권리는 인증보다 더 넓으며, [시스템 분류 기록](core_05.040_band_continuity.md#system-classification-record)이나 [시스템 데이터 유형 기록](core_05.040_band_continuity.md#system-data-types-record)과 별도로 기록을 만들도록 요구하지 않습니다.

정당한 비공개 처리에는 합리적으로 가능한 가장 강력한 공개 대체물이 함께 제공되어야 합니다([§3.4.5 시스템 등급별 인프라 보증](#345-system-class-scaled-infrastructure-assurance)에 예시가 있습니다). 해당 용어는 제5장이 담당하고, 기준 내용과 공개 방식은 CS-6.305(*정보 유형 및 처리*)와 CS-6.310(*데이터 분류*)이 담당합니다.

<a id="342-privacy-discipline"></a>
