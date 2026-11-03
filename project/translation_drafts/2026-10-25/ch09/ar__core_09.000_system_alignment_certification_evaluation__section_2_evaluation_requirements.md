<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (ar)

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

يبيّن هذا القسم ما يجب أن يتحقق منه التصديق:

- **متطلب التقييم:**
  - ما إذا كانت فئة النظام المعيّنة تعكس الأثر والتبعية والمخاطر الملحوظة والمتوقعة على نحو معقول بموجب CS-9.305 (*آلية تصنيف الأنظمة*) وCS-9.310 (*تصنيفات أثر النظام*)، بما في ذلك:
    - الآثار الإجمالية؛
    - آثار التفاعل؛
    - الآثار العدائية؛
    - آثار العتبات؛
  - أن التصنيف يتحدد بحسب السلوك والآثار الفعلية للنظام، لا بحسب:
    - النية المعلنة؛
    - النطاق الاسمي؛
    - نص [ميثاق النظام](core_05.040_band_continuity.md#system-charter) وحده؛ أو
    - الوصف الذاتي وحده؛
  - أن فئة النظام أعيد التحقق منها بموجب **[متطلب إعادة التصنيف في CS-9.305 §3.5](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** كلما استدعى تغيير مهم ذلك؛ و
  - أن [سجل تصنيف النظام](core_05.040_band_continuity.md#system-classification-record) يبيّن **أعلى فئة نظام تنطبق** في الظروف الراهنة.
- **الضمان واختبار الانحدار:**
  - أن الضمان المتناسب مع فئة النظام، ومتانة البنية التحتية، وتغطية الانحدار تتوافق مع فئة النظام المعيّنة بموجب:
    - CS-9.305 (*آلية تصنيف الأنظمة*) وCS-9.310 (*تصنيفات أثر النظام*)؛ و
    - CS-6.345 (*دورة حياة النظام*)، بالاقتران مع المصطلحات التشغيلية المشتركة التالية حيثما كانت ذات صلة جوهرية:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*الاستمرارية: مصطلحات التدهور السلس وسلامة أنماط الإخفاق*)؛
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*الاستمرارية: مصطلحات قابلية العكس والاحتواء*)؛
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*الاستمرارية: مصطلحات المتانة في مواجهة الخصومة ومقاومة إساءة الاستخدام*)؛
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*التكامل: مصطلحات السرية المقيّدة والتحقيق المحمي*)، عندما تجعل فئة النظام أو وظيفته ذلك ذا صلة جوهرية؛ و
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*التكامل: مصطلحات سلامة التدخل والتجاوز*)، عندما تجعل فئة النظام أو وظيفته ذلك ذا صلة جوهرية؛ و
  - أن اختبار الانحدار أُجري عند كل إعادة تصديق، وفق ما تقتضيه CS-6.345 (*دورة حياة النظام*)، وأُدرجت نتائجه في السجل بموجب [§8.1 الحد الأدنى لمحتويات السجل](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents).
