<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (te)

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

ఈ విభాగం ధృవీకరణ తప్పనిసరిగా ఏమి నిర్ధారించాలో చెబుతుంది:

- **మూల్యాంకన అవసరం:**
  - కేటాయించిన వ్యవస్థ తరగతి, CS-9.305 (*వ్యవస్థ వర్గీకరణ యంత్రాంగం*) మరియు CS-9.310 (*వ్యవస్థ ప్రభావ వర్గీకరణలు*) ప్రకారం గమనించిన మరియు సహేతుకంగా ముందుగా ఊహించగల **ప్రభావం**, **ఆధారపడటం**, **ప్రమాదం**లను ప్రతిబింబిస్తుందా, వీటిలో:
    - సమగ్ర ప్రభావాలు;
    - పరస్పర చర్య ప్రభావాలు;
    - విరోధాత్మక ప్రభావాలు;
    - పరిమితి ప్రభావాలు;
  - వర్గీకరణ వాస్తవ వ్యవస్థ ప్రవర్తన, ప్రభావాల ఆధారంగా నిర్ణయించబడుతుంది; కింది వాటి ఆధారంగా కాదు:
    - ప్రకటించిన ఉద్దేశం;
    - నామమాత్ర పరిధి;
    - [వ్యవస్థ చార్టర్](core_05.040_band_continuity.md#system-charter) పాఠ్యం మాత్రమే; లేదా
    - స్వీయ వివరణ మాత్రమే;
  - గణనీయమైన మార్పు అవసరమైనప్పుడల్లా **[CS-9.305 §3.5 పునర్వర్గీకరణ అవసరం](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** ప్రకారం వ్యవస్థ తరగతిని మళ్లీ తనిఖీ చేశారా; మరియు
  - [వ్యవస్థ వర్గీకరణ రికార్డు](core_05.040_band_continuity.md#system-classification-record) ప్రస్తుత పరిస్థితులలో వర్తించే **అత్యున్నత వ్యవస్థ తరగతిని** చూపుతుందా.
- **హామీ మరియు రిగ్రెషన్ పరీక్ష:**
  - తరగతికి అనుగుణంగా నిర్ణయించిన హామీ, మౌలిక సదుపాయాల దృఢత్వం, రిగ్రెషన్ పరీక్షల పరిధి కేటాయించిన వ్యవస్థ తరగతికి అనుగుణంగా ఉన్నాయి, వీటి ప్రకారం:
    - CS-9.305 (*వ్యవస్థ వర్గీకరణ యంత్రాంగం*) మరియు CS-9.310 (*వ్యవస్థ ప్రభావ వర్గీకరణలు*); మరియు
    - CS-6.345 (*వ్యవస్థ జీవితచక్రం*), గణనీయంగా వర్తించే చోట ఈ ఉమ్మడి కార్యాచరణ పదాలతో కలిపి చదవాలి:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*నిరంతరత: క్రమంగా క్షీణత మరియు వైఫల్య-రీతి సమగ్రత పదాలు*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*నిరంతరత: తిరోగమనసాధ్యత మరియు నియంత్రణ పదాలు*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*నిరంతరత: విరోధాత్మక దృఢత్వం మరియు దుర్వినియోగ నిరోధకత పదాలు*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*సమగ్రత: పరిమిత రహస్యత్వం మరియు రక్షిత దర్యాప్తు పదాలు*), వ్యవస్థ తరగతి లేదా విధి దానిని గణనీయంగా వర్తింపజేసినప్పుడు; మరియు
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*సమగ్రత: జోక్యం మరియు అధిగమింపు సమగ్రత పదాలు*), వ్యవస్థ తరగతి లేదా విధి దానిని గణనీయంగా వర్తింపజేసినప్పుడు; మరియు
  - CS-6.345 (*వ్యవస్థ జీవితచక్రం*) కోరినట్లుగా ప్రతి పునఃధృవీకరణలో రిగ్రెషన్ పరీక్ష నిర్వహించి, దాని ఫలితాలను [§8.1 కనిష్ఠ రికార్డు విషయాలు](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents) ప్రకారం రికార్డులో చేర్చారా.
