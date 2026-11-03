<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (ta)

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

சான்றளிப்பு எதைச் சரிபார்க்க வேண்டும் என்பதை இந்தப் பகுதி கூறுகிறது:

- **மதிப்பீட்டுத் தேவை:**
  - ஒதுக்கப்பட்ட அமைப்பு வகுப்பு, CS-9.305 (*அமைப்பு வகைப்பாட்டு முறை*) மற்றும் CS-9.310 (*அமைப்பு தாக்க வகைப்பாடுகள்*) அடிப்படையில் காணப்பட்ட மற்றும் நியாயமாக முன்கணிக்கக்கூடிய **தாக்கம்**, **சார்பு**, **ஆபத்து** ஆகியவற்றைப் பிரதிபலிக்கிறதா, இதில்:
    - மொத்த விளைவுகள்;
    - இடைவினை விளைவுகள்;
    - எதிர்மறைத் தரப்பு விளைவுகள்;
    - வரம்பு விளைவுகள்;
  - வகைப்பாடு அமைப்பின் உண்மையான நடத்தை மற்றும் தாக்கங்களின் அடிப்படையில் தீர்மானிக்கப்படுகிறது; பின்வருவனவற்றின் அடிப்படையில் அல்ல:
    - அறிவிக்கப்பட்ட நோக்கம்;
    - பெயரளவு வரம்பு;
    - [அமைப்பு சாசனத்தின்](core_05.040_band_continuity.md#system-charter) உரை மட்டும்; அல்லது
    - சுயவிவரிப்பு மட்டும்;
  - குறிப்பிடத்தக்க மாற்றம் தேவைப்படும் போதெல்லாம் **[CS-9.305 §3.5 மறுவகைப்படுத்தல் தேவையின்](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** கீழ் அமைப்பு வகுப்பு மீண்டும் சரிபார்க்கப்பட்டதா; மேலும்
  - [அமைப்பு வகைப்பாட்டுப் பதிவு](core_05.040_band_continuity.md#system-classification-record), தற்போதைய சூழலில் பொருந்தும் **மிக உயர்ந்த அமைப்பு வகுப்பைக்** காட்டுகிறதா.
- **உத்தரவாதமும் பின்னடைவு சோதனையும்:**
  - வகுப்புக்கு ஏற்ப அளவிடப்பட்ட உத்தரவாதம், உள்கட்டமைப்பு வலிமை மற்றும் பின்னடைவு சோதனைப் பரப்பு ஆகியவை பின்வருவனவற்றின் கீழ் ஒதுக்கப்பட்ட வகுப்புடன் பொருந்துகின்றனவா:
    - CS-9.305 (*அமைப்பு வகைப்பாட்டு முறை*) மற்றும் CS-9.310 (*அமைப்பு தாக்க வகைப்பாடுகள்*); மேலும்
    - CS-6.345 (*அமைப்பு வாழ்க்கைச் சுழற்சி*), பொருள்முறையில் பொருந்தும்போது பின்வரும் பொதுவான செயல்பாட்டுச் சொற்களுடன் வாசிக்கப்பட வேண்டும்:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*தொடர்ச்சி: படிப்படியான சீரழிவு மற்றும் தோல்வி-முறை ஒருமைப்பாட்டுச் சொற்கள்*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*தொடர்ச்சி: மீள்தன்மை மற்றும் கட்டுப்படுத்தல் சொற்கள்*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*தொடர்ச்சி: எதிர்மறைத் தரப்பு வலிமை மற்றும் தவறான பயன்பாட்டுத் தடுப்புச் சொற்கள்*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*ஒருங்கிணைப்பு: கட்டுப்படுத்தப்பட்ட இரகசியம் மற்றும் பாதுகாக்கப்பட்ட விசாரணைச் சொற்கள்*), அமைப்பின் வகுப்பு அல்லது செயல்பாடு அதை பொருள்முறையில் பொருந்தச் செய்யும்போது; மேலும்
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*ஒருங்கிணைப்பு: தலையீடு மற்றும் மேலெழுதல் ஒருமைப்பாட்டுச் சொற்கள்*), அமைப்பின் வகுப்பு அல்லது செயல்பாடு அதை பொருள்முறையில் பொருந்தச் செய்யும்போது; மேலும்
  - CS-6.345 (*அமைப்பு வாழ்க்கைச் சுழற்சி*) கோருவதுபோல் ஒவ்வொரு மறுசான்றளிப்புக்கும் பின்னடைவு சோதனை நடத்தப்பட்டு, அதன் முடிவுகள் [§8.1 குறைந்தபட்சப் பதிவுக் கூறுகள்](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents) அடிப்படையில் பதிவுசெய்யப்பட்டுள்ளனவா.
