<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (bn)

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

এই অনুচ্ছেদে বলা হয়েছে, প্রত্যয়নকে কী যাচাই করতে হবে:

- **মূল্যায়নের শর্ত:**
  - নির্ধারিত সিস্টেম-শ্রেণি পর্যবেক্ষিত এবং যুক্তিসঙ্গতভাবে পূর্বানুমেয় **প্রভাব**, **নির্ভরতা** ও **ঝুঁকি** প্রতিফলিত করে কি না, CS-9.305 (*সিস্টেম শ্রেণিবিন্যাসের কাঠামো*) এবং CS-9.310 (*সিস্টেম-প্রভাব শ্রেণিবিভাগ*) অনুসারে; এর মধ্যে রয়েছে:
    - সামগ্রিক প্রভাব;
    - পারস্পরিক ক্রিয়ার প্রভাব;
    - প্রতিপক্ষসুলভ প্রভাব;
    - সীমা-অতিক্রমের প্রভাব;
  - শ্রেণিবিন্যাস প্রকৃত সিস্টেম-আচরণ ও প্রভাবের ভিত্তিতে নির্ধারিত হয়, নিচের ভিত্তিতে নয়:
    - ঘোষিত অভিপ্রায়;
    - নামমাত্র পরিধি;
    - শুধু [সিস্টেম সনদ](core_05.040_band_continuity.md#system-charter)-এর পাঠ্য; অথবা
    - শুধু স্ব-বর্ণনা;
  - উল্লেখযোগ্য পরিবর্তন হলে **[CS-9.305 §3.5 পুনঃশ্রেণিবিন্যাসের শর্ত](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** অনুযায়ী সিস্টেমের শ্রেণি পুনরায় যাচাই করা হয়েছে; এবং
  - [সিস্টেম শ্রেণিবিন্যাস রেকর্ডে](core_05.040_band_continuity.md#system-classification-record) বর্তমান অবস্থায় প্রযোজ্য **সর্বোচ্চ সিস্টেম-শ্রেণি** দেখানো হয়েছে।
- **নিশ্চয়তা ও রিগ্রেশন পরীক্ষা:**
  - শ্রেণি-অনুপাতে নিশ্চয়তা, অবকাঠামোর দৃঢ়তা এবং রিগ্রেশন পরীক্ষার পরিধি নির্ধারিত সিস্টেম-শ্রেণির সঙ্গে সামঞ্জস্যপূর্ণ, নিম্নলিখিত অনুসারে:
    - CS-9.305 (*সিস্টেম শ্রেণিবিন্যাসের কাঠামো*) এবং CS-9.310 (*সিস্টেম-প্রভাব শ্রেণিবিভাগ*); এবং
    - CS-6.345 (*সিস্টেম জীবনচক্র*), যেখানে যথেষ্ট প্রাসঙ্গিক সেখানে এই যৌথ কার্যক্রম-সংক্রান্ত পরিভাষাসহ:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*ধারাবাহিকতা: মসৃণ অবনতি ও ব্যর্থতার ধরন অখণ্ডতার পরিভাষা*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*ধারাবাহিকতা: প্রত্যাবর্তনযোগ্যতা ও নিয়ন্ত্রণের পরিভাষা*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*ধারাবাহিকতা: প্রতিপক্ষ-সহনশীলতা ও অপব্যবহার-প্রতিরোধের পরিভাষা*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*সমন্বয়: সীমাবদ্ধ গোপনীয়তা ও সুরক্ষিত তদন্তের পরিভাষা*), যেখানে সিস্টেমের শ্রেণি বা কাজ একে যথেষ্ট প্রাসঙ্গিক করে; এবং
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*সমন্বয়: হস্তক্ষেপ ও অগ্রাহ্যকরণ অখণ্ডতার পরিভাষা*), যেখানে সিস্টেমের শ্রেণি বা কাজ একে যথেষ্ট প্রাসঙ্গিক করে; এবং
  - প্রতিটি পুনঃপ্রত্যয়নের সময় CS-6.345 (*সিস্টেম জীবনচক্র*) অনুযায়ী রিগ্রেশন পরীক্ষা করা হয়েছে এবং ফলাফল [§8.1 ন্যূনতম রেকর্ড বিষয়বস্তু](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents)-এর অধীনে নথিভুক্ত হয়েছে।
