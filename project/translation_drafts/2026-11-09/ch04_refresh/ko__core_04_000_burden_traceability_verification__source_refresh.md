<!-- Locale: Korean (ko) | Source commit: 630b161c | Baseline commit: 5148086b9fb43a343616db52cf3ef2018e2c46cb | AI-drafted, unreviewed | Partial changed-passage refresh -->

> **하위:** [제9장 — 시스템 정렬 인증](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification); [제11장 — 지위 기록](core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened).

> - **헌법상 담당:** 입증 부담 배분, 준수 증거, 정의 추적성, 관찰 가능성, 보안 제약을 받는 검증. 이 장과 함께 읽는 지위 기록 및 검증된 입력 규율은 **제11장**이 담당한다.

> - **관할 이전 금지 규칙:** 이 장은 입증 부담, 추적, 관찰 가능성, 보안 한계, 증거만을 다룬다. 제5장 정의, **제12장**의 기여 또는 지위 측정, 제14장의 반헌법적 위법행위 기준을 다시 서술하지 않는다. 검증된 비준수의 지위 절차 회부는 [제3장 §3 — 비준수 판단 프로필](core_03.000_definition_integrity.md#3-non-compliance-finding-profiles)과 [제11장 — 지위 기록](core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened)이 정한다. **§6**은 제2장에서 제4장까지와 [제9장 — 시스템 정렬 인증](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification)의 차이를 밝힌다.

| **1 — 누가 입증하는가** | 준수를 주장하는 쪽에 입증 부담이 있다 | [§1 배타적 집행과 입증 부담 배분](#1-exclusive-enforcement-and-burden-allocation) |
| **2 — 지도를 제시하라** | 정의에서 관찰 가능한 행동까지의 구조화된 추적 | [§2 정의 추적성 요건](#2-definition-traceability-requirement) |
| **3 — 확인 가능하게 하라** | 이론이 아니라 실제로 지도를 검증할 수 있도록 시스템이 충분한 정보를 드러내야 한다 | [§3 추적성 관찰 가능성 요건](#3-observability-of-traceability-requirement) |
| **4 — 보안 한계** | 실제 보안 한계는 허용되지만, 구실로 만든 차단은 허용되지 않는다 | [§4 보안 제약형 관찰 가능성 및 검증 규칙](#4-security-constrained-observability-and-verification-rule) |
| **5 — 무엇이 증거인가** | 증거는 실재하고 완전하며 독립적이고 지속적이어야 한다 | [§5 준수 증거 기준](#5-compliance-evidence-standard) |

**쉬운 언어 접근.** [제1장 §5.2 — 쉬운 언어 접근성(참여 및 관리 의무)](core_01.000_values_principles.md#52-plain-language-accessibility-participation-and-stewardship-duty)은 센티언트가 권리를 행사하고, 결정에 이의를 제기하거나 준수를 검증할 때 사용하는 거버넌스·재판·운영 자료에 적용된다. 쉬운 언어는 제2장부터 제4장까지의 요구를 **바꾸거나 줄이지 않는다**. 쉬운 언어판이 여기의 정의 또는 검증 규칙과 다르면 해당 규칙이 우선한다. 전문용어, 복잡성의 누적 또는 불투명성을 이용해 [이의제기 가능성](core_05.035_band_accountability.md#contestability)이나 [제16조: 감사, 투명성 및 독립 검증](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification) 접근을 막는 것은 이 장과 **제1장 §5.2 쉬운 언어 접근성(참여 및 관리 의무)**에 따른 비준수다.

- **측정 방법(M)** — 각 층위에 적용되는 측정치

*쉽게 말해: §2는 추적 지도를 요구한다. 이 절은 권한이 있는 당사자나 영향을 받는 당사자가 이론뿐 아니라 실제로도 지도를 확인할 수 있도록 시스템이 충분히 드러내야 한다고 요구한다. 불투명한 구조, 외부 의존성, 블랙박스 구성요소는 면책되지 않는다.*

- 상위 원칙: [제4장 §3 — 추적성 관찰 가능성 요건](#3-observability-of-traceability-requirement); [제1장 §6.2 — 인식론적 공개 제약](core_01.005_interaction_interpretation.md#132-epistemic-disclosure-constraints) (1.005).
- 하위: [제4장 §5 — 준수 증거 기준](#5-compliance-evidence-standard); [CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*정보 유형과 취급*) 및 [CS-6.310 — 데이터 분류](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications), 그리고 [CS-6.340](corpus_systems/cs_06.340_system_requirements.md#cs-6340-system-requirements) (*시스템 요건*) — 사용자 대면 기능 표면, 자격 증명, 정보 유형 취급.

암호화 및 정보 유형 취급은 헌법 및 **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*정보 유형과 취급*) 및 [CS-6.310 — 데이터 분류](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**와 정렬되어야 한다. 중대한 관련성이 있는 경우 이 장에 따른 완전한 준수 검증이 여전히 가능해야 한다. 암호화 및 정보 유형 취급은 [진실(헌법상 제약)](core_05.050_band_oversight.md#truth-constitutional-constraint)이나 [안전(헌법상 제약)](core_05.040_band_continuity.md#safety-constitutional-constraint), 또는 **§2**, **§3**, **§5**의 의무를 대체해서는 안 된다.

- 하위: [제11장 — 지위 기록](core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (11.000).

  - [제1장 §13 — 헌법 충돌 해결 절차](core_01.005_interaction_interpretation.md#13-constitutional-collision-resolution-process) (1.005 §13);

- 같은 평가에서 헌법상 가치나 제약이 충돌하면 [제1장 §13 — 헌법 충돌 해결 절차](core_01.005_interaction_interpretation.md#13-constitutional-collision-resolution-process)에 부합해야 한다

- 하위: [제9장 — 시스템 정렬 인증](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification) (9.000); [제11장 — 지위 기록](core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (11.000).
- 함께 읽기: [제9장 §7 — 인증 결과](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) — 제2장부터 제4장까지에 따른 검증된 비준수는 이전 인증 여부와 관계없이 인증을 재개하거나 무효화할 수 있다.

**[제9장 — 시스템 정렬 인증](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification)**은 중대한 경우 포럼 감독을 받는 **인증 절차**를 제공한다. 여기에는 시스템 전체 평가 영역, 시스템 및 기관 인증 기록 의무, 인증 결과, 인증 간격, 이의제기 가능성 경로, 제11장으로 이어지는 검증 입력 연결고리가 포함된다. 이 장은 제2장에서 제4장까지를 **적용**하며 이를 다시 서술하지는 않는다.

- **시스템 또는 기관 인증 기록**을 제2장에서 제4장까지에 따른 지속적 준수의 대체물로 취급하는 것
