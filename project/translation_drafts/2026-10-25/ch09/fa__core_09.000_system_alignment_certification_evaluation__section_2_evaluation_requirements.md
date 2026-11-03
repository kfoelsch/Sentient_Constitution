<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (fa)

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

این بخش مشخص می‌کند گواهی‌سازی باید چه چیزهایی را راستی‌آزمایی کند:

- **الزام ارزیابی:**
  - آیا ردهٔ سامانهٔ تخصیص‌یافته، **اثر**، **وابستگی** و **خطر** مشاهده‌شده و به‌طور معقول قابل‌پیش‌بینی را طبق CS-9.305 (*سازوکار طبقه‌بندی سامانه*) و CS-9.310 (*طبقه‌بندی‌های اثر سامانه*) بازتاب می‌دهد، از جمله:
    - آثار تجمیعی؛
    - آثار تعاملی؛
    - آثار خصمانه؛
    - آثار آستانه‌ای؛
  - اینکه طبقه‌بندی بر پایهٔ رفتار و آثار واقعی سامانه تعیین می‌شود، نه بر پایهٔ:
    - قصد اعلام‌شده؛
    - دامنهٔ اسمی؛
    - صرفاً متن [منشور سامانه](core_05.040_band_continuity.md#system-charter)؛ یا
    - صرفاً توصیف خود سامانه؛
  - هرگاه تغییر مهمی بازبینی را ایجاب کند، ردهٔ سامانه طبق **[الزام بازطبقه‌بندی CS-9.305 §3.5](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** دوباره بررسی شده است؛ و
  - [سابقهٔ طبقه‌بندی سامانه](core_05.040_band_continuity.md#system-classification-record) **بالاترین ردهٔ سامانهٔ قابل‌اعمال** در شرایط کنونی را نشان می‌دهد.
- **تضمین و آزمون رگرسیون:**
  - تضمین متناسب با ردهٔ سامانه، استحکام زیرساخت و پوشش رگرسیون با ردهٔ تخصیص‌یافته مطابق است، طبق:
    - CS-9.305 (*سازوکار طبقه‌بندی سامانه*) و CS-9.310 (*طبقه‌بندی‌های اثر سامانه*)؛ و
    - CS-6.345 (*چرخهٔ عمر سامانه*)، همراه با این اصطلاحات عملیاتی مشترک هرجا که از نظر ماهوی کاربرد داشته باشند:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*تداوم: اصطلاحات تنزل تدریجی و یکپارچگی حالت‌های شکست*)؛
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*تداوم: اصطلاحات برگشت‌پذیری و مهار*)؛
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*تداوم: اصطلاحات استحکام در برابر خصومت و مقاومت در برابر سوءاستفاده*)؛
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*یکپارچگی: اصطلاحات محرمانگی مقید و تحقیق حفاظت‌شده*)، هرگاه رده یا کارکرد سامانه آن را از نظر ماهوی مرتبط سازد؛ و
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*یکپارچگی: اصطلاحات یکپارچگی مداخله و بازنویسی*)، هرگاه رده یا کارکرد سامانه آن را از نظر ماهوی مرتبط سازد؛ و
  - آزمون رگرسیون برای هر بازگواهی، مطابق الزام CS-6.345 (*چرخهٔ عمر سامانه*) انجام شده و نتایج آن طبق [§8.1 حداقل محتوای سابقه](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents) ثبت شده است.
