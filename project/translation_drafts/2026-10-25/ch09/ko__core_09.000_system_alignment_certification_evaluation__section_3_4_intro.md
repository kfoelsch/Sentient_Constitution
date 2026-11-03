<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (ko)

## English source (lines 636–650)

*In plain terms: certification also has to look at what kinds of data the system touches and whether it handles them appropriately — including whether types are still right on the current review cycle, and whether the underlying infrastructure is strong enough for that data at that system class. The type rules and the System Data Types Record live in the systems corpus; certification checks that the rules were actually applied and that the record is honest.*

System alignment certification must evaluate **data types and handling** as part of every materially impactful certification record. This section states what certification must verify. The type taxonomy and handling mechanics live in **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Information types and handling*) and [CS-6.310 — Data classifications](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, together with:

- canonical information-type definitions;
- handling rules and separation requirements;
- lifecycle detail; and
- the durable [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record).

**Evaluation requirement.** The certification process must determine whether the system:

- identifies the data types materially in scope; and
- handles them under the **most restrictive applicable** classification, including across transformation, aggregation, delegation, storage, retention, and cross-domain linkage.

Evaluation must reflect functional effect, not label, format, or pipeline stage alone.

## Translation draft

*쉽게 말해, 인증은 시스템이 어떤 유형의 데이터를 다루는지, 그리고 적절하게 처리하는지도 살펴야 한다. 현재 검토 주기에도 데이터 유형이 여전히 적절한지, 해당 시스템 등급에서 그 데이터를 다루기에 기반시설이 충분히 견고한지도 포함된다. 유형 규칙과 [시스템 데이터 유형 기록](core_05.040_band_continuity.md#system-data-types-record)은 시스템 코퍼스에 있으며, 인증은 규칙이 실제로 적용되었고 기록이 정직한지 확인한다.*

시스템 정렬 인증은 중대한 영향을 미치는 모든 인증 기록의 일부로 **데이터 유형 및 처리**를 평가해야 한다. 이 절은 인증이 무엇을 확인해야 하는지 정한다. 유형 분류 체계와 처리 방식은 **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*정보 유형 및 처리*) 및 [CS-6.310 — 데이터 분류](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**에 있으며, 다음도 포함한다.

- 정보 유형의 정식 정의;
- 처리 규칙과 분리 요건;
- 수명주기 세부사항; 및
- 지속적으로 유지되는 [시스템 데이터 유형 기록](core_05.040_band_continuity.md#system-data-types-record).

**평가 요건.** 인증 절차는 시스템이 다음을 수행하는지 판정해야 한다.

- 실질적으로 범위에 포함된 데이터 유형을 식별하는지; 그리고
- 변환, 집계, 위임, 저장, 보존, 도메인 간 연결을 포함해 **적용 가능한 가장 엄격한** 분류에 따라 처리하는지.

평가는 라벨, 형식 또는 파이프라인 단계만이 아니라 기능적 효과를 반영해야 한다.
