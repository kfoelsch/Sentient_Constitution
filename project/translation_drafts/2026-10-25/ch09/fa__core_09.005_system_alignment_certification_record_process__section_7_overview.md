### ۷. پیامدهای گواهی‌سازی

<details>
<summary><strong><span style="color: #2563eb;">ردیابی</span></strong></summary>

- پیش‌نیازها:
  - [§6](#6-forum-process) (*فرایند فوروم و اعتراض معتبر*)؛
  - [بخش A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) تا
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*طبقه‌بندی نادرست، عدم هم‌راستایی و نقص‌های کشف‌شده در ارزیابی*)؛
  - [دو هدف قانون اساسی](core_00.000_preamble.md#two-constitutional-aims)؛
  - [فصل سه §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) و
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*یکپارچگی تعریف و طفره‌روی*)؛
  - [فصل سه §2.1 الگوهای متداول طفره‌روی](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*طفره‌روی از دامنه و مرزها*)؛
  - [منشور سامانه](core_05.040_band_continuity.md#system-charter) (*ناهماهنگی منشور سامانه و رفتار و بازبینی به‌تعویق‌افتاده*).
- پیامدها:
  - [بخش C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*نتیجه در سابقه بیان می‌شود*)؛
  - [بخش C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*مسیر اعتراض با نتیجه باز می‌شود*)؛
  - [بخش C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*گواهی‌سازی مجدد و بازگشایی*)؛
  - [بخش C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*دروازه ورودی تأییدشده، جایی که واقعیت‌ها یافته‌های زیان‌بار را پشتیبانی می‌کنند*)؛
  - [فصل سیزده](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*نظارت فوروم*)؛
  - [فصل ده](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- برای ارزیابی مجدد برنامه‌ریزی‌شده نوع داده، همراه با **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*بازطبقه‌بندی و حکمرانی چرخه عمر*)، و برای محرک‌های ارزیابی دوباره رده سامانه و راستی‌آزمایی SAC، همراه با **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*الزام بازطبقه‌بندی*) خوانده شود.
- زیربخش‌ها:
  - [§7.1](#71-go-live-gate) (*دروازه راه‌اندازی*، شامل
  - [§7.1.1 سامانه‌های فعال](#711-systems-already-operating) و
  - [§7.1.2 پایلوت‌ها](#712-pilots))؛
  - [§7.2](#72-certification-defects-and-correction) (*نقص‌های گواهی‌سازی و اصلاح*)؛
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*آمادگی اصلاح: تمایل و توان اصلاح*، شامل
  - [§7.3.1 تمایل](#731-willingness)،
  - [§7.3.2 توان](#732-capacity)،
  - [§7.3.3 گام اثبات](#733-proof-step)،
  - [§7.3.4 یافته‌ها](#734-findings)، و
  - [§7.3.5 شرایط یکسان برای هر گرداننده](#735-same-terms-for-every-operator))؛
  - [§7.4](#74-denial-and-revocation) (*رد و لغو*، شامل
  - [§7.4.1 رد و لغو چیست](#741-what-denial-and-revocation-are)،
  - [§7.4.2 چه زمان رد یا لغو لازم است](#742-when-denial-or-revocation-is-required)،
  - [§7.4.3 حفاظت در اولویت](#743-protection-first)،
  - [§7.4.4 فرایند](#744-process)،
  - [§7.4.5 اثر](#745-effect)، و
  - [§7.4.6 منع دائمی نیست](#746-not-a-permanent-bar)).

</details>

<br>

*به زبان ساده: هر بازبینی گواهی‌سازی با نتیجه‌ای اعلام‌شده پایان می‌یابد که شواهد و نگرانی‌های مطرح‌شده در مسیر از آن پشتیبانی می‌کنند. هیچ سامانه‌ای تا زمان گواهی‌شدن، فراهم‌شدن فرصت عملی اعتراض برای موجودات ذی‌شعور متأثر از طریق نتیجه منتشرشده، و بررسی حفاظت‌های لازم پیش از راه‌اندازی، فعال نمی‌شود.*

این بخش **مرحله چهارم، تصمیم‌گیری** است، پس از [§6 فرایند فوروم](#6-forum-process) (**مرحله سوم، بازبینی**). نتیجه‌ای را پوشش می‌دهد که فوروم‌ها به آن می‌رسند. [§7.1 دروازه راه‌اندازی](#71-go-live-gate) شرط راه‌اندازی را می‌گوید و [§7.2 نقص‌های گواهی‌سازی و اصلاح](#72-certification-defects-and-correction) پیامد یافتن نقص را تعیین می‌کند.

تصمیم گواهی‌سازی باید طبق [بخش C §8.1 حداقل محتوای سابقه](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)، نتیجه خود را همراه با نگرانی‌های مطرح‌شده در مسیر رسیدن به آن در سابقه بیان کند. نتیجه یکی از این موارد است:

- گواهی‌سازی موقت؛
- گواهی‌سازی کامل؛
- گواهی‌سازی مشروط؛
- گواهی‌سازی به‌تعویق‌افتاده؛
- عدم گواهی‌سازی؛
- لغو؛
- انقضا؛ یا
- رهایی از شرط‌ها.

سامانه‌ای که نه گواهی‌سازی موقت دارد و نه کامل، **گواهی‌نشده** است. این حالت وقتی است که گواهی‌سازی:

- به‌تعویق‌افتاده باشد؛
- رد شده باشد؛
- لغو شده باشد؛ یا
- منقضی شده باشد.

گواهی‌سازی موقت و کامل دو **وضعیت** گواهی‌سازی هستند. [بخش C §9.2 گواهی‌سازی موقت و کامل](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) توضیح می‌دهد سامانه چگونه هر وضعیت را به دست می‌آورد، حفظ می‌کند و از دست می‌دهد. شرط‌های گواهی‌سازی مشروط ممکن است به هر یک از دو وضعیت پیوند بخورند.

<a id="71-go-live-gate"></a>
