<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (hi)

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

*सरल शब्दों में: प्रमाणन को यह भी देखना होगा कि सिस्टम किस प्रकार के डेटा को छूता है और क्या वह उन्हें उचित रूप से संभालता है—जिसमें यह भी शामिल है कि वर्तमान समीक्षा-चक्र में प्रकार अब भी सही हैं या नहीं, और उस सिस्टम वर्ग में उस डेटा के लिए अंतर्निहित अवसंरचना पर्याप्त मजबूत है या नहीं। प्रकार-नियम और [सिस्टम डेटा प्रकार अभिलेख](core_05.040_band_continuity.md#system-data-types-record) सिस्टम कॉर्पस में हैं; प्रमाणन जाँचता है कि नियम वास्तव में लागू हुए और अभिलेख सही है।*

सिस्टम संरेखण प्रमाणन को हर महत्त्वपूर्ण प्रभाव वाले प्रमाणन अभिलेख के हिस्से के रूप में **डेटा प्रकारों और उनके प्रबंधन** का मूल्यांकन करना होगा। यह अनुभाग बताता है कि प्रमाणन को क्या सत्यापित करना है। प्रकार-वर्गीकरण और प्रबंधन की कार्यविधि **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*सूचना के प्रकार और प्रबंधन*) तथा [CS-6.310 — डेटा वर्गीकरण](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** में हैं, साथ में:

- सूचना-प्रकारों की प्रामाणिक परिभाषाएँ;
- प्रबंधन नियम और पृथक्करण आवश्यकताएँ;
- जीवनचक्र का विवरण; और
- टिकाऊ [सिस्टम डेटा प्रकार अभिलेख](core_05.040_band_continuity.md#system-data-types-record)।

**मूल्यांकन की आवश्यकता।** प्रमाणन प्रक्रिया को तय करना होगा कि सिस्टम:

- उन डेटा प्रकारों की पहचान करता है जो सार्थक रूप से दायरे में हैं; और
- रूपांतरण, समेकन, प्रत्यायोजन, भंडारण, प्रतिधारण और डोमेन-पार लिंकिंग सहित **सबसे प्रतिबंधात्मक लागू** वर्गीकरण के अनुसार उन्हें संभालता है।

मूल्यांकन में कार्यात्मक प्रभाव दिखना चाहिए, केवल लेबल, प्रारूप या पाइपलाइन-चरण नहीं।
