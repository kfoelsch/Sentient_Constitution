<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (mr)

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

*सोप्या शब्दांत: प्रणाली कोणत्या प्रकारच्या डेटाला स्पर्श करते आणि तो योग्यरीत्या हाताळते का हेही प्रमाणनाने पाहिले पाहिजे — सध्याच्या पुनरावलोकन चक्रात डेटा प्रकार योग्य आहेत का आणि त्या प्रणाली-वर्गात त्या डेटासाठी अंतर्निहित पायाभूत सुविधा पुरेशी मजबूत आहे का हेही यात येते. प्रकारांचे नियम आणि [प्रणाली डेटा प्रकार नोंद](core_05.040_band_continuity.md#system-data-types-record) प्रणाली-संग्रहात आहेत; नियम प्रत्यक्ष लागू केले गेले आणि नोंद प्रामाणिक आहे का हे प्रमाणन तपासते.*

प्रणाली-संरेखन प्रमाणनाने प्रत्येक महत्त्वपूर्ण प्रभाव असलेल्या प्रमाणन नोंदीचा भाग म्हणून **डेटा प्रकार आणि हाताळणी**चे मूल्यांकन केले पाहिजे. प्रमाणनाने काय पडताळावे हे हा विभाग सांगतो. प्रकार-वर्गीकरण आणि हाताळणी यंत्रणा **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*माहितीचे प्रकार आणि हाताळणी*) आणि [CS-6.310 — डेटा वर्गीकरणे](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** मध्ये आहेत; तसेच:

- माहिती-प्रकारांच्या प्रमाणित व्याख्या;
- हाताळणी नियम आणि विभाजन आवश्यकता;
- जीवनचक्र तपशील; आणि
- टिकाऊ [प्रणाली डेटा प्रकार नोंद](core_05.040_band_continuity.md#system-data-types-record).

**मूल्यांकनाची आवश्यकता.** प्रमाणन प्रक्रियेने प्रणाली:

- महत्त्वपूर्णरीत्या व्याप्तीत असलेले डेटा प्रकार ओळखते का; आणि
- रूपांतरण, एकत्रीकरण, प्रतिनिधीकरण, साठवण, जतन आणि क्षेत्रांमधील जोडणी यांसह **लागू असलेल्या सर्वाधिक प्रतिबंधक** वर्गीकरणानुसार ते हाताळते का;

हे ठरवले पाहिजे. मूल्यांकनाने कार्यात्मक परिणाम दाखवला पाहिजे; केवळ लेबल, स्वरूप किंवा प्रक्रियाप्रवाहातील टप्पा नव्हे.
