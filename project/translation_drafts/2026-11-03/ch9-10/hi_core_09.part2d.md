##### 3.4.2 निजता अनुशासन

प्रमाणन में डेटा प्रबंधन को निम्न निजता अनुशासन के अधीन रखना होगा:

- *प्रकार H, I, N, S और Y।* **Type H**, **Type I**, **Type N**, **Type S** और **Type Y** डेटा के लिए प्रमाणन सत्यापित करेगा कि उसका प्रबंधन **CS-6.305 (*Information types and handling*) और CS-6.310** (*Data classifications*) में हर प्रकार द्वारा नामित [privacy homes](corpus_systems/cs_06.310_data_classifications.md#privacy-link) का पालन करता है, जिसमें [Necessity](core_05.035_band_accountability.md#necessity), [Proportionality](core_05.035_band_accountability.md#proportionality), न्यूनतमकरण और सहमति या अन्य पर्याप्त प्राधिकार शामिल हैं।
- *संयुक्त आह्वान।* जहाँ एक से अधिक privacy locus लागू हों, वहाँ [§4.1 Privacy (Informational) Joint Invocation](#41-privacy-informational-joint-invocation) भी लागू होता है।
- *लेबल पर्याप्त नहीं।* सही type label अपने आप निजता अनुपालन सिद्ध नहीं करता।
- *प्रकार W, U और T।* **Type W**, **Type U** और **Type T** कृतियों के लिए प्रमाणन सत्यापित करेगा कि रचनाकार का नियंत्रण सम्मानित है, जिसमें शामिल हैं:
  - [CS-6.310 Part B §9.9](corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published) (*Type W: प्रकाशित कृतियाँ*) के तहत सार्वजनिक रूप से जारी कृति वापस लेना;
  - [CS-6.310 Part B §9.13](corpus_systems/cs_06.310_data_classifications.md#913-commercial-grants) (*वाणिज्यिक अनुदान*) के तहत दर्ज हर अनुदान की सीमाएँ; और
  - रचनाकार के [आरक्षित अधिकार](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights)।
- *निहित सहमति नहीं।* कोई अनुदान केवल उन उपयोगों पर लागू होता है जिन्हें वह अपने बताए दायरे, अवधि, क्षेत्र और माध्यम के भीतर नामित करता है। जो वह नामित नहीं करता, वह रचनाकार के पास रहता है। प्रमाणन किसी default setting, bundled शर्त, मौन या व्यापक अनुदान को ऐसे उपयोग की सहमति नहीं मानेगा जिसे अनुदान नामित नहीं करता। उदाहरणार्थ, किसी कृति को प्रकाशित या बेचने का सामान्य लाइसेंस उसे training data के रूप में उपयोग करने की सहमति नहीं है; इसके लिए रचनाकार की अपनी विशिष्ट सहमति चाहिए (देखें [आरक्षित अधिकार](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights))।

<a id="343-protective-storage-and-key-custody"></a>
##### 3.4.3 सुरक्षात्मक भंडारण और key custody

डिफ़ॉल्ट रूप से प्रतिबंधित और पहुँच-अयोग्य bands के डेटा के लिए, प्रमाणन सत्यापित करेगा कि प्रणाली [CS-6.305 Part A §5.0 Access-posture bands](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands) में दिए सुरक्षात्मक भंडारण और key custody के न्यूनतम मान पूरे करती है। अभिलेख में दिखना चाहिए:

- प्रतिबंधित डेटा और उसकी keys वास्तव में कहाँ रखी हैं, backups, caches, logs और swap सहित;
- plaintext केवल उन्हीं प्रक्रियाओं तक सीमित है जिन्हें इसकी ज़रूरत है; और
- audit, export और वैध override मार्ग अब भी काम करते हैं।

इस प्रमाण के बिना encryption का दावा इस आवश्यकता को पूरा नहीं करता।

<a id="344-scheduled-data-type-re-evaluation"></a>
<a id="344-periodic-data-type-re-evaluation"></a>
##### 3.4.4 नियत डेटा-प्रकार पुनर्मूल्यांकन

हर बार जब भौतिक प्रभाव वाली प्रणाली प्रमाणित या पुनःप्रमाणित हो, समीक्षा में जाँचना होगा कि उसके महत्त्वपूर्ण dataset का:

- **पुनर्मूल्यांकन** **[CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*पुनर्वर्गीकरण और जीवनचक्र शासन*) तथा **CJS-5.130 §18** (*डेटा-धारण और जीवनचक्र-अखंडता शर्तें*) के तहत उचित वर्गीकरण के लिए हुआ; और
- जहाँ उस समीक्षा में आवश्यक हुआ वहाँ **पुनर्वर्गीकरण** किया गया।

CS-6.305 (*Information types and handling*) और CS-6.310 (*Data classifications*) के तहत घटना-आधारित retyping इस नियत प्रमाणन जाँच का स्थान नहीं लेता।

<a id="345-system-class-scaled-infrastructure-assurance"></a>
##### 3.4.5 प्रणाली-वर्ग-आधारित अवसंरचना आश्वासन

[§2.2 How system class scales every evaluation](#22-how-system-class-scales-every-evaluation), CS-9.305 (*System classification machinery*) और CS-9.310 (*System impact classifications*) के तहत उच्च वर्ग की प्रणालियों के लिए आनुपातिक रूप से मजबूत प्रमाण आवश्यक हैं कि प्रबंधन, भंडारण, प्रसंस्करण, संचार, backup, recovery और monitoring अवसंरचना दबाव में निम्न की रक्षा कर सकती है:

- वर्गीकरण अखंडता;
- आरोपण; और
- चुनौती-योग्यता।

जहाँ CS-6.305 (*Information types and handling*) तथा CS-6.310 (*Data classifications*) के लोक-हित दृश्यता default लागू हों, प्रमाणन सत्यापित करेगा कि प्रतिबंध:

- संकीर्ण दायरे के हैं;
- दस्तावेज़ित और लेखापरीक्षण-योग्य हैं; और
- उनके साथ यथोचित रूप से संभव सबसे मजबूत सार्वजनिक विकल्प भी दिया गया है (उदाहरण के लिए सारांश, समेकित जानकारी, पहचान-रहित संस्करण, विलंबित प्रकाशन या योग्य लेखापरीक्षा पहुँच), ताकि रोकी गई बात को समझाया जाए, केवल छिपाया नहीं।

<a id="346-infrastructure-robustness-for-data"></a>
##### 3.4.6 डेटा के लिए अवसंरचना मजबूती

प्रमाणन को मूल्यांकन करना होगा कि डेटा-प्रबंधन अवसंरचना संबंधित डेटा प्रकारों और प्रणाली वर्ग के लिए उपयुक्त है या नहीं। इस अवसंरचना में शामिल हैं:

- स्थायित्व परतें और pipelines;
- पहुँच नियंत्रण;
- encryption या पृथक्करण सीमाएँ;
- backup और पुनर्स्थापन मार्ग; और
- operator या vendor delegation शृंखलाएँ।

जीवनचक्र अखंडता, विरोधी मजबूती, पोर्टेबिलिटी या पुनर्प्राप्ति-क्षमता की भौतिक कमी अभिलेख में बताई जानी चाहिए और प्रमाणन परिणाम, प्रमाणन-शर्तों या निर्भरता सीमाओं में परिलक्षित होनी चाहिए।

<a id="347-defects-and-misalignment"></a>
##### 3.4.7 त्रुटियाँ और संरेखणहीनता

निम्न में से हर बात को प्रमाणन त्रुटि माना जाएगा:

- डेटा का गलत वर्गीकरण;
- बचने के लिए पुनर्गठन;
- असुरक्षित cross-domain linking;
- ऐसा प्रबंधन जिसमें सही type label होने पर भी उस प्रकार की आवश्यक निजता सुरक्षा टूटती हो;
- किसने डेटा तक पहुँच बनाई, संसाधित किया या बदला इसका कोई अभिलेख न होना, जिससे महत्त्वपूर्ण हानि की जाँच संभव न हो;
- **नियत डेटा-प्रकार पुनर्मूल्यांकन में देरी या उसे छोड़ना**;
- प्रतिबंधित डेटा को भंडारण में या अधिकृत प्रसंस्करण सीमा के बाहर plaintext के रूप में रखना, या ऐसी प्रक्रियाओं को keys तक पहुँच देना जिन्हें उनकी ज़रूरत नहीं; और
- ऐसी अवसंरचनात्मक भंगुरता जो पूर्वानुमेय रूप से CS-6.305 (*Information types and handling*) और CS-6.310 (*Data classifications*) की सुरक्षा विफल करे।

इनके परिणाम [§7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) में तय हैं।

<a id="4-evaluations-where-implicated"></a>
