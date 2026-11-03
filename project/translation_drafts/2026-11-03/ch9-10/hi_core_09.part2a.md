#### 2.2 हर मूल्यांकन का माप प्रणाली वर्ग कैसे तय करता है

प्रणाली वर्ग तय करता है कि इस अध्याय का हर मूल्यांकन कितनी गहराई से किया जाएगा — [§3 Whole-System Certification Evaluation](#3-whole-system-certification-evaluation) में संपूर्ण-प्रणाली कारक, [§3.4 Data Types and Handling Evaluation](#34-data-types-and-handling-evaluation) में डेटा प्रबंधन, और [§5 Rights-Floor and Domain Evaluations](#5-rights-floor-and-domain-evaluations) में प्रत्येक अधिकार-तल और क्षेत्र मूल्यांकन — तथा उसे कितनी बार दोहराया जाएगा:

- उच्च वर्ग की प्रणालियों के लिए आनुपातिक रूप से मजबूत प्रमाण चाहिए कि हर लागू मूल्यांकन वास्तव में किया गया, केवल दावा नहीं किया गया। कोई प्रणाली वर्ग केवल कागज़ पर मौजूद योग्यताओं, लेबलों या सुविधाओं, या ऐसी जाँचों और निर्णयों से संतुष्ट नहीं हो सकता जिनके भीतर कोई देख न सके।
- जहाँ trigger लागू हो, वहाँ निम्न प्रणाली वर्गों के लिए भी ईमानदार, आनुपातिक मूल्यांकन आवश्यक है।
- प्रणाली वर्ग कभी आवश्यक मूल्यांकन छोड़ने की अनुमति नहीं देता। अपनी वास्तविक भूमिका के कारण प्रणाली अपने वर्ग से आगे बढ़ जाए तो उसका पुनर्वर्गीकरण और अधिक गहराई पर पुनर्मूल्यांकन होना चाहिए। पैमाने, पहुँच या अपनाए जाने में वृद्धि, और ऐसी निर्भरता जो अधिक मजबूत, व्यापक या बदलने में कठिन हो जाए, **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Reclassification requirement*) के अधीन पुनर्मूल्यांकन trigger हैं; वे [§9.2 Reopening triggers](core_09.010_system_alignment_certification_record_recertification.md#92-reopening-triggers) के तहत समीक्षा फिर खोलते हैं। [Chapter One §11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) के तहत अपनाने वाले द्वारा तय सीमा से ऊपर संकेंद्रण, इस वृद्धि का अतिरिक्त प्रमाण है। पुनर्मूल्यांकन सीमा पार होने की प्रतीक्षा नहीं करता; सीमा तय न हो या बहुत ऊँची तय हो तो भी देरी नहीं होती।

सहभागिता और आनुपातिकता की आवश्यकताएँ भी इसी तरह मापी जाती हैं:

- **वर्ग A** प्रणालियों के लिए व्यवहार्य सबसे मजबूत सहभागिता मार्ग आवश्यक हैं, क्योंकि उपचार संभव होने से पहले त्रुटियाँ जीवन-रक्षा की आवश्यक सेवाओं तक पहुँच बंद कर सकती हैं। इनमें शामिल हैं:
  - सुलभ चुनौती;
  - stakeholder समीक्षा; और
  - [भाग B §6.1 Forum supervision and component roles](core_09.005_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles) के तहत प्रभावित दाँव के लिए नियत मंच-परिवार के निष्कर्ष, जिनमें उस खंड की माँग के अनुसार Institutional या Sentient Forums भी शामिल हैं।
- **वर्ग B** प्रणालियों के लिए मजबूत सहभागिता आवश्यक है जहाँ प्रणाली इन तक पहुँच नियंत्रित करे:
  - स्वास्थ्य देखभाल;
  - शिक्षा;
  - लाभ;
  - काम; या
  - तुलनीय दैनिक जीवन।
- **वर्ग C** प्रणालियों के लिए भी चुनौती-योग्य अभिलेख और आनुपातिक प्रकटीकरण आवश्यक हैं, खासकर जहाँ समन्वय प्रभाव:
  - संरक्षित समूहों पर अधिक बोझ डालें;
  - अनेक संज्ञ प्राणियों को उसी प्रणाली पर निर्भर छोड़ें; या
  - संकेत दें कि प्रणाली शीघ्र ही वर्ग B या वर्ग A में जा सकती है।

<a id="23-pilot-certification"></a>

#### 2.3 पायलट प्रमाणन

**[pilot](core_05.040_band_continuity.md#pilot)** एक [go-live](core_05.040_band_continuity.md#go-live) है, इसलिए [भाग B §7.1 Go-Live Gate](core_09.005_system_alignment_certification_record_process.md#71-go-live-gate) के go-live नियम के तहत शुरू होने से पहले उसका अपना प्रमाणन आवश्यक है।

- किसी भी प्रणाली वर्ग की प्रणाली से पूर्ण deployment से पहले पायलट चलाने की अपेक्षा है; ऐसा न करने वाली प्रणाली कारण दर्ज करती है।
- पायलट को भी ईमानदार वर्गीकरण और लागू trigger वाले हर मूल्यांकन की ज़रूरत है, और उसका दायरा, आबादी और अवधि अभिलेख में दर्ज होते हैं।
- उसका मूल्यांकन अपने अभिलेख पर, प्रणाली वर्ग और प्रणाली की प्रतिस्थापन-योग्यता के अनुसार गहराई में किया जाता है: क्या प्रभावित होने वाले या उस पर निर्भर रहने वाले संज्ञ प्राणियों के लिए व्यवहार्य विकल्प है, और किस लागत, देरी तथा कार्यक्षमता-हानि पर (देखें [Dependency](core_05.040_band_continuity.md#dependency))।
  - प्रणाली जितनी आसानी से बदली जा सके और उसका वर्ग जितना कम हो, पायलट मूल्यांकन उतना हल्का हो सकता है।
  - ऐसी प्रणाली का पायलट जिसे आसानी से बदला न जा सके, पूर्ण deployment पर उसके प्रणाली वर्ग के अनुसार आवश्यक गहराई से मूल्यांकित होता है।

<a id="3-whole-system-certification-evaluation"></a>

### 3. संपूर्ण-प्रणाली प्रमाणन मूल्यांकन

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- पूर्ववर्ती:
  - [Chapter One §12 Systemic Evaluation Requirement](core_01.000_values_principles.md#12-systemic-evaluation-requirement) (1.000 §12); Flourishing मापन परिवार (*कल्याण, सुरक्षा, हानि और जीवन-रक्षा न्यूनतम तक पहुँच*); Constitutional Performance मापन परिवार (*संवैधानिक दक्षता, टाली जा सकने वाली बाध्यता और उत्पादक क्षमता*);
  - [Constitutional Tetrad](core_00.000_preamble.md#constitutional-tetrad);
  - [Two Constitutional Aims](core_00.000_preamble.md#two-constitutional-aims);
  - [भौतिक दाँव](core_00.000_preamble.md#material-stake);
  - [§1 Purpose and Role](#1-purpose-and-role)।
- अनुवर्ती:
  - [CS-9.320 §4](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class) (*प्रणाली वर्ग के अनुसार संपूर्ण-प्रणाली अनुप्रयोग के उदाहरण*);
  - [§3.4](#34-data-types-and-handling-evaluation) से
  - [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) तक (*क्षेत्र मूल्यांकन*);
  - [CS-9.320 §2](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-2-illustrative-system-class-profiles) (*उदाहरणात्मक प्रणाली वर्ग प्रोफ़ाइल*);
  - [भाग C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*अभिलेख सामग्री*);
  - [भाग C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*अभिलेख अखंडता*);
  - [भाग B §6](core_09.005_system_alignment_certification_record_process.md#6-forum-process) (9.005 §6) (*चुनौती-योग्यता शृंखला*);
  - [भाग B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*प्रमाणन परिणाम*)।
- साथ पढ़ें:
  - [अध्याय एक §16](core_01.010_stewardship_capacity_principles.md#16-stewardship-in-depth) (1.010 §16),
  - [§18](core_01.010_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline), और
  - [§19](core_01.010_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture);
  - [अध्याय एक §7.4 Voluntary Discontinuation, Major Self-Modification, and Exit Rights](core_01.000_values_principles.md#74-voluntary-discontinuation-and-exit-rights) (1.000 §7.4);
  - [अध्याय एक §7.2 Assembly, Collective Organization, and Institutional Formation](core_01.000_values_principles.md#72-assembly-collective-organization-and-institutional-formation) (1.000 §7.2); जहाँ लेखापरीक्षा, पारदर्शिता या स्वतंत्र सत्यापन के अधिकार-तल भौतिक दाँव पर हों वहाँ **Article XVI** (*लेखापरीक्षा, पारदर्शिता और स्वतंत्र सत्यापन*); Continuity मापन परिवार (
  - [§3.2](#32-systemic-scope-and-risk-factors) — लचीलापन, उत्क्रमणीयता और प्रणालीगत जोखिम);
  - [Risk Evaluation](core_05.040_band_continuity.md#risk-evaluation);
  - [Risk Disclosure](core_05.050_band_oversight.md#risk-disclosure);
  - [Public Oversight Baseline Disclosure](core_05.050_band_oversight.md#public-oversight-baseline-disclosure); Participation मापन परिवार (
  - [§4.1](#41-privacy-informational-joint-invocation) — निजता और डेटा प्रबंधन); Accountability मापन परिवार (
  - [§3.1](#31-governance-incentive-and-contestability-discipline) — प्रोत्साहन-संरेखण और बाज़ार चुनौती-योग्यता);
  - [System Boundaries](core_05.040_band_continuity.md#system-boundaries);
  - [System Charter](core_05.040_band_continuity.md#system-charter)।
- उपखंड:
  - [§3.1](#31-governance-incentive-and-contestability-discipline) से
  - [§3.4](#34-data-types-and-handling-evaluation) तक (*हमेशा: शासन, प्रणालीगत कारक, समय-क्षितिज और डेटा प्रकार व प्रबंधन*)। चरण II आगे चलता है
  - [§4 Evaluations Where Implicated](#4-evaluations-where-implicated) (*जहाँ संदर्भित हो: निजता केंद्र, बाहर निकलने के अधिकार, सभा और असहमति*) और
  - [§5 Rights-Floor and Domain Evaluations](#5-rights-floor-and-domain-evaluations) (*trigger लागू होने पर*) में।

</details>

<br>

*साधारण शब्दों में: प्रणाली के एक हिस्से को हरी झंडी देकर बाकी को अनदेखा नहीं किया जा सकता। समीक्षकों को पूरी तस्वीर चाहिए — यह किस पर निर्भर है, ऊपर की कोई चीज़ विफल होने पर क्या टूटता है, बाद में दिखने वाली या समय के साथ जुड़ने वाली हानियाँ, क्या संज्ञ प्राणी वास्तव में इसका उपयोग कर सकते हैं (केवल कागज़ पर नहीं), क्या निजी जानकारी उचित रूप से अलग रहती है, क्या संज्ञ प्राणी फँसे बिना बाहर जा सकते हैं, क्या समूह प्रणाली द्वारा विभाजित हुए बिना संगठित हो सकते हैं, क्या अल्पकालीन लाभ दीर्घकालीन क्षति छिपाते हैं, और क्या बहुत कुछ दाँव पर होने पर भी वास्तविक निगरानी और जवाबदेही काम करेगी।*

*उदाहरण: [CS-9.320 §4 Illustrative whole-system application by system class](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class) दिखाता है कि यह खंड व्यवहार में कैसे लागू होता है। इसमें तीन नमूना प्रणालियाँ — प्रत्येक प्रणाली वर्ग के लिए एक — लेकर ऊपर के मूल्यांकन से गुज़ारा गया है।*

प्रमाणन मूल्यांकन को पुष्टि करनी होगी कि समीक्षाधीन प्रणाली का [भौतिक दाँव](core_00.000_preamble.md#material-stake) पूरा करने के लिए [Constitutional Tetrad](core_00.000_preamble.md#constitutional-tetrad) (सहभागिता, निगरानी, जवाबदेही और समयबद्धता) पर्याप्त रूप से मजबूत होगा।

System Certification Records में दिखना चाहिए कि इस खंड, [§4 Evaluations Where Implicated](#4-evaluations-where-implicated) और [§5 Rights-Floor and Domain Evaluations](#5-rights-floor-and-domain-evaluations) के प्रत्येक कारक पर विचार किया गया, जहाँ वह निम्न में से किसी के लिए भौतिक रूप से प्रासंगिक हो:

- प्रमाणन;
- validation;
- पुनःप्रमाणन;
- निरंतर निर्भरता;
- deployment; या
- प्रमाणन-शर्त हटाना।

केवल प्रणाली के तात्कालिक या स्थानीय प्रभावों का मूल्यांकन पर्याप्त नहीं। चरण II, संपूर्ण-प्रणाली मूल्यांकन, इस कमी को तीन भागों में पूरा करता है, जैसा नीचे तालिका में है। यह खंड **IIa** कवर करता है। [§4 Evaluations Where Implicated](#4-evaluations-where-implicated) **IIb**, और [§5 Rights-Floor and Domain Evaluations](#5-rights-floor-and-domain-evaluations) **IIc** कवर करता है। तालिका केवल मार्गदर्शिका है; इससे किसी खंड की आवश्यकता नहीं बदलती।

| कब | उपचरण | खंड | लागू |
|------|-----------|----------|---------|
| **हमेशा** | IIa | [§3.1 Governance, Incentive, and Contestability Discipline](#31-governance-incentive-and-contestability-discipline); [§3.2 Systemic Scope and Risk Factors](#32-systemic-scope-and-risk-factors); [§3.3 Time-Consistency Constraint](#33-time-consistency-constraint); [§3.4 Data Types and Handling Evaluation](#34-data-types-and-handling-evaluation) | हर भौतिक प्रभाव वाले System Certification Record पर |
| **जहाँ संदर्भित हो** | IIb | [§4.1 Privacy (Informational) Joint Invocation](#41-privacy-informational-joint-invocation); [§4.2 Voluntary Discontinuation, Major Self-Modification, and Exit Rights](#42-voluntary-discontinuation-major-self-modification-and-exit-rights); [§4.3 Assembly, Collective Organization, and Institutional Formation](#43-assembly-collective-organization-and-institutional-formation), जिसमें [§4.3.1](#431-dissent-and-peaceful-protest) शामिल है | जहाँ प्रमाणन विषय उस स्थल या सिद्धांत को भौतिक रूप से प्रभावित करे जिसका उपखंड नाम लेता है |
| **trigger लागू होने पर** | IIc | [§5 Rights-Floor and Domain Evaluations](#5-rights-floor-and-domain-evaluations) | जहाँ §5 तालिका का trigger पूरा हो |

<a id="31-governance-incentive-and-contestability-discipline"></a>
