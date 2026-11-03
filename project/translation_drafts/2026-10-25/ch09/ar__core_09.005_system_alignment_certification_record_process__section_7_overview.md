### 7. نتائج التصديق

<details>
<summary><strong><span style="color: #2563eb;">التتبع</span></strong></summary>

- المنبع:
  - [§6](#6-forum-process) (*عملية المنتدى والطعن الموثوق*)؛
  - [الجزء A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) حتى
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*سوء التصنيف وعدم المواءمة والعيوب التي كشفها التقييم*)؛
  - [المقصدان الدستوريان](core_00.000_preamble.md#two-constitutional-aims)؛
  - [الفصل الثالث §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) و
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*نزاهة التعريف والتهرّب*)؛
  - [الفصل الثالث §2.1 أنماط التهرّب الشائعة](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*التهرب من النطاق والحدود*)؛
  - [ميثاق النظام](core_05.040_band_continuity.md#system-charter) (*عدم التطابق بين سلوك النظام والميثاق والمراجعة المتأخرة*).
- المصب:
  - [الجزء C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*تُذكر النتيجة في السجل*)؛
  - [الجزء C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*يفتح مسار الطعن مع النتيجة*)؛
  - [الجزء C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*إعادة التصديق وإعادة الفتح*)؛
  - [الجزء C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*بوابة المدخلات المتحقق منها حين تسند الوقائع نتائج سلبية*)؛
  - [الفصل الثالث عشر](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*إشراف المنتدى*)؛
  - [الفصل العاشر](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- يُقرأ مع: **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*إعادة التصنيف وحوكمة دورة الحياة*) لإعادة التقييم المجدولة لنوع البيانات، و**[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*متطلب إعادة التصنيف*) لمحفزات إعادة تقييم فئة النظام والتحقق من SAC.
- الأقسام الفرعية:
  - [§7.1](#71-go-live-gate) (*بوابة بدء التشغيل*، وتشمل
  - [§7.1.1 الأنظمة قيد التشغيل بالفعل](#711-systems-already-operating) و
  - [§7.1.2 التجارب الأولية](#712-pilots))؛
  - [§7.2](#72-certification-defects-and-correction) (*عيوب التصديق وتصحيحها*)؛
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*الاستعداد للمعالجة: الرغبة والقدرة على التصحيح*، ويشمل
  - [§7.3.1 الرغبة](#731-willingness)،
  - [§7.3.2 القدرة](#732-capacity)،
  - [§7.3.3 خطوة الإثبات](#733-proof-step)،
  - [§7.3.4 النتائج](#734-findings)، و
  - [§7.3.5 الشروط نفسها لكل مشغّل](#735-same-terms-for-every-operator))؛
  - [§7.4](#74-denial-and-revocation) (*الرفض والسحب*، ويشمل
  - [§7.4.1 ماهية الرفض والسحب](#741-what-denial-and-revocation-are)،
  - [§7.4.2 متى يلزم الرفض أو السحب](#742-when-denial-or-revocation-is-required)،
  - [§7.4.3 الحماية أولًا](#743-protection-first)،
  - [§7.4.4 الإجراءات](#744-process)،
  - [§7.4.5 الأثر](#745-effect)، و
  - [§7.4.6 ليس حظرًا دائمًا](#746-not-a-permanent-bar)).

</details>

<br>

*بعبارات بسيطة: تنتهي كل مراجعة للتصديق بنتيجة معلنة، تسندها الأدلة والشواغل التي أُثيرت أثناء العملية. ولا يبدأ أي نظام تشغيله حتى يُصدّق عليه، وتتيح النتيجة المنشورة للكائنات الواعية المتأثرة فرصة عملية للطعن فيها، ويُتحقق من تدابير الحماية المطلوبة قبل التشغيل.*

هذا القسم هو **المرحلة الرابعة، القرار**، بعد [§6 عملية المنتدى](#6-forum-process) (**المرحلة الثالثة، المراجعة**). وهو يتناول النتيجة التي تصل إليها المنتديات. وتحدد [§7.1 بوابة بدء التشغيل](#71-go-live-gate) شرط بدء التشغيل، وتحدد [§7.2 عيوب التصديق وتصحيحها](#72-certification-defects-and-correction) ما يحدث عند العثور على عيب.

يجب أن يذكر قرار التصديق نتيجته في السجل بموجب [الجزء C §8.1 الحد الأدنى لمحتوى السجل](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)، إلى جانب الشواغل التي أثيرت عند التوصل إليه. والنتيجة واحدة مما يلي:

- تصديق مؤقت؛
- تصديق كامل؛
- تصديق مشروط؛
- تأجيل التصديق؛
- عدم التصديق؛
- السحب؛
- انتهاء المدة؛ أو
- الإعفاء من الشروط.

النظام الذي لا يحمل تصديقًا مؤقتًا ولا كاملًا هو **غير مصدّق**. ويكون ذلك حين يكون التصديق:

- مؤجلًا؛
- مرفوضًا؛
- مسحوبًا؛ أو
- منتهي المدة.

التصديق المؤقت والتصديق الكامل هما **حالَتا** التصديق. ويوضح [الجزء C §9.2 التصديق المؤقت والكامل](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) كيفية حصول النظام على كل حالة والاحتفاظ بها وفقدانها. وقد تنطبق شروط التصديق المشروط على أي من الحالتين.

<a id="71-go-live-gate"></a>
