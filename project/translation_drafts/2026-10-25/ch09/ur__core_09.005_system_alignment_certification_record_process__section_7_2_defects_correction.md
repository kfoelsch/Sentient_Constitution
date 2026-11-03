<!-- AI-assisted translation draft; unreviewed. Source lines 576–616; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

#### 7.2 تصدیقی نقائص اور اصلاح

*سادہ الفاظ میں: نقائص شرائط، التوا، انکار، واپسی یا نئے جائزے کا باعث بن سکتے ہیں۔ اجازت یا شرائط سے رہائی کی بنیاد بننے سے پہلے اصلاح کی آزادانہ توثیق ضروری ہے۔ آپریٹر کی اصلاح کے لیے آمادگی اور صلاحیت طے کرتی ہے کہ فورم ان میں سے کس راستے کا انتخاب کرے ([§7.3 تدارک کی تیاری: اصلاح کی آمادگی اور صلاحیت](#73-remediation-readiness-willingness-and-capacity-to-correct)، [§7.4 انکار اور منسوخی](#74-denial-and-revocation))۔*

حصہ A کے کسی بھی جائزے میں پائے جانے والے تصدیقی نقائص معمولی کاغذی کارروائی کی غلطیاں نہیں۔ ان میں شامل ہیں:

- [§2 نظامی زمرے کے جائزے](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) کے تحت غلط درجہ بندی؛
- [§3.2.2 نقائص اور عدم مطابقت](core_09.000_system_alignment_certification_evaluation.md#322-defects-and-misalignment) کے تحت خطرے کی جانچ اور خطرے کے انکشاف کے نقائص؛
- [§3.4 ڈیٹا کی اقسام اور ہینڈلنگ کے جائزے](core_09.000_system_alignment_certification_evaluation.md#34-data-types-and-handling-evaluation) کے تحت ڈیٹا ہینڈلنگ کے نقائص؛ اور
- [§5.1 ماحولیاتی اثرات کے جائزے](core_09.000_system_alignment_certification_evaluation.md#51-ecological-footprint-evaluation) سے [§5.6 قابلِ اعتماد ہونے اور نظام پر انحصار کی سالمیت کے جائزے](core_09.000_system_alignment_certification_evaluation.md#56-trustworthiness-and-system-reliance-integrity-evaluation) تک بیان کردہ شعبہ جاتی نقائص۔

ایسا نقص پائے جانے پر فورمز یہ کر سکتے ہیں:

- شرائط کے ساتھ تصدیق کرنا؛
- تصدیق ملتوی کرنا؛
- تصدیق سے انکار کرنا؛
- تصدیق واپس لینا؛
- تصدیقی وقفہ تبدیل کرنا؛ یا
- [حصہ C §9 دوبارہ تصدیق اور دوبارہ کھولنا](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) کے تحت جائزہ دوبارہ کھولنا یا نئے جائزے کا حکم دینا۔

فورم ان میں سے کس راستے کا انتخاب کرتا ہے، اس کا انحصار اس بات پر ہے کہ آپریٹر یا نگران نقص درست کرنے کے لیے آمادہ اور اہل ہے یا نہیں۔ [§7.3 تدارک کی تیاری: اصلاح کی آمادگی اور صلاحیت](#73-remediation-readiness-willingness-and-capacity-to-correct) یہ جانچ بیان کرتا ہے، اور [§7.4 انکار اور منسوخی](#74-denial-and-revocation) بتاتا ہے کہ انکار یا واپسی کب لازم ہے۔

**تحفظ، اصلاح اور توثیق۔** نقص پائے جانے پر فورم کو یہ بتانا ہوگا:

- متاثرہ دائرۂ کار؛
- عبوری تحفظ اور انحصار کی حدود؛ اور
- مطلوبہ اصلاحی کام۔

یہ [حصہ C §9.2 عارضی اور مکمل تصدیق](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) میں سبب کی شناخت اور درجہ وار مدتوں کو استعمال کرتا ہے۔

آپریٹر یا نگران اصلاح کے شواہد فراہم کرتا ہے۔ مقررہ اتھارٹی ان شواہد کی آزادانہ توثیق کرتی ہے، اس سے پہلے کہ انہیں اس دائرۂ کار کی اجازت یا اس کی شرائط سے رہائی کے لیے استعمال کیا جائے۔ اصلاح کو لازماً:

- نقص اور اس کی شناخت شدہ وجہ کا ازالہ کرنا ہوگا؛ اور
- یہ دکھانا ہوگا کہ متاثرہ حفاظتی اقدامات برقرار ہیں، جس میں جہاں [CS-6.345 §10 دوبارہ تصدیق، ریگریشن ٹیسٹنگ، اور تصدیقی نقائص](corpus_systems/cs_06.345_design_testing_verification_deployment.md#cs-6345-10-recertification-regression-testing-and-certification-defects) لازم کرے وہاں ریگریشن کی تصدیق بھی شامل ہے۔

اصلاح کا وعدہ یا آپریٹر کا یہ اعلان کہ کام مکمل ہے، کافی نہیں۔ آپریٹر کو تصدیق شدہ شواہد پیش کرنے ہوں گے کہ ہر اصلاح براہِ راست شناخت شدہ مخصوص مسئلے کا ازالہ کرتی ہے۔ آپریٹر کے کام کرنے یا نظام کے اب چلنے کا ثبوت کافی نہیں، جب تک وہ یہ نہ دکھائے کہ شناخت شدہ مسئلہ واقعی حل ہو گیا ہے۔

غیر مصدقہ نظام نیا آپریشن شروع نہیں کر سکتا۔ اگر اس دوران چلتے ہوئے نظام پر انحصار جاری رہتا ہے تو اس کا فیصلہ قابلِ اطلاق فورم کے طریقۂ کار اور [حصہ C §9.2 عارضی اور مکمل تصدیق](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) میں بقا کے لیے ضروری تحفظ کے تحت الگ سے کیا جاتا ہے۔

<a id="73-remediation-readiness-willingness-and-capacity-to-correct"></a>
