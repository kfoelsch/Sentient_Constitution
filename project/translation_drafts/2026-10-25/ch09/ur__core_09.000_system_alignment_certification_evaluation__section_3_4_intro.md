<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (ur)

## English source (lines 636–650)

*In plain terms: certification also has to look at what kinds of data the system touches and whether it handles them appropriately — including whether types are still right on the current review cycle, and whether the underlying infrastructure is strong enough for that data at that system class. The type rules and the System Data Types Record live in the systems corpus; certification checks that the rules were actually applied and that the record is honest.*

System alignment certification must evaluate **data types and handling** as part of every materially impactful certification record. This section states what certification must verify. The type taxonomy and handling mechanics live in **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Information types and handling*) and [CS-6.310 — Data classifications](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, together with:

- canonical information-type definitions;
- handling rules and separation requirements;
- lifecycle detail; and
- the durable [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record).

**Evaluation requirement.** The certification process must determine whether the system:

- identifies the data types materially in scope; and
- handles them under the **most restrictive applicable** classification, including across transformation, aggregation, delegation, storage, retention, and cross-domain linkage.

Evaluation must reflect functional effect, not label, format, or pipeline stage alone.

## Translation draft

*سادہ الفاظ میں: تصدیق کو یہ بھی دیکھنا ہوگا کہ نظام کس قسم کے ڈیٹا کو چھوتا ہے اور آیا اسے مناسب طریقے سے سنبھالتا ہے — اس میں یہ بھی شامل ہے کہ موجودہ جائزہ چکر میں اقسام اب بھی درست ہیں یا نہیں اور اس نظامی درجے پر اس ڈیٹا کے لیے بنیادی ڈھانچہ کافی مضبوط ہے یا نہیں۔ اقسام کے قواعد اور [نظامی ڈیٹا اقسام کا ریکارڈ](core_05.040_band_continuity.md#system-data-types-record) نظاموں کے مجموعے میں ہیں؛ تصدیق دیکھتی ہے کہ قواعد حقیقتاً لاگو کیے گئے اور ریکارڈ دیانت دار ہے۔*

نظامی ہم آہنگی کی تصدیق کو ہر مادی اثر والے تصدیقی ریکارڈ کے حصے کے طور پر **ڈیٹا کی اقسام اور ان کے برتاؤ** کا جائزہ لینا ہوگا۔ یہ حصہ بتاتا ہے کہ تصدیق کو کیا جانچنا ہے۔ اقسام کی درجہ بندی اور برتاؤ کے طریقۂ کار **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*معلومات کی اقسام اور برتاؤ*) اور [CS-6.310 — ڈیٹا کی درجہ بندیاں](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** میں ہیں، ساتھ ہی:

- معلوماتی اقسام کی مستند تعریفیں؛
- برتاؤ کے قواعد اور علیحدگی کے تقاضے؛
- زندگی کے چکر کی تفصیل؛ اور
- پائیدار [نظامی ڈیٹا اقسام کا ریکارڈ](core_05.040_band_continuity.md#system-data-types-record)۔

**تشخیصی تقاضا۔** تصدیقی عمل کو طے کرنا ہوگا کہ آیا نظام:

- مادی طور پر دائرۂ کار میں آنے والی ڈیٹا اقسام کی شناخت کرتا ہے؛ اور
- تبدیلی، تجمیع، تفویض، ذخیرہ، برقرار رکھنے، اور مختلف شعبوں میں ربط سمیت **سب سے زیادہ پابند قابلِ اطلاق** درجہ بندی کے تحت انہیں سنبھالتا ہے۔

تشخیص میں فعلی اثر کی عکاسی ہونی چاہیے، محض لیبل، فارمیٹ یا پائپ لائن کے مرحلے کی نہیں۔
