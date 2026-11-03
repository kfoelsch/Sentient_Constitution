<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (te)

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

*సరళంగా చెప్పాలంటే: వ్యవస్థ ఏ రకమైన డేటాను తాకుతుంది, దానిని సరిగ్గా నిర్వహిస్తుందా అన్నదీ ధృవీకరణ చూడాలి—ప్రస్తుత సమీక్ష చక్రంలో రకాలు ఇంకా సరైనవేనా, ఆ వ్యవస్థ తరగతిలో ఆ డేటాకు మౌలిక సదుపాయాలు తగినంత బలంగా ఉన్నాయా అన్నది కూడా ఇందులో భాగం. రకాలకు సంబంధించిన నియమాలు, [వ్యవస్థ డేటా రకాల రికార్డు](core_05.040_band_continuity.md#system-data-types-record) వ్యవస్థల కార్పస్‌లో ఉంటాయి; నియమాలు నిజంగా అమలయ్యాయా, రికార్డు నిజాయితీగా ఉందా అని ధృవీకరణ తనిఖీ చేస్తుంది.*

ప్రతి గణనీయ ప్రభావం గల ధృవీకరణ రికార్డులో భాగంగా వ్యవస్థ అనుసరణ ధృవీకరణ **డేటా రకాలు మరియు నిర్వహణ**ను మూల్యాంకనం చేయాలి. ధృవీకరణ ఏమి తనిఖీ చేయాలో ఈ విభాగం చెబుతుంది. రకాల వర్గీకరణ, నిర్వహణ విధానాలు **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*సమాచార రకాలు మరియు నిర్వహణ*) మరియు [CS-6.310 — డేటా వర్గీకరణలు](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**లో ఉంటాయి; వీటితో పాటు:

- సమాచార రకాల ప్రామాణిక నిర్వచనాలు;
- నిర్వహణ నియమాలు, వేర్పాటు అవసరాలు;
- జీవితచక్ర వివరాలు; మరియు
- శాశ్వత [వ్యవస్థ డేటా రకాల రికార్డు](core_05.040_band_continuity.md#system-data-types-record).

**మూల్యాంకన అవసరం.** వ్యవస్థ:

- గణనీయంగా పరిధిలో ఉన్న డేటా రకాలను గుర్తిస్తుందా; మరియు
- మార్పు, సమీకరణ, అప్పగింత, నిల్వ, నిలుపుదల, విభిన్న డొమైన్‌ల మధ్య అనుసంధానం సహా **వర్తించే అత్యంత కఠినమైన** వర్గీకరణ కింద వాటిని నిర్వహిస్తుందా;

అని ధృవీకరణ ప్రక్రియ నిర్ణయించాలి. మూల్యాంకనం లేబుల్, ఫార్మాట్ లేదా పైప్‌లైన్ దశను మాత్రమే కాకుండా కార్యాచరణ ప్రభావాన్ని ప్రతిబింబించాలి.
