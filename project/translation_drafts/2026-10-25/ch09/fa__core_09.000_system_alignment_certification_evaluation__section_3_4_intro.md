<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (fa)

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

*به زبان ساده: گواهی‌سازی باید بررسی کند سامانه با چه انواع داده‌ای سروکار دارد و آیا آن‌ها را به‌درستی مدیریت می‌کند — از جمله اینکه آیا انواع در چرخهٔ بازبینی جاری هنوز درست‌اند و آیا زیرساخت زیربنایی برای آن داده‌ها در آن ردهٔ سامانه به‌اندازهٔ کافی نیرومند است. قواعد انواع و [سابقهٔ انواع دادهٔ سامانه](core_05.040_band_continuity.md#system-data-types-record) در مدونهٔ سامانه‌ها قرار دارند؛ گواهی‌سازی بررسی می‌کند که قواعد واقعاً اعمال شده‌اند و سابقه صادقانه است.*

گواهی‌سازی همسویی سامانه باید **انواع داده و نحوهٔ برخورد با آن‌ها** را در هر سابقهٔ گواهی‌سازی با اثر بااهمیت ارزیابی کند. این بخش می‌گوید گواهی‌سازی چه چیزی را باید راستی‌آزمایی کند. رده‌بندی انواع و سازوکارهای برخورد در **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*انواع اطلاعات و نحوهٔ برخورد*) و [CS-6.310 — طبقه‌بندی‌های داده](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** قرار دارند، همراه با:

- تعریف‌های معیار انواع اطلاعات؛
- قواعد برخورد و الزامات جداسازی؛
- جزئیات چرخهٔ عمر؛ و
- [سابقهٔ انواع دادهٔ سامانه](core_05.040_band_continuity.md#system-data-types-record) پایدار.

**الزام ارزیابی.** فرایند گواهی‌سازی باید تعیین کند آیا سامانه:

- انواع داده‌ای را که از نظر ماهوی در دامنه‌اند شناسایی می‌کند؛ و
- آن‌ها را طبق **محدودکننده‌ترین طبقه‌بندی قابل‌اعمال** مدیریت می‌کند، از جمله هنگام تبدیل، تجمیع، تفویض، ذخیره‌سازی، نگهداری و پیوند میان حوزه‌ها.

ارزیابی باید اثر کارکردی را بازتاب دهد، نه صرفاً برچسب، قالب یا مرحلهٔ خط لوله را.
