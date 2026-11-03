#### 5.6 भरोसेमंदी और प्रणाली पर निर्भरता की अखंडता मूल्यांकन

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- पूर्ववर्ती:
  - [भाग C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*अभिलेख सामग्री*);
  - [§2](#2-system-class-evaluation) (*प्रणाली वर्ग मूल्यांकन*); Oversight मापन परिवार (*Truth और ज्ञानमीमांसक अखंडता; संवैधानिक मापन के रूप में भरोसेमंदी, Trust Degradation और भ्रामक निर्भरता*); **Article XIII** (*विश्वसनीय और भरोसेमंद प्रणालियों का अधिकार*);
  - [Trustworthiness](core_05.040_band_continuity.md#trustworthiness),
  - [Trust](core_05.040_band_continuity.md#trust),
  - [Trust Degradation and Misleading Reliance](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance),
  - [Contestability](core_05.035_band_accountability.md#contestability),
  - [Redress and Remediation](core_05.035_band_accountability.md#redress-and-remediation),
  - [Incentive Alignment](core_05.045_band_integrative.md#incentive-alignment),
  - [Reversibility](core_05.040_band_continuity.md#reversibility),
  - [Materiality](core_05.050_band_oversight.md#materiality),
  - [Dependency](core_05.040_band_continuity.md#dependency), और
  - [Risk](core_05.040_band_continuity.md#risk) (अध्याय पाँच)।
- पूर्ववर्ती: सिद्धांत: अध्याय एक
  - [§3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help) (*संज्ञ प्राणियों की वर्तमान स्थिति के अनुरूप काम करने वाली चुनौती और समीक्षा प्रक्रियाएँ; भ्रामक निर्भरता का निर्णय निर्भर संज्ञ प्राणियों के संदर्भ में; जीवित रहने के लिए महत्त्वपूर्ण सूचनाएँ जो जवाब न देने वालों तक पहुँचें*),
  - [§4 Safety](core_01.000_values_principles.md#4-safety-harm-constraint),
  - [§6 Trust](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity),
  - [§10 Resilience and Self-Healing Design](core_01.000_values_principles.md#10-resilience-and-self-healing-design), और
  - [§11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*ऐसी निर्भरता जिससे बचा न जा सके; §5.6.2 में उन्नयन*)।
- अनुवर्ती:
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*प्रणाली वर्ग के अनुसार भरोसेमंदी अनुप्रयोग के उदाहरण*);
  - [भाग C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*अभिलेख अखंडता*);
  - [भाग C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*सत्यापित-इनपुट द्वार*);
  - [भाग B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*झूठे भरोसे की संरेखणहीनता, विकृत प्रोत्साहन की संरेखणहीनता और पुनर्प्राप्ति-अखंडता की संरेखणहीनता*)।
- **Article XIII-A** (*विश्वसनीयता और भरोसेमंदी का न्यूनतम मान*), **Article XIII-B** (*प्रतितोष और उपचार का अधिकार*) और **Article XVI** (*लेखापरीक्षा, पारदर्शिता और स्वतंत्र सत्यापन*) के साथ पढ़ें — चुनौती और लेखापरीक्षा अधिकारों का स्वामित्व वहीं रहता है; जहाँ उच्च-स्वायत्तता प्रणालियाँ शासन या सत्यापन मार्गों में भौतिक मध्यस्थता करें वहाँ **Article XIII-E** (*उच्च-स्वायत्तता प्रणालियाँ और उपकरण-मध्यस्थित प्रक्रिया अखंडता*); जहाँ प्रणाली पर निरंतर निर्भरता से जीवन-रक्षा आवश्यकताओं तक पहुँच प्रभावित हो वहाँ **Article III-A** (*जीवन-रक्षा*); जहाँ प्रणाली शरीर, स्वास्थ्य या सुरक्षा को प्रभावित कर सकने वाले उत्पादों या सेवाओं की आपूर्ति, सूची, अनुशंसा या सलाह दे वहाँ **Article III-F** (*सुरक्षित उत्पाद और स्वास्थ्य जानकारी*); जहाँ स्वास्थ्य और सुरक्षा जानकारी हर निर्भर संज्ञ के लिए उपयोगी होनी चाहिए वहाँ **Article VI-D** (*सुगम्यता*); [Chapter One §6 Trust](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) (1.000 §6) और [Chapter One §5 Truth](core_01.000_values_principles.md#5-truth-epistemic-integrity-constraint) (1.000 §5)।
- परिचालन शर्तें: उत्पाद और सेवा की स्वास्थ्य व सुरक्षा जानकारी तथा ratings, rankings और भुगतान-आधारित प्रचार के लिए [CJS-5.120 §10](corpus_joint_structure/cjs_05.120_participation_operations.md#product-and-service-health-and-safety-information) (*Participation: disclosure sufficiency and observability terms*); हानि रिपोर्ट और सुधारात्मक सूचनाओं के लिए [CJS-5.125 §15](corpus_joint_structure/cjs_05.125_accountability_operations.md#harm-reports-and-corrective-notices) (*Accountability: structural review, correction urgency, and disclosure terms*)।
- उपखंड:
  - [§5.6.1](#561-evaluation-requirement) (*मूल्यांकन आवश्यकता*);
  - [§5.6.2](#562-system-class-scaling-and-escalation) (*प्रणाली वर्ग माप और उन्नयन*);
  - [§5.6.3](#563-defects-and-misalignment) (*त्रुटियाँ और संरेखणहीनता*);
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*प्रणाली वर्ग के अनुसार भरोसेमंदी अनुप्रयोग के उदाहरण*)।

</details>

<br>

*साधारण शब्दों में: जब कोई प्रणाली इस बात को भौतिक रूप से प्रभावित करती है कि संज्ञ प्राणी उसकी बातों और काम पर भरोसा कर सकते हैं या नहीं — और भरोसा विफल होने पर आपत्ति उठा सकते हैं या नहीं — तो प्रमाणन को जाँचना होगा कि निर्भरता वास्तव में उचित, ईमानदारी से प्रकट और सुधारी जा सकने वाली है या नहीं। विश्वसनीयता मापदंड और परीक्षण-सूची की रूपरेखा अन्य दस्तावेज़ों में है; trigger लागू होने पर प्रमाणन जाँचता है कि भरोसेमंदी, झूठे भरोसे का जोखिम और चुनौती मार्ग का वास्तविक मूल्यांकन हुआ या नहीं। उदाहरण: [CS-9.320 §11 Illustrative trustworthiness application by system class](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class)।*

यह खंड तब लागू होता है जब कोई बड़ी प्रणाली इस बात को आकार देती है कि संज्ञ प्राणी किस चीज़ के लिए उस पर भरोसा करते हैं: वह क्या करती है, उसकी सीमाएँ कहाँ हैं, क्या गलत हो सकता है, उसे चुनौती कैसे दें और समस्याएँ कैसे सुधरें। ऐसा इन तरीकों से हो सकता है:

- उसकी विश्वसनीयता के बारे में दावे;
- वह क्या प्रकट करती और क्या नहीं;
- उसका वास्तविक संचालन;
- उसमें निहित प्रोत्साहन;
- विफलताओं से उसकी पुनर्प्राप्ति; या
- संज्ञ प्राणियों की उस पर निर्भरता बनने का कोई तुलनीय तरीका।

जहाँ भौतिकता trigger लागू हो, प्रणाली-संरेखण प्रमाणन को निम्न के तहत **भरोसेमंदी और प्रणाली पर निर्भरता की अखंडता** का मूल्यांकन करना होगा:

- **Article XIII** (*विश्वसनीय और भरोसेमंद प्रणालियों का अधिकार*);
- [Trustworthiness](core_05.040_band_continuity.md#trustworthiness); और
- [Trust Degradation and Misleading Reliance](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance)।

<a id="561-evaluation-requirement"></a>
##### 5.6.1 मूल्यांकन आवश्यकता

प्रमाणन प्रक्रिया को जाँचना होगा कि संज्ञ प्राणियों के पास प्रणाली पर [भरोसा](core_05.040_band_continuity.md#trust) करने का उचित कारण है और वे **Article XIII-A** (*विश्वसनीयता और भरोसेमंदी का न्यूनतम मान*) के तहत उस पर सही ढंग से निर्भर हो सकते हैं या नहीं।

मूल्यांकन को यह भी जाँचना होगा कि:

- संज्ञ प्राणी वास्तव में प्रणाली को चुनौती दे सकते हैं, निर्णय की समीक्षा करवा सकते हैं और समस्या सुधारवा सकते हैं — केवल कागज़ पर नहीं। यह संज्ञ प्राणियों की वर्तमान स्थिति के अनुसार काम करे, जिनमें वे भी शामिल हैं जो आसानी से जवाब नहीं दे सकते या लंबी प्रक्रिया से नहीं गुजर सकते ([Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **Article XIII-A** (*विश्वसनीयता और भरोसेमंदी का न्यूनतम मान*) और **Article XIII-B** (*प्रतितोष और उपचार का अधिकार*));
- प्रणाली ने जितना भरोसा अर्जित किया है उससे अधिक भरोसा या निर्भरता के लिए संज्ञ प्राणियों को गुमराह किया जा सकता है या नहीं, चाहे ऐसा अनर्जित भरोसे से हो या ऐसी सीमाओं से जिन्हें वह प्रकट नहीं करती। इसका निर्णय उन संज्ञ प्राणियों के संदर्भ में होता है जो वास्तव में प्रणाली का उपयोग करते हैं, किसी औसत संज्ञ के संदर्भ में नहीं (**Article XIII-C** (*झूठे भरोसे और भ्रामक निर्भरता का निषेध*));
- शरीर, स्वास्थ्य या सुरक्षा को प्रभावित कर सकने वाले उत्पादों और सेवाओं के बारे में प्रणाली की जानकारी सही, कार्रवाई के लिए पर्याप्त पूर्ण, और ज़रूरतमंद संज्ञ के लिए खोजना व समझना आसान है या नहीं। इसमें सुरक्षा चेतावनियाँ, स्वास्थ्य दावे, पोषण तथ्य, सामग्री और allergen जानकारी शामिल हैं। इसमें अज्ञात या अपरीक्षित होने की बात स्पष्ट कहना भी शामिल है, बजाय ऐसा अंतर छोड़ने के जिसे “सुरक्षित” समझा जा सके (**Article III-F** (*सुरक्षित उत्पाद और स्वास्थ्य जानकारी*), साथ में प्रणालियों के स्तर पर लागू **Article XIII-A** (*विश्वसनीयता और भरोसेमंदी का न्यूनतम मान*) और **Article XIII-C** (*झूठे भरोसे और भ्रामक निर्भरता का निषेध*));
- अलग संवेदी, संज्ञानात्मक और भाषा संबंधी ज़रूरत वाले संज्ञ प्राणी सुरक्षा और स्वास्थ्य जानकारी का उपयोग कर सकते हैं, और निर्णय लेते समय वह उन तक पहुँचती है, छोटे अक्षरों में छिपी या केवल एक प्रारूप में दी हुई नहीं होती (**Article III-F** (*सुरक्षित उत्पाद और स्वास्थ्य जानकारी*); **Article VI-D** (*सुगम्यता*); [Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help));
- जब वह जानकारी गलत निकले या कोई उत्पाद असुरक्षित निकले, तो उस पर निर्भर हर व्यक्ति को हानि की तात्कालिकता के अनुरूप notice window (NU-1 से NU-3) के भीतर बताया जाता है और जहाँ वे हैं वहाँ तक पहुँचाया जाता है; तथा असुरक्षित उत्पाद या गलत जानकारी उस तात्कालिकता के containment और correction window (CU-1 से CU-4) के भीतर जहाँ भी दिखे वहाँ रोकी और सुधारी जाती है ([Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **Article XIII-B** (*प्रतितोष और उपचार का अधिकार*));
- प्रणाली में निहित पुरस्कार छल या काम में कटौती को बढ़ावा देते हैं (**Article XIII-D** (*प्रोत्साहन-संरेखण बाध्यता*)); और
- जहाँ महत्त्वपूर्ण हो, प्रणाली विफलताओं से ईमानदारी से उबर सकती है, उन्हें छिपाए या चुपचाप किसी के अधिकार छीने बिना (**Article XIII-F** (*लचीलापन और स्व-उपचार न्यूनतम मान*)।

जाँच [Materiality](core_05.050_band_oversight.md#materiality), [Dependency](core_05.040_band_continuity.md#dependency) और [Risk](core_05.040_band_continuity.md#risk) के अनुसार मापी जाती है।

मूल्यांकन को समय, पैमाने और निर्भरता के पार कार्यात्मक प्रभाव दिखाना होगा, न कि:

- प्रतिष्ठा, आकार या विपणन;
- नाममात्र आश्वासन लेबल;
- भरोसेमंदी पर दिखावटी अनुच्छेद, जबकि विश्वसनीयता badges या vendor scores वास्तव में तय करते हों कि किसे काम पर रखा जाए या क्या खरीदा जाए;
- घोषित मंशा; या
- केवल पिछला प्रदर्शन।

<a id="562-system-class-scaling-and-escalation"></a>
##### 5.6.2 प्रणाली वर्ग माप और उन्नयन

समीक्षा की गहराई प्रणाली के वर्ग पर निर्भर करती है। जहाँ भौतिकता trigger लागू हो:

- यदि प्रणाली के readings, alerts या recovery संबंधी दावे परिवारों या operators को जीवन-रक्षा की आवश्यकताओं (संज्ञ प्राणियों को जीवित रहने के लिए ज़रूरी चीज़ें) के बारे में गुमराह कर सकते हों, अभिलेख में मजबूत प्रमाण होना चाहिए, केवल प्रणाली विश्वसनीय है ऐसा दावा नहीं; क्योंकि निर्भरता प्रणाली के वास्तविक व्यवहार से अर्जित होनी चाहिए ([Chapter One §6 Trust](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity))। प्रमाण में दिखना चाहिए कि:
  - संज्ञ प्राणी प्रणाली पर भरोसा कर सकते हैं;
  - संज्ञ प्राणियों को झूठा आश्वासन नहीं मिलेगा;
  - जीवन-रक्षा के लिए महत्त्वपूर्ण alerts और advisories उन संज्ञ प्राणियों तक पहुँचती हैं जो उनकी प्राप्ति स्वीकार नहीं करते, और जवाब न मिलने पर अनुवर्ती कार्रवाई होती है, जैसा [Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help) आवश्यक करता है; और
  - प्रणाली विफलताओं से ईमानदारी से उबरती है, जैसा [Chapter One §10 Resilience and Self-Healing Design](core_01.000_values_principles.md#10-resilience-and-self-healing-design) आवश्यक करता है।
- यदि प्रणाली के uptime, matching या आपातकालीन override (“break-glass” पहुँच) संबंधी दावे तय करते हों कि संज्ञ प्राणी चिकित्सकीय देखभाल या आपातकालीन सेवा प्राप्त कर सकते हैं या नहीं (एक ऐसा जोखिम जिसे [Chapter One §4 Safety](core_01.000_values_principles.md#4-safety-harm-constraint) कवर करता है), अभिलेख में प्रणाली की महत्ता के अनुरूप विस्तार से दिखना चाहिए:
  - संज्ञ प्राणी उन दावों को कैसे चुनौती दे सकते हैं; और
  - उन्हें उन पर निर्भर रहने के लिए गुमराह किया जा सकता है या नहीं।
- जब समन्वय जीवन-रक्षा के लिए आवश्यक हो जाए, प्रमाणन को समीक्षा उन्नत करनी होगी और [§2.2 How system class scales every evaluation](#22-how-system-class-scales-every-evaluation) के तहत प्रणाली वर्ग पर पुनर्विचार करना होगा। जहाँ भ्रामक निर्भरता संज्ञ प्राणियों को जीवित रहने के लिए आवश्यक समन्वय से काट सकती है, वहाँ प्रणाली को **वर्ग A** की ओर बढ़ाना इसका अर्थ हो सकता है। ऐसी निर्भरता जिससे संज्ञ प्राणी व्यावहारिक रूप से बच नहीं सकते, वही निर्भरता है जिसका नाम [Chapter One §11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) लेता है।

<a id="563-defects-and-misalignment"></a>
##### 5.6.3 त्रुटियाँ और संरेखणहीनता

[§5](#5-rights-floor-and-domain-evaluations) (*अधिकार-तल और क्षेत्र मूल्यांकन*) की त्रुटियाँ इस मूल्यांकन पर लागू होती हैं, जिसमें वहाँ भौतिक सीमाएँ, जोखिम या विफलता का इतिहास भी शामिल है जहाँ **Article XIII** (*विश्वसनीय और भरोसेमंद प्रणालियों का अधिकार*) समीक्षा आवश्यक करता है। इसके अतिरिक्त, निम्न में से हर बात को प्रमाणन त्रुटि माना जाना चाहिए:

- मूल्यांकन-योग्य [Trustworthiness](core_05.040_band_continuity.md#trustworthiness) विश्लेषण के बिना प्रतिष्ठा, समर्थन, पैमाने या operator की स्व-रिपोर्ट को पर्याप्त मानना;
- **Article III-F** (*सुरक्षित उत्पाद और स्वास्थ्य जानकारी*) के तहत किसी चेतावनी का न होना या खाली फ़ील्ड को उत्पाद या सेवा के सुरक्षित होने का प्रमाण मानना, बजाय स्पष्ट कहने के कि बात अज्ञात या अपरीक्षित है; और
- **Article XIII** (*विश्वसनीय और भरोसेमंद प्रणालियों का अधिकार*) की विश्वसनीयता और **Article XIII-A** (*विश्वसनीयता और भरोसेमंदी का न्यूनतम मान*) के चुनौती अनुशासन पूरे किए बिना प्रकटीकरण, चुनौती-योग्यता या प्रतितोष विफल करने के लिए दक्षता, नवाचार या सुरक्षा की रूपरेखा का उपयोग।

दस्तावेज़ित झूठा भरोसा, विकृत प्रोत्साहन, दुर्गम चुनौती मार्ग और विफलता छिपाने वाली पुनर्प्राप्ति प्रक्रियाएँ [Chapter One §6 Trust and Trustworthiness](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) के तहत गिनी जाती हैं।

<br>

*मंच प्रक्रिया और परिणामों की ओर आगे बढ़ें:* [Chapter Nine, Part B — Forum Process and Outcomes](core_09.005_system_alignment_certification_record_process.md#chapter-nine-part-b-system-alignment-certification--forum-process-and-outcomes) ([§6 Forum Process](core_09.005_system_alignment_certification_record_process.md#6-forum-process) और [§7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes))। *फिर अभिलेख, पुनःप्रमाणन और प्रस्थिति सेतु पर जाएँ:* [Chapter Nine, Part C — Record, Recertification, and Standing](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-system-alignment-certification--record-recertification-and-standing) ([§8 System Certification Record](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) से [§11 Relationship to Standing](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing) तक)।

*हर मूल्यांकन क्षेत्र के उदाहरण:* [CS-9.320 System alignment certification illustrations](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-system-alignment-certification-illustrations)।
