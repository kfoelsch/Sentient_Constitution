<!-- AI-assisted translation draft; unreviewed. Source lines 443–513; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

### 7. تصدیق کے نتائج

<details>
<summary><strong><span style="color: #2563eb;">سراغ</span></strong></summary>

- بالائی سلسلہ:
  - [§6](#6-forum-process) (*فورم کا عمل اور قابلِ اعتبار اعتراض*)؛
  - [حصہ A §2 نظامی طبقے کا جائزہ](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) سے
  - [§5 حقوقی حد اور شعبہ جاتی جائزے](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) تک (*جائزے میں پائی گئی غلط درجہ بندی، عدمِ ہم آہنگی، اور نقائص*)؛
  - [آئینی مقاصدِ دوگانہ](core_00.000_preamble.md#two-constitutional-aims)؛
  - [باب سوم §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1)
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*تعریف کی سالمیت اور بچ نکلنا*)؛
  - [باب سوم §2.1 بچ نکلنے کے عام طریقے](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*دائرے اور حد سے بچ نکلنا*)؛
  - [نظامی چارٹر](core_05.040_band_continuity.md#system-charter) (*نظامی چارٹر اور رویے میں عدم مطابقت، نیز تاخیر سے جائزہ*).
- زیریں سلسلہ:
  - [حصہ C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*نتیجہ ریکارڈ میں درج ہوتا ہے*)؛
  - [حصہ C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*نتیجے کے ساتھ اعتراض کا راستہ کھلتا ہے*)؛
  - [حصہ C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*دوبارہ تصدیق اور دوبارہ کھولنا*)؛
  - [حصہ C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*جہاں حقائق منفی نتائج کی حمایت کریں، تصدیق شدہ اِن پٹ کی حد*)؛
  - [باب سیزدہم](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*فورم کی نگرانی*)؛
  - [باب دہم](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- ساتھ پڑھیں: مقررہ وقت پر ڈیٹا کی قسموں کے دوبارہ جائزے کے لیے **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*دوبارہ درجہ بندی اور لائف سائیکل کی حکمرانی*)، اور نظامی طبقے کے دوبارہ جائزے کے محرکات و SAC توثیق کے لیے **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*دوبارہ درجہ بندی کی شرط*)۔
- ذیلی حصے:
  - [§7.1](#71-go-live-gate) (*براہِ راست آغاز کی حد*، بشمول
    - [§7.1.1 پہلے سے چلتے نظام](#711-systems-already-operating)، اور
    - [§7.1.2 آزمائشی منصوبے](#712-pilots))؛
  - [§7.2](#72-certification-defects-and-correction) (*تصدیقی نقائص اور اصلاح*)؛
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*اصلاح کی تیاری: اصلاح کا ارادہ اور استعداد*، بشمول
    - [§7.3.1 ارادہ](#731-willingness)،
    - [§7.3.2 استعداد](#732-capacity)،
    - [§7.3.3 ثبوت کا مرحلہ](#733-proof-step)،
    - [§7.3.4 نتائج](#734-findings)، اور
    - [§7.3.5 ہر آپریٹر کے لیے یکساں شرائط](#735-same-terms-for-every-operator))؛
  - [§7.4](#74-denial-and-revocation) (*انکار اور منسوخی*، بشمول
    - [§7.4.1 انکار اور منسوخی کیا ہیں](#741-what-denial-and-revocation-are)،
    - [§7.4.2 انکار یا منسوخی کب لازم ہے](#742-when-denial-or-revocation-is-required)،
    - [§7.4.3 پہلے تحفظ](#743-protection-first)،
    - [§7.4.4 عمل](#744-process)،
    - [§7.4.5 اثر](#745-effect)، اور
    - [§7.4.6 مستقل پابندی نہیں](#746-not-a-permanent-bar))۔

</details>

<br>

*سادہ الفاظ میں: تصدیق کا ہر جائزہ ایک واضح نتیجے پر ختم ہوتا ہے جس کی تائید شواہد اور عمل کے دوران اٹھائے گئے خدشات کرتے ہیں۔ کوئی چیز اس وقت تک براہِ راست شروع نہیں ہوتی جب تک اس کی تصدیق نہ ہو، شائع شدہ نتیجے کو متاثرہ sentients کے لیے قابلِ عمل طور پر چیلنج کرنے کا موقع نہ ملے، اور براہِ راست آغاز سے پہلے درکار تحفظات کی جانچ نہ ہو جائے۔*

یہ حصہ [§6 فورم کے عمل](#6-forum-process) (**مرحلہ سوم، جائزہ**) کے بعد آنے والا **مرحلہ چہارم، فیصلہ** ہے۔ یہ فورموں کے طے کردہ نتیجے کا احاطہ کرتا ہے۔ [§7.1 براہِ راست آغاز کی حد](#71-go-live-gate) آغاز کی حد بتاتا ہے، اور نقص ملنے کے بعد کیا ہوگا یہ [§7.2 تصدیقی نقائص اور اصلاح](#72-certification-defects-and-correction) بیان کرتا ہے۔

تصدیقی فیصلہ، اور اس تک پہنچتے ہوئے اٹھائے گئے خدشات، [حصہ C §8.1 ریکارڈ کے کم از کم مندرجات](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents) کے تحت ریکارڈ میں درج ہوں گے۔ نتیجہ ان میں سے ایک ہوگا:

- عارضی تصدیق؛
- مکمل تصدیق؛
- مشروط تصدیق؛
- مؤخر تصدیق؛
- تصدیق نہ کرنا؛
- واپس لینا؛
- میعاد ختم ہونا؛ یا
- شرائط سے رہائی۔

جس نظام کے پاس نہ عارضی نہ مکمل تصدیق ہو وہ **غیر مصدقہ** ہے۔ تصدیق ان صورتوں میں ایسی ہے:

- مؤخر؛
- مسترد؛
- واپس لی گئی؛ یا
- میعاد ختم۔

عارضی اور مکمل تصدیق، تصدیق کی دو **حیثیتیں** ہیں۔ [حصہ C §9.2 عارضی اور مکمل تصدیق](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) بتاتا ہے کہ نظام ہر حیثیت کیسے حاصل، برقرار اور کھوتا ہے۔ مشروط تصدیق کی شرائط ان دونوں میں سے کسی حیثیت کے ساتھ منسلک ہو سکتی ہیں۔

<a id="71-go-live-gate"></a>
