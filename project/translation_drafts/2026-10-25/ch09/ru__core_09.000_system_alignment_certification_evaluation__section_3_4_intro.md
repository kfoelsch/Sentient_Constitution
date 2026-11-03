<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (ru)

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

*Проще говоря: сертификация должна также проверять, с какими типами данных работает система и надлежащим ли образом она с ними обращается, в том числе сохраняют ли типы актуальность в текущем цикле проверки и достаточно ли надежна базовая инфраструктура для таких данных в данном классе системы. Правила типов и [Запись типов данных системы](core_05.040_band_continuity.md#system-data-types-record) находятся в корпусе систем; сертификация проверяет, что правила действительно применялись, а запись достоверна.*

Сертификация согласования системы должна оценивать **типы данных и обращение с ними** в рамках каждой записи о сертификации с существенным воздействием. Этот раздел устанавливает, что должна проверять сертификация. Таксономия типов и механизмы обращения приведены в **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Типы информации и обращение с ней*) и [CS-6.310 — Классификации данных](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, а также включают:

- канонические определения типов информации;
- правила обращения и требования разделения;
- сведения о жизненном цикле; и
- долговременную [Запись типов данных системы](core_05.040_band_continuity.md#system-data-types-record).

**Требование к оценке.** Процесс сертификации должен определить, выполняет ли система следующее:

- определяет ли типы данных, существенно входящие в сферу рассмотрения; и
- обращается ли с ними по **наиболее строгой применимой** классификации, включая преобразование, агрегирование, делегирование, хранение, удержание и связывание между доменами.

Оценка должна отражать функциональное воздействие, а не только метку, формат или этап конвейера.
