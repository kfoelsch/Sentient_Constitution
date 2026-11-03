<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (pt)

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

*Em termos simples: a certificação também precisa examinar que tipos de dados o sistema acessa e se os trata adequadamente — incluindo se os tipos continuam corretos no ciclo de revisão atual e se a infraestrutura subjacente é suficientemente robusta para esses dados naquela classe de sistema. As regras de tipos e o [Registro de Tipos de Dados do Sistema](core_05.040_band_continuity.md#system-data-types-record) estão no corpus de sistemas; a certificação verifica se as regras foram realmente aplicadas e se o registro é fiel.*

A certificação de alinhamento do sistema deve avaliar **tipos e tratamento de dados** como parte de todo registro de certificação com impacto material. Esta seção estabelece o que a certificação deve verificar. A taxonomia de tipos e os mecanismos de tratamento estão em **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Tipos e tratamento de informações*) e [CS-6.310 — Classificações de dados](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, juntamente com:

- definições canônicas dos tipos de informação;
- regras de tratamento e requisitos de separação;
- detalhes do ciclo de vida; e
- o [Registro de Tipos de Dados do Sistema](core_05.040_band_continuity.md#system-data-types-record), durável.

**Requisito de avaliação.** O processo de certificação deve determinar se o sistema:

- identifica os tipos de dados materialmente incluídos no escopo; e
- os trata conforme a classificação **mais restritiva aplicável**, inclusive durante transformação, agregação, delegação, armazenamento, retenção e vinculação entre domínios.

A avaliação deve refletir o efeito funcional, não apenas o rótulo, o formato ou a etapa do pipeline.
