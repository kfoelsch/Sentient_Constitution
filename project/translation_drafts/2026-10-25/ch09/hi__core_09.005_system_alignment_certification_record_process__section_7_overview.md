### 7. प्रमाणन परिणाम

<details>
<summary><strong><span style="color: #2563eb;">अनुसरण</span></strong></summary>

- पूर्ववर्ती:
  - [§6](#6-forum-process) (*फोरम प्रक्रिया और विश्वसनीय चुनौती*);
  - [भाग A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) से
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*मूल्यांकन में मिले गलत वर्गीकरण, असंरेखण और दोष*);
  - [दो संवैधानिक उद्देश्य](core_00.000_preamble.md#two-constitutional-aims);
  - [अध्याय तीन §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) और
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*परिभाषा की अखंडता और बचाव*);
  - [अध्याय तीन §2.1 बचाव के सामान्य तरीके](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*दायरे और सीमा से बचना*);
  - [प्रणाली चार्टर](core_05.040_band_continuity.md#system-charter) (*प्रणाली चार्टर और व्यवहार में असंगति तथा विलंबित समीक्षा*)।
- अनुवर्ती:
  - [भाग C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*परिणाम रिकॉर्ड में बताया जाता है*);
  - [भाग C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*परिणाम के साथ चुनौती मार्ग खुलता है*);
  - [भाग C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*पुनःप्रमाणन और पुनःखोलना*);
  - [भाग C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*जहाँ तथ्य प्रतिकूल निष्कर्षों का समर्थन करते हैं, वहाँ सत्यापित-इनपुट द्वार*);
  - [अध्याय तेरह](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*फोरम पर्यवेक्षण*);
  - [अध्याय दस](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000)।
- डेटा-प्रकार की नियत पुनर्मूल्यांकन के लिए **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*पुनर्वर्गीकरण और जीवन-चक्र शासन*) तथा प्रणाली-वर्ग के पुनर्मूल्यांकन ट्रिगर और SAC सत्यापन के लिए **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*पुनर्वर्गीकरण आवश्यकता*) के साथ पढ़ें।
- उपखंड:
  - [§7.1](#71-go-live-gate) (*संचालन-प्रारंभ द्वार*, जिसमें
  - [§7.1.1 पहले से चल रही प्रणालियाँ](#711-systems-already-operating) और
  - [§7.1.2 पायलट](#712-pilots));
  - [§7.2](#72-certification-defects-and-correction) (*प्रमाणन दोष और सुधार*);
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*सुधार तत्परता: सुधारने की इच्छा और क्षमता*, जिसमें
  - [§7.3.1 इच्छा](#731-willingness),
  - [§7.3.2 क्षमता](#732-capacity),
  - [§7.3.3 प्रमाण चरण](#733-proof-step),
  - [§7.3.4 निष्कर्ष](#734-findings), और
  - [§7.3.5 हर संचालक के लिए समान शर्तें](#735-same-terms-for-every-operator));
  - [§7.4](#74-denial-and-revocation) (*अस्वीकृति और निरसन*, जिसमें
  - [§7.4.1 अस्वीकृति और निरसन क्या हैं](#741-what-denial-and-revocation-are),
  - [§7.4.2 अस्वीकृति या निरसन कब आवश्यक है](#742-when-denial-or-revocation-is-required),
  - [§7.4.3 पहले सुरक्षा](#743-protection-first),
  - [§7.4.4 प्रक्रिया](#744-process),
  - [§7.4.5 प्रभाव](#745-effect), और
  - [§7.4.6 स्थायी रोक नहीं](#746-not-a-permanent-bar))।

</details>

<br>

*सरल शब्दों में: हर प्रमाणन समीक्षा एक घोषित परिणाम पर समाप्त होती है, जिसे साक्ष्य और रास्ते में उठी चिंताएँ समर्थन देती हैं। कोई प्रणाली तब तक चालू नहीं होती जब तक प्रमाणित न हो, प्रकाशित परिणाम प्रभावित संवेदनशील प्राणियों को चुनौती देने का व्यावहारिक अवसर न दे, और संचालन से पहले आवश्यक सुरक्षा जाँच न ली जाए।*

यह अनुभाग **चरण IV, निर्णय** है, [§6 फोरम प्रक्रिया](#6-forum-process) (**चरण III, समीक्षा**) के बाद। इसमें फोरमों द्वारा पहुँचे परिणाम आते हैं। [§7.1 संचालन-प्रारंभ द्वार](#71-go-live-gate) चालू करने की शर्त बताता है और [§7.2 प्रमाणन दोष और सुधार](#72-certification-defects-and-correction) दोष मिलने पर आगे की प्रक्रिया बताता है।

प्रमाणन निर्णय को [भाग C §8.1 न्यूनतम रिकॉर्ड सामग्री](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents) के अनुसार अपना परिणाम रिकॉर्ड में बताना होगा, साथ ही उस तक पहुँचने में उठी चिंताएँ भी। परिणाम इनमें से एक है:

- अस्थायी प्रमाणन;
- पूर्ण प्रमाणन;
- सशर्त प्रमाणन;
- स्थगित प्रमाणन;
- गैर-प्रमाणन;
- वापसी;
- समाप्ति; या
- शर्तों से मुक्ति।

जिस प्रणाली के पास न अस्थायी और न पूर्ण प्रमाणन है, वह **प्रमाणित नहीं** है। ऐसा तब होता है जब प्रमाणन:

- स्थगित हो;
- अस्वीकृत हो;
- वापस लिया गया हो; या
- समाप्त हो गया हो।

अस्थायी और पूर्ण प्रमाणन, प्रमाणन की दो **स्थितियाँ** हैं। [भाग C §9.2 अस्थायी और पूर्ण प्रमाणन](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) बताता है कि प्रणाली प्रत्येक स्थिति कैसे अर्जित करती है, बनाए रखती है और खोती है। सशर्त प्रमाणन की शर्तें किसी भी स्थिति के साथ जुड़ सकती हैं।

<a id="71-go-live-gate"></a>
