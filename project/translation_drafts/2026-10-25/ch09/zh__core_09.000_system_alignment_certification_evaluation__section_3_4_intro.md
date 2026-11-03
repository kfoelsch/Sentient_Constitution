<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (zh)

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

*简言之，认证还必须检查系统接触哪些类型的数据，以及是否妥善处理这些数据——包括这些类型在当前审查周期内是否仍然正确，以及底层基础设施对于该系统类别中的这些数据是否足够稳健。类型规则和[系统数据类型记录](core_05.040_band_continuity.md#system-data-types-record)位于系统语料库中；认证要核查规则是否实际得到应用，以及记录是否真实。*

系统对齐认证必须在每一份具有重大影响的认证记录中评估**数据类型和处理方式**。本节规定认证必须核验的事项。类型分类体系和处理机制载于**[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling)（*信息类型和处理*）和[CS-6.310 — 数据分类](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**，并包括：

- 信息类型的规范定义；
- 处理规则和隔离要求；
- 生命周期细节；以及
- 持久的[系统数据类型记录](core_05.040_band_continuity.md#system-data-types-record)。

**评估要求。**认证流程必须确定系统是否：

- 识别了实质上属于范围内的数据类型；并且
- 按照**适用的最严格**分类处理这些数据，包括转换、聚合、委派、存储、保留以及跨域关联。

评估必须反映功能效果，而不能仅依据标签、格式或处理管线阶段。
