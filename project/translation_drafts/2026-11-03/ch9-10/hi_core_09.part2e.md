### 4. जहाँ संदर्भित हो वहाँ के मूल्यांकन

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- पूर्ववर्ती: [§3](#3-whole-system-certification-evaluation) (*संपूर्ण-प्रणाली मूल्यांकन, जिसमें हमेशा लागू उपचरण भी है*); [§2](#2-system-class-evaluation) (*प्रणाली वर्ग मूल्यांकन*); [Chapter One §12 Systemic Evaluation Requirement](core_01.000_values_principles.md#12-systemic-evaluation-requirement) (1.000 §12)।
- अनुवर्ती:
  - [§4.1](#41-privacy-informational-joint-invocation) (*निजता केंद्र*);
  - [§4.2](#42-voluntary-discontinuation-major-self-modification-and-exit-rights) (*बाहर निकलने के अधिकार*);
  - [§4.3](#43-assembly-collective-organization-and-institutional-formation) (*सभा और असहमति*);
  - [भाग C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*अभिलेख सामग्री*)।
- साथ पढ़ें: [§5 Rights-Floor and Domain Evaluations](#5-rights-floor-and-domain-evaluations) (*trigger लागू होने पर लागू उपचरण*)।

</details>

<br>

*साधारण शब्दों में: तीन जाँचें तभी लागू होती हैं जब प्रणाली वास्तव में उन विषयों को छूती है — क्या निजी जानकारी उचित रूप से अलग रहती है, क्या संज्ञ प्राणी फँसे बिना बाहर जा सकते हैं, और क्या समूह अब भी संगठित होकर असहमति जता सकते हैं। प्रणाली इनमें से किसी को छूती है तो प्रमाणन को उसकी जाँच करनी होगी।*

यह खंड चरण II (Evaluate) का उपचरण **IIb** है। इसमें वे संपूर्ण-प्रणाली मूल्यांकन एक साथ रखे गए हैं जो केवल तब लागू होते हैं जब किसी उपखंड का अपना trigger पूरा हो।

<a id="41-privacy-informational-joint-invocation"></a>
#### 4.1 निजता (सूचनात्मक) का संयुक्त आह्वान

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- साथ पढ़ें: अध्याय पाँच के [**Def.C3** (*Privacy (Informational)* — सहकर्मी-स्तर cluster head)](core_05.040_band_continuity.md#defc3-privacy-informational--peer-level-cluster-head) और [Privacy (Informational)](core_05.040_band_continuity.md#privacy-informational), cluster-head का मूल स्थान, जो अर्थ के स्वामी हैं।

</details>

<br>

*साधारण शब्दों में: अध्याय छह निजता सुरक्षा कई अनुच्छेदों में बाँटता है — एक ही व्यवस्थित कोने में नहीं। यदि प्रमाणन समीक्षा एक से अधिक सुरक्षा को छूती है, समीक्षकों को वास्तव में लागू हर सुरक्षा जाँचनी होगी। सबसे आसान खाने पर निशान लगाकर काम पूरा कहना पर्याप्त नहीं।*

जहाँ प्रमाणन विषय अध्याय छह के एक से अधिक निजता केंद्रों को भौतिक रूप से प्रभावित करे, प्रमाणन को हर ऐसे केंद्र से निपटना होगा। केवल एक केंद्र के तहत विषय बंद करना पर्याप्त नहीं।

**लागू सिद्धांत।** ये तय करते हैं कि केंद्रों को साथ कैसे पढ़ा जाए:

- *संयुक्त मूल्यांकन।* विषय को एक केंद्र के रास्ते इस तरह नहीं भेजा जा सकता कि दूसरे से बच निकला जाए ([§15.1.1 Anti-Segmentation Principle](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle))।
- *पार-पठन से मानक ढीला नहीं।* हर cluster सदस्य का स्थानीय रूप से बताया मानक उसके अपने दायरे में लागू होता है और दूसरे सदस्य से कम कठोर मानक आयात करके ढीला नहीं किया जा सकता ([§15.1.1 Anti-Segmentation Principle](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle))।
- *प्रकार के न्यूनतम मान सुरक्षित।* यह कारक दायरे के डेटा पर लागू **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Information types and handling*) और [CS-6.310](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** (*Data classifications*) के किसी प्रकार का प्रबंधन सीमित नहीं करता। [CS-6.310 Part B §9](corpus_systems/cs_06.310_data_classifications.md#cs-6310-9-data-classifications) (*Data classifications*) के तहत हर लागू प्रकार की पहुँच-स्थिति और प्रबंधन कर्तव्य पूरी तरह लागू होते हैं, साथ में उस प्रकार द्वारा नामित [privacy homes](corpus_systems/cs_06.310_data_classifications.md#privacy-link) भी।
- *सबसे सुरक्षात्मक प्रकार लागू।* जहाँ एक से अधिक प्रकार एक ही डेटा पर लागू हों, [CS-6.305 Part A §2](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-2-determination-of-classification) (*वर्गीकरण का निर्धारण*) के तहत लागू सबसे सुरक्षात्मक प्रबंधन लागू होगा; एक प्रकार का प्रबंधन पूरा करने से दूसरे का दायित्व पूरा नहीं होता।

**Cluster के निजता केंद्र।** वितरित निजता सुरक्षा निम्न में फैली है, और हर एक उन डेटा प्रकारों के साथ है जिन पर वह लागू होता है:

- **Article VII-A** (*शरीर का स्वामित्व*) — स्वास्थ्य, जैवमितीय और आधार-संलग्न अभिलेखों के लिए [**Type I**](corpus_systems/cs_06.310_data_classifications.md#95-type-i-identity-and-attribution-data);
- **Article VII-B** (*मन का स्वामित्व*) — आंतरिक अवस्थाओं, उनके पुनर्निर्माण या अनुमान सहित, के लिए [**Type N**](corpus_systems/cs_06.310_data_classifications.md#96-type-n-neurocognitive-and-internal-data);
- **Article IX** (*रूप-समानता, अनुभवजन्य डेटा और प्रकाशन अधिकार*):
  - [Article IX-A](core_06.005_rights_part_b.md#article-ix-a-self-ownership-of-likeness-and-reputation) (*रूप-समानता और प्रतिष्ठा का स्वामित्व*) के तहत रूप-समानता और आवाज़ के लिए **Type I**;
  - [Article IX-B](core_06.005_rights_part_b.md#article-ix-b-experiential-and-derived-data-rights) (*अनुभवजन्य और व्युत्पन्न डेटा अधिकार*) के तहत अनुभवजन्य और अंतःक्रिया से निकले डेटा के लिए [**Type H**](corpus_systems/cs_06.310_data_classifications.md#94-type-h-historical-relational-transactional-and-participation-data); और
  - [Article IX-D](core_06.005_rights_part_b.md#article-ix-d-creative-work-training-data-use-and-anti-displacement) (*रचनात्मक कृति, प्रशिक्षण-डेटा उपयोग और विस्थापन-विरोध*) के तहत रचनाकार की कृतियों के लिए [**Type Y**](corpus_systems/cs_06.310_data_classifications.md#98-type-y-yours), जिसकी सुरक्षा [**Type W**](corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published), [**Type U**](corpus_systems/cs_06.310_data_classifications.md#911-type-u-use-licensed) और [**Type T**](corpus_systems/cs_06.310_data_classifications.md#912-type-t-transferred) में रचनाकार के [आरक्षित अधिकारों](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights) के साथ बनी रहती है;
- **Article X-A** (*अभिकरण और हेरफेर से स्वतंत्रता*) — आंतरिक अवस्थाओं, उनके पुनर्निर्माण या अनुमान सहित, के लिए [**Type N**](corpus_systems/cs_06.310_data_classifications.md#96-type-n-neurocognitive-and-internal-data); और
- **Article XIV-A** (*सुरक्षा, आसूचना और गुप्त शक्ति की सीमाएँ*) — प्रतिबंधित सुरक्षा और जाँच सामग्री के लिए [**Type S**](corpus_systems/cs_06.310_data_classifications.md#97-type-s-safety-security-and-restricted-investigation-data); प्रतिबंध समाप्त होने पर उसके **H**, **I** या **N** घटक उस प्रकार की सुरक्षा बनाए रखते हैं।

**प्रमाणन को क्या दिखाना होगा:**

- *सहभागिता सक्षम करना।* [Privacy (Informational)](core_05.040_band_continuity.md#privacy-informational) सार्थक [Participation](core_05.025_apex_participation_leg.md#participation-constitutional) को सक्षम करती है। प्रमाणन पुष्टि करेगा कि आवाज़, विचार-विमर्श, संगठन और चुनौती का समर्थन करने वाली निजता सुरक्षा खंड-विभाजन, पार-पठन या उजागर करने के दबाव से विफल नहीं होती।
- *खुले और लेखापरीक्षा-सुलभ प्रकार।* न्यूनतम सुरक्षा दोनों दिशाओं में लागू हैं:
  - **Type E**, **Type G** या **Type O** सामग्री के भीतर की व्यक्तिगत, संबंधपरक या आंतरिक-अवस्था सामग्री अपना **H**, **I** या **N** प्रबंधन बनाए रखती है;
  - कोई निजता केंद्र अपने आप नियमों द्वारा अनुमत सीमित रोक से आगे **Type O** या **Type E** डेटा रोकने का औचित्य नहीं देता; और
  - जब किसी की निजता की रक्षा और जनता को देय जानकारी प्रकाशित करना वास्तव में परस्पर टकराएँ, तो स्वतः कोई पक्ष नहीं जीतता: संघर्ष [CS-6.305 §7](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems) (*वर्ग A/B/C प्रणालियों के लिए Type O न्यूनतम मान*) के तहत खुले तौर पर और अभिलेख में तय होगा।
- *डेटा-प्रकार प्रमाण।* प्रमाणन को [§3.4 Data Types and Handling Evaluation](#34-data-types-and-handling-evaluation) के तहत सत्यापित [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record) को हर उस निजता केंद्र का प्रमाण मानना होगा जिस तक वह पहुँचता है: दायरे में आए प्रकार और उनका उद्देश्य, प्राप्तकर्ता, आधार तथा व्युत्पन्न डेटा। जिस प्रबंधन का अभिलेख में उल्लेख नहीं, उसके आधार पर निजता केंद्र बंद नहीं किया जा सकता।

<a id="42-voluntary-discontinuation-major-self-modification-and-exit-rights"></a>
#### 4.2 स्वैच्छिक बंद करना, बड़ा स्व-संशोधन और बाहर निकलने के अधिकार

जहाँ [Chapter One §7.4 Voluntary Discontinuation, Major Self-Modification, and Exit Rights](core_01.000_values_principles.md#74-voluntary-discontinuation-and-exit-rights) प्रमाणन विषय पर लागू हो, प्रमाणन-दावे के मान्य होने से पहले प्रमाणन को स्वैच्छिकता, सहमति, दबाव-विरोध, निर्भरता का दबाव, जानकारी और उत्क्रमणीयता की जाँच करनी होगी। केवल औपचारिक सहमति पर्याप्त नहीं।

<a id="43-assembly-collective-organization-and-institutional-formation"></a>
#### 4.3 सभा, सामूहिक संगठन और संस्थागत गठन

जहाँ [Chapter One §7.2 Assembly, Collective Organization, and Institutional Formation](core_01.000_values_principles.md#72-assembly-collective-organization-and-institutional-formation) प्रमाणन विषय पर लागू हो, प्रमाणन को [Anti-Segmentation Principle](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle) के तहत इस मुद्दे का संयुक्त मूल्यांकन करना होगा। यदि विषय को केवल एक रूपरेखा के रास्ते इस तरह भेजा जाए कि सभा या सामूहिक-संगठन सुरक्षा विफल हो, तो मूल्यांकन अधूरा है।

<a id="431-dissent-and-peaceful-protest"></a>
