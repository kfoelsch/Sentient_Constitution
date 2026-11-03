### ৭. সার্টিফিকেশনের ফলাফল

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণ</span></strong></summary>

- পূর্বসূত্র:
  - [§6](#6-forum-process) (*ফোরাম প্রক্রিয়া ও বিশ্বাসযোগ্য আপত্তি*);
  - [পার্ট A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) থেকে
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*মূল্যায়নে পাওয়া ভুল শ্রেণিবিন্যাস, alignment-এর ত্রুটি ও অন্যান্য ত্রুটি*);
  - [দুই সাংবিধানিক লক্ষ্য](core_00.000_preamble.md#two-constitutional-aims);
  - [অধ্যায় তিন §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) এবং
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*সংজ্ঞার অখণ্ডতা ও ফাঁকি*);
  - [অধ্যায় তিন §2.1 সাধারণ ফাঁকির ধরন](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*পরিধি ও সীমানা এড়ানো*);
  - [ব্যবস্থা চার্টার](core_05.040_band_continuity.md#system-charter) (*ব্যবস্থা চার্টার ও আচরণের অমিল এবং অতিরিক্ত দেরির পর্যালোচনা*)।
- পরবর্তী সংযোগ:
  - [পার্ট C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*ফল রেকর্ডে বলা হয়*);
  - [পার্ট C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*ফলের সঙ্গে আপত্তির পথ খোলে*);
  - [পার্ট C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*পুনঃসার্টিফিকেশন ও পুনরায় খোলা*);
  - [পার্ট C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*প্রতিকূল সিদ্ধান্ত সমর্থনকারী তথ্যের ক্ষেত্রে যাচাইকৃত-ইনপুট দ্বার*);
  - [অধ্যায় তেরো](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*ফোরাম তদারকি*);
  - [অধ্যায় দশ](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000)।
- সঙ্গে পড়ুন: নির্ধারিত তথ্য-ধরন পুনর্মূল্যায়নের জন্য **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*পুনঃশ্রেণিবিন্যাস ও জীবনচক্র পরিচালনা*) এবং ব্যবস্থা-শ্রেণি পুনর্মূল্যায়নের ট্রিগার ও SAC যাচাইয়ের জন্য **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*পুনঃশ্রেণিবিন্যাসের শর্ত*)।
- উপধারা:
  - [§7.1](#71-go-live-gate) (*চালু-করার দ্বার*, যার মধ্যে
  - [§7.1.1 আগে থেকেই চালু ব্যবস্থা](#711-systems-already-operating) এবং
  - [§7.1.2 পাইলট](#712-pilots));
  - [§7.2](#72-certification-defects-and-correction) (*সার্টিফিকেশনের ত্রুটি ও সংশোধন*);
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*সংশোধনের প্রস্তুতি: ইচ্ছা ও সংশোধনের সক্ষমতা*, যার মধ্যে
  - [§7.3.1 ইচ্ছা](#731-willingness),
  - [§7.3.2 সক্ষমতা](#732-capacity),
  - [§7.3.3 প্রমাণের ধাপ](#733-proof-step),
  - [§7.3.4 অনুসন্ধান](#734-findings), এবং
  - [§7.3.5 প্রত্যেক পরিচালকের জন্য একই শর্ত](#735-same-terms-for-every-operator));
  - [§7.4](#74-denial-and-revocation) (*প্রত্যাখ্যান ও প্রত্যাহার*, যার মধ্যে
  - [§7.4.1 প্রত্যাখ্যান ও প্রত্যাহার কী](#741-what-denial-and-revocation-are),
  - [§7.4.2 কখন প্রত্যাখ্যান বা প্রত্যাহার আবশ্যক](#742-when-denial-or-revocation-is-required),
  - [§7.4.3 আগে সুরক্ষা](#743-protection-first),
  - [§7.4.4 প্রক্রিয়া](#744-process),
  - [§7.4.5 প্রভাব](#745-effect), এবং
  - [§7.4.6 স্থায়ী নিষেধাজ্ঞা নয়](#746-not-a-permanent-bar))।

</details>

<br>

*সহজ ভাষায়: প্রতিটি সার্টিফিকেশন পর্যালোচনার শেষে একটি ঘোষিত ফল থাকে, যার ভিত্তি প্রমাণ এবং চলার পথে উত্থাপিত উদ্বেগ। কোনো ব্যবস্থা সার্টিফাই না হওয়া পর্যন্ত চালু হয় না; প্রকাশিত ফল প্রভাবিত সংবেদনশীল সত্তাদের আপত্তি জানানোর বাস্তব সুযোগ না দেওয়া পর্যন্ত এবং চালুর আগে প্রয়োজনীয় সুরক্ষা যাচাই না হওয়া পর্যন্ত নয়।*

এই অংশটি **পর্যায় IV, সিদ্ধান্ত**, [§6 ফোরাম প্রক্রিয়া](#6-forum-process) (**পর্যায় III, পর্যালোচনা**)-এর পরে। এতে ফোরামগুলোর গৃহীত ফল রয়েছে। [§7.1 চালু-করার দ্বার](#71-go-live-gate) চালুর শর্ত নির্ধারণ করে এবং [§7.2 সার্টিফিকেশনের ত্রুটি ও সংশোধন](#72-certification-defects-and-correction) ত্রুটি পাওয়া গেলে কী হবে তা নির্ধারণ করে।

সার্টিফিকেশনের সিদ্ধান্তে [পার্ট C §8.1 ন্যূনতম রেকর্ডের বিষয়বস্তু](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents) অনুসারে রেকর্ডে ফল জানাতে হবে এবং সেই সিদ্ধান্তে পৌঁছানোর পথে উত্থাপিত উদ্বেগও লিখতে হবে। ফল হলো:

- সাময়িক সার্টিফিকেশন;
- পূর্ণ সার্টিফিকেশন;
- শর্তযুক্ত সার্টিফিকেশন;
- স্থগিত সার্টিফিকেশন;
- সার্টিফিকেশন না-হওয়া;
- প্রত্যাহার;
- মেয়াদোত্তীর্ণ হওয়া; অথবা
- শর্ত থেকে অব্যাহতি।

যে ব্যবস্থার সাময়িক বা পূর্ণ সার্টিফিকেশন কোনোটিই নেই, সেটি **সার্টিফাইড নয়**। সার্টিফিকেশন:

- স্থগিত;
- প্রত্যাখ্যাত;
- প্রত্যাহৃত; অথবা
- মেয়াদোত্তীর্ণ হলে এমন হয়।

সাময়িক ও পূর্ণ সার্টিফিকেশন হলো সার্টিফিকেশনের দুটি **অবস্থা**। [পার্ট C §9.2 সাময়িক ও পূর্ণ সার্টিফিকেশন](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) ব্যাখ্যা করে কীভাবে ব্যবস্থা প্রতিটি অবস্থা অর্জন, বজায় ও হারায়। শর্তযুক্ত সার্টিফিকেশনের শর্ত যেকোনো এক অবস্থার সঙ্গে যুক্ত হতে পারে।

<a id="71-go-live-gate"></a>
