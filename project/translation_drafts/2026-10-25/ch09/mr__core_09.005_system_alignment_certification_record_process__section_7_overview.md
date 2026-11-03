### 7. प्रमाणन निकाल

<details>
<summary><strong><span style="color: #2563eb;">संदर्भ मागोवा</span></strong></summary>

- ऊर्ध्वसंदर्भ:
  - [§6](#6-forum-process) (*मंच प्रक्रिया आणि विश्वासार्ह आक्षेप*);
  - [भाग A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) पासून
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*मूल्यमापनात आढळलेले चुकीचे वर्गीकरण, विसंरेखन, आणि दोष*);
  - [दोन संवैधानिक उद्दिष्टे](core_00.000_preamble.md#two-constitutional-aims);
  - [अध्याय तीन §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) आणि
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*व्याख्या सचोटी आणि चुकवणे*);
  - [अध्याय तीन §2.1 सामान्य चुकवण्याचे नमुने](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*व्याप्ती आणि सीमा चुकवणे*);
  - [प्रणाली सनद](core_05.040_band_continuity.md#system-charter) (*प्रणाली सनद–वर्तन विसंगती आणि थकीत समीक्षा*).
- अधःसंदर्भ:
  - [भाग C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*निकाल अभिलेखात नमूद होतो*);
  - [भाग C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*निकालासोबत आक्षेप मार्ग उघडतो*);
  - [भाग C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*पुनःप्रमाणन आणि पुन्हा उघडणे*);
  - [भाग C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*प्रतिकूल निष्कर्षांना तथ्यांचा आधार असेल तेव्हाचे पडताळलेले-इनपुट प्रवेशद्वार*);
  - [अध्याय तेरा](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*मंच देखरेख*);
  - [अध्याय दहा](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- यासोबत वाचा: नियोजित माहिती-प्रकार पुनर्मूल्यांकनासाठी **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*पुनर्वर्गीकरण आणि जीवनचक्र प्रशासन*), आणि प्रणाली-वर्ग पुनर्मूल्यांकन ट्रिगर्स व SAC पडताळणीसाठी **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*पुनर्वर्गीकरण आवश्यकता*).
- उपविभाग:
  - [§7.1](#71-go-live-gate) (*गो-लाइव्ह प्रवेशद्वार*, यासह
  - [§7.1.1 आधीपासून कार्यरत प्रणाली](#711-systems-already-operating) आणि
  - [§7.1.2 पायलट](#712-pilots));
  - [§7.2](#72-certification-defects-and-correction) (*प्रमाणन दोष आणि दुरुस्ती*);
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*निवारण सज्जता: दुरुस्तीची इच्छा आणि क्षमता*, यासह
  - [§7.3.1 इच्छा](#731-willingness),
  - [§7.3.2 क्षमता](#732-capacity),
  - [§7.3.3 पुरावा पायरी](#733-proof-step),
  - [§7.3.4 निष्कर्ष](#734-findings), आणि
  - [§7.3.5 प्रत्येक ऑपरेटरसाठी समान अटी](#735-same-terms-for-every-operator));
  - [§7.4](#74-denial-and-revocation) (*नकार आणि रद्द करणे*, यासह
  - [§7.4.1 नकार आणि रद्द करणे म्हणजे काय](#741-what-denial-and-revocation-are),
  - [§7.4.2 नकार किंवा रद्द करणे कधी आवश्यक आहे](#742-when-denial-or-revocation-is-required),
  - [§7.4.3 संरक्षण प्रथम](#743-protection-first),
  - [§7.4.4 प्रक्रिया](#744-process),
  - [§7.4.5 परिणाम](#745-effect), आणि
  - [§7.4.6 कायमची मनाई नाही](#746-not-a-permanent-bar)).

</details>

<br>

*सोप्या भाषेत: प्रत्येक प्रमाणन समीक्षा स्पष्ट केलेल्या निकालाने संपते; त्या निकालाला पुरावे आणि प्रक्रियेदरम्यान मांडलेल्या चिंतांचा आधार असतो. प्रमाणन होईपर्यंत, प्रकाशित निकालाने प्रभावित संज्ञांना आव्हान देण्याची व्यवहार्य संधी मिळेपर्यंत, आणि गो-लाइव्हपूर्वी आवश्यक संरक्षणे तपासली जाईपर्यंत कोणतीही प्रणाली कार्यरत होत नाही.*

हा विभाग [§6 मंच प्रक्रिया](#6-forum-process) (**टप्पा III, समीक्षा**) नंतरचा **टप्पा IV, निर्णय** आहे. मंच ज्या निकालापर्यंत पोहोचतात, तो यात समाविष्ट आहे. [§7.1 गो-लाइव्ह प्रवेशद्वार](#71-go-live-gate) गो-लाइव्ह प्रवेशद्वार सांगतो, आणि [§7.2 प्रमाणन दोष आणि दुरुस्ती](#72-certification-defects-and-correction) दोष आढळल्यावर काय होते ते सांगतो.

प्रमाणन निर्णयात निकाल [भाग C §8.1 अभिलेखाची किमान सामग्री](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents) नुसार अभिलेखात नमूद केला पाहिजे; तो गाठताना मांडलेल्या चिंताही त्यासोबत नोंदवल्या पाहिजेत. निकाल पुढीलपैकी एक असतो:

- तात्पुरते प्रमाणन;
- पूर्ण प्रमाणन;
- सशर्त प्रमाणन;
- स्थगित प्रमाणन;
- अप्रमाणन;
- माघार;
- कालबाह्यता; किंवा
- अटीतून मुक्तता.

तात्पुरते किंवा पूर्ण प्रमाणन नसलेली प्रणाली **अप्रमाणित** असते. प्रमाणन पुढीलपैकी काही असेल, तेव्हा ही स्थिती लागू होते:

- स्थगित;
- नाकारलेले;
- मागे घेतलेले; किंवा
- कालबाह्य.

तात्पुरते आणि पूर्ण प्रमाणन हे प्रमाणनाचे दोन **दर्जे** आहेत. [भाग C §9.2 तात्पुरते आणि पूर्ण प्रमाणन](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) प्रणाली प्रत्येक दर्जा कसा मिळवते, टिकवते, आणि गमावते हे स्पष्ट करतो. सशर्त प्रमाणनातील अटी यांपैकी कोणत्याही दर्जाला जोडल्या जाऊ शकतात.

<a id="71-go-live-gate"></a>

