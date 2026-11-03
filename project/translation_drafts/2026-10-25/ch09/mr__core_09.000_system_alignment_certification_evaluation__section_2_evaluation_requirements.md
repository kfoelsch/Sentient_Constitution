<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (mr)

## English source (lines 311–335)

This section states what certification must verify:

- **Evaluation requirement:**
  - whether the assigned system class reflects observed and reasonably foreseeable **impact**, **dependency**, and **risk** under CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*), including:
    - aggregate effects;
    - interaction effects;
    - adversarial effects;
    - threshold effects;
  - that classification is determined by actual system behavior and impacts, not from:
    - declared intent;
    - nominal scope;
    - [System Charter](core_05.040_band_continuity.md#system-charter) text alone; or
    - self-description alone;
  - that the system's class was re-checked under the **[CS-9.305 §3.5 reclassification requirement](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** whenever a significant change called for it; and
  - that the [System Classification Record](core_05.040_band_continuity.md#system-classification-record) shows the **highest system class that applies** under current conditions.
- **Assurance and regression testing:**
  - that system-class-scaled assurance, infrastructure robustness, and regression coverage match the assigned system class under:
    - CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*); and
    - CS-6.345 (*System lifecycle*), read with these shared operational terms where materially applicable:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*Continuity: graceful degradation and failure-mode integrity terms*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*Continuity: reversibility and containment terms*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*Continuity: adversarial robustness and abuse-resistance terms*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*Integrative: constrained-secrecy and protected-investigation terms*), where the system's class or function makes it materially applicable; and
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*Integrative: intervention and override integrity terms*), where the system's class or function makes it materially applicable; and
  - that regression testing was run for each recertification, as CS-6.345 (*System lifecycle*) requires, with its results on the record under [§8.1 Minimum record contents](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents).

## Translation draft

या विभागात प्रमाणनाने काय पडताळले पाहिजे ते सांगितले आहे:

- **मूल्यांकनाची आवश्यकता:**
  - नियुक्त प्रणाली-वर्ग CS-9.305 (*प्रणाली वर्गीकरण यंत्रणा*) आणि CS-9.310 (*प्रणाली-प्रभाव वर्गीकरण*) अंतर्गत निरीक्षित आणि वाजवीपणे पूर्वानुमेय **प्रभाव**, **अवलंबित्व**, आणि **जोखीम** दर्शवतो का, यामध्ये:
    - एकत्रित परिणाम;
    - परस्परसंवादाचे परिणाम;
    - प्रतिकूल परिणाम;
    - उंबरठा-परिणाम;
  - वर्गीकरण प्रत्यक्ष प्रणाली-वर्तन आणि परिणामांवर ठरते, खालील बाबींवर नाही:
    - घोषित हेतू;
    - नाममात्र व्याप्ती;
    - केवळ [प्रणाली सनदेचा](core_05.040_band_continuity.md#system-charter) मजकूर; किंवा
    - केवळ स्व-वर्णन;
  - लक्षणीय बदलामुळे गरज निर्माण झाल्यास **[CS-9.305 §3.5 पुनर्वर्गीकरण आवश्यकतेनुसार](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** प्रणाली-वर्गाची पुन्हा तपासणी केली गेली; आणि
  - [प्रणाली वर्गीकरण नोंद](core_05.040_band_continuity.md#system-classification-record) सध्याच्या परिस्थितीत लागू होणारा **सर्वोच्च प्रणाली-वर्ग** दाखवते.
- **आश्वासन आणि प्रतिगमन चाचणी:**
  - प्रणाली-वर्गानुसार प्रमाणबद्ध आश्वासन, पायाभूत सुविधांची मजबुती आणि प्रतिगमन व्याप्ती नियुक्त प्रणाली-वर्गाशी खालीलप्रमाणे जुळते:
    - CS-9.305 (*प्रणाली वर्गीकरण यंत्रणा*) आणि CS-9.310 (*प्रणाली-प्रभाव वर्गीकरण*); आणि
    - CS-6.345 (*प्रणाली जीवनचक्र*), तसेच महत्त्वपूर्णरीत्या लागू असल्यास या सामायिक कार्यकारी संज्ञा:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*सातत्य: क्रमिक अवनती आणि अपयश-प्रकार अखंडतेच्या संज्ञा*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*सातत्य: उलटक्षमता आणि नियंत्रणाच्या संज्ञा*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*सातत्य: प्रतिकूल-परिस्थितीतील मजबुती आणि गैरवापर-प्रतिरोधाच्या संज्ञा*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*एकात्मता: मर्यादित गोपनीयता आणि संरक्षित तपासाच्या संज्ञा*), प्रणालीचा वर्ग किंवा कार्यामुळे महत्त्वपूर्णरीत्या लागू असल्यास; आणि
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*एकात्मता: हस्तक्षेप आणि अध्यारोपण अखंडतेच्या संज्ञा*), प्रणालीचा वर्ग किंवा कार्यामुळे महत्त्वपूर्णरीत्या लागू असल्यास; आणि
  - CS-6.345 (*प्रणाली जीवनचक्र*) नुसार प्रत्येक पुनःप्रमाणनासाठी प्रतिगमन चाचणी केली गेली आणि तिचे निष्कर्ष [§8.1 किमान नोंद-सामग्री](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents) अंतर्गत नोंदवले गेले.
