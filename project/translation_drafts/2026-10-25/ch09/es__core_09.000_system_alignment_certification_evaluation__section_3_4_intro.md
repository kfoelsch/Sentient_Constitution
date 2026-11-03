<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (es)

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

*En términos sencillos: la certificación también debe examinar qué tipos de datos toca el sistema y si los trata adecuadamente, incluidos si las clasificaciones siguen siendo correctas en el ciclo de revisión actual y si la infraestructura subyacente es suficientemente sólida para esos datos en esa clase de sistema. Las reglas sobre tipos y el [Registro de Tipos de Datos del Sistema](core_05.040_band_continuity.md#system-data-types-record) están en el corpus de sistemas; la certificación comprueba que las reglas se aplicaron realmente y que el registro es veraz.*

La certificación de alineación del sistema debe evaluar **los tipos de datos y su tratamiento** como parte de cada registro de certificación con impacto material. Esta sección establece qué debe verificar la certificación. La taxonomía de tipos y los mecanismos de tratamiento se encuentran en **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Tipos y tratamiento de la información*) y [CS-6.310 — Clasificaciones de datos](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, junto con:

- definiciones canónicas de tipos de información;
- reglas de tratamiento y requisitos de separación;
- detalles del ciclo de vida; y
- el [Registro de Tipos de Datos del Sistema](core_05.040_band_continuity.md#system-data-types-record), duradero.

**Requisito de evaluación.** El proceso de certificación debe determinar si el sistema:

- identifica los tipos de datos que están materialmente dentro del alcance; y
- los trata conforme a la clasificación **más restrictiva que corresponda**, también durante la transformación, agregación, delegación, almacenamiento, conservación y vinculación entre dominios.

La evaluación debe reflejar el efecto funcional, no solo la etiqueta, el formato o la etapa de la canalización.
