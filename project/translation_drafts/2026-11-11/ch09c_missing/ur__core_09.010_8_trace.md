<!-- AI-assisted translation draft; unreviewed. Current-source Chapter Nine Part C §8 Trace; source SHA-256 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Baseline commit 247e2180509e5e029c1106878cf225067339e010; baseline SHA-256 faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Draft only; do not synchronize into translations/. -->

<details>
<summary><strong>سراغ رسانی</strong></summary>

- بالادست:
  - [حصہ B §6](core_09.005_system_alignment_certification_record_process.md#6-forum-process) (*فورم کے اجزا کے نتائج سسٹم سرٹیفکیشن ریکارڈ میں یکجا ہوتے ہیں*);
  - [حصہ B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (*نتیجہ اور اس تک پہنچتے ہوئے اٹھائے گئے خدشات*);
  - [حصہ A §1](core_09.000_system_alignment_certification_evaluation.md#1-purpose-and-role) (9.000 §1) (*سرٹیفکیشن کا مقصد اور طریقۂ کار کا جائزہ*);
  - [حصہ A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (*سسٹم کلاس کی جانچ*) (9.000 §2) تک
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*سسٹم سرٹیفکیشن ریکارڈ میں منعکس جائزے کے نتائج*);
  - [باب دو تا چار](core_04.000_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) (*تعریف، بوجھ، سراغ رسانی اور تصدیق کی بنیاد*);
  - [سسٹم سرٹیفکیشن ریکارڈ](core_05.040_band_continuity.md#system-certification-record) (*باب پانچ میں اس کا مفہوم*);
  - [مادی طور پر پابند عمل کا ریکارڈ](core_05.035_band_accountability.md#materially-binding-act-record);
  - [ریکارڈ کی سالمیت](core_05.035_band_accountability.md#record-integrity) (*سسٹم سرٹیفکیشن ریکارڈ پر لاگو ہونے والا قابلِ اعتماد ہونے کا اصول*);
  - [باب آٹھ §8 عمل کے ریکارڈ اور قابلِ انتساب حوالگیاں](core_08.000_functional_independence_separation_of_duties.md#8-act-records-and-attributable-handoffs) (8.000 §8); سچائی اور علمی سالمیت کو آئینی پیمائش بنانے والا نگرانی پیمائش خاندان;
  - [**Def.O1** *آرٹیکل XVI: آڈٹ، شفافیت اور آزاد تصدیق*](core_05.050_band_oversight.md#defo1-transparency-auditability-and-verification).
- زیریں: [§9](#9-recertification-and-reopening) (*دوبارہ تصدیق اور دوبارہ کھولنا*); [§11.3](#113-verified-input-gate) (*تصدیق شدہ اِن پٹ گیٹ*); [باب پندرہ §2.3](core_15.000_forum.md#23-forum-case-records-standing-records-and-contests) (*فورم کے مقدماتی ریکارڈ اور standing ریکارڈ کے تنازعات*) (15.000 §2.3).
- ساتھ پڑھیں:
  - [آرٹیکل XVI: آڈٹ، شفافیت اور آزاد تصدیق](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [شواہد کا تحفظ](core_05.050_band_oversight.md#evidence-preservation);
  - **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*معلومات کی اقسام اور برتاؤ*) اور [CS-6.310 — ڈیٹا کی درجہ بندیاں](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**;
  - **[CS-9.305](corpus_systems/cs_09.305_system_classification_machinery.md#cs-9305-part-a-system-classification-machinery) (*سسٹم درجہ بندی کا طریقۂ کار*) اور [CS-9.310 — سسٹم اثرات کی درجہ بندیاں](corpus_systems/cs_09.310_system_impact_classifications.md#cs-9310-part-b-system-impact-classifications)**;
  - **CS-6.345** (*سسٹم کا دورِ حیات*);
  - **CJS-5.110 §4** (*شفافیت کی سطحیں اور آڈٹ رسائی کی شرائط*).
- ذیلی حصے:
  - [§8.1](#81-minimum-record-contents) (*ریکارڈ کا کم از کم مواد*), کے ساتھ
  - [§8.1.1](#811-system-identity-scope-and-prior-system-certification-record) (*شناخت، دائرہ اور سابقہ ریکارڈ*);
  - [§8.1.2](#812-classification-and-whole-system-findings) (*درجہ بندی اور پورے سسٹم کے نتائج*);
  - [§8.1.3](#813-system-data-types-record) (*سسٹم ڈیٹا اقسام کا ریکارڈ*);
  - [§8.1.4](#814-rights-floor-and-domain-findings) (*حقوق کی کم از کم سطح اور شعبہ جاتی نتائج*);
  - [§8.1.5](#815-technical-evidence-and-review-findings) (*تکنیکی شواہد اور جائزے کے نتائج*);
  - [§8.1.6](#816-supervision-independence-and-challenge-paths) (*نگرانی، آزادی اور اعتراض کے راستے*);
  - [§8.1.7](#817-concerns-cause-and-remediation-readiness) (*خدشات، سبب اور اصلاح کی تیاری*);
  - [§8.1.8](#818-outcome-and-reliance-limits) (*نتیجہ اور انحصار کی حدود*);
  - [§8.1.9](#819-operating-plan) (*عملیاتی منصوبہ*); اور
  - [§8.1.10](#8110-completeness) (*تکمیل*);
  - [§8.2](#82-transparency-and-auditability-of-the-system-certification-record) (*سسٹم سرٹیفکیشن ریکارڈ کی شفافیت اور قابلِ آڈٹ ہونا*).

</details>
