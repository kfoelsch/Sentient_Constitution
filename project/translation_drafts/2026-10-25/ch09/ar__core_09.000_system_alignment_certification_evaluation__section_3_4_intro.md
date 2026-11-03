<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (ar)

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

*بعبارات بسيطة: يجب أن ينظر التصديق أيضًا إلى أنواع البيانات التي يمسها النظام وما إذا كان يتعامل معها على النحو المناسب — بما في ذلك ما إذا كانت الأنواع لا تزال صحيحة في دورة المراجعة الحالية، وما إذا كانت البنية التحتية الأساسية قوية بما يكفي لتلك البيانات في فئة النظام المعنية. توجد قواعد الأنواع و[سجل أنواع بيانات النظام](core_05.040_band_continuity.md#system-data-types-record) في مدونة الأنظمة؛ ويتحقق التصديق من تطبيق القواعد فعليًا ومن صدق السجل.*

يجب أن يقيّم تصديق مواءمة النظام **أنواع البيانات والتعامل معها** ضمن كل سجل تصديق ذي أثر جوهري. يبيّن هذا القسم ما يجب أن يتحقق منه التصديق. ويقع تصنيف الأنواع وآليات التعامل معها في **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*أنواع المعلومات والتعامل معها*) و[CS-6.310 — تصنيفات البيانات](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**، إلى جانب:

- التعريفات المعتمدة لأنواع المعلومات؛
- قواعد التعامل ومتطلبات الفصل؛
- تفاصيل دورة الحياة؛ و
- [سجل أنواع بيانات النظام](core_05.040_band_continuity.md#system-data-types-record) الدائم.

**متطلب التقييم.** يجب أن تحدد عملية التصديق ما إذا كان النظام:

- يحدد أنواع البيانات الداخلة جوهريًا في النطاق؛ و
- يتعامل معها وفق **أشد تصنيف منطبق**، بما يشمل التحويل والتجميع والتفويض والتخزين والاحتفاظ والربط بين المجالات.

يجب أن يعكس التقييم الأثر الوظيفي، لا التسمية أو التنسيق أو مرحلة خط المعالجة وحدها.
