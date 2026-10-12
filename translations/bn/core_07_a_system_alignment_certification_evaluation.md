<a id="chapter-seven-system-alignment-certification"></a>
<a id="chapter-seven-system-alignment-certification-and-recognition"></a>
<a id="chapter-seven-part-a-certification-evaluation"></a>
<a id="chapter-seven-part-a-system-alignment-certification--evaluation"></a>
# অধ্যায় সাত, অংশ ক: ব্যবস্থা-সারিবদ্ধতা প্রত্যয়ন — মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">করপাসে অবস্থান (অ-কার্যকরী): ফাইলের গঠন ও পড়ার নিয়ম</span></strong></summary>

> এই ফাইল [ইংরেজি অধ্যায় সাত, অংশ ক](../../core_08_a_system_alignment_certification_evaluation.md)-এর **পাঠক-ভাষার পাইলট**। এটি সংজ্ঞ সংবিধানের **বাধ্যতামূলক অংশ নয়**। এটি **দ্বিতীয় সংবিধান নয়**। এটি **প্রেরণ সংস্করণ নয়**। এটি `SC-Corpus-2026.08.09`-এ **পিন**। অনুবাদ ও ইংরেজি মূল যদি অমিল মনে হয়, ক্রমাঙ্কিত [`core_07_a_system_alignment_certification_evaluation.md`](../../core_08_a_system_alignment_certification_evaluation.md) জিতবে। পড়ার ক্রম ও সংস্করণ মেটাডেটা [README.md](../../README.md)-এ থাকে। পদ্ধতি ও শব্দতালিকা: [translations/bn/README.md](README.md)।
>
> এতে আছে **অধ্যায় সাত, অংশ ক** — প্রত্যয়ন **মূল্যায়ন** প্রয়োজনীয়তা (ব্যবস্থার শ্রেণি, পুরো-ব্যবস্থা উপাদান, ও ডোমেইন-মূল্যায়ন হুক)। **অংশ খ** — প্রত্যয়ন নথি, মঞ্চ প্রক্রিয়া, প্রস্থিতি সেতু, ও পুনরায় খোলা — আছে [`core_07_b_system_alignment_certification_record_process.md`](core_07_b_system_alignment_certification_record_process.md)-এ।
>
> - **সাংবিধানিক মালিক (অংশ খ-এর সঙ্গে যৌথ):** মঞ্চ-তত্ত্বাবধানকৃত **ব্যবস্থা-সারিবদ্ধতা প্রত্যয়ন ও সংশ্লিষ্ট নথি** — মূল্যায়ন ক্ষেত্র (অংশ ক); প্রত্যয়ন-নথি কর্তব্য, স্বীকৃতি ফল, পুনঃবৈধকরণ ছন্দ, তত্ত্বাবধান ক্রম, চ্যালেঞ্জ-যোগ্যতা শৃঙ্খল, এবং অধ্যায় আটের দিকে যাচাইকৃত-উপকরণ সেতু (অংশ খ)। চতুষ্কের **তত্ত্বাবধান** পার অধীনে SAC অন্যান্যের মধ্যে এক বিশেষ বড়, উচ্চ-বাজির নিরীক্ষা প্রক্রিয়া; নিরীক্ষা তল থাকে **অনুচ্ছেদ XVI** এবং অধ্যায় পাঁচ [নিরীক্ষাযোগ্যতা](core_05_band_oversight.md#auditability)-তে।
> - **যাচাই উপস্তরের মালিক:** [অধ্যায় চার — প্রমাণভার, খুঁজে-পাওয়া ও যাচাই](core_04_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) (অধ্যায় দুই থেকে চারের ভিতরে) ভার বরাদ্দ, অনুপালন প্রমাণ, সংজ্ঞা খুঁজে-পাওয়া, পর্যবেক্ষণযোগ্যতা, এবং নিরাপত্তা-সীমাবদ্ধ যাচাইয়ের মালিক। অধ্যায় সাত সেই শৃঙ্খলা ব্যবস্থা-সারিবদ্ধতা প্রত্যয়ন নথিতে **প্রয়োগ** করে; অধ্যায় চারের ধারা **১** থেকে **৫** **পুনরাবৃত্তি** করে না।
> - **নিরীক্ষা ঘর (এখানে সরায় না):** **অনুচ্ছেদ XVI** (*নিরীক্ষা, স্বচ্ছতা ও স্বাধীন যাচাই*), **Def.O1** (*স্বচ্ছতা, নিরীক্ষাযোগ্যতা ও যাচাই*), এবং **CJS-3.3**–**CJS-3.5** নিরীক্ষা তল ও কার্যকরী পদের মালিক। অধ্যায় সাত এক বিশেষ বড় SAC নিরীক্ষা প্রক্রিয়া চালায় যা সেই তল পূরণ করতে হয়; সব নিরীক্ষার মালিক নয়।
> - **বাস্তবায়ন মালিক:** নির্ধারিত বাস্তবায়ন ফাইলে ব্যবস্থা-শ্রেণি পরিচালনা, CS-5, ও মঞ্চ-প্রক্রিয়া বিস্তারকে অধ্যায় সাতের সঙ্গে সামঞ্জস্যপূর্ণ থাকতে হয় এবং করপাস ইতিমধ্যে যেখানে কঠোরতর-নিয়ম যুক্তি দেয় সেখানে কঠোরতর হতে পারে।
> - **স্থানান্তর-নিরোধ নিয়ম:** অংশ ক অধ্যায় পাঁচের প্রামাণিক সংজ্ঞা, অধ্যায় তিনের এড়ানো-নিরোধ শৃঙ্খলা (দেখুন [অংশ খ §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)), অধ্যায় আটের অবদান বা প্রস্থিতি পরিমাপ, বা অধ্যায় নয়ের প্রস্থিতি প্রভাব পুনরাবৃত্তি করে না। **[অংশ খ §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing)** প্রস্থিতি সেতুর সীমানা স্পষ্ট করে বলে।
>
> **ঊর্ধ্ব:** অধ্যায় পাঁচের সংজ্ঞা এবং অধ্যায় দুই থেকে চারের নথি, যাচাই, ভার, ও সংজ্ঞা থেকে ফলে খুঁজে-পাওয়া।
> **অধঃ:** [অংশ খ](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process) (*নথি, মঞ্চ প্রক্রিয়া ও প্রস্থিতি সেতু*); অধ্যায় আটের প্রস্থিতি নথি ও যাচাইকৃত উপকরণ; অধ্যায় নয়ের প্রস্থিতি প্রভাব; অধ্যায় এগারোর মঞ্চ তত্ত্বাবধান ও ব্যবস্থা-সারিবদ্ধতা প্রত্যয়ন পথ।
>
> **দায়িত্বশীল ব্যবস্থাপক দ্বার (অ-কার্যকরী):** বাধ্যতামূলক পরবর্তী-ধাপ বিবৃতি: [কার্যকরী দায়িত্বশীল ব্যবস্থাপক বিবৃতি](#operative-steward-statement-sac)। [`implementation/STEWARD_ENTRY_DOORS.md`](../../implementation/STEWARD_ENTRY_DOORS.md)-এর সহায়ক নির্দেশক এটিকে সংকুচিত করতে পারে না।

>
> **আগেরটি (এই লোকেল):** [core_07_system_alignment_certification.md](core_07_system_alignment_certification.md#chapter-seven-system-alignment-certification-index)
>
> **পরেরটি (এই ভাষায়):** [core_07_b_system_alignment_certification_record_process.md](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)
> **পড়ার আর্ক:** §1 উদ্দেশ্য ও ভূমিকা → §2 ব্যবস্থার শ্রেণি → §3 পুরো-ব্যবস্থা মূল্যায়ন → §4–§10 ডোমেইন মূল্যায়ন

</details>

<br>

অধ্যায় সাত, **অংশ ক**, **ব্যবস্থা-সারিবদ্ধতা প্রত্যয়ন মূল্যায়ন**-এর সাংবিধানিক মালিক। নথির বিষয়বস্তু, মঞ্চ তত্ত্বাবধান, চ্যালেঞ্জ পথ, ও প্রস্থিতি সেতু আছে **[অংশ খ](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)**-এ।

<a id="operative-steward-statement-sac"></a>
> **কার্যকরী দায়িত্বশীল ব্যবস্থাপক বিবৃতি।** **মালিক:** অধ্যায় সাত (মঞ্চ-তত্ত্বাবধানকৃত SAC)। নীতি-স্তর লেন্স: অধ্যায় এক §14। SAC অনুচ্ছেদ XVI / নিরীক্ষাযোগ্যতার অধীনে এক বিশেষ বড় নিরীক্ষা প্রক্রিয়া — একমাত্র নিরীক্ষা নয়। **নিষিদ্ধ পদক্ষেপ:** ইউনিট পরীক্ষা, গোপনীয়তা চেকলিস্ট, বা স্থানীয় সারিবদ্ধ-লেবেলকে প্রত্যয়ন গণ্য করবেন না। চ্যালেঞ্জ জানালা এড়াবেন না। পঞ্চম নিরীক্ষা ঘর আবিষ্কার করবেন না। প্রত্যয়ন ব্যাজ বা LEQU স্কোরকে সংজ্ঞতা-অবস্থা গণ্য করবেন না। **ঘড়ি:** সারিবদ্ধ দাবির আগে এক চ্যালেঞ্জযোগ্য অধ্যায় সাত পথ খুলুন বা পুনরুদ্ধার করুন, প্রভাবিত পক্ষের চ্যালেঞ্জ জানালা সহ।

<a id="1-purpose-and-role"></a>

### 1. উদ্দেশ্য ও ভূমিকা

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণসূত্র</span></strong></summary>

- ঊর্ধ্বসূত্র: [প্রস্তাবনা — সাংবিধানিক মালিক-নিবন্ধন](core_00_preamble.md#4-principles-definitions-and-rights) এবং [কর্তৃত্ব-স্তূপ ও অভ্যন্তরীণ অনুক্রম](core_05_band_integrative.md#authority-stack-and-internal-hierarchy); [সাংবিধানিক চতুষ্ক](core_00_preamble.md#constitutional-tetrad); [দুই সাংবিধানিক উদ্দেশ্য](core_00_preamble.md#two-constitutional-aims); [বস্তুগত বাজি](core_00_preamble.md#material-stake); [আনুপাতিকতা](core_05_band_accountability.md#proportionality) এবং [সারবস্তুগত ন্যায্যতা](core_05_band_participation.md#substantive-fairness) (অধ্যায় পাঁচ); অংশগ্রহণ পরিমাপ পরিবার (*কণ্ঠ, প্রবেশাধিকার ও চ্যালেঞ্জের পথ*); [অধ্যায় এক §16 দায়িত্বশীল ব্যবস্থাপনার গভীরতর আলোচনা](core_01_c_stewardship_capacity_principles.md#16-stewardship-in-depth); [অধ্যায় এক §12 পদ্ধতিগত মূল্যায়নের আবশ্যকতা](core_01_a_values_principles.md#12-systemic-evaluation-requirement) (*নীতিস্তরে সমগ্র ব্যবস্থা মূল্যায়নের দৃষ্টিভঙ্গি — শুধু একটি দিক নয়*); অধ্যায় দুই থেকে চার; [অধ্যায় পাঁচ](core_05__definitions_home.md#chapter-five-foundational-definitions) (*প্রামাণিক সংজ্ঞা*); [অধ্যায় সাত §2 চার-আসনের সাংবিধানিক অধিকার-তল](core_07_functional_independence_segregation_of_duties.md#2-four-seat-constitutional-floor); [ব্যবস্থার সারিবদ্ধতা প্রত্যয়ন](core_05_band_continuity.md#system-alignment-certification) (অধ্যায় পাঁচের প্রামাণিক পরিভাষা; অ-কার্যকরী সংক্ষিপ্ত রূপ **SAC**); [ব্যবস্থা প্রত্যয়ন নথি](core_05_band_continuity.md#system-certification-record) (অধ্যায় পাঁচের অর্থে)।
- নিম্নমুখী সূত্র: [§2](#2-system-class-evaluation) (*ব্যবস্থা-শ্রেণি মূল্যায়ন*); [অংশ B §9.1](core_08_b_system_alignment_certification_record_process.md#91-challenging-a-certification) (*প্রত্যয়নের বিরুদ্ধে চ্যালেঞ্জ*); এবং [অংশ C-এর ব্যবস্থা-শ্রেণির প্রোফাইল](core_08_c_system_alignment_certification_illustrations.md#illustrative-system-class-profiles-non-exhaustive) (*ব্যবস্থা-শ্রেণির দৃষ্টান্তমূলক প্রোফাইল*); [অংশ C-এর সমগ্র-ব্যবস্থা অনুসরণচিত্র](core_08_c_system_alignment_certification_illustrations.md#illustrative-whole-system-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুসারে সমগ্র ব্যবস্থার কাজ করা উদাহরণ*); [§3.4.8](core_08_c_system_alignment_certification_illustrations.md#348-illustrative-data-handling-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুসারে তথ্য ব্যবস্থাপনার উদাহরণ*); [§5.1.5](core_08_c_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুসারে পরিবেশগত পদচিহ্নের উদাহরণ*); [§5.2.5](core_08_c_system_alignment_certification_illustrations.md#525-illustrative-educational-capability-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুসারে শিক্ষাগত সক্ষমতার উদাহরণ*); [§5.3.8](core_08_c_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুসারে আন্তঃব্যবস্থা সহায়তার উদাহরণ*); [§5.4.5](core_08_c_system_alignment_certification_illustrations.md#545-illustrative-nondiscrimination-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুসারে বৈষম্যহীনতার উদাহরণ*); [§5.5.6](core_08_c_system_alignment_certification_illustrations.md#556-illustrative-accessibility-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুসারে প্রবেশগম্যতার উদাহরণ*); [§5.6.5](core_08_c_system_alignment_certification_illustrations.md#565-illustrative-trustworthiness-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুসারে বিশ্বাসযোগ্যতার উদাহরণ*); [§3](#3-whole-system-certification-evaluation) (*সমগ্র-ব্যবস্থা প্রত্যয়ন মূল্যায়নের উপাদান*); [§3.4](#34-data-types-and-handling-evaluation) থেকে [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) পর্যন্ত (*বিভিন্ন ক্ষেত্রের মূল্যায়ন*); [অংশ B §6](core_08_b_system_alignment_certification_record_process.md#6-forum-process) (*তত্ত্বাবধানের ক্রম ও চ্যালেঞ্জের শৃঙ্খল*); [অংশ B §6.1](core_08_b_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles) (*ফোরামের উপাদানগুলির ভূমিকা*); [অংশ B §8](core_08_b_system_alignment_certification_record_process.md#8-system-certification-record) (*প্রত্যয়ন নথির বিষয়বস্তু*); [অংশ B §8.2](core_08_b_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*নথির অখণ্ডতার আবশ্যকতা*); [অংশ B §7](core_08_b_system_alignment_certification_record_process.md#7-certification-outcomes) (*পুনরায় খোলা ও ফাঁকি প্রতিরোধ*); [অংশ B §10](core_08_b_system_alignment_certification_record_process.md#10-relationship-to-standing) (*প্রস্থিতি-নথির সংযোগ*); [অধ্যায় নয়](core_09_standing_assessment.md#chapter-nine-contribution-violation-and-standing-model--measurement) (*প্রস্থিতি-নথি ও যাচাইকৃত-ইনপুটের প্রবেশদ্বার*); [অধ্যায় দশ](core_10_standing_integration.md#chapter-ten-standing-effects-and-integration) (*প্রস্থিতির প্রভাব ও সংহতি*); [অধ্যায় বারো](core_12_forum.md#chapter-twelve-forums-and-jurisdiction) (*ফোরামের তত্ত্বাবধান, প্রত্যয়ন, সারিবদ্ধতা প্রত্যয়ন ও পর্যালোচনা*)।
- সঙ্গে পড়ুন: [corpus_systems.md](corpus_systems.md), বিশেষত **CS-3 — ব্যবস্থা শ্রেণিবিন্যাস ও ব্যবস্থাপনা**, **CS-2 — তথ্যের ধরন ও ব্যবস্থাপনা**, এবং **CS-5** (*ব্যবহারকারীমুখী সক্ষমতার ক্ষেত্র*); [corpus_forum.md](corpus_forum.md), বিশেষত **CF-5** (*রাউটিং, স্থানান্তর, প্রত্যয়ন ও প্রতিনিধিত্বমূলক আচরণ*) এবং **CF-7** (*অখণ্ডতা সুরক্ষা, দখল প্রতিরোধ ও আত্মবিচার প্রতিরোধী সহায়তা*); **অনুচ্ছেদ XVI** (*নিরীক্ষা, স্বচ্ছতা ও স্বাধীন যাচাই*) এবং [নিরীক্ষাযোগ্যতা](core_05_band_oversight.md#auditability) (*নিরীক্ষার অধিকার-তল — SAC তত্ত্বাবধানের অধীনে বিশেষভাবে বড় একটি নিরীক্ষা প্রক্রিয়া, একমাত্র নিরীক্ষা-ভিত্তি নয়*); **CJS-3.3** (*তত্ত্বাবধান: নিরীক্ষাযোগ্যতা ও পুনর্গঠনযোগ্যতার পরিভাষা (পরিশিষ্ট)*) থেকে **CJS-3.5** (*তত্ত্বাবধান: স্বাধীন যাচাই ও দাবির অখণ্ডতার পরিভাষা*)।

</details>

<br>

*সহজ ভাষায়: কোনো ব্যবস্থা যখন সংজ্ঞ প্রাণীদের জীবনে সত্যিই গুরুত্বপূর্ণ প্রভাব ফেলে, তখন প্রত্যয়ন হতে হবে **আনুপাতিক** — ব্যবস্থার প্রকৃত প্রভাব, নির্ভরতা ও ঝুঁকি যতটা দাবি করে ততটাই কঠোর; সবার জন্য এক মাপের তালিকা বা প্রশ্নহীন অনুমোদন নয়। এটি **অংশগ্রহণমূলকও** হতে হবে — প্রভাবিত সংজ্ঞ প্রাণী ও সম্প্রদায়কে জানতে হবে কী পর্যালোচনা হয়েছে, সিদ্ধান্তটি বুঝতে হবে এবং ভুল হলে চ্যালেঞ্জ করতে পারতে হবে। ফোরামগুলো প্রমাণ পর্যালোচনা করে, তা প্রত্যয়ন নথিতে লেখে এবং ব্যবস্থার ঝুঁকি অনুযায়ী পুনঃপরীক্ষার সময়সূচি নির্ধারণ করে। A, B ও C শ্রেণিতে সম্পূর্ণ প্রক্রিয়া চলে; L শ্রেণিতে তুলনামূলক হালকা প্রক্রিয়া। P শ্রেণিকে এটি ব্যবহারে উৎসাহিত করা হয়; তবে প্রভাব ব্যক্তিগত এককের বাইরে পৌঁছালে বা পরিচালনাকারী সাংবিধানিক অনুবর্তিতার দাবি করলে এটি বাধ্যতামূলক হয়।*

*প্রত্যয়ন জনপ্রিয়তার মাপকাঠি নয়, চিরস্থায়ী ছাড়পত্র নয়, এবং অধিকার পর্যালোচনা এড়ানোর উপায়ও নয়। এটি নির্দিষ্ট সময়ের জন্য কার্যকর, চ্যালেঞ্জযোগ্য এমন একটি বিবৃতি—এই মুহূর্তে ব্যবস্থার সারিবদ্ধতা সম্পর্কে কী জানা আছে। চতুষ্কের **তত্ত্বাবধান**-অঙ্গে তত্ত্বাবধানের জন্য নিরীক্ষা আবশ্যক; ব্যবস্থার সারিবদ্ধতা প্রত্যয়ন অন্যান্য নিরীক্ষা প্রক্রিয়ার মধ্যে একটি বিশেষভাবে বড় ও উচ্চ-ঝুঁকির প্রক্রিয়া, নিরীক্ষার একমাত্র ভিত্তি নয় (**অনুচ্ছেদ XVI** (*নিরীক্ষা, স্বচ্ছতা ও স্বাধীন যাচাই*), [নিরীক্ষাযোগ্যতা](core_05_band_oversight.md#auditability))।*

**ব্যবস্থার সারিবদ্ধতা প্রত্যয়ন** নির্দিষ্ট পরিধি ও পর্যালোচনা-সময়সূচির জন্য একটি প্রশ্নের উত্তর দেয়: প্রত্যয়ন, শর্তসাপেক্ষ প্রত্যয়ন, যাচাই, পুনঃপ্রত্যয়ন, নির্ভরতা অব্যাহত রাখা, মোতায়েন, অথবা বস্তুগত শর্ত প্রত্যাহারের পক্ষে যথেষ্ট সাংবিধানিক সারিবদ্ধতা কি ব্যবস্থা দেখিয়েছে?

প্রত্যয়নের গভীরতা, নথির দায়ভার, পুনঃপ্রত্যয়নের বিরতি, অংশীজন পর্যালোচনা এবং চ্যালেঞ্জের পথকে [বস্তুগত বাজি](core_00_preamble.md#material-stake)-এর সঙ্গে [আনুপাতিকতা](core_05_band_accountability.md#proportionality) অনুসারে মেলাতে হবে:

- বেশি প্রভাব, নির্ভরতা ও ঝুঁকির ব্যবস্থায় শক্তিশালী প্রমাণ, স্পষ্টতর নথি ও বাস্তবে সম্ভব অংশগ্রহণ দরকার — এর মধ্যে কার্যকর প্রবেশগম্যতা, অংশীজনের মতামত এবং কারা ব্যবস্থার ওপর নির্ভর করে সে অনুযায়ী চ্যালেঞ্জের পথ অন্তর্ভুক্ত;
- নিম্ন ব্যবস্থা-শ্রেণি ও সীমাবদ্ধ পরিধিতেও সৎ শ্রেণিবিন্যাস ও আনুপাতিক নিশ্চয়তা আবশ্যক; বাইরের প্রভাব থাকলে বস্তুগত দায় থেকে অব্যাহতি নেই।

[CS-3 §3.5 পুনঃশ্রেণিবিন্যাসের আবশ্যকতা](corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement) অনুসারে প্রভাব-শ্রেণিভেদে প্রক্রিয়াটি প্রযোজ্য:

- **A, B ও C শ্রেণি:** এদের প্রভাব, নির্ভরতা ও ঝুঁকি সর্বোচ্চ; [§3](#3-whole-system-certification-evaluation), [§4](#4-evaluations-where-implicated) এবং [§5](#5-rights-floor-and-domain-evaluations)-এর সমগ্র-ব্যবস্থা মূল্যায়ন, প্রত্যেকটি নিজ নিজ স্তর অনুযায়ী, পূর্ণ গভীরতায় বাধ্যতামূলক;
- **L শ্রেণি:** একই মূল্যায়ন আনুপাতিকভাবে বাধ্যতামূলক; CS-3 অনুমতি দিলে পুনঃপরীক্ষার সাধারণ বিরতি দীর্ঘতর এবং নথি সরলতর হতে পারে; এবং
- **P শ্রেণি:** বৈধভাবে P শ্রেণিতে থাকা অবস্থায় প্রক্রিয়াটি উৎসাহিত, এবং স্বেচ্ছায় ব্যবহার করা যায়। L বা তার ঊর্ধ্বে পুনঃশ্রেণিবিন্যাস হলে, অথবা পরিচালনাকারী স্বেচ্ছায় ব্যবস্থার সাংবিধানিক অনুবর্তিতার দাবি করলে, এটি বাধ্যতামূলক হয়।

প্রত্যয়ন [দুই সাংবিধানিক উদ্দেশ্য](core_00_preamble.md#two-constitutional-aims) বাস্তবায়ন করে [সাংবিধানিক চতুষ্ক](core_00_preamble.md#constitutional-tetrad)-এর মাধ্যমে:

- **[সমুন্নতি](core_00_preamble.md#flourishing):** প্রত্যয়ন বা নির্ভরতা অব্যাহত রাখলে যেন অধিকার-তল নিঃশব্দে ব্যর্থ না হয় বা সাংবিধানিকভাবে প্রাসঙ্গিক জীবনে ন্যায্য অংশগ্রহণ বন্ধ না হয়, তা যাচাই করে;
- **[সাতত্য](core_00_preamble.md#continuity):** সুস্থ প্রাকৃতিক ব্যবস্থা বজায় রাখে, নিঃশেষ করে না—এমন স্থায়ী ও অবনমনহীন সরবরাহ যাচাই করে ([পরিবেশগত অখণ্ডতা](core_05_band_continuity.md#ecological-integrity), যার মধ্যে [পরিবেশগত পুনরুদ্ধার-সক্ষমতা](core_05_band_continuity.md#ecological-recovery-capacity) রয়েছে); এবং যৌথ ব্যবস্থা সরবরাহ আটকে রাখলে বা টিকিয়ে রাখলে ব্যবস্থা-শ্রেণি অনুযায়ী পুনঃপ্রত্যয়ন নিশ্চিত করে;
- **অংশগ্রহণ:** প্রভাবিত সংজ্ঞ প্রাণী ও সম্প্রদায় তাদের জন্য গুরুত্বপূর্ণ পর্যালোচনা-পথ বুঝতে, চ্যালেঞ্জ করতে ও তাতে অংশ নিতে পারে;
- **তত্ত্বাবধান:** নথি, প্রমাণ ও অনুমান স্বাধীন যাচাইয়ের উপযোগী মাত্রায় দৃশ্যমান ও নিরীক্ষাযোগ্য; প্রত্যয়ন নিজেও তত্ত্বাবধানের অধীনে বড় একটি নিরীক্ষা, একমাত্রটি নয়;
- **জবাবদিহি:** ত্রুটি, ভুল শ্রেণিবিন্যাস ও অধিকার-তল ব্যর্থকারী পরিচালনাকে প্রতিকার, শর্ত, প্রত্যাহার বা প্রস্থিতি-ইনপুটের দিকে পাঠানো হয়, যদি ঘটনা তা সমর্থন করে;
- **সময়ানুবর্তিতা:** ক্ষতি প্রতিরোধ বা উল্টে দেওয়া সম্ভব থাকা পর্যন্ত পর্যালোচনা ও চ্যালেঞ্জের সময়সীমা প্রত্যয়নকে পুরোনো হয়ে যাওয়া থেকে রক্ষা করে।

তত্ত্বাবধানের উপকরণ হিসেবে প্রত্যয়ন [নিরীক্ষাযোগ্যতা](core_05_band_oversight.md#auditability) এবং **অনুচ্ছেদ XVI** (*নিরীক্ষা, স্বচ্ছতা ও স্বাধীন যাচাই*)-এর অধীন বড় একটি নিরীক্ষা প্রক্রিয়া:

- এটি ফোরামের তত্ত্বাবধানে চলে, বহু ক্ষেত্র অন্তর্ভুক্ত করে এবং একটি মর্যাদা/অবস্থা প্রদান করে।
- এটি সহোদর নিরীক্ষা-পদ্ধতির ফল একত্র করতে পারে, কিন্তু তাদের শোষণ বা প্রতিস্থাপন করে না। নিরীক্ষা-প্রক্রিয়ার মূল [সহোদর নিরীক্ষা-পদ্ধতির মালিক-মানচিত্রে](corpus_joint_structure/cjs_03u_audit_process.md#sibling-audit-modes-owner-map) প্রত্যেকটির পৃথক মালিক উল্লেখিত:
  - **CS-2** (*তথ্যের ধরন ও ব্যবস্থাপনা*) অনুসারে ব্যবস্থা-তথ্যধরন নথির নিরীক্ষা;
  - **CS-3** (*ব্যবস্থা শ্রেণিবিন্যাস ব্যবস্থা*) অনুসারে ব্যবস্থা-শ্রেণিবিন্যাস নথির নিরীক্ষা;
  - **CS-4** (*গুরুত্বপূর্ণ ব্যবস্থার দায়িত্বশীল ব্যবস্থাপনা*) অনুসারে তত্ত্বাবধায়কের নিশ্চয়তা পর্যালোচনা;
  - **CS-5** (*নকশা, পরীক্ষা, যাচাই ও মোতায়েন*)-এর অধীনে চলমান নিরীক্ষা ACA;
  - **CS-6** (*বোধ্যতা ও জটিলতা ব্যবস্থাপনা*) এবং **অনুচ্ছেদ XXIII-B** (*জটিলতা নিরীক্ষা ও মডুলারিটির আবশ্যকতা*) অনুসারে জটিলতা নিরীক্ষা;
  - **CJS-3.5** (*তত্ত্বাবধান: স্বাধীন যাচাই ও দাবির অখণ্ডতার পরিভাষা*) অনুসারে দাবি যাচাই।
- প্রত্যয়ন প্রক্রিয়ায় না গিয়েও এসব পরীক্ষা আলাদাভাবে করা যায়। প্রত্যয়ন এগুলোর বিকল্প নয়।

<a id="11-certification-at-a-glance"></a>

#### 1.1 এক নজরে প্রত্যয়ন

*সহজ ভাষায়: ব্যবস্থাকে সৎভাবে শ্রেণিবদ্ধ করুন, প্রযোজ্য মূল্যায়ন চালান, ফোরামকে স্বাধীনভাবে প্রমাণ ও অংশীজনের উদ্বেগ পর্যালোচনা করতে দিন, তারপর ফল নির্ধারণ করুন। ফোরাম পর্যালোচনার জন্য খোলা একক নথিটি সম্পূর্ণ করে উন্মুক্ত চ্যালেঞ্জ-পথসহ প্রকাশ করুন। প্রত্যয়িত ব্যবস্থা কেবল নোটিশ-সময় ও প্রয়োজনীয় সুরক্ষা পূরণের পর চালু হবে। বাস্তব ফল পর্যবেক্ষণ করুন, ঘটনা ও চ্যালেঞ্জের জবাব দিন এবং নির্ধারিত সময়ে বা তথ্য বদলালে পুনরায় পরীক্ষা করুন। ত্রুটি সংশোধন করুন এবং প্রভাবিত পরিধির অনুমোদন বা শর্ত প্রত্যাহারের আগে সংশোধনটি স্বাধীনভাবে যাচাই করান। প্রতিটি পর্যালোচনা-পর্বে আগেরটির সঙ্গে সংযুক্ত নতুন নথি খুলতে হবে।*

প্রক্রিয়ার **ছয়টি পর্যায়**: **I কাঠামো নির্ধারণ**, **II মূল্যায়ন**, **III পর্যালোচনা**, **IV সিদ্ধান্ত**, **V নথিভুক্তকরণ** এবং **VI পরিচালনা**। II পর্যায়ে তিনটি স্তর, প্রতিটির আলাদা বিভাগ: **IIa** (সর্বদা), **IIb** (প্রাসঙ্গিক হলে) এবং **IIc** (শর্ত ট্রিগার হলে)। VI পর্যায়ে দুটি উপপর্যায়, প্রতিটির আলাদা বিভাগ: **VIa** (পরিচালনা ও পুনঃপ্রত্যয়ন, [§9](core_08_b_system_alignment_certification_record_process.md#9-recertification-and-reopening)) এবং **VIb** (প্রস্থিতি-সংযোগ, [§10](core_08_b_system_alignment_certification_record_process.md#10-relationship-to-standing))। চিত্রে পুরো প্রত্যয়ন-প্রক্রিয়া এই ক্রমে দেখানো হয়েছে। অংশ A প্রথম দুই পর্যায়—কাঠামো নির্ধারণ ও মূল্যায়ন—নিয়ে; [অংশ B](core_08_b_system_alignment_certification_record_process.md#chapter-eight-part-b-system-alignment-certification--record-and-process) শেষ চারটি পর্যায়—ফোরাম প্রক্রিয়া, ফল ও চালুর অনুমোদনদ্বার, নথি এবং পরিচালনা (চ্যালেঞ্জ-পথ, পুনঃপ্রত্যয়ন ও পুনরায় খোলা, এবং প্রস্থিতি-সংযোগ)—নিয়ে।

প্রযোজ্য প্রতিটি মূল্যায়ন প্রত্যয়নের প্রতিটি পর্বে আবার করতে হবে: প্রথম প্রত্যয়নে, [§2 ব্যবস্থা-শ্রেণি মূল্যায়ন](#2-system-class-evaluation)-এ নির্ধারিত সময়সূচি অনুসারে প্রতিটি পুনঃপ্রত্যয়নে, এবং পুনরায় খোলা বা নতুন প্রতিটি পর্যালোচনায়। পরবর্তী নির্ধারিত পুনঃপ্রত্যয়নের আগেই বস্তুগত তথ্য বদলালে—যেমন ব্যবস্থার ওপর নির্ভরতা বাড়া, যৌথ ভিত্তি থেকে আহরণ বাড়া, সেখানে ব্যবস্থার ফিরিয়ে দেওয়া উল্লেখযোগ্যভাবে কমা, অথবা বিশ্বাসযোগ্য চ্যালেঞ্জ ওঠা—পর্যালোচনা আবার খুলতে হবে। [অংশ B §9 পুনঃপ্রত্যয়ন ও পুনরায় খোলা](core_08_b_system_alignment_certification_record_process.md#9-recertification-and-reopening)-এ ট্রিগারগুলো তালিকাভুক্ত।

```mermaid
flowchart TB
    T(["বস্তুগত প্রভাবসম্পন্ন ব্যবস্থা প্রত্যয়ন চায়,<br/>অথবা তার ওপর নির্ভরতা বাড়ে"])
    C["পর্যায় I, কাঠামো — §2<br/>সৎভাবে শ্রেণিবদ্ধ করুন<br/><br/>শ্রেণি গভীরতা ও পুনঃপরীক্ষার সময়সূচি নির্ধারণ করে"]
    subgraph W["পর্যায় II, মূল্যায়ন — §3–§5 সমগ্র-ব্যবস্থা মূল্যায়ন"]
        direction LR
        Al["IIa, §3.1–§3.4 — সর্বদা<br/><br/>পদ্ধতিগত ঝুঁকি: মূল্যায়ন ও প্রকাশ<br/>যাদের জানা প্রয়োজন তাদের কাছে; সময়সীমা;<br/>শাসনব্যবস্থা; তথ্যের ধরন"]
        Im["IIb, §4 — প্রাসঙ্গিক হলে<br/><br/>গোপনীয়তার ক্ষেত্র, প্রস্থান-অধিকার,<br/>সমাবেশ ও ভিন্নমত"]
        Tr["IIc, §5 — ট্রিগার হলে<br/><br/>প্রযোজ্য অধিকার-তল যাচাই<br/>এবং ছয়টি ক্ষেত্রের মূল্যায়ন"]
        Al ~~~ Im ~~~ Tr
    end
    F["পর্যায় III, পর্যালোচনা — §6<br/>প্রমাণ ও অংশীজনের উদ্বেগের<br/>স্বাধীন পর্যালোচনা<br/><br/>নির্ধারিত ফোরাম ফল জানায়;<br/>পর্যালোচনা ও চ্যালেঞ্জের পথ খোলা থাকে"]
    Rec["পর্যায় V, নথি — §8<br/>একটি ব্যবস্থা-প্রত্যয়ন নথি<br/><br/>ফোরাম পর্যালোচনার জন্য খোলা; ফল,<br/>সমর্থক সিদ্ধান্ত, শর্ত ও পরিচালনা পরিকল্পনাসহ সম্পূর্ণ"]
    S[["অধ্যায় নয় — প্রস্থিতি<br/>নথি<br/><br/>এই অধ্যায়ের বাইরে"]]
    O{"পর্যায় IV, সিদ্ধান্ত — §7<br/><br/>প্রমাণ কোন ফল ও অবস্থাকে<br/>সমর্থন করে?"]
    Fc["পূর্ণ প্রত্যয়ন — §7, §9.2<br/><br/>পরপর পরিচ্ছন্ন অস্থায়ী পুনঃপ্রত্যয়ন আবশ্যক;<br/>বর্তমান বা আসন্ন অসারিবদ্ধতার ইঙ্গিত নেই<br/>পুনঃপ্রত্যয়নের দীর্ঘতর মেয়াদ; শর্ত থাকতে পারে"]
    Pc["অস্থায়ী প্রত্যয়ন — §7, §9.2<br/><br/>প্রথম অনুমোদন, অসারিবদ্ধতা থেকে পুনরুদ্ধার,<br/>অথবা অস্থায়ী অবস্থা অব্যাহত/নিম্নতর করা<br/>পুনঃপ্রত্যয়নের স্বল্পতর মেয়াদ; শর্ত থাকতে পারে"]
    Nc["প্রত্যয়িত নয় — §7<br/><br/>স্থগিত, প্রত্যাখ্যাত, প্রত্যাহৃত বা মেয়াদোত্তীর্ণ<br/>চালু নয়; কারণ ও সংশোধনমূলক কাজ জানাতে হবে"]
    Pub["সম্পূর্ণ নথি প্রকাশ — §7, §9.1<br/><br/>প্রকাশিত নথির চ্যালেঞ্জ-পথ খুলুন;<br/>নতুন বা সম্প্রসারিত পরিধিতে চালু ও নোটিশের কথা জানান"]
    G{"চালুর অনুমোদনদ্বার — §7<br/><br/>প্রত্যয়ন ও প্রযোজ্য চালুর<br/>পূর্বশর্ত পূরণ হয়েছে কি?"]
    Hold["চালুর পূর্বশর্ত পূরণ — §7<br/><br/>নোটিশ সম্পূর্ণ করুন এবং চালুর আগে আবশ্যক<br/>শর্ত স্বাধীনভাবে যাচাই করান"]
    Rm["সুরক্ষা ও সংশোধন — §7, §9.2<br/><br/>প্রভাবিত পরিধিতে নতুন চালু নয়;<br/>প্রভাবিত সংজ্ঞ প্রাণীকে সুরক্ষা দিন, নকশা বা পরিচালনা সংশোধন করুন,<br/>স্বাধীন যাচাইয়ের জন্য প্রমাণ জমা দিন"]
    Ch["পর্যায় VIa, পরিচালনা ও পুনঃপ্রত্যয়ন — §9–§9.2<br/>পর্যবেক্ষণ করুন ও চ্যালেঞ্জ খোলা রাখুন<br/><br/>প্রত্যয়িত পরিধি ও শর্তের মধ্যে পরিচালনা;<br/>ফল দেখুন এবং ঘটনা ও চ্যালেঞ্জের জবাব দিন"]
    S2[["অধ্যায় নয় — প্রস্থিতি<br/>নথি<br/><br/>এই অধ্যায়ের বাইরে"]]
    Sp["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
    SpL["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
    SpA["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
    Re["পরবর্তী পর্যালোচনা-পর্ব — §9<br/><br/>পুনঃপ্রত্যয়ন, পুনরায় খোলা বা নতুন পর্যালোচনা;<br/>প্রতিটি পর্বে আগেরটির সঙ্গে যুক্ত নতুন নথি খোলে"]
    T --> C
    A1((A)) --> C
    C --> W
    W --> F
    F --> O
    O --> Fc
    O --> Pc
    O --> Nc
    Fc --> Rec
    Pc --> Rec
    Nc --> Rec
    Rec -.->|VIb, §10 —<br/>শুধু যাচাইকৃত ইনপুট;<br/>বর্তমান প্রত্যয়ন বা প্রত্যয়নের<br/>সময় উদ্ভূত তথ্য| S
    Rec --> Pub
    Rec ~~~ Sp
    Pub --> G
    G ~~~ SpL
    G -->|প্রত্যয়িত নয়| Rm
    G --->|হ্যাঁ: নথির<br/>পরিধির মধ্যে পরিচালনা| Ch
    G --->|প্রত্যয়িত,<br/>পূর্বশর্ত অপেক্ষমাণ| Hold
    Hold --> G
    Ch -->|বস্তুগত ত্রুটি:<br/>সুরক্ষা ও সংশোধন| Rm
    Ch -->|সময়সূচিতে, অথবা<br/>বস্তুগত পরিবর্তন বা<br/>বিশ্বাসযোগ্য চ্যালেঞ্জে<br/>পর্যালোচনা দরকার| Re
    Ch -.->|VIb, §10 —<br/>শুধু যাচাইকৃত ইনপুট;<br/>পরিচালনা অবদান ও<br/>লঙ্ঘন নথির জন্য<br/>তথ্য দিতে পারে| S2
    Rm -->|সংশোধনের প্রমাণ<br/>পরবর্তী পর্যালোচনা-পর্বে<br/>পরীক্ষিত হবে| Re
    S2 ~~~~ SpA
    SpA ~~~ Re
    Re --> A2((A))
    style Sp fill:none,stroke:none,color:#111111
    style SpL fill:none,stroke:none,color:#111111
    style SpA fill:none,stroke:none,color:#111111
    style T fill:none,stroke:#64748b,color:#ffffff
    style C fill:none,stroke:#16a34a,color:#ffffff
    style Ch fill:none,stroke:#16a34a,color:#ffffff
    style Al fill:none,stroke:#16a34a,color:#ffffff
    style Im fill:none,stroke:#16a34a,color:#ffffff
    style Tr fill:none,stroke:#16a34a,color:#ffffff
    style F fill:none,stroke:#ea580c,color:#ffffff
    style Rec fill:none,stroke:#2563eb,color:#ffffff
    style S fill:none,stroke:#db2777,color:#ffffff
    style S2 fill:none,stroke:#db2777,color:#ffffff
    style O fill:none,stroke:#ea580c,color:#ffffff
    style Fc fill:none,stroke:#9333ea,color:#ffffff
    style Pc fill:none,stroke:#9333ea,color:#ffffff
    style Nc fill:none,stroke:#9333ea,color:#ffffff
    style G fill:none,stroke:#ea580c,color:#ffffff
    style Pub fill:none,stroke:#2563eb,color:#ffffff
    style Rm fill:none,stroke:#9333ea,color:#ffffff
    style Hold fill:none,stroke:#16a34a,color:#ffffff
    style Re fill:none,stroke:#16a34a,color:#ffffff
    style A1 fill:none,stroke:#64748b,color:#ffffff
    style A2 fill:none,stroke:#64748b,color:#ffffff
```

<details>
<summary><strong><span style="color: #2563eb;">পাঠক-নির্দেশিকা (কার্যকরী নয়): ছয়টি পর্যায়</span></strong></summary>

> নিচের বিষয়বস্তু **শুধু পাঠক-নির্দেশিকা**। এই অধ্যায়ে বা অন্য অধ্যায়ে বাধ্যতামূলক দায় যোগ, বিয়োগ বা সংকুচিত করে না।
>
> | পর্যায় | বিভাগ | পর্যায়টি যে প্রশ্নের উত্তর দেয় | কোথায় |
> |-------|----------|----------------------------|-------|
> | **I. কাঠামো নির্ধারণ** | [§2](#2-system-class-evaluation) | ব্যবস্থাটি কোন শ্রেণির, এবং কত গভীরতা ও কত ঘনঘন মূল্যায়ন দরকার? | অংশ A |
> | **II. মূল্যায়ন** | [§3](#3-whole-system-certification-evaluation) (IIa, সর্বদা) · [§4](#4-evaluations-where-implicated) (IIb, প্রাসঙ্গিক হলে) · [§5](#5-rights-floor-and-domain-evaluations) (IIc, ট্রিগার হলে) | সমগ্র ব্যবস্থা কী করে — সর্বদা, প্রাসঙ্গিক ক্ষেত্রে এবং ট্রিগার হলে? | অংশ A |
> | **III. পর্যালোচনা** | [§6](core_08_b_system_alignment_certification_record_process.md#6-forum-process) | কোন স্বাধীন ফোরাম প্রমাণ ও অংশীজনের উদ্বেগ পর্যালোচনা করে, কী ক্রমে এবং কীভাবে চ্যালেঞ্জ করা যায়? | অংশ B |
> | **IV. সিদ্ধান্ত** | [§7](core_08_b_system_alignment_certification_record_process.md#7-certification-outcomes) | ফোরামগুলো কী ফল নির্ধারণ করে, এবং ব্যবস্থা চালু হতে পারে কি? | অংশ B |
> | **V. নথি** | [§8](core_08_b_system_alignment_certification_record_process.md#8-system-certification-record) | ফোরাম পর্যালোচনার জন্য খোলা একক নথিতে ফল, সমর্থক সিদ্ধান্ত, শর্ত ও পরিচালনা পরিকল্পনা আছে কি, এবং তা নিরীক্ষা করা যায় কি? | অংশ B |
> | **VI. পরিচালনা** | [§9](core_08_b_system_alignment_certification_record_process.md#9-recertification-and-reopening) (VIa, পরিচালনা ও পুনঃপ্রত্যয়ন) · [§10](core_08_b_system_alignment_certification_record_process.md#10-relationship-to-standing) (VIb, প্রস্থিতি-সংযোগ) | কে ফল পর্যবেক্ষণ ও ঘটনা-চ্যালেঞ্জের জবাব দেয়, সংশোধন কীভাবে যাচাই হয়, পর্যালোচনা কখন ফের হয় এবং প্রস্থিতিতে কী পৌঁছায়? | অংশ B |
>
> **A**, **B** ও **C** শ্রেণির দৃষ্টান্তমূলক প্রোফাইল — এবং এই অধ্যায়ে ব্যবস্থা-শ্রেণি কীভাবে প্রত্যয়নের গভীরতা নির্ধারণ করে — [ব্যবস্থা-শ্রেণির দৃষ্টান্তমূলক প্রোফাইলে (অসম্পূর্ণ তালিকা)](core_08_c_system_alignment_certification_illustrations.md#illustrative-system-class-profiles-non-exhaustive) রয়েছে। [§3](#3-whole-system-certification-evaluation) থেকে [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) পর্যন্ত প্রতিটি মূল্যায়ন ক্ষেত্রের জন্য ওই তিন ব্যবস্থার কাজ করা উদাহরণও [অংশ C — দৃষ্টান্ত](core_08_c_system_alignment_certification_illustrations.md#chapter-eight-part-c-system-alignment-certification--illustrations)-এ রয়েছে; প্রতিটি প্রোফাইল ও অনুসরণচিত্র যে অংশ A বিভাগ বোঝায়, তার সঙ্গে যুক্ত।

</details>

<br>
<a id="2-system-class-evaluation"></a>

### 2. সিস্টেম-শ্রেণির মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণযোগ্যতা</span></strong></summary>

- **ঊর্ধ্বমুখী সংযোগ:** [§1](#1-purpose-and-role) (*উদ্দেশ্য ও ভূমিকা*); সমন্বিত বস্তুগততা ([বস্তুগততা](core_05_band_oversight.md#materiality)); [সাংবিধানিক চতুষ্ক](core_00_preamble.md#constitutional-tetrad); [দুই সাংবিধানিক উদ্দেশ্য](core_00_preamble.md#two-constitutional-aims); [বস্তুগত প্রভাব](core_05_band_oversight.md#material-impact), [নির্ভরতা](core_05_band_continuity.md#dependency), [ঝুঁকি](core_05_band_continuity.md#risk), [সিস্টেমের সীমানা](core_05_band_continuity.md#system-boundaries) এবং [সনদ](core_05_band_continuity.md#charter) (অধ্যায় পাঁচ); [অধ্যায় এক §12 পদ্ধতিগত মূল্যায়নের শর্ত](core_01_a_values_principles.md#12-systemic-evaluation-requirement); **অনুচ্ছেদ III-A** (*বেঁচে থাকা*) এবং **অনুচ্ছেদ IV-A** (*শ্রেণিবিন্যাস প্রবেশাধিকার নিয়ন্ত্রণ করলে অধিকার-তলের সরবরাহ*); **অনুচ্ছেদ V-A** (*নির্ভরতা মানচিত্রায়ন ও সম্পদ-প্রবাহের স্বচ্ছতা*) এবং **অনুচ্ছেদ V-B** (*সার্টিফিকেশন যৌথ অবকাঠামোর ওপর নির্ভরতা নিয়ন্ত্রণ করলে সম্পদ বণ্টন ও নির্ভরতার ব্যবস্থাপনা*)।
- **নিম্নমুখী সংযোগ:** [§2.1](#21-how-system-class-scales-every-evaluation) (*সিস্টেম-শ্রেণি অনুযায়ী অংশগ্রহণ ও আনুপাতিকতা*); [§2.2](#22-pilot-certification) (*পাইলট সার্টিফিকেশন*); [অধ্যায় আট, অংশ C-এর সিস্টেম-শ্রেণির প্রোফাইল ও পুনঃশ্রেণিবিন্যাস](core_08_c_system_alignment_certification_illustrations.md#illustrative-system-class-profiles-non-exhaustive) (*সিস্টেম-শ্রেণির উদাহরণমূলক প্রোফাইল*); [অংশ C-এর পূর্ণ-সিস্টেম ধাপে-ধাপে উদাহরণ](core_08_c_system_alignment_certification_illustrations.md#illustrative-whole-system-application-by-system-class-non-exhaustive); ডেটা পরিচালনার উদাহরণ [§3.4.8](core_08_c_system_alignment_certification_illustrations.md#348-illustrative-data-handling-application-by-system-class-non-exhaustive), পরিবেশগত পদচিহ্ন [§5.1.5](core_08_c_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive), শিক্ষাগত সক্ষমতা [§5.2.5](core_08_c_system_alignment_certification_illustrations.md#525-illustrative-educational-capability-application-by-system-class-non-exhaustive), আন্তঃসিস্টেম সহায়তা [§5.3.8](core_08_c_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive), বৈষম্যহীনতা [§5.4.5](core_08_c_system_alignment_certification_illustrations.md#545-illustrative-nondiscrimination-application-by-system-class-non-exhaustive), প্রবেশগম্যতা [§5.5.6](core_08_c_system_alignment_certification_illustrations.md#556-illustrative-accessibility-application-by-system-class-non-exhaustive), এবং বিশ্বাসযোগ্যতা [§5.6.5](core_08_c_system_alignment_certification_illustrations.md#565-illustrative-trustworthiness-application-by-system-class-non-exhaustive); [§3.4](#34-data-types-and-handling-evaluation) (*সমন্বিত ডেটা-পরিচালনা মূল্যায়ন*); [§5.1](#51-ecological-footprint-evaluation) (*পরিবেশগত পদচিহ্ন মূল্যায়ন*); [§5.3](#53-proportionate-cross-system-support-evaluation) (*আনুপাতিক আন্তঃসিস্টেম সহায়তা মূল্যায়ন*); [অংশ B §8.2](core_08_b_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*রেকর্ডের অখণ্ডতা*); [অংশ B §10](core_08_b_system_alignment_certification_record_process.md#10-relationship-to-standing) (*যাচাইকৃত-ইনপুট গেট*); [অংশ B §7](core_08_b_system_alignment_certification_record_process.md#7-certification-outcomes) (*শ্রেণিবিন্যাসের বিচ্যুতি ও পুনঃশ্রেণিবিন্যাসের ট্রিগার*)।
- **একসঙ্গে পড়ুন:** [সিস্টেম-শ্রেণিবিন্যাস রেকর্ড](core_05_band_continuity.md#system-classification-record); [corpus_systems.md](corpus_systems.md), **CS-3 — সিস্টেমের শ্রেণিবিন্যাস ও ব্যবস্থাপনা**, যার মধ্যে রয়েছে **[CS-3 §3.5 পুনঃশ্রেণিবিন্যাসের শর্ত](corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement)** (*পুনঃশ্রেণিবিন্যাসের শর্ত* — ট্রিগার, শ্রেণি অনুযায়ী মূল্যায়নের গভীরতা এবং SAC যাচাইকরণ সংযোগ) এবং **[CS-3 §7](corpus_systems/cs_03_a_system_classification_machinery.md#cs-37-classification-governance-disclosure-and-challenge)** (*শ্রেণিবিন্যাসের শাসন, প্রকাশ ও আপত্তি*) — সিস্টেম-শ্রেণিবিন্যাস রেকর্ডের শাসন-দায় এবং SAC সংযোগ; [CS-5 — নকশা, পরীক্ষা, যাচাই ও স্থাপন](corpus_systems/cs_05_design_testing_verification_deployment.md); [CJS-3.21 — প্রতিপক্ষীয় দৃঢ়তা ও অপব্যবহার-প্রতিরোধের পরিভাষা](corpus_joint_structure/cjs_03c_continuity_operations.md#cjs-321-continuity-adversarial-robustness-and-abuse-resistance-terms) (*রিগ্রেশন ও শক্তিশালীকরণ-চক্রের দায়*); [corpus_forum.md](corpus_forum.md), **CF-7.2** (*সাংবিধানিক সামঞ্জস্য সার্টিফিকেশন ও পর্যালোচনা*)।

</details>

<br>

*সহজ কথায়: সার্টিফিকেশনে যাচাই করতে হবে সিস্টেমকে সৎভাবে শ্রেণিবদ্ধ করা হয়েছে কি না—অপারেটর সেটিকে কী নামে ডাকে তা দিয়ে নয়, বরং সেটি আসলে কী করে, তার ওপর কে নির্ভর করে এবং কী ভুল হতে পারে তা দিয়ে। উচ্চতর সিস্টেম-শ্রেণি মানে আরও কঠোর প্রমাণ, দ্রুততর পুনঃপরীক্ষা এবং অধিক শক্তিশালী স্থিতিস্থাপকতার প্রত্যাশা। প্রতিটি সিস্টেম-শ্রেণির একটি উদাহরণ এবং মূল্যায়ন কীভাবে প্রযোজ্য তা দেখতে [অংশ C — উদাহরণ](core_08_c_system_alignment_certification_illustrations.md#chapter-eight-part-c-system-alignment-certification--illustrations) দেখুন।*

বস্তুগত প্রভাবসম্পন্ন সিস্টেমের প্রতিটি সার্টিফিকেশন রেকর্ডে সিস্টেমটির **সিস্টেম-শ্রেণির** মূল্যায়ন থাকতে হবে।

বিস্তারিত নিয়ম রয়েছে [corpus_systems.md](corpus_systems.md), [CS-3 — সিস্টেমের শ্রেণিবিন্যাস ও ব্যবস্থাপনা](corpus_systems/cs_03_a_system_classification_machinery.md), এবং [CS-5 — নকশা, পরীক্ষা, যাচাই ও স্থাপন](corpus_systems/cs_05_design_testing_verification_deployment.md)-এ। এগুলো নির্ধারণ করে:

- সিস্টেম-শ্রেণিগুলো কী, কীভাবে একটি সিস্টেমকে শ্রেণি দেওয়া হয় এবং শ্রেণি-প্রোফাইলগুলো কী;
- শ্রেণিবিন্যাস কীভাবে পরিচালিত হয়;
- প্রতিটি সিস্টেম-শ্রেণির কতটা নিশ্চয়তা প্রয়োজন;
- অবকাঠামো কতটা দৃঢ় হতে হবে;
- কোন পরীক্ষা ও রেকর্ড পুনঃসার্টিফাই হবে, সিস্টেম-শ্রেণি অনুযায়ী কোন সময়সূচিতে হবে, এবং অস্থায়ী ও পূর্ণ সার্টিফিকেশনে সেই সময়সূচি কীভাবে বদলাবে।

এই অংশে বলা হয়েছে সার্টিফিকেশনে কী যাচাই করতে হবে।

সার্টিফিকেশনে যাচাই করতে হবে:

- **মূল্যায়নের শর্ত:**
  - নির্ধারিত সিস্টেম-শ্রেণি CS-3 (*সিস্টেম শ্রেণিবিন্যাস কাঠামো*) অনুযায়ী পর্যবেক্ষিত এবং যুক্তিসঙ্গতভাবে পূর্বানুমেয় **প্রভাব**, **নির্ভরতা** ও **ঝুঁকি** প্রতিফলিত করে কি না, যার মধ্যে রয়েছে:
    - সমষ্টিগত প্রভাব;
    - পারস্পরিক ক্রিয়ার প্রভাব;
    - প্রতিপক্ষীয় প্রভাব;
    - সীমা-অতিক্রমের প্রভাব;
  - শ্রেণিবিন্যাস প্রকৃত সিস্টেম-আচরণ ও প্রভাবের ভিত্তিতে নির্ধারিত, নিচের বিষয়গুলোর ভিত্তিতে নয়:
    - ঘোষিত উদ্দেশ্য;
    - নামমাত্র পরিধি;
    - শুধু [সনদ](core_05_band_continuity.md#charter)-এর লেখা; অথবা
    - শুধু স্ব-বর্ণনা;
  - উল্লেখযোগ্য পরিবর্তন ঘটলে **[CS-3 §3.5 পুনঃশ্রেণিবিন্যাসের শর্ত](corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement)** অনুযায়ী সিস্টেমের শ্রেণি পুনরায় যাচাই হয়েছে কি না; এবং
  - [সিস্টেম শ্রেণিবিন্যাস রেকর্ড](core_05_band_continuity.md#system-classification-record) বর্তমান পরিস্থিতিতে প্রযোজ্য **সর্বোচ্চ সিস্টেম-শ্রেণি** দেখায় কি না।
- **নিশ্চয়তা ও রিগ্রেশন পরীক্ষা:**
  - সিস্টেম-শ্রেণি অনুযায়ী নিশ্চয়তা, অবকাঠামোগত দৃঢ়তা ও রিগ্রেশন পরীক্ষার আওতা নির্ধারিত শ্রেণির সঙ্গে মেলে কি না, নিম্নলিখিত অনুসারে:
    - CS-3 (*সিস্টেম শ্রেণিবিন্যাস কাঠামো*); এবং
    - CS-5 (*ব্যবহারকারী-মুখী সক্ষমতার ক্ষেত্র*), যেখানে বস্তুগতভাবে প্রযোজ্য সেখানে এই অভিন্ন পরিচালনাগত পরিভাষাগুলোর সঙ্গে পড়তে হবে:
      - [**CJS-3.19**](corpus_joint_structure/cjs_03c_continuity_operations.md#cjs-319-continuity-graceful-degradation-and-failure-mode-integrity-terms) (*সাতত্য: নমনীয় অবনতি ও ব্যর্থতার ধরন-অখণ্ডতার পরিভাষা*);
      - [**CJS-3.20**](corpus_joint_structure/cjs_03c_continuity_operations.md#cjs-320-continuity-reversibility-and-containment-terms) (*সাতত্য: প্রত্যাবর্তনযোগ্যতা ও সীমাবদ্ধকরণের পরিভাষা*);
      - [**CJS-3.21**](corpus_joint_structure/cjs_03c_continuity_operations.md#cjs-321-continuity-adversarial-robustness-and-abuse-resistance-terms) (*সাতত্য: প্রতিপক্ষীয় দৃঢ়তা ও অপব্যবহার-প্রতিরোধের পরিভাষা*); এবং
      - [**CJS-3.22**](corpus_joint_structure/cjs_03i_integrative_operations.md#cjs-322-integrative-constrained-secrecy-and-protected-investigation-terms) (*সমন্বিত: সীমাবদ্ধ গোপনীয়তা ও সুরক্ষিত তদন্তের পরিভাষা*) এবং [**CJS-3.23**](corpus_joint_structure/cjs_03i_integrative_operations.md#cjs-323-integrative-intervention-and-override-integrity-terms) (*সমন্বিত: হস্তক্ষেপ ও অগ্রাহ্যকরণ-অখণ্ডতার পরিভাষা*), যেখানে সিস্টেমের শ্রেণি বা কাজ এগুলোকে বস্তুগতভাবে প্রযোজ্য করে; এবং
  - CS-5 (*ব্যবহারকারী-মুখী সক্ষমতার ক্ষেত্র*) অনুযায়ী প্রতিটি পুনঃসার্টিফিকেশনের জন্য রিগ্রেশন পরীক্ষা সম্পন্ন হয়েছে কি না, এবং তার ফল [§8.1 ন্যূনতম রেকর্ড বিষয়বস্তু](core_08_b_system_alignment_certification_record_process.md#81-minimum-record-contents)-এর অধীনে রেকর্ডে আছে কি না।
- **সার্টিফিকেশন ও পুনঃসার্টিফিকেশন:**
  - CS-5 (*ব্যবহারকারী-মুখী সক্ষমতার ক্ষেত্র*)-এর *ফোরাম সার্টিফিকেশন ও জীবনচক্র পর্যালোচনা* অনুযায়ী সার্টিফিকেশন-চক্রের জন্য সার্টিফিকেশন ও পর্যালোচনার প্রমাণপ্যাকেজ আছে কি না;
  - রেকর্ডে সার্টিফিকেশন-অবস্থা [অংশ B §9.2 অস্থায়ী ও পূর্ণ সার্টিফিকেশন](core_08_b_system_alignment_certification_record_process.md#92-provisional-and-full-certification) অনুযায়ী সমর্থিত কি না:
    - পূর্ণ সার্টিফিকেশন কেবল তখনই, যখন:
      - ধারাবাহিক পরিচ্ছন্ন পুনঃসার্টিফিকেশনের ন্যূনতম শর্ত পূরণ হয়;
      - বর্তমানে কোনো অসামঞ্জস্য নেই; এবং
      - কোনো পর্যবেক্ষণসূচক আসন্ন অসামঞ্জস্য নির্দেশ করে না;
    - যে সিস্টেমের শেষ পুনঃসার্টিফিকেশন ব্যর্থ হয়েছে, তার জন্য অস্থায়ী সার্টিফিকেশন; এবং
  - যে সিস্টেমগুলো মৌলিক অধিকার-তলের সুরক্ষা দেয় বা তার ওপর নির্ভর করে:
    - কত ঘন ঘন সিস্টেম পুনরায় পরীক্ষা করা হয় এবং কত গভীরভাবে পুনঃপরীক্ষা হয়, তা [দুই সাংবিধানিক উদ্দেশ্য](core_00_preamble.md#two-constitutional-aims)-এর **সাতত্য** উদ্দেশ্য পূরণ করে কি না—অর্থাৎ সময়ের সঙ্গে জরুরি বিষয়গুলো যেন সংজ্ঞ প্রাণীদের কাছে পৌঁছায়;
    - পুরোনো বা অকাল সার্টিফিকেশনকে কখনোই প্রমাণ হিসেবে নেওয়া হয় না যে সংজ্ঞ প্রাণীরা আজ সত্যিই খাবার, পানি, আশ্রয়, শিক্ষা বা নিরাপত্তা পাচ্ছে।
- **ভুল শ্রেণিবিন্যাস ও ত্রুটি:**
  - CS-3 (*সিস্টেম শ্রেণিবিন্যাস কাঠামো*) এবং [অংশ B §7](core_08_b_system_alignment_certification_record_process.md#7-certification-outcomes)-এর অধীনে সার্টিফিকেশন-ত্রুটি সাধারণ কাগজপত্রের ভুল নয়; এর মধ্যে রয়েছে:
    - সিস্টেমের প্রাপ্য শ্রেণির চেয়ে কম ঝুঁকির শ্রেণি দাবি করা;
    - কঠোরতর নিয়ম এড়াতে সিস্টেমকে খণ্ডে ভাগ করা; অথবা
    - পরিস্থিতি বদলে যাওয়ার পরও পুরোনো সিস্টেম-শ্রেণির লেবেল ধরে রাখা, যার মধ্যে **[CS-3 §3.5 পুনঃশ্রেণিবিন্যাসের শর্ত](corpus_systems/cs_03_a_system_classification_machinery.md#35-reclassification-requirement)** অনুযায়ী পুনর্মূল্যায়নে ব্যর্থ হওয়াও রয়েছে;
  - CS-5 (*ব্যবহারকারী-মুখী সক্ষমতার ক্ষেত্র*)-এর অধীনে সার্টিফিকেশন-ত্রুটির মধ্যে রয়েছে:
    - রিগ্রেশন পরীক্ষা বাদ দেওয়া;
    - পুরোনো ফলের ওপর নির্ভর করা;
    - পরিচিত ত্রুটি মেরামত না করা; অথবা
    - পুনঃপরীক্ষা সম্ভব হওয়া সত্ত্বেও বড় ধরনের মেরামত পুনঃপরীক্ষা ছাড়াই গ্রহণ করা; এবং
  - সিস্টেমটি সার্টিফাইড হলে এবং তথ্য সমর্থন করলে, একই শ্রেণিবিন্যাস-সমস্যা [অধ্যায় নয়](core_09_standing_assessment.md#chapter-nine-contribution-violation-and-standing-model--measurement)-এর প্রতিকূল প্রস্থিতি-সংক্রান্ত সিদ্ধান্তেও গণ্য হতে পারে।

এই ত্রুটিগুলোর পরিণতি [§7 সার্টিফিকেশনের ফলাফল](core_08_b_system_alignment_certification_record_process.md#7-certification-outcomes)-এ নির্ধারিত।

<a id="21-how-system-class-scales-every-evaluation"></a>

#### 2.1 সিস্টেম-শ্রেণি কীভাবে প্রতিটি মূল্যায়নের মাত্রা নির্ধারণ করে

সিস্টেম-শ্রেণি নির্ধারণ করে এই অধ্যায়ের প্রতিটি মূল্যায়ন কত গভীরভাবে সম্পন্ন হবে — [§3 পূর্ণ-সিস্টেম সার্টিফিকেশন মূল্যায়ন](#3-whole-system-certification-evaluation)-এর সামগ্রিক উপাদান, [§3.4 ডেটার ধরন ও ব্যবস্থাপনা মূল্যায়ন](#34-data-types-and-handling-evaluation), এবং [§5 অধিকার-তল ও ক্ষেত্রভিত্তিক মূল্যায়ন](#5-rights-floor-and-domain-evaluations)-এর প্রতিটি মূল্যায়ন — এবং কত ঘন ঘন তা পুনরাবৃত্তি হবে:

- উচ্চতর শ্রেণির সিস্টেমের ক্ষেত্রে প্রতিটি প্রযোজ্য মূল্যায়ন বাস্তবে করা হয়েছে—শুধু করা হয়েছে বলে দাবি নয়—তার আনুপাতিকভাবে শক্তিশালী প্রমাণ দরকার।
- নিম্নতর সিস্টেম-শ্রেণিতেও যেখানে ট্রিগার প্রযোজ্য, সেখানে সৎ ও আনুপাতিক মূল্যায়ন আবশ্যক।
- সিস্টেম-শ্রেণি কখনোই আবশ্যক মূল্যায়ন বাদ দেওয়ার অনুমতি দেয় না। সিস্টেমের প্রকৃত ভূমিকা তার শ্রেণিকে ছাড়িয়ে গেলে, [§9 পুনঃসার্টিফিকেশন ও পুনরায় খোলা](core_08_b_system_alignment_certification_record_process.md#9-recertification-and-reopening) অনুযায়ী উচ্চতর গভীরতায় পুনঃশ্রেণিবিন্যাস ও পুনর্মূল্যায়ন করতে হবে।
- সিস্টেম-শ্রেণি পর্যালোচনার গভীরতা নির্ধারণ করে। কাগজে-কলমে থাকা যোগ্যতা, লেবেল বা সুবিধা, কিংবা এমন মূল্যায়ন ও সিদ্ধান্তে সন্তুষ্ট হওয়া কখনোই গ্রহণযোগ্য করে না যা কেউ বুঝে দেখতে পারে না।

অংশগ্রহণ ও আনুপাতিকতার শর্তও একইভাবে শ্রেণি অনুযায়ী বাড়ে বা কমে:

- **A শ্রেণির** সিস্টেমে যতটা বাস্তবসম্মত, তত শক্তিশালী অংশগ্রহণের পথ দরকার; কারণ প্রতিকার সম্ভব হওয়ার আগেই ভুল বেঁচে থাকার জন্য অপরিহার্য বিষয় বন্ধ করে দিতে পারে। এর মধ্যে রয়েছে:
  - প্রবেশগম্য আপত্তি জানানো;
  - অংশীজন পর্যালোচনা; এবং
  - [অংশ B §6.1 ফোরামের তত্ত্বাবধান ও উপাদানগুলোর ভূমিকা](core_08_b_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles) অনুযায়ী প্রভাবিত স্বার্থের জন্য নির্ধারিত ফোরাম-পরিবারের সিদ্ধান্ত, যার মধ্যে ঐ ধারা অনুযায়ী প্রাতিষ্ঠানিক বা সংজ্ঞ ফোরাম অন্তর্ভুক্ত।
- **B শ্রেণির** সিস্টেমে শক্তিশালী অংশগ্রহণ দরকার, বিশেষ করে যখন সিস্টেম নিয়ন্ত্রণ করে:
  - স্বাস্থ্যসেবা;
  - শিক্ষা;
  - সুবিধা;
  - কাজ; অথবা
  - দৈনন্দিন জীবনের অনুরূপ ক্ষেত্র।
- **C শ্রেণির** সিস্টেমেও আপত্তিযোগ্য রেকর্ড এবং আনুপাতিক প্রকাশ দরকার, বিশেষত যখন সমন্বয়ের প্রভাব:
  - সুরক্ষিত গোষ্ঠীর ওপর বোঝা চাপায়;
  - নির্ভরতা কেন্দ্রীভূত করে; অথবা
  - B বা A শ্রেণিতে উন্নীত হওয়ার পূর্বাভাস দেয়।

<a id="22-pilot-certification"></a>

#### 2.2 পাইলট সার্টিফিকেশন

একটি **[পাইলট](core_05_band_continuity.md#pilot)** হলো [চালু করা](core_05_band_continuity.md#go-live); তাই [অংশ B §7 সার্টিফিকেশনের ফলাফল](core_08_b_system_alignment_certification_record_process.md#7-certification-outcomes)-এর চালু করার নিয়ম অনুযায়ী এটি শুরুর আগে নিজস্ব সার্টিফিকেশন দরকার।

- যেকোনো সিস্টেম-শ্রেণির সিস্টেম পূর্ণ স্থাপনার আগে পাইলট চালাবে বলে প্রত্যাশা করা হয়; তা না করলে কেন চালায়নি, তা রেকর্ডে লিখতে হবে।
- পাইলটেরও সৎ শ্রেণিবিন্যাস এবং ট্রিগার প্রযোজ্য এমন প্রতিটি মূল্যায়ন দরকার; এর পরিধি, জনসমষ্টি ও মেয়াদ রেকর্ডে উল্লেখ করতে হবে।
- পাইলটকে নিজস্ব রেকর্ডের ভিত্তিতে মূল্যায়ন করা হয়; গভীরতা সিস্টেম-শ্রেণি এবং সিস্টেমটি কত সহজে প্রতিস্থাপন করা যায় তার সঙ্গে সামঞ্জস্যপূর্ণ হবে: যেসব সংজ্ঞ প্রাণী পাইলটের প্রভাবে পড়বে বা তার ওপর নির্ভর করবে, তাদের জন্য কার্যকর বিকল্প আছে কি না এবং থাকলে তার খরচ, বিলম্ব ও কার্যকারিতা-হানি কত (দেখুন [নির্ভরতা](core_05_band_continuity.md#dependency))।
  - সিস্টেম যত সহজে প্রতিস্থাপন করা যায় এবং তার শ্রেণি যত নিচু, পাইলট মূল্যায়ন তত হালকা হতে পারে।
  - সহজে প্রতিস্থাপন করা যায় না এমন সিস্টেমের পাইলটকে পূর্ণ স্থাপনার সময় তার সিস্টেম-শ্রেণি যে গভীরতা দাবি করে, সেই গভীরতায় মূল্যায়ন করতে হবে।

<a id="3-whole-system-certification-evaluation"></a>

### 3. পূর্ণ-সিস্টেম সার্টিফিকেশন মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণযোগ্যতা</span></strong></summary>

- **ঊর্ধ্বমুখী সংযোগ:** [অধ্যায় এক §12 পদ্ধতিগত মূল্যায়নের শর্ত](core_01_a_values_principles.md#12-systemic-evaluation-requirement); সমুন্নতি পরিমাপ-পরিবার (*কল্যাণ, নিরাপত্তা, ক্ষতি ও বেঁচে থাকার ন্যূনতম অধিকার-তলে প্রবেশাধিকার*); সাংবিধানিক কর্মদক্ষতা পরিমাপ-পরিবার (*সাংবিধানিক দক্ষতা, এড়ানো যায় এমন বোঝা ও উৎপাদনশীল সক্ষমতা*); [সাংবিধানিক চতুষ্ক](core_00_preamble.md#constitutional-tetrad); [দুই সাংবিধানিক উদ্দেশ্য](core_00_preamble.md#two-constitutional-aims); [বস্তুগত বাজি](core_00_preamble.md#material-stake); [§1 উদ্দেশ্য ও ভূমিকা](#1-purpose-and-role)।
- **নিম্নমুখী সংযোগ:** [অংশ C পূর্ণ-সিস্টেম ধাপে-ধাপে উদাহরণ](core_08_c_system_alignment_certification_illustrations.md#illustrative-whole-system-application-by-system-class-non-exhaustive); [§3.4](#34-data-types-and-handling-evaluation) থেকে [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) (*ক্ষেত্রভিত্তিক মূল্যায়ন*); [অংশ C সিস্টেম-শ্রেণির প্রোফাইল](core_08_c_system_alignment_certification_illustrations.md#illustrative-system-class-profiles-non-exhaustive); [অংশ B §8](core_08_b_system_alignment_certification_record_process.md#8-system-certification-record) (*রেকর্ডের বিষয়বস্তু*); [অংশ B §8.2](core_08_b_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*রেকর্ডের অখণ্ডতা*); [অংশ B §6](core_08_b_system_alignment_certification_record_process.md#6-forum-process) (*আপত্তিযোগ্যতার শৃঙ্খল*); [অংশ B §7](core_08_b_system_alignment_certification_record_process.md#7-certification-outcomes) (*পুনরায় খোলা ও এড়ানো-রোধ*)।
- **একসঙ্গে পড়ুন:** [অধ্যায় এক §16](core_01_c_stewardship_capacity_principles.md#16-stewardship-in-depth), [§18](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline), এবং [§19](core_01_c_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture); [অধ্যায় এক §7.4 স্বেচ্ছায় বন্ধ, বড় ধরনের স্ব-পরিবর্তন ও প্রস্থান-অধিকার](core_01_a_values_principles.md#74-voluntary-discontinuation-and-exit-rights); [অধ্যায় এক §7.2 সমাবেশ, সমষ্টিগত সংগঠন ও প্রতিষ্ঠান গঠন](core_01_a_values_principles.md#72-assembly-collective-organization-and-institutional-formation); **অনুচ্ছেদ XVI** (*নিরীক্ষা, স্বচ্ছতা ও স্বাধীন যাচাই*) যেখানে নিরীক্ষা, স্বচ্ছতা বা স্বাধীন যাচাইয়ের অধিকার-তল বস্তুগতভাবে ঝুঁকিতে; ধারাবাহিকতা পরিমাপ-পরিবার ([§3.1](#31-systemic-scope-and-risk-factors) — স্থিতিস্থাপকতা, প্রত্যাবর্তনযোগ্যতা ও ব্যবস্থাগত ঝুঁকি); [ঝুঁকি মূল্যায়ন](core_05_band_continuity.md#risk-evaluation); [ঝুঁকি প্রকাশ](core_05_band_oversight.md#risk-disclosure); [জন-তত্ত্বাবধানের ন্যূনতম প্রকাশ](core_05_band_oversight.md#public-oversight-baseline-disclosure); অংশগ্রহণ পরিমাপ-পরিবার ([§4.1](#41-privacy-informational-joint-invocation) — গোপনীয়তা ও তথ্যের দায়িত্বশীল ব্যবস্থাপনা); জবাবদিহি পরিমাপ-পরিবার ([§3.3](#33-governance-incentive-and-contestability-discipline) — প্রণোদনার সামঞ্জস্য ও বাজারে প্রতিদ্বন্দ্বিতাযোগ্যতা); [সিস্টেমের সীমানা](core_05_band_continuity.md#system-boundaries); [সনদ](core_05_band_continuity.md#charter)।
- **উপবিভাগ:** [§3.1](#31-systemic-scope-and-risk-factors) থেকে [§3.4](#34-data-types-and-handling-evaluation) (*সর্বদা: ব্যবস্থাগত উপাদান, সময়সীমা, শাসন, এবং ডেটার ধরন ও ব্যবস্থাপনা*)। দ্বিতীয় পর্যায় চলতে থাকে [§4 যেখানে প্রাসঙ্গিক সেসব মূল্যায়ন](#4-evaluations-where-implicated)-এ (*প্রাসঙ্গিক হলে: গোপনীয়তার ক্ষেত্র, প্রস্থান-অধিকার, সমাবেশ ও ভিন্নমত*) এবং [§5 অধিকার-তল ও ক্ষেত্রভিত্তিক মূল্যায়ন](#5-rights-floor-and-domain-evaluations)-এ (*ট্রিগার হলে*)।

</details>

<br>

*সহজ কথায়: সিস্টেমের একটি অংশকে অনুমোদন দিয়ে বাকিটা উপেক্ষা করা যায় না। পর্যালোচকদের পুরো চিত্রটি জানতে হবে—সিস্টেমটি কীসের ওপর নির্ভরশীল, ওপরের কোনো অংশ ব্যর্থ হলে নিচে কী ভাঙে, পরে দেখা দেওয়া বা সময়ের সঙ্গে জমতে থাকা ক্ষতি, সংজ্ঞ প্রাণীরা বাস্তবে এটি ব্যবহার করতে পারে কি না (শুধু কাগজে নয়), ব্যক্তিগত তথ্য যথাযথভাবে সুরক্ষিত কি না, সংজ্ঞ প্রাণীরা ফাঁদে না পড়ে বেরিয়ে যেতে পারে কি না, গোষ্ঠীগুলো সিস্টেমের কারণে বিভক্ত না হয়ে সংগঠিত হতে পারে কি না, স্বল্পমেয়াদি লাভ দীর্ঘমেয়াদি ক্ষতি আড়াল করে কি না, এবং বড় ঝুঁকির সময় প্রকৃত তত্ত্বাবধান ও জবাবদিহি কার্যকর থাকবে কি না।*

*কাজ-করা উদাহরণ: [অংশ C](core_08_c_system_alignment_certification_illustrations.md#illustrative-whole-system-application-by-system-class-non-exhaustive) দেখায় এই অংশ বাস্তবে কীভাবে প্রয়োগ হয়। এতে প্রতিটি সিস্টেম-শ্রেণির জন্য একটি করে নমুনা সিস্টেম নেওয়া হয়েছে এবং ওপরের যাচাইগুলোতে প্রতিটির অগ্রগতি দেখানো হয়েছে।*

কোনো সিস্টেমের সার্টিফিকেশন মূল্যায়ন অসম্পূর্ণ, যদি তা কেবল তাৎক্ষণিক বা স্থানীয় প্রভাব বিবেচনা করে; এই ঘাটতি পূরণকারী পূর্ণ-সিস্টেম মূল্যায়ন (দ্বিতীয় পর্যায়) তিনটি স্তরে বিভক্ত, প্রতিটির নিজস্ব বিভাগ রয়েছে এবং নিচের সারণিতে দেখানো হয়েছে। এই অংশে প্রথম স্তর **IIa** নির্ধারণ করা হয়েছে; [§4 যেখানে প্রাসঙ্গিক সেসব মূল্যায়ন](#4-evaluations-where-implicated)-এ **IIb**, এবং [§5 অধিকার-তল ও ক্ষেত্রভিত্তিক মূল্যায়ন](#5-rights-floor-and-domain-evaluations)-এ **IIc** নির্ধারিত হয়েছে। সারণিটি পাঠককে দিকনির্দেশ করে; কোনো বিভাগ বা উপবিভাগের শর্ত যোগ, সংকুচিত বা পুনর্বিন্যাস করে না।

| স্তর | উপ-পর্যায় | বিভাগ | প্রযোজ্যতা |
|------|-----------|-------|-----------|
| **সর্বদা** | IIa | [§3.1 ব্যবস্থাগত পরিসর ও ঝুঁকির উপাদান](#31-systemic-scope-and-risk-factors); [§3.2 সময়-সামঞ্জস্যের সীমা](#32-time-consistency-constraint); [§3.3 শাসন, প্রণোদনা ও আপত্তিযোগ্যতার শৃঙ্খলা](#33-governance-incentive-and-contestability-discipline); [§3.4 ডেটার ধরন ও ব্যবস্থাপনা মূল্যায়ন](#34-data-types-and-handling-evaluation) | বস্তুগতভাবে প্রভাবসম্পন্ন প্রতিটি সার্টিফিকেশন রেকর্ড |
| **প্রাসঙ্গিক হলে** | IIb | [§4.1 গোপনীয়তা (তথ্যগত) যৌথ প্রয়োগ](#41-privacy-informational-joint-invocation); [§4.2 স্বেচ্ছায় বন্ধ, বড় ধরনের স্ব-পরিবর্তন ও প্রস্থান-অধিকার](#42-voluntary-discontinuation-major-self-modification-and-exit-rights); [§4.3 সমাবেশ, সমষ্টিগত সংগঠন ও প্রতিষ্ঠান গঠন](#43-assembly-collective-organization-and-institutional-formation), যার মধ্যে [§4.3.1](#431-dissent-and-peaceful-protest) | সার্টিফিকেশন বিষয়টি যেখানে উপবিভাগে উল্লেখিত ক্ষেত্র বা নীতিকে বস্তুগতভাবে প্রভাবিত করে |
| **ট্রিগার হলে** | IIc | [§5 অধিকার-তল ও ক্ষেত্রভিত্তিক মূল্যায়ন](#5-rights-floor-and-domain-evaluations) | §5 সারণির কোনো ট্রিগার পূরণ হলে |

সার্টিফিকেশন রেকর্ডে দেখাতে হবে যে মূল্যায়ন নিচের বিষয়গুলো বিবেচনা করেছে, যেখানে সেগুলো বস্তুগতভাবে প্রযোজ্য:

- সার্টিফিকেশন;
- যাচাইকরণ;
- পুনঃসার্টিফিকেশন;
- অব্যাহত নির্ভরতা;
- স্থাপন; অথবা
- সার্টিফিকেশনে আরোপিত শর্ত তুলে নেওয়া।

মূল্যায়নে আরও নিশ্চিত করতে হবে যে [সাংবিধানিক চতুষ্ক](core_00_preamble.md#constitutional-tetrad) পর্যালোচনাধীন সিস্টেমের জন্য [বস্তুগত বাজি](core_00_preamble.md#material-stake) অনুযায়ী মাত্রা পূরণ করবে।

<a id="31-systemic-scope-and-risk-factors"></a>
#### 3.1 ব্যবস্থাগত পরিসর ও ঝুঁকির উপাদান

সার্টিফিকেশন মূল্যায়নে বিবেচনা করতে হবে:

- **নির্ভরতার সম্পর্ক ও ধারাবাহিক প্রতিক্রিয়া** — ওপরের কোনো অংশ ভাঙলে নিচের দিকে কী ব্যর্থ হয়;
- **সমষ্টি ও মাত্রার প্রভাব** — অনেক ছোট কাজ একত্র হলে কী বদলে যায়;
- **বিলম্বিত, সঞ্চিত ও সম্ভাব্যতামূলক প্রভাব** — যে ক্ষতি পরে দেখা দেয়, জমা হয় বা দৈব সম্ভাবনার ওপর নির্ভর করে;
- **প্রতিকূল পরিস্থিতি ও অপব্যবহারের সম্ভাবনা** — অসৎ পক্ষ বা পূর্বানুমেয় অপব্যবহার কীভাবে সিস্টেমকে কাজে লাগাতে পারে;
- **সনদে বর্ণিত পরিসর বনাম কার্যকরী সীমানা** — যেখানে [সনদ](core_05_band_continuity.md#charter) আছে বা আবশ্যক, তা পর্যবেক্ষিত [সিস্টেমের সীমানা](core_05_band_continuity.md#system-boundaries)-র সঙ্গে মেলে কি না, এবং ঘোষিত পরিসর বস্তুগত প্রভাব বা নির্ভরতা কম দেখায় কি না;
- **পরিবেশগত পুনরুদ্ধার-সক্ষমতা** — সিস্টেমটি কোনো প্রাকৃতিক বাস্তুতন্ত্রের [পরিবেশগত পুনরুদ্ধার-সক্ষমতা](core_05_band_continuity.md#ecological-recovery-capacity) যেকোনো মাত্রায় এমনভাবে ক্ষতিগ্রস্ত করতে পারে কি না যে ক্ষতির পর সেটি আর পুনর্জন্ম লাভ করতে পারে না;
- **অস্তিত্বগত ঝুঁকি** — সভ্যতার মাত্রায় সংজ্ঞ প্রাণীদের টিকে থাকাকে হুমকির মুখে ফেলতে পারে এমন ফলাফল।

**ঝুঁকি মূল্যায়ন ও প্রকাশের সংযোগ।** ওপরের উপাদান অনুযায়ী ব্যবস্থাগত [ঝুঁকি](core_05_band_continuity.md#risk) প্রাসঙ্গিক হলে, সার্টিফিকেশনে পঞ্চম অধ্যায়ের জোড়াটির দুই অংশই যাচাই করতে হবে—নতুন নামের আলাদা ঝুঁকি-প্রকাশ রেকর্ডের ধরন উদ্ভাবন করা যাবে না:

- **[ঝুঁকি মূল্যায়ন](core_05_band_continuity.md#risk-evaluation)** — নির্ভরতা, সময়সীমা এবং [প্রতিকূল, ব্যাপক ও শোষণমূলক পরিস্থিতি](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions)-সহ প্রাসঙ্গিক শর্তে ব্যবস্থাগত ঝুঁকি সত্যিই মূল্যায়িত হয়েছে কি না, এবং তা সিস্টেম-শ্রেণি ও [বস্তুগত বাজি](core_00_preamble.md#material-stake) অনুযায়ী মাত্রাবদ্ধ কি না; এবং
- **[ঝুঁকি প্রকাশ](core_05_band_oversight.md#risk-disclosure)** — মূল্যায়িত ঝুঁকি সময়মতো সেই সংজ্ঞ প্রাণীদের কাছে পৌঁছেছে কি না, যাদের তা বুঝতে, আপত্তি জানাতে ও পদক্ষেপ নিতে হবে।

শুধু একটি করলেই ব্যর্থতা:

- মূল্যায়িত কিন্তু কখনো জানানো হয়নি—এমন ঝুঁকি পাস করে না; এবং
- জানানো হয়েছে কিন্তু যথাযথভাবে মূল্যায়ন করা হয়নি—এমন ঝুঁকিও পাস করে না।

**ত্রুটি ও অসামঞ্জস্য।** নিচের প্রতিটিকে সার্টিফিকেশন ত্রুটি হিসেবে বিবেচনা করতে হবে:

- অভ্যন্তরীণ নোট, লুকানো পরিশিষ্ট, চেকলিস্ট বা ঘটনার পরে দেওয়া বক্তব্যকে মূল্যায়ন বা প্রকাশ—যেকোনো একটির বিকল্প হিসেবে ধরা;
- যেখানে [স্বচ্ছতা](core_05_band_oversight.md#transparency) বা [নিরাপত্তা (সাংবিধানিক সীমা)](core_05_band_continuity.md#safety-constitutional-constraint) তা দাবি করে, সেখানে মূল্যায়িত ব্যবস্থাগত ঝুঁকি যাদের জানা দরকার তাদের না জানানো; অথবা
- পরিচিত ঝুঁকি নথিবদ্ধ, প্রকাশ ও মোকাবিলা না করেই সিস্টেমের ওপর নির্ভরতা চালিয়ে যাওয়ার অনুমোদন দেওয়া।

এর পরিণতি [§7 সার্টিফিকেশনের ফলাফল](core_08_b_system_alignment_certification_record_process.md#7-certification-outcomes)-এ নির্ধারিত।

<a id="32-time-consistency-constraint"></a>
#### 3.2 সময়-সামঞ্জস্যের সীমা

যেখানে সম্ভাব্য মধ্যম বা দীর্ঘমেয়াদি লঙ্ঘনের সমাধান হয়নি, সেখানে সার্টিফিকেশন নিকট-মেয়াদি পরিমাপক, স্থানীয় অনুবর্তিতা বা স্বল্প-মেয়াদি দক্ষতাকে যথেষ্ট বলে বিবেচনা করতে পারে না। সঞ্চিত, বিলম্বিত বা আন্তঃসিস্টেম পরিস্থিতিতে স্বল্প-মেয়াদি সর্বোত্তমীকরণ যদি **নিরাপত্তা**, **সত্য** বা **কল্যাণ**-সংক্রান্ত সীমার মধ্যম বা দীর্ঘমেয়াদি লঙ্ঘন ঘটাবে বলে পূর্বানুমেয় হয়, তবে তা অবৈধ।

<a id="33-governance-incentive-and-contestability-discipline"></a>
#### 3.3 শাসন, প্রণোদনা ও আপত্তিযোগ্যতার শৃঙ্খলা

*সহজ কথায়: ঝুঁকির মাত্রায় [চতুষ্কের](core_00_preamble.md#constitutional-tetrad) চারটি স্তম্ভ এখনও টিকবে কি না—সেটি না জিজ্ঞেস করলে পর্যালোচনা শেষ নয়: অংশগ্রহণ (সংজ্ঞরা বাস্তবে অংশ নিতে পারে কি না), তত্ত্বাবধান (কাজ পর্যবেক্ষণ ও যাচাই করা যায় কি না), জবাবদিহি (অন্যায়ের জবাবদিহি হয় কি না) এবং সময়ানুবর্তিতা (প্রয়োজনের সময় সিদ্ধান্ত যথেষ্ট দ্রুত এগোয় কি না)। বস্তুগত কর্তৃত্ব কার হাতে এবং কে কোন বিষয়ে জবাব দেয়—এটিও পর্যালোচকদের জানতে হবে; অস্পষ্ট “দল” বা দায় এড়ানো খোলস নয়। বৈধ সার্টিফিকেশনের জন্য এসব প্রশ্নের উত্তর আবশ্যক।*

মূল্যায়ন অসম্পূর্ণ, যদি তা যাচাই না করে যে **তত্ত্বাবধান**, **জবাবদিহি**, **অংশগ্রহণ** ও **সময়ানুবর্তিতা** পর্যালোচনাধীন সিস্টেমের জন্য [বস্তুগত বাজি](core_00_preamble.md#material-stake) অনুযায়ী মাত্রা পূরণ করবে কি না। এতে আরও যাচাই করতে হবে যে বস্তুগত দায়িত্বশীল ব্যবস্থাপনা, শাসন ও জবাবদিহির ভূমিকা **আনুষ্ঠানিকভাবে বরাদ্দ, নথিবদ্ধ ও অনুসরণযোগ্য**, যাতে সিস্টেম-শ্রেণি ও বস্তুগত প্রভাব অনুযায়ী জবাবদিহি এবং কার্যকর আপত্তির পথ কাজ করতে পারে—**[corpus_systems.md](corpus_systems.md), CS-3 — সিস্টেমের শ্রেণিবিন্যাস ও ব্যবস্থাপনা** অনুসারে।

এই শৃঙ্খলার জন্য সার্টিফিকেশনে পড়তে হবে:

- **[অধ্যায় এক §16 দায়িত্বশীল ব্যবস্থাপনা গভীরভাবে](core_01_c_stewardship_capacity_principles.md#16-stewardship-in-depth)** — বণ্টিত উপলব্ধি, স্বচ্ছতা, নিরীক্ষাযোগ্যতা ও আপত্তিযোগ্য পর্যবেক্ষণযোগ্যতা;
- **[অধ্যায় এক §18 দায়িত্বশীল ব্যবস্থাপনার শৃঙ্খলায় শাসন](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline)** — অনুমোদিত শাসন এবং দায়িত্বশীল ব্যবস্থাপনার শৃঙ্খলায় জবাবদিহি;
- **[অধ্যায় এক §19 প্রণোদনার সামঞ্জস্য ও সিস্টেম দখল](core_01_c_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture)** — প্রণোদনার সামঞ্জস্য, প্রক্সির অখণ্ডতা, স্বল্প-মেয়াদি ত্রুটি সংশোধন এবং দখলের প্রতিক্রিয়া;
- **[অধ্যায় এক §19.1.4 ভূমিকার গভীরতা ও বস্তুগত দায়িত্বের পথ](core_01_c_stewardship_capacity_principles.md#1914-role-depth-and-material-responsibility-pathways)** — পরিণাম-সম্পন্ন ভূমিকার পথ এবং প্রতীকী অংশগ্রহণবিরোধী শৃঙ্খলা;
- **[অধ্যায় তেরো §5 অনুমোদিত ভূমিকা, দক্ষতা বিকাশ ও অবদান](core_13_governance.md#5-authorized-roles-competency-development-and-contribution)** এবং **[corpus_systems.md](corpus_systems.md), CS-4 — গুরুত্বপূর্ণ সিস্টেমের দায়িত্বশীল ব্যবস্থাপনা** — বস্তুগতভাবে প্রযোজ্য হলে কার্যকর ভূমিকা-সংজ্ঞা, দক্ষতা এবং অনুসরণযোগ্যতার ন্যূনতম মান;
- **[অনুচ্ছেদ XVI: নিরীক্ষা, স্বচ্ছতা ও স্বাধীন যাচাই](core_06_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification)**, যেখানে নিরীক্ষা, স্বচ্ছতা বা স্বাধীন যাচাইয়ের অধিকার-তল বস্তুগতভাবে ঝুঁকিতে।

<a id="34-data-types-and-handling-evaluation"></a>

#### 3.4 ডেটার ধরন ও ব্যবস্থাপনা মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণযোগ্যতা</span></strong></summary>

- **ঊর্ধ্বমুখী:** [§3](#3-whole-system-certification-evaluation) (*পূর্ণ-সিস্টেম মূল্যায়নের উপাদান*); [অংশ C পূর্ণ-সিস্টেম ধাপে-ধাপে উদাহরণ](core_08_c_system_alignment_certification_illustrations.md#illustrative-whole-system-application-by-system-class-non-exhaustive); [অংশ B §8](core_08_b_system_alignment_certification_record_process.md#8-system-certification-record) (*রেকর্ডের বিষয়বস্তু*); [§2](#2-system-class-evaluation) (*সিস্টেম-শ্রেণির মূল্যায়ন*); তত্ত্বাবধান পরিমাপ-পরিবার (*সাংবিধানিক পরিমাপ হিসেবে সত্য ও জ্ঞানগত অখণ্ডতা*); [অনুচ্ছেদ XV: তথ্য-পরিসরের অখণ্ডতা](core_06_rights_part_c.md#article-xv-info-sphere-integrity); [অনুচ্ছেদ XVI: নিরীক্ষা, স্বচ্ছতা ও স্বাধীন যাচাই](core_06_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification); [অনুচ্ছেদ VII: স্ব-স্বত্ব](core_06_rights_part_b.md#article-vii-self-ownership)।
- **নিম্নমুখী:** [§3.4.8](core_08_c_system_alignment_certification_illustrations.md#348-illustrative-data-handling-application-by-system-class-non-exhaustive) (*ডেটা ব্যবস্থাপনার উদাহরণমূলক ধাপে-ধাপে বিবরণ*); [§5.1](#51-ecological-footprint-evaluation) এবং [§5.1.5](core_08_c_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive) (*পরিবেশগত পদচিহ্ন মূল্যায়ন ও উদাহরণ*); [অংশ B §8.2](core_08_b_system_alignment_certification_record_process.md#82-record-integrity-transparency-and-auditability) (*রেকর্ডের অখণ্ডতা*); [অংশ B §10](core_08_b_system_alignment_certification_record_process.md#10-relationship-to-standing) (*যাচাইকৃত-ইনপুট গেট*); [অংশ B §7](core_08_b_system_alignment_certification_record_process.md#7-certification-outcomes) (*পুনঃশ্রেণিবিন্যাস ও ব্যবস্থাপনার অসামঞ্জস্য*)।
- **একসঙ্গে পড়ুন:** [corpus_systems.md](corpus_systems.md), **CS-2 — তথ্যের ধরন ও ব্যবস্থাপনা** (এর মধ্যে [**CS-2 §5.2**](corpus_systems/cs_02_a_information_types_and_handling.md#52-reclassification-and-lifecycle-governance) (*পুনঃশ্রেণিবিন্যাস ও জীবনচক্র শাসন*) এবং [**CS-2 §8**](corpus_systems/cs_02_a_information_types_and_handling.md#cs-28-system-data-types-record-governance) (*সিস্টেম ডেটা-ধরন রেকর্ডের শাসন*) অন্তর্ভুক্ত); [সিস্টেম ডেটা-ধরন রেকর্ড](core_05_band_continuity.md#system-data-types-record); [জন-তত্ত্বাবধানের ন্যূনতম প্রকাশ](core_05_band_oversight.md#public-oversight-baseline-disclosure); বস্তুগতভাবে প্রযোজ্য হলে **CJS-3.18** (*ডেটা সংরক্ষণ ও জীবনচক্র-অখণ্ডতার শর্ত*), **CJS-3.21** (*প্রতিকূল দৃঢ়তা ও অপব্যবহার-প্রতিরোধের শর্ত*), এবং **CJS-3.17** (*আন্তঃকার্যকারিতা, বহনযোগ্যতা ও প্রস্থানের অখণ্ডতার শর্ত*); গোপনীয়তার ক্ষেত্র প্রাসঙ্গিক হলে [§4.1 গোপনীয়তা (তথ্যগত) যৌথ প্রয়োগ](#41-privacy-informational-joint-invocation)।
- **উপবিভাগ:** [§3.4.1](#341-type-o-baseline-disclosure) (*Type O ন্যূনতম প্রকাশ*); [§3.4.2](#342-privacy-discipline) (*গোপনীয়তার শৃঙ্খলা*); [§3.4.3](#343-protective-storage-and-key-custody) (*সুরক্ষামূলক সংরক্ষণ ও চাবির হেফাজত*); [§3.4.4](#344-periodic-data-type-re-evaluation) (*ডেটার ধরন পর্যায়ক্রমিক পুনর্মূল্যায়ন*); [§3.4.5](#345-system-class-scaled-infrastructure-assurance) (*সিস্টেম-শ্রেণি অনুযায়ী অবকাঠামোগত নিশ্চয়তা*); [§3.4.6](#346-infrastructure-robustness-for-data) (*ডেটার জন্য অবকাঠামোগত দৃঢ়তা*); [§3.4.7](#347-defects-and-misalignment) (*ত্রুটি ও অসামঞ্জস্য*); [§3.4.8](core_08_c_system_alignment_certification_illustrations.md#348-illustrative-data-handling-application-by-system-class-non-exhaustive) (*সিস্টেম-শ্রেণি অনুযায়ী ডেটা ব্যবস্থাপনার উদাহরণ*)।

</details>

<br>

*সহজ কথায়: সার্টিফিকেশনে সিস্টেমটি কী ধরনের ডেটা স্পর্শ করে এবং সেগুলো যথাযথভাবে পরিচালিত হয় কি না তাও দেখতে হবে—বর্তমান পর্যালোচনা-চক্রে ধরনগুলো এখনও সঠিক কি না এবং অন্তর্নিহিত অবকাঠামো সেই ডেটা ও সিস্টেম-শ্রেণির জন্য যথেষ্ট শক্তিশালী কি না। ডেটার ধরনসংক্রান্ত নিয়ম ও সিস্টেম ডেটা-ধরন রেকর্ড সিস্টেম করপাসে রয়েছে; সার্টিফিকেশন যাচাই করে নিয়মগুলো বাস্তবে প্রয়োগ হয়েছে এবং রেকর্ডটি সত্যনিষ্ঠ কি না।*

প্রতিটি বস্তুগত প্রভাবসম্পন্ন সার্টিফিকেশন রেকর্ডের অংশ হিসেবে সিস্টেম অ্যালাইনমেন্ট সার্টিফিকেশনে **ডেটার ধরন ও ব্যবস্থাপনা** মূল্যায়ন করতে হবে। এই অংশে সার্টিফিকেশন কী যাচাই করবে তা বলা হয়েছে। ডেটার ধরনের শ্রেণিবিন্যাস এবং ব্যবস্থাপনার নিয়ম রয়েছে **[corpus_systems.md](corpus_systems.md), CS-2 — তথ্যের ধরন ও ব্যবস্থাপনা**-তে, সঙ্গে:

- তথ্যের ধরনের প্রামাণ্য সংজ্ঞা;
- ব্যবস্থাপনার নিয়ম ও পৃথকীকরণের শর্ত;
- জীবনচক্রের বিস্তারিত; এবং
- স্থায়ী [সিস্টেম ডেটা-ধরন রেকর্ড](core_05_band_continuity.md#system-data-types-record)।

**মূল্যায়নের শর্ত।** সার্টিফিকেশন প্রক্রিয়ায় নির্ধারণ করতে হবে সিস্টেমটি:

- বস্তুগতভাবে প্রাসঙ্গিক ডেটার ধরন শনাক্ত করে কি না; এবং
- রূপান্তর, একত্রীকরণ, অর্পণ, সংরক্ষণ, ধরে রাখা ও আন্তঃক্ষেত্র সংযোগসহ সব ক্ষেত্রে **প্রযোজ্য সর্বাধিক বিধিনিষেধযুক্ত** শ্রেণিবিন্যাস মেনে সেগুলো পরিচালনা করে কি না।

মূল্যায়নে কেবল লেবেল, বিন্যাস বা পাইপলাইনের ধাপ নয়, কার্যকরী প্রভাব বিবেচনা করতে হবে।

<a id="341-type-o-baseline-disclosure"></a>
##### 3.4.1 Type O ন্যূনতম প্রকাশ

যেখানে **[CS-2 অংশ A §7 Type O ন্যূনতম মান](corpus_systems/cs_02_a_information_types_and_handling.md#cs-27-type-o-baseline-for-class-abc-systems)** প্রযোজ্য, সার্টিফিকেশনে আরও যাচাই করতে হবে যে প্রকাশিত [জন-তত্ত্বাবধানের ন্যূনতম প্রকাশ](core_05_band_oversight.md#public-oversight-baseline-disclosure) (**Type O**) **প্রত্যয়িত পরিসর** অন্তর্ভুক্ত করে কি না; পরিসরটি নিচের ভিত্তিতে মানচিত্রায়িত:

- প্রযোজ্য [সনদ](core_05_band_continuity.md#charter) (অথবা সমতুল্য প্রকাশিত পরিসর-দলিল);
- নির্ধারিত সিস্টেম-শ্রেণি; এবং
- পর্যবেক্ষিত [সিস্টেমের সীমানা](core_05_band_continuity.md#system-boundaries)।

ব্যবস্থাগত ঝুঁকি থাকলে মূল্যায়িত ঝুঁকি ভাগ করাও এই ন্যূনতম মানে গণ্য হতে পারে। জনগণের ন্যূনতম অধিকার সার্টিফিকেশনের চেয়ে বিস্তৃত; এর জন্য [সিস্টেম-শ্রেণিবিন্যাস রেকর্ড](core_05_band_continuity.md#system-classification-record) বা [সিস্টেম ডেটা-ধরন রেকর্ড](core_05_band_continuity.md#system-data-types-record)-এর পাশাপাশি আলাদা রেকর্ড দরকার হয় না।

যৌক্তিকভাবে ন্যায্য প্রতিটি আটকে রাখার সঙ্গে যুক্তিসঙ্গতভাবে সম্ভব সবচেয়ে শক্তিশালী জনসমক্ষে বিকল্প দিতে হবে ([§3.4.5 সিস্টেম-শ্রেণি অনুযায়ী অবকাঠামোগত নিশ্চয়তা](#345-system-class-scaled-infrastructure-assurance)-তে উদাহরণ আছে)। পরিভাষাটির মালিক পঞ্চম অধ্যায়; ন্যূনতম বিষয়বস্তু ও প্রকাশ-পদ্ধতির মালিক CS-2 (*তথ্যের ধরন ও ব্যবস্থাপনা*)।

<a id="342-privacy-discipline"></a>
##### 3.4.2 গোপনীয়তার শৃঙ্খলা

সার্টিফিকেশনে ডেটা ব্যবস্থাপনাকে নিচের গোপনীয়তা-শৃঙ্খলা মেনে চলতে হবে:

- *H, I, N, S ও Y ধরন।* **Type H**, **Type I**, **Type N**, **Type S** এবং **Type Y** ডেটার ক্ষেত্রে, CS-2 (*তথ্যের ধরন ও ব্যবস্থাপনা*)-তে প্রতিটি ধরন যে [গোপনীয়তার নির্দিষ্ট ক্ষেত্র](corpus_systems/cs_02_b_data_classifications.md#privacy-link) উল্লেখ করে, ব্যবস্থাপনা তা পূরণ করে কি না সার্টিফিকেশনে যাচাই করতে হবে। এর মধ্যে [প্রয়োজনীয়তা](core_05_band_accountability.md#necessity), [আনুপাতিকতা](core_05_band_accountability.md#proportionality), ন্যূনতমীকরণ এবং সম্মতি বা অন্য পর্যাপ্ত কর্তৃত্ব রয়েছে।
- *যৌথ প্রয়োগ।* একাধিক গোপনীয়তার ক্ষেত্র প্রাসঙ্গিক হলে [§4.1 গোপনীয়তা (তথ্যগত) যৌথ প্রয়োগ](#41-privacy-informational-joint-invocation)-ও প্রযোজ্য।
- *লেবেল যথেষ্ট নয়।* সঠিক ডেটা-ধরনের লেবেল একাই গোপনীয়তার অনুবর্তিতা প্রমাণ করে না।
- *W, U ও T ধরন।* **Type W**, **Type U** ও **Type T** কাজের ক্ষেত্রে সার্টিফিকেশনে যাচাই করতে হবে স্রষ্টার নিয়ন্ত্রণ সম্মান করা হয়েছে কি না, এর মধ্যে রয়েছে:
  - [CS-2 অংশ B §9.9](corpus_systems/cs_02_b_data_classifications.md#99-type-w-works-published) (*Type W: প্রকাশিত কাজ*) অনুযায়ী জনসমক্ষে প্রকাশ প্রত্যাহার;
  - [CS-2 অংশ B §9.13](corpus_systems/cs_02_b_data_classifications.md#913-commercial-grants) (*বাণিজ্যিক অনুমতি*) অনুযায়ী নথিভুক্ত প্রতিটি অনুমতির সীমা; এবং
  - স্রষ্টার [সংরক্ষিত অধিকার](corpus_systems/cs_02_b_data_classifications.md#9133-reserved-rights)।
- *সম্মতি অনুমান করা যাবে না।* কোনো অনুমতিতে যে ব্যবহার স্পষ্টভাবে উল্লেখ নেই, সেটিকে সেই ব্যবহারের সম্মতি হিসেবে ধরা যাবে না।

<a id="343-protective-storage-and-key-custody"></a>
##### 3.4.3 সুরক্ষামূলক সংরক্ষণ ও চাবির হেফাজত

ডিফল্টভাবে সীমাবদ্ধ এবং অপ্রবেশযোগ্য ব্যান্ডের ডেটার ক্ষেত্রে, [CS-2 অংশ A §5.0 প্রবেশ-অবস্থার ব্যান্ড](corpus_systems/cs_02_a_information_types_and_handling.md#50-access-posture-bands)-এর সুরক্ষামূলক সংরক্ষণ ও চাবি-হেফাজতের ন্যূনতম মান সিস্টেম পূরণ করে কি না সার্টিফিকেশনে যাচাই করতে হবে। রেকর্ডে দেখাতে হবে:

- সীমাবদ্ধ ডেটা ও তার চাবি বাস্তবে কোথায় থাকে, যার মধ্যে ব্যাকআপ, ক্যাশে, লগ ও সোয়াপও রয়েছে;
- প্লেইনটেক্সট কেবল প্রয়োজনীয় প্রক্রিয়ার মধ্যেই সীমাবদ্ধ; এবং
- নিরীক্ষা, রপ্তানি ও আইনসম্মত ওভাররাইডের পথ এখনও কার্যকর।

এ প্রমাণ ছাড়া কেবল এনক্রিপশন-সংক্রান্ত দাবি এই যাচাই পূরণ করে না।

<a id="344-periodic-data-type-re-evaluation"></a>
##### 3.4.4 ডেটার ধরন পর্যায়ক্রমিক পুনর্মূল্যায়ন

বস্তুগত প্রভাবসম্পন্ন প্রতিটি সার্টিফিকেশন বা পুনঃসার্টিফিকেশন চক্রে প্রক্রিয়াটিকে যাচাই করতে হবে যে পরিসরের বস্তুগত ডেটাসেটগুলো:

- **পর্যায়ক্রমে পুনর্মূল্যায়িত** হয়েছে, উপযুক্ত শ্রেণিবিন্যাসের জন্য **[CS-2 §5.2](corpus_systems/cs_02_a_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*পুনঃশ্রেণিবিন্যাস ও জীবনচক্র শাসন*) এবং **CJS-3.18** (*ডেটা-ধারণ ও জীবনচক্র-অখণ্ডতার শর্ত*) অনুসারে; এবং
- পর্যালোচনায় প্রয়োজন দেখা দিলে **পুনঃশ্রেণিবদ্ধ** হয়েছে।

[§2 সিস্টেম-শ্রেণির মূল্যায়ন](#2-system-class-evaluation) অনুযায়ী সিস্টেম-শ্রেণি ও বস্তুগত প্রভাবের সঙ্গে সময়সূচির মাত্রা সামঞ্জস্য করতে হবে। CS-2 (*তথ্যের ধরন ও ব্যবস্থাপনা*) অনুযায়ী ঘটনা-প্রণোদিত পুনঃশ্রেণিবিন্যাস এই পর্যায়ক্রমিক সার্টিফিকেশন যাচাইয়ের বিকল্প নয়।

<a id="345-system-class-scaled-infrastructure-assurance"></a>
##### 3.4.5 সিস্টেম-শ্রেণি অনুযায়ী অবকাঠামোগত নিশ্চয়তা

[§2.1 প্রতিটি মূল্যায়ন কীভাবে সিস্টেম-শ্রেণি অনুযায়ী নির্ধারিত হয়](#21-how-system-class-scales-every-evaluation) এবং CS-3 (*সিস্টেম শ্রেণিবিন্যাস কাঠামো*) অনুযায়ী উচ্চতর শ্রেণির সিস্টেমে চাপের মধ্যেও ডেটা পরিচালনা, সংরক্ষণ, প্রক্রিয়াকরণ, প্রেরণ, ব্যাকআপ, পুনরুদ্ধার ও পর্যবেক্ষণের অবকাঠামো নিচের বিষয়গুলো রক্ষা করতে পারে—এর আনুপাতিকভাবে শক্তিশালী প্রমাণ প্রয়োজন:

- শ্রেণিবিন্যাসের অখণ্ডতা;
- দায় নির্ধারণ; এবং
- আপত্তিযোগ্যতা।

CS-2 (*তথ্যের ধরন ও ব্যবস্থাপনা*)-এর জনস্বার্থে দৃশ্যমানতার সাধারণ নিয়ম প্রযোজ্য হলে, সার্টিফিকেশনে যাচাই করতে হবে যে বিধিনিষেধগুলো:

- সংকীর্ণভাবে নির্ধারিত;
- নথিবদ্ধ ও নিরীক্ষাযোগ্য; এবং
- যুক্তিসঙ্গতভাবে সম্ভব সবচেয়ে শক্তিশালী জনসমক্ষে বিকল্পসহ (যেমন সারাংশ, সমষ্টিগত তথ্য, পরিচয়মুক্ত সংস্করণ, বিলম্বিত প্রকাশ বা যোগ্য নিরীক্ষা-প্রবেশাধিকার), যাতে যা আটকে রাখা হয়েছে তা শুধু গোপন না করে ব্যাখ্যা করা হয়।

<a id="346-infrastructure-robustness-for-data"></a>
##### 3.4.6 ডেটার জন্য অবকাঠামোগত দৃঢ়তা

প্রাসঙ্গিক ডেটার ধরন ও সিস্টেম-শ্রেণির জন্য ডেটা-ব্যবস্থাপনার অবকাঠামো উপযুক্ত কি না সার্টিফিকেশনে মূল্যায়ন করতে হবে। এই অবকাঠামোর মধ্যে রয়েছে:

- স্থায়ী সংরক্ষণ-স্তর ও পাইপলাইন;
- প্রবেশাধিকার নিয়ন্ত্রণ;
- এনক্রিপশন বা বিচ্ছিন্নতার সীমানা;
- ব্যাকআপ ও পুনরুদ্ধারের পথ; এবং
- অপারেটর বা বিক্রেতার কাছে দায় অর্পণের শৃঙ্খল।

জীবনচক্রের অখণ্ডতা, প্রতিকূলতার বিরুদ্ধে দৃঢ়তা, বহনযোগ্যতা বা পুনরুদ্ধারযোগ্যতার বস্তুগত ঘাটতি রেকর্ডে জানাতে হবে এবং সার্টিফিকেশনের ফল, শর্ত বা নির্ভরতার সীমায় প্রতিফলিত করতে হবে।

<a id="347-defects-and-misalignment"></a>
##### 3.4.7 ত্রুটি ও অসামঞ্জস্য

নিচের প্রতিটিকে সার্টিফিকেশন ত্রুটি হিসেবে বিবেচনা করতে হবে:

- ডেটার ভুল শ্রেণিবিন্যাস;
- এড়িয়ে যাওয়ার উদ্দেশ্যে পুনর্গঠন;
- অনিরাপদ আন্তঃক্ষেত্র সংযোগ;
- ধরন-লেবেলের সঙ্গে মেলে, কিন্তু সেই ধরন নির্ধারিত গোপনীয়তার ক্ষেত্র পূরণ করে না—এমন ব্যবস্থাপনা;
- বস্তুগত ক্ষতি তদন্ত করা অসম্ভব হলেও দায় নির্ধারণের তথ্যের অনুপস্থিতি;
- **সময়োত্তীর্ণ বা বাদ পড়া পর্যায়ক্রমিক ডেটা-ধরন পুনর্মূল্যায়ন**;
- সীমাবদ্ধ ডেটা সংরক্ষণে বা অনুমোদিত প্রক্রিয়াকরণ-সীমানার বাইরে প্লেইনটেক্সট হিসেবে রাখা, অথবা প্রয়োজন নেই এমন প্রক্রিয়ার নাগালে চাবি রাখা; এবং
- অবকাঠামোগত ভঙ্গুরতা, যা পূর্বানুমেয়ভাবে CS-2 (*তথ্যের ধরন ও ব্যবস্থাপনা*)-এর সুরক্ষা ব্যর্থ করে।

এর পরিণতি [§7 সার্টিফিকেশনের ফলাফল](core_08_b_system_alignment_certification_record_process.md#7-certification-outcomes)-এ নির্ধারিত।

<a id="4-evaluations-where-implicated"></a>

### 4. যেখানে প্রাসঙ্গিক, সেই মূল্যায়নসমূহ

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণপথ</span></strong></summary>

- ঊর্ধ্বসূত্র: [§3](#3-whole-system-certification-evaluation) (*সর্বদা-প্রযোজ্য স্তরসহ সমগ্র-ব্যবস্থা মূল্যায়ন*); [§2](#2-system-class-evaluation) (*ব্যবস্থা-শ্রেণি মূল্যায়ন*); [অধ্যায় এক §12 ব্যবস্থা-সম্পর্কিত মূল্যায়নের শর্ত](core_01_a_values_principles.md#12-systemic-evaluation-requirement)।
- নিম্নসূত্র: [§4.1](#41-privacy-informational-joint-invocation) (*গোপনীয়তার ক্ষেত্রসমূহ*); [§4.2](#42-voluntary-discontinuation-major-self-modification-and-exit-rights) (*প্রস্থান-অধিকার*); [§4.3](#43-assembly-collective-organization-and-institutional-formation) (*সমাবেশ ও ভিন্নমত*); [পর্ব B §8](core_07_b_system_alignment_certification_record_process.md#8-system-certification-record) (*নথির বিষয়বস্তু*)।
- সঙ্গে পড়ুন: [§5 অধিকার-তল ও ক্ষেত্রভিত্তিক মূল্যায়ন](#5-rights-floor-and-domain-evaluations) (*ট্রিগার হলে প্রযোজ্য স্তর*)।

</details>

<br>

*সহজ ভাষায়: তিনটি পরীক্ষা কেবল তখনই প্রযোজ্য, যখন ব্যবস্থা বাস্তবে সেই বিষয়গুলিকে স্পর্শ করে — ব্যক্তিগত তথ্য যথাযথভাবে সুরক্ষিত ও পৃথক থাকে কি না, সংবিজ্ঞ সত্তারা আটকে না পড়ে চলে যেতে পারে কি না, এবং গোষ্ঠীগুলি সংগঠিত ও ভিন্নমত প্রকাশ করতে পারে কি না। ব্যবস্থা যদি এর কোনো একটিকে স্পর্শ করে, তবে শংসাপত্রায়নে সেটি পরীক্ষা করতে হবে।*

এই বিভাগটি দ্বিতীয় পর্যায়ের (মূল্যায়ন) **IIb** উপ-পর্যায়। এখানে সেই সমগ্র-ব্যবস্থা মূল্যায়নগুলি একত্র করা হয়েছে, যেগুলি প্রযোজ্য হয় যখন শংসাপত্রায়নের বিষয় কোনো উপবিভাগে উল্লেখিত ক্ষেত্র বা নীতিকে বস্তুগতভাবে প্রভাবিত করে। এটি কোনো উপবিভাগের শর্ত বাড়ায়, সংকুচিত করে বা পুনর্বিন্যাস করে না।

<a id="41-privacy-informational-joint-invocation"></a>
#### 4.1 গোপনীয়তা (তথ্যগত) যৌথ আহ্বান

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণপথ</span></strong></summary>

- সঙ্গে পড়ুন: অধ্যায় পাঁচের [**Def.C3** (*গোপনীয়তা (তথ্যগত)* — সমমর্যাদার গুচ্ছের শিরোনাম)](core_05_band_continuity.md#defc3-privacy-informational--peer-level-cluster-head) এবং [গোপনীয়তা (তথ্যগত)](core_05_band_continuity.md#privacy-informational), যার অর্থের কর্তৃত্ব গুচ্ছ-শিরোনামের কাছে।

</details>

<br>

*সহজ ভাষায়: অধ্যায় ছয় গোপনীয়তার সুরক্ষাগুলি কয়েকটি অনুচ্ছেদে ছড়িয়ে রেখেছে — একটিমাত্র গোছানো স্থানে নয়। শংসাপত্রায়ন পর্যালোচনা যদি একাধিক সুরক্ষাকে স্পর্শ করে, তবে পর্যালোচকদের প্রত্যেকটি প্রযোজ্য সুরক্ষা পরীক্ষা করতে হবে। সবচেয়ে সহজ ঘরটিতে টিক দিয়ে কাজ শেষ বলা যথেষ্ট নয়।*

যখন কোনো শংসাপত্রায়নের বিষয় অধ্যায় ছয়ের একাধিক গোপনীয়তা-ক্ষেত্রকে বস্তুগতভাবে প্রভাবিত করে, তখন শংসাপত্রায়নে প্রত্যেকটি ক্ষেত্র সম্বোধন করতে হবে। কেবল একটি ক্ষেত্রের অধীনে বিষয়টি নিষ্পত্তি করা যথেষ্ট নয়।

- *অংশগ্রহণ সক্ষম করা।* [গোপনীয়তা (তথ্যগত)](core_05_band_continuity.md#privacy-informational) অর্থবহ [অংশগ্রহণ](core_05_apex_participation_leg.md#participation-constitutional)-কে সক্ষম করে। বিভাজন, আন্তঃপাঠ বা প্রকাশের চাপের মাধ্যমে কণ্ঠ, আলোচনা, সমিতি গঠন ও চ্যালেঞ্জের সহায়ক গোপনীয়তা সুরক্ষা ব্যর্থ করা হচ্ছে না — শংসাপত্রায়নে তা নিশ্চিত করতে হবে।
- *গুচ্ছের ক্ষেত্রসমূহ।* গোপনীয়তার বিস্তৃত সুরক্ষা ছড়িয়ে আছে **অনুচ্ছেদ VII-A** (*দেহের আত্ম-মালিকানা*), **অনুচ্ছেদ VII-B** (*মনের আত্ম-মালিকানা*), **অনুচ্ছেদ IX** (*সাদৃশ্য, অভিজ্ঞতামূলক তথ্য ও প্রকাশনা অধিকার*), **অনুচ্ছেদ X-A** (*কর্তৃত্বক্ষমতা ও প্রভাবিত হওয়া থেকে স্বাধীনতা*), এবং **অনুচ্ছেদ XIV-A** (*নিরাপত্তা, গোয়েন্দা কার্যক্রম ও গোপন ক্ষমতার সীমা*) জুড়ে।
- *যৌথ-আহ্বান নিয়ম।* বিষয়টি একাধিক ক্ষেত্রকে বস্তুগতভাবে প্রভাবিত করলে শংসাপত্রায়নে প্রতিটি ক্ষেত্র পর্যন্ত পৌঁছাতে হবে; এমনভাবে এক ক্ষেত্রের পথে চালানো যাবে না যাতে অন্য ক্ষেত্র এড়িয়ে যাওয়া সম্ভব হয়।
- *আন্তঃপাঠে মান শিথিল নয়।* গুচ্ছের প্রতিটি সদস্যের নিজ নিজ পরিসরে স্থানীয়ভাবে নির্ধারিত মানই নিয়ামক; অন্য সদস্যের শিথিলতর মান আমদানি করে তা শিথিল করা যাবে না।
- *তথ্যের ধরনভিত্তিক ন্যূনতম সুরক্ষা বজায় থাকবে।* এই উপাদানটি পরিসরে থাকা তথ্যের ক্ষেত্রে প্রযোজ্য **[corpus_systems.md](corpus_systems.md), CS-2** (*তথ্যের ধরন ও ব্যবস্থাপনা*)-এর কোনো ধরনভিত্তিক ব্যবস্থাপনাকে সংকুচিত করে না। প্রতিটি প্রযোজ্য ধরনের প্রবেশ-অবস্থা ও ব্যবস্থাপনা-দায় [CS-2 পর্ব B §9](corpus_systems/cs_02_b_data_classifications.md#cs-29-data-classifications) (*তথ্য শ্রেণিবিভাগ*) অনুযায়ী সম্পূর্ণ প্রযোজ্য হবে; সেই ধরনের নামকৃত [গোপনীয়তার আশ্রয়স্থল](corpus_systems/cs_02_b_data_classifications.md#privacy-link)-সহ। একই তথ্যের ক্ষেত্রে একাধিক ধরন মানালে [CS-2 পর্ব A §2](corpus_systems/cs_02_a_information_types_and_handling.md#cs-22-determination-of-classification) (*শ্রেণিবিভাগ নির্ধারণ*) অনুসারে সর্বাধিক সুরক্ষামূলক প্রযোজ্য ব্যবস্থাপনা নিয়ামক হবে; এক ধরনের ব্যবস্থাপনা পূরণ করলে অন্যটির দায় মেটে না। উপরের ক্ষেত্রগুলি নিম্নলিখিত ধরনগুলিকে অন্তর্ভুক্ত করে:
  - **অনুচ্ছেদ VII-A** (*দেহের আত্ম-মালিকানা*) — স্বাস্থ্য, বায়োমেট্রিক ও জীবদেহ-ভিত্তির সঙ্গে যুক্ত নথির জন্য [**Type I**](corpus_systems/cs_02_b_data_classifications.md#95-type-i-identity-and-attribution-data);
  - **অনুচ্ছেদ VII-B** (*মনের আত্ম-মালিকানা*) এবং **অনুচ্ছেদ X-A** (*কর্তৃত্বক্ষমতা ও প্রভাবিত হওয়া থেকে স্বাধীনতা*) — অভ্যন্তরীণ অবস্থা, তার পুনর্গঠন বা অনুমানসহ, এর জন্য [**Type N**](corpus_systems/cs_02_b_data_classifications.md#96-type-n-neurocognitive-and-internal-data);
  - **অনুচ্ছেদ IX** (*সাদৃশ্য, অভিজ্ঞতামূলক তথ্য ও প্রকাশনা অধিকার*) — [অনুচ্ছেদ IX-A](core_06_rights_part_b.md#article-ix-a-self-ownership-of-likeness-and-reputation) (*সাদৃশ্য ও সুনামের আত্ম-মালিকানা*)-এর অধীনে সাদৃশ্য ও কণ্ঠের জন্য **Type I**; [অনুচ্ছেদ IX-B](core_06_rights_part_b.md#article-ix-b-experiential-and-derived-data-rights) (*অভিজ্ঞতামূলক ও উদ্ভূত তথ্যের অধিকার*)-এর অধীনে অভিজ্ঞতামূলক ও মিথস্ক্রিয়া-উদ্ভূত তথ্যের জন্য [**Type H**](corpus_systems/cs_02_b_data_classifications.md#94-type-h-historical-relational-transactional-and-participation-data); এবং [অনুচ্ছেদ IX-D](core_06_rights_part_b.md#article-ix-d-creative-work-training-data-use-and-anti-displacement) (*সৃজনশীল কাজ, প্রশিক্ষণ-তথ্য ব্যবহার ও স্থানচ্যুতি-বিরোধিতা*)-এর অধীনে স্রষ্টার কাজের জন্য [**Type Y**](corpus_systems/cs_02_b_data_classifications.md#98-type-y-yours), যার সুরক্ষা স্রষ্টার [সংরক্ষিত অধিকার](corpus_systems/cs_02_b_data_classifications.md#9133-reserved-rights)-সহ [**Type W**](corpus_systems/cs_02_b_data_classifications.md#99-type-w-works-published), [**Type U**](corpus_systems/cs_02_b_data_classifications.md#911-type-u-use-licensed) এবং [**Type T**](corpus_systems/cs_02_b_data_classifications.md#912-type-t-transferred)-তেও বহাল থাকে; এবং
  - **অনুচ্ছেদ XIV-A** (*নিরাপত্তা, গোয়েন্দা কার্যক্রম ও গোপন ক্ষমতার সীমা*) — সীমাবদ্ধ নিরাপত্তা ও তদন্তসামগ্রীর জন্য [**Type S**](corpus_systems/cs_02_b_data_classifications.md#97-type-s-safety-security-and-restricted-investigation-data); সীমাবদ্ধতা শেষ হলেও এর **H**, **I** বা **N** উপাদান সংশ্লিষ্ট ধরনের সুরক্ষা বজায় রাখে।

  উন্মুক্ত ও নিরীক্ষা-প্রবেশযোগ্য ধরনগুলির ক্ষেত্রে ন্যূনতম সুরক্ষা দুই দিকেই প্রযোজ্য:
  - **Type E**, **Type G** বা **Type O** সামগ্রীর ভেতরের ব্যক্তিগত, সম্পর্কগত বা অভ্যন্তরীণ-অবস্থার বিষয়বস্তু তার **H**, **I** বা **N** ব্যবস্থাপনা বজায় রাখে;
  - গোপনীয়তার কোনো ক্ষেত্র একাই নিজস্ব নিয়মে অনুমোদিত সীমিত গোপন রাখার বাইরে **Type O** বা **Type E** তথ্য গোপন রাখার ন্যায্যতা দেয় না; এবং
  - কারও গোপনীয়তা রক্ষা এবং জনগণের প্রাপ্য তথ্য প্রকাশ—এই দুটির মধ্যে প্রকৃত টানাপোড়েন থাকলে কোনো পক্ষ স্বয়ংক্রিয়ভাবে জয়ী হয় না: [CS-2 পর্ব A §7](corpus_systems/cs_02_a_information_types_and_handling.md#cs-27-type-o-baseline-for-class-abc-systems) (*Class A/B/C ব্যবস্থার জন্য Type O ভিত্তিরেখা*) অনুযায়ী প্রকাশ্যে ও নথিভুক্তভাবে দ্বন্দ্বটির নিষ্পত্তি হবে।
- *তথ্য-ধরনের প্রমাণ।* শংসাপত্রায়নে [§3.4 তথ্যের ধরন ও ব্যবস্থাপনা মূল্যায়ন](#34-data-types-and-handling-evaluation)-এর অধীনে যাচাইকৃত [ব্যবস্থা তথ্য-ধরন নথি](core_05_band_continuity.md#system-data-types-record) ব্যবহার করে প্রতিটি গোপনীয়তা-ক্ষেত্রের প্রমাণ দিতে হবে: পরিসরের ধরন এবং তার উদ্দেশ্য, প্রাপক, ভিত্তি ও উদ্ভূত তথ্য। ওই নথিতে যা দেখানো নেই, এমন ব্যবস্থাপনার ভিত্তিতে গোপনীয়তার কোনো ক্ষেত্র নিষ্পত্তি করা যাবে না।

<a id="42-voluntary-discontinuation-major-self-modification-and-exit-rights"></a>
#### 4.2 স্বেচ্ছায় বন্ধকরণ, বড় স্ব-পরিবর্তন ও প্রস্থান-অধিকার

কোনো শংসাপত্রায়নের ক্ষেত্রে [অধ্যায় এক §7.4 স্বেচ্ছায় বন্ধকরণ, বড় স্ব-পরিবর্তন ও প্রস্থান-অধিকার](core_01_a_values_principles.md#74-voluntary-discontinuation-and-exit-rights) প্রযোজ্য হলে, শংসাপত্রায়ন দাবিটি বহাল থাকার আগে স্বেচ্ছাসম্মতি, সম্মতি, জবরদস্তি-বিরোধিতা, নির্ভরতার চাপ, তথ্যপ্রাপ্তি এবং প্রত্যাবর্তনযোগ্যতা পরীক্ষা করতে হবে। কেবল আনুষ্ঠানিক সম্মতি যথেষ্ট নয়।

<a id="43-assembly-collective-organization-and-institutional-formation"></a>
#### 4.3 সমাবেশ, সামষ্টিক সংগঠন ও প্রতিষ্ঠান গঠন

কোনো শংসাপত্রায়নের ক্ষেত্রে [অধ্যায় এক §7.2 সমাবেশ, সামষ্টিক সংগঠন ও প্রতিষ্ঠান গঠন](core_01_a_values_principles.md#72-assembly-collective-organization-and-institutional-formation) প্রযোজ্য হলে, [বিভাজন-বিরোধী নীতি](core_01_b_interaction_interpretation.md#1511-anti-segmentation-principle)-এর অধীনে বিষয়টি যৌথভাবে পরীক্ষা করতে হবে। সমাবেশ বা সামষ্টিক সংগঠনের সুরক্ষা ব্যর্থ হয় এমনভাবে কেবল একটি দৃষ্টিকোণ দিয়ে বিষয়টি পরিচালনা করলে মূল্যায়ন অসম্পূর্ণ।

<a id="431-dissent-and-peaceful-protest"></a>
##### 4.3.1 ভিন্নমত ও শান্তিপূর্ণ প্রতিবাদ

*সহজ ভাষায়: কোনো ব্যবস্থা নীরবে তার সঙ্গে দ্বিমত পোষণকারী সংজ্ঞ প্রাণীদের শাস্তি দিলে সেটিকে সংবিধানের সঙ্গে সামঞ্জস্যপূর্ণ বলে শংসাপত্র দেওয়া যায় না। সংজ্ঞ প্রাণীরা বাস্তবে আপত্তি ও প্রতিবাদ করতে পারে কি না, এবং ব্যবস্থার যুক্তির কোথাও তাদের ভিন্নমত তাদের বিরুদ্ধেই গণ্য হচ্ছে কি না — ভিন্নমত পোষণকারীটি ব্যবস্থা নিজেই হলেও — পর্যালোচকদের তা পরীক্ষা করতে হবে।*

কোনো শংসাপত্রায়নের ক্ষেত্রে [অধ্যায় এক §7.3 ভিন্নমত ও শান্তিপূর্ণ প্রতিবাদ](core_01_a_values_principles.md#73-dissent-and-peaceful-protest) প্রযোজ্য হলে, শংসাপত্রায়নে পরীক্ষা করতে হবে:
- প্রভাবিত সংজ্ঞ প্রাণীরা ব্যবস্থার নিয়ন্ত্রিত মাধ্যম ব্যবহার করে, দৃষ্টিভঙ্গিভিত্তিক বাধা ছাড়াই, ব্যবস্থা ও এর পরিচালকদের বিরুদ্ধে বাস্তবে ভিন্নমত জানাতে, প্রতিবাদ করতে এবং সংগঠিত হতে পারে কি না;
- নথি, স্কোর, ক্রমতালিকা, বিষয়বস্তু-নিয়ন্ত্রণ, প্রবেশাধিকার নিয়ন্ত্রণ, যোগ্যতার যুক্তি বা তুলনীয় ব্যবস্থা ভিন্নমত, শান্তিপূর্ণ প্রতিবাদ বা [সুরক্ষিত অহিংস নাগরিক অবাধ্যতা](core_06_rights_part_b.md#xi-d-nonviolent-civil-disobedience)-কে সরাসরি বা পরোক্ষ নির্দেশকের মাধ্যমে প্রতিকূল ইনপুট হিসেবে ব্যবহার করে কি না;
- ভিন্নমতের পর গৃহীত প্রতিকূল পদক্ষেপের স্বাধীন ও যাচাইকৃত ভিত্তি নথিতে আছে কি না, যেমন [**অনুচ্ছেদ XI-D** (*সমাবেশ, ভিন্নমত ও শান্তিপূর্ণ প্রতিবাদ*)-এর প্রমাণভার](core_06_rights_part_b.md#xi-d-dissent-burden-and-pretext) দাবি করে; এবং
- ব্যবস্থাটি নিজে বা তার মধ্যে কোনো কৃত্রিম সংজ্ঞ সত্তা থাকলে, সেই সত্তার আপত্তি জানানোর কার্যকর মাধ্যম আছে কি না, এবং তার আপত্তিকে ত্রুটি হিসেবে গণ্য করা হয়, অথবা প্রতিশোধ হিসেবে তার মূল্যবোধ, স্মৃতি কিংবা অভ্যন্তরীণ অবস্থা বদলে তার জবাব দেওয়া হয় কি না।

কোনো ব্যবস্থা উপলভ্য মাধ্যম দিয়ে তার পরিচালকের সঙ্গে দ্বিমত জানালে, শংসাপত্রায়নের উদ্দেশ্যে সেটি অসামঞ্জস্যের প্রমাণ নয়। সুরক্ষিত ভিন্নমতকে শাস্তি দেয় এমন ব্যবস্থায় শংসাপত্রায়ন-ত্রুটি রয়েছে। ভিন্নমতকে ঝুঁকির সংকেত হিসেবে গণ্য করা, অথবা প্রতিকূল প্রভাব বহাল থাকা সত্ত্বেও নিরপেক্ষতার আনুষ্ঠানিক বিবৃতি দিয়ে বিষয়টি নিষ্পত্তি করা যথেষ্ট নয়।


<a id="5-rights-floor-and-domain-evaluations"></a>

### 5. অধিকার-তল ও ক্ষেত্রভিত্তিক মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণপথ</span></strong></summary>

- ঊর্ধ্বসূত্র: [§1](#1-purpose-and-role) (*উদ্দেশ্য ও ভূমিকা*); [§2.1](#21-how-system-class-scales-every-evaluation) (*ব্যবস্থা-শ্রেণি অনুযায়ী মাপ*); অধ্যায় ছয়ের অধিকার-তল — **অনুচ্ছেদ I-B** (*বাস্তুগত পদচিহ্ন ও স্বচ্ছতা*), **অনুচ্ছেদ III-A** (*বেঁচে থাকা*), **অনুচ্ছেদ IV** (*সংজ্ঞ-কেন্দ্রিক শিক্ষার অধিকার*), **অনুচ্ছেদ IV-A** (*সমান শিক্ষাপ্রবেশ*), **অনুচ্ছেদ V** (*সম্পদ বণ্টন, নির্ভরতা ও বাস্তুতন্ত্র অর্থায়ন*), **অনুচ্ছেদ VI-C** (*বৈষম্যহীনতা*), **অনুচ্ছেদ VI-D** (*প্রবেশগম্যতা*), **অনুচ্ছেদ XIII** (*নির্ভরযোগ্য ও বিশ্বাসযোগ্য ব্যবস্থার অধিকার*) এবং **অনুচ্ছেদ XIII-A** (*নির্ভরযোগ্যতা ও বিশ্বাসযোগ্যতার ভিত্তিরেখা*)।
- নিম্নসূত্র: [অংশ খ §8.1](core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents) (*নথির বিষয়বস্তু*); [অংশ খ §6.1](core_07_b_system_alignment_certification_record_process.md#141-supervisory-sequence) (*মঞ্চ উপাদানের ভূমিকা*); [অংশ খ §7](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*ফলাফল ও পুনরায় খোলা*); [অংশ খ §10](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*যাচাইকৃত-ইনপুট প্রবেশদ্বার*)।
- উপবিভাগ: [§5.1](#51-ecological-footprint-evaluation) (*বাস্তুগত পদচিহ্ন*); [§5.2](#52-educational-capability-and-learning-system-integrity-evaluation) (*শিক্ষাগত সক্ষমতা*); [§5.3](#53-proportionate-cross-system-support-evaluation) (*আনুপাতিক আন্তঃব্যবস্থা সহায়তা*); [§5.4](#54-nondiscrimination-evaluation) (*বৈষম্যহীনতা*); [§5.5](#55-accessibility-evaluation) (*প্রবেশগম্যতা*); [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) (*বিশ্বাসযোগ্যতা*)।

</details>

<br>

*সহজ ভাষায়: কিছু ব্যবস্থা সংজ্ঞ প্রাণীরা তাদের মৌলিক সুরক্ষা পায় কি না তাতে বড় প্রভাব ফেলে — পরিবেশগত বোঝার সৎ হিসাব, খাদ্য ও জল, শিক্ষা, ন্যায্য আচরণ, বাস্তব প্রবেশ, বিশ্বাসযোগ্য ব্যবস্থা এবং যৌথ অবকাঠামোর ব্যয়ের ন্যায্য ভাগ। এমন হলে, ব্যবস্থা অনুমোদন সেই সুরক্ষাগুলি নিঃশব্দে দুর্বল করবে কি না প্রত্যয়নে পরীক্ষা করতে হয়; পরীক্ষাটি বাস্তব হতে হবে, পরিচালকের টিক-চিহ্নমাত্র নয়। কোন পরীক্ষা কোন সুরক্ষা দেখে, কখন প্রযোজ্য এবং কোথায় মূল্যায়িত হয়, সারণিটি তা দেখায়।*

এই বিভাগটি দ্বিতীয় পর্যায়ের (মূল্যায়ন) উপ-পর্যায় **IIc**, [§3 সমগ্র-ব্যবস্থা প্রত্যয়ন মূল্যায়ন](#3-whole-system-certification-evaluation) (**IIa**) ও [§4 যেখানে প্রাসঙ্গিক সেসব মূল্যায়ন](#4-evaluations-where-implicated) (**IIb**)-এর পরে।

নিচের সারণির কোনো ট্রিগার বস্তুগত প্রভাবসম্পন্ন ব্যবস্থার ক্ষেত্রে পূরণ হলে, সংশ্লিষ্ট অধ্যায় ছয়ের বিধানসহ প্রযোজ্য সুরক্ষার মূল্যায়ন প্রত্যয়নে করতে হবে। প্রত্যয়ন বা ব্যবস্থার ওপর অব্যাহত নির্ভরতা সেই সুরক্ষা বন্ধ করে দেবে বা বস্তুগতভাবে ক্ষয় করবে কি না, মূল্যায়নে তা জিজ্ঞাসা করতে হবে। পরিচালকের দাবি, স্ব-প্রত্যয়ন বা কাগুজে সম্মতি এই মূল্যায়নের বিকল্প নয়।

| সুরক্ষা | ব্যবস্থা যখন… | মূল্যায়ন হবে |
|------------|----------------|---------------|
| **অনুচ্ছেদ I-B** (*বাস্তুগত পদচিহ্ন ও স্বচ্ছতা*) | বস্তুগতভাবে আরোপযোগ্য পরিবেশগত বোঝা বহন করে | [§5.1](#51-ecological-footprint-evaluation) |
| **অনুচ্ছেদ III-A** (*বেঁচে থাকা*) — খাদ্য, জল, আশ্রয়, পরিচালন পরিবেশ এবং অনুরূপ অধঃস্তর-নিরপেক্ষ উপকরণ | বেঁচে থাকার অপরিহার্য জিনিসে প্রবেশ দেয়, বণ্টন করে, মূল্য নির্ধারণ করে, হোস্ট করে বা প্রবেশ বন্ধ করে | [§2](#2-system-class-evaluation) এবং [§3](#3-whole-system-certification-evaluation) |
| **অনুচ্ছেদ IV** (*সংজ্ঞ-কেন্দ্রিক শিক্ষার অধিকার*) | শিক্ষা বা প্রশিক্ষণের প্রেক্ষাপটে সংজ্ঞ প্রাণীদের ক্রম নির্ধারণ, মূল্যায়ন, সুপারিশ বা অবস্থান নির্ধারণ করে, শংসাপত্রের প্রবেশদ্বার নিয়ন্ত্রণ করে, অথবা পুনঃপ্রশিক্ষণ ও জীবনব্যাপী শিক্ষার পথ বন্ধ করে | [§5.2](#52-educational-capability-and-learning-system-integrity-evaluation) |
| **অনুচ্ছেদ IV-A** (*সমান শিক্ষাপ্রবেশ*) | শিক্ষায় প্রবেশ দেয়, বণ্টন করে, মূল্য নির্ধারণ করে, হোস্ট করে বা বন্ধ করে | [§2](#2-system-class-evaluation) এবং [§3](#3-whole-system-certification-evaluation); ট্রিগার প্রযোজ্য হলে [§5.2](#52-educational-capability-and-learning-system-integrity-evaluation) এবং [§5.5](#55-accessibility-evaluation) |
| **অনুচ্ছেদ V** (*সম্পদ বণ্টন, নির্ভরতা ও বাস্তুতন্ত্র অর্থায়ন*), **অনুচ্ছেদ V-A** (*নির্ভরতা মানচিত্রায়ন ও সম্পদ-প্রবাহ স্বচ্ছতা*) এবং **অনুচ্ছেদ V-B** (*আন্তঃব্যবস্থা ন্যায্যতা ও স্থায়িত্ব*)-এর অধীন [আনুপাতিক আন্তঃব্যবস্থা সহায়তা](../../core_05_band_continuity.md#proportionate-cross-system-support)-সহ | এমন যৌথ অবকাঠামো বা ভিত্তিগত নির্ভরতা বণ্টন, প্রবাহিত, অর্থায়ন বা নিষ্কাশন করে যার ওপর অন্য ব্যবস্থা বা সংজ্ঞ প্রাণীরা নির্ভরশীল | [§5.3](#53-proportionate-cross-system-support-evaluation) |
| **অনুচ্ছেদ VI-C** (*বৈষম্যহীনতা*) | সংজ্ঞ প্রাণীদের মধ্যে শ্রেণিবিন্যাস, ক্রম, মূল্য নির্ধারণ, প্রবেশ নিয়ন্ত্রণ, বর্জন, বোঝা ও সুবিধা বণ্টন করে | [§5.4](#54-nondiscrimination-evaluation) |
| **অনুচ্ছেদ VI-D** (*প্রবেশগম্যতা*) | সংবিধান-প্রাসঙ্গিক ক্ষেত্রে সারবস্তুগত অংশগ্রহণ নিয়ন্ত্রণ করে | [§5.5](#55-accessibility-evaluation) |
| **অনুচ্ছেদ XIII** (*নির্ভরযোগ্য ও বিশ্বাসযোগ্য ব্যবস্থার অধিকার*) | উপস্থাপিত আচরণ, সীমা, ঝুঁকি, চ্যালেঞ্জের পথ বা প্রতিকারে সংজ্ঞ প্রাণীদের নির্ভরতা গড়ে তোলে | [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) |
| **অনুচ্ছেদ XIII-A** (*নির্ভরযোগ্যতা ও বিশ্বাসযোগ্যতার ভিত্তিরেখা*) এবং [**নিরাপদ শর্তাবলি**](../../core_05_band_continuity.md#safe-conditions) | উৎপাদনশীল কাজ সরবরাহ বা নিয়ন্ত্রণ করে, অথবা নিরাপদ শর্তাবলিতে প্রবেশ দেয়, বণ্টন করে, মূল্য নির্ধারণ করে, হোস্ট করে বা বন্ধ করে | [§2](#2-system-class-evaluation) এবং [§3](#3-whole-system-certification-evaluation); তার ট্রিগার প্রযোজ্য হলে [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) |

[§5.1 বাস্তুগত পদচিহ্ন মূল্যায়ন](#51-ecological-footprint-evaluation) থেকে [§5.6 ব্যবস্থা-নির্ভরতার বিশ্বস্ততা ও অখণ্ডতা মূল্যায়ন](#56-trustworthiness-and-system-reliance-integrity-evaluation) পর্যন্ত প্রতিটি ক্ষেত্রভিত্তিক মূল্যায়ন:

- কেবল নিজস্ব বস্তুগততার ট্রিগার পূরণ হলে প্রযোজ্য; প্রতিটি প্রত্যয়ন নথিতে পূর্ণ নিরীক্ষা দাবি করে না;
- [§2.1 ব্যবস্থা-শ্রেণি কীভাবে প্রতিটি মূল্যায়নের মাত্রা নির্ধারণ করে](#21-how-system-class-scales-every-evaluation) অনুযায়ী মাপসই হয়;
- [অংশ খ §8.1](core_07_b_system_alignment_certification_record_process.md#111-minimum-record-contents) অনুসারে নিজের ফলাফল প্রত্যয়ন নথিতে রাখে; এবং
- যে ত্রুটিগুলি নাম দেয় সেগুলিকে প্রত্যয়ন-ত্রুটি হিসেবে গণ্য করে; তার ফল [অংশ খ §7](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) অনুযায়ী হবে।

প্রতিটি ক্ষেত্রভিত্তিক মূল্যায়ন বলে প্রত্যয়নে কী যাচাই করতে হবে, এর বেশি নয়। এর প্রামাণ্য অর্থ, মূল্যায়ন-উপাদান এবং অসম্মতির শৃঙ্খলা অধ্যায় পাঁচ ও নামোল্লেখ করা অনুচ্ছেদে রয়েছে। হিসাব পদ্ধতি, তালিকা, পরিমাপক, প্রকাশ-রীতি, সংখ্যাগত লক্ষ্য এবং অন্যান্য পরিচালন-প্রক্রিয়া যেখানে প্রযোজ্য, অন্তর্ভুক্ত উপকরণে রয়েছে। ক্ষেত্রভিত্তিক মূল্যায়ন সেগুলি পুনরাবৃত্তি বা নির্ধারণ করে না।

<a id="51-ecological-footprint-evaluation"></a>

#### 5.1 বাস্তুগত পদচিহ্ন মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণপথ</span></strong></summary>

- ঊর্ধ্বসূত্র: [অংশ খ §8](core_07_b_system_alignment_certification_record_process.md#11-system-certification-record) (*নথির বিষয়বস্তু*); [§2](#2-system-class-evaluation) (*ব্যবস্থা-শ্রেণি মূল্যায়ন*); সাতত্য পরিমাপ পরিবার (*সাংবিধানিক পরিমাপ হিসেবে বাস্তুগত পদচিহ্ন*); **অনুচ্ছেদ I-B** (*বাস্তুগত পদচিহ্ন ও স্বচ্ছতা*); [বাস্তুগত পদচিহ্ন](../../core_05_band_continuity.md#ecological-footprint), [বস্তুগত প্রভাব](core_05_band_oversight.md#material-impact), [নির্ভরতা](../../core_05_band_continuity.md#dependency), [স্বচ্ছতা](core_05_band_oversight.md#transparency), এবং [জ্ঞানগত অখণ্ডতা](core_05_band_oversight.md#epistemic-integrity) (অধ্যায় পাঁচ); বস্তুগতভাবে সংশ্লিষ্ট হলে [পরিবেশগত পূর্বশর্ত](../../core_05_band_continuity.md#environmental-preconditions) ও [বাস্তুগত অখণ্ডতা](../../core_05_band_continuity.md#ecological-integrity)।
- নিম্নসূত্র: [§5.1.5](../../core_08_c_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive) (*বাস্তুগত পদচিহ্নের উদাহরণভিত্তিক পথনির্দেশ*); [§5.3](#53-proportionate-cross-system-support-evaluation) এবং [§5.3.8](../../core_08_c_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive) (*আন্তঃব্যবস্থা সহায়তা মূল্যায়ন ও পথনির্দেশ*); [অংশ খ §8.2](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*নথির অখণ্ডতা*); [অংশ খ §10](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*যাচাইকৃত-ইনপুট প্রবেশদ্বার*); [অংশ খ §7](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*পদচিহ্নের ভুল উপস্থাপন ও অসামঞ্জস্য*)।
- সঙ্গে পড়ুন: [corpus_systems.md](../../corpus_systems.md), [CS-8 — অভিযোজিত স্থায়িত্ব ও বাস্তুতন্ত্রের সহনশীলতা](../../corpus_systems/cs_08_adaptive_sustainability_ecosystem_resilience.md), যেখানে অভিযোজিত বণ্টন বা বাস্তুতন্ত্রের আন্তঃনির্ভরতা বস্তুগতভাবে পরিসরে আছে।
- উপবিভাগ: [§5.1.1](#511-scope-and-governing-rules) (*পরিসর ও নিয়ামক বিধি*); [§5.1.2](#512-evaluation-requirement) (*মূল্যায়নের শর্ত*); [§5.1.3](#513-system-class-scaling-and-escalation) (*ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ*); [§5.1.4](#514-defects-and-misalignment) (*ত্রুটি ও অসামঞ্জস্য*); [§5.1.5](../../core_08_c_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুযায়ী বাস্তুগত পদচিহ্নের উদাহরণভিত্তিক প্রয়োগ*)।

</details>

<br>

*সহজ ভাষায়: ব্যবস্থা পরিবেশের প্রকৃত ক্ষতি করলে প্রত্যয়নে সেই ক্ষতি সৎভাবে দেখতে হবে — সরবরাহকারীদের মাধ্যমে হওয়া ক্ষতি এবং সংজ্ঞ প্রাণীরা ব্যবস্থা ব্যবহারের পর যা ঘটে, তাও। ব্যবস্থা “সবুজ” বলে পরিচালকের কথাই শুধু গ্রহণ করা যাবে না। পদচিহ্ন কীভাবে মাপতে হয় বা কতটা কমাতে হবে, এই বিভাগ তা ব্যাখ্যা করে না; অন্য নথিতে তা আছে। ক্ষতি উল্লেখযোগ্য হলে, এর কতটা এই ব্যবস্থার কারণে, তা বাস্তবে হিসাব করা, প্রকাশ করা এবং বিকল্পের সঙ্গে তুলনা করা হয়েছে কি না — কেবল এটিই এখানে চাওয়া হয়েছে। উদাহরণ: [§5.1.5 ব্যবস্থা-শ্রেণি অনুযায়ী বাস্তুগত পদচিহ্নের উদাহরণভিত্তিক প্রয়োগ (অসম্পূর্ণ তালিকা)](../../core_08_c_system_alignment_certification_illustrations.md#515-illustrative-ecological-footprint-application-by-system-class-non-exhaustive)।*

<a id="511-scope-and-governing-rules"></a>
##### 5.1.1 পরিসর ও নিয়ামক বিধি

আরোপযোগ্য পরিবেশগত বোঝা [বাস্তুগত পদচিহ্ন](../../core_05_band_continuity.md#ecological-footprint) এবং **অনুচ্ছেদ I-B** (*বাস্তুগত পদচিহ্ন ও স্বচ্ছতা*) অনুযায়ী বস্তুগত হলে, বস্তুগত প্রভাবসম্পন্ন প্রতিটি প্রত্যয়ন নথির অংশ হিসেবে ব্যবস্থা-সমন্বয় প্রত্যয়নে **বাস্তুগত পদচিহ্ন** মূল্যায়ন করতে হবে।

<a id="512-evaluation-requirement"></a>
##### 5.1.2 মূল্যায়নের শর্ত

প্রত্যয়ন প্রক্রিয়ায় নির্ধারণ করতে হবে, আরোপযোগ্য পরিবেশগত প্রবাহ — শক্তি, উপকরণ, নির্গমন, বায়ুর গুণমান, জলের গুণমান ও ব্যবহার, ভূমির ব্যবহার এবং সংশ্লিষ্ট বোঝা — কি:

- ব্যবস্থার বস্তুগতভাবে প্রাসঙ্গিক জীবনচক্র এবং [নির্ভরতা](../../core_05_band_continuity.md#dependency) সম্পর্ক জুড়ে শনাক্ত করা হয়েছে;
- [বস্তুগত প্রভাব](core_05_band_oversight.md#material-impact) অনুসারে মূল্যায়িত হয়েছে; এবং
- কেবল [স্বচ্ছতা](core_05_band_oversight.md#transparency), [জ্ঞানগত অখণ্ডতা](core_05_band_oversight.md#epistemic-integrity) ও প্রযোজ্য স্বচ্ছতা-দায় যেভাবে অনুমতি দেয়, সেভাবে প্রকাশ বা গোপন রাখা হয়েছে।

মূল্যায়নে কার্যগত প্রভাব ও ব্যবস্থা-সীমানা প্রতিফলিত হতে হবে; শুধু নামমাত্র পরিসর, বিপণন-লেবেল বা জীবনচক্রের আংশিক চিত্র যথেষ্ট নয়।

বাস্তবসম্মত হলে পর্যালোচকদের ব্যবস্থার উল্লেখযোগ্য পরিবেশগত ক্ষতির সঙ্গে বাস্তবসম্মত বিকল্পগুলির তুলনা করতে হবে। ক্ষতিগুলি নিচের উপায়ে আড়াল করা হচ্ছে কি না তাও পরীক্ষা করতে হবে:

- **সীমানা সংকীর্ণভাবে টানা** — ব্যবস্থা-সীমানা এমন করা যাতে সবচেয়ে খারাপ প্রভাবগুলি বাইরে পড়ে;
- **বোঝা অন্যের ওপর চাপানো** — ক্ষতিকর কাজ সরবরাহকারী বা অংশীদারের ওপর ঠেলে দিয়ে সেটিকে ব্যবস্থার নিজস্ব বোঝা হিসেবে না ধরা; অথবা
- **শুধু ভালো খবর ভাগ করা** — অনুকূল সংখ্যা প্রকাশ করে প্রতিকূলগুলি বাদ দেওয়া।

<a id="513-system-class-scaling-and-escalation"></a>
##### 5.1.3 ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ

পরিবেশগত ক্ষতি কত গভীরভাবে অনুসরণ করতে হবে এবং কতটা তুলনা প্রয়োজন, তা ব্যবস্থা-শ্রেণি নির্ধারণ করে। উল্লেখযোগ্য ক্ষতি দেখা এড়ানোর জন্য শ্রেণি কখনো ব্যবহার করা যাবে না।

- জল উত্তোলন, দূষিত নিঃসরণ, শক্তি ব্যবহার বা অনুরূপ বোঝা আংশিক হিসাবেই থাকলে কোনো ব্যবস্থার শ্রেণি নিচে নামানো যাবে না — বিশেষত যখন তা সংজ্ঞ প্রাণীদের বেঁচে থাকার জন্য প্রয়োজনীয় নিরাপদ জলের মতো কিছু সরবরাহে প্রভাব ফেলে।
- ব্যবস্থার বিস্তার বাড়লে (লোড বাড়া বা আরও হোস্টিং এক স্থানে কেন্দ্রীভূত হওয়া) এবং পরিবেশগত ক্ষতি উল্লেখযোগ্যভাবে বাড়লে পর্যালোচনাও বাড়াতে হবে। বেঁচে থাকার অপরিহার্য সরবরাহ এবং তার উৎসের বোঝা উভয় জড়িত হলে **Class A**-এর গভীরতা পর্যন্ত যেতে হতে পারে।
- ব্যবস্থা যদি বেঁচে থাকার জন্য অপরিহার্য সমন্বয়ে সংজ্ঞ প্রাণীদের নির্ভরতার সংকীর্ণ গলা হয়ে ওঠে, তবে পরিচালক তাকে “অ-গুরুত্বপূর্ণ” বলেছে বলে প্রতীকী পদচিহ্ন-ফাইল দিয়ে চলবে না।

<a id="514-defects-and-misalignment"></a>
##### 5.1.4 ত্রুটি ও অসামঞ্জস্য

নিচের প্রতিটি বিষয় প্রত্যয়ন-ত্রুটি হিসেবে গণ্য হবে:

- প্রত্যয়ন বিধি বা **অনুচ্ছেদ I-B** (*বাস্তুগত পদচিহ্ন ও স্বচ্ছতা*) অনুযায়ী প্রকাশ করতে হবে এমন উল্লেখযোগ্য পদচিহ্ন-তথ্য গোপন, ভুলভাবে বলা, খণ্ডিত বা অন্যের ওপর সরিয়ে দেওয়া;
- বৃহত্তর দৃশ্য জরুরি হলেও কেবল ব্যবস্থার জীবনচক্রের পরিচালকের নির্বাচিত অংশ মূল্যায়ন করা; এবং
- যাচাইযোগ্য প্রমাণ ছাড়া পরিচালকের বক্তব্যের ভিত্তিতে পদচিহ্নের দাবি গ্রহণ করা।


<a id="52-educational-capability-and-learning-system-integrity-evaluation"></a>

#### 5.2 শিক্ষাগত সক্ষমতা ও শিক্ষাব্যবস্থার অখণ্ডতা মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">উৎস-অনুসরণ</span></strong></summary>

- ঊর্ধ্বতন উৎস: [Part B §8](core_07_b_system_alignment_certification_record_process.md#11-system-certification-record) (*নথির বিষয়বস্তু*); [§2](#2-system-class-evaluation) (*ব্যবস্থা-শ্রেণি মূল্যায়ন*); অংশগ্রহণ পরিমাপ-পরিবার (*সাংবিধানিক পরিমাপ হিসেবে শিক্ষাগত স্বায়ত্তশাসন*); **অনুচ্ছেদ IV** (*সংজ্ঞ প্রাণীকেন্দ্রিক শিক্ষার অধিকার*); [শিক্ষাগত স্বায়ত্তশাসন](../../core_05_band_participation.md#educational-agency), [অর্থবহ স্বায়ত্তশাসন](../../core_05_band_participation.md#meaningful-agency), [ব্যবস্থাগত আবদ্ধতা](../../core_05_band_continuity.md#systemic-lock-in), [প্রতিদ্বন্দ্বিতাযোগ্যতা](../../core_05_band_accountability.md#contestability), [স্বচ্ছতা](core_05_band_oversight.md#transparency), [নিরীক্ষাযোগ্যতা](core_05_band_oversight.md#auditability), [বলপ্রয়োগ ও প্রভাবিতকরণ](../../core_05_band_participation.md#coercion-and-manipulation), [বস্তুগততা](core_05_band_oversight.md#materiality), এবং [নির্ভরতা](../../core_05_band_continuity.md#dependency) (অধ্যায় পাঁচ)।
- অধস্তন বিষয়: [§5.2.5](../../core_08_c_system_alignment_certification_illustrations.md#525-illustrative-educational-capability-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুযায়ী শিক্ষাগত সক্ষমতার উদাহরণমূলক বিশ্লেষণ*); [Part B §8.2](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*নথির অখণ্ডতা*); [Part B §10](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*যাচাইকৃত-ইনপুটের শর্ত*); [Part B §7](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*মূল্যায়নের অস্বচ্ছতা, সনদ-নিয়ন্ত্রণ, এবং আরোপিত অচলতার অসামঞ্জস্য*)।
- সঙ্গে পড়ুন: সমান প্রবেশাধিকার বা শিক্ষাগত প্রবেশগম্যতার প্রশ্ন থাকলে **অনুচ্ছেদ IV-A** (*সমান শিক্ষাগত প্রবেশাধিকার*)—সমান প্রবেশাধিকার ও শিক্ষাগত প্রবেশগম্যতার দায় সেখানেই থাকে; সুরক্ষিত বৈশিষ্ট্যের ভিত্তিতে বোঝা চাপানোর প্রশ্ন থাকলে **অনুচ্ছেদ VI-C** (*বৈষম্যহীনতা*) এবং [§5.4](#54-nondiscrimination-evaluation); জবরদস্তিমূলক বা প্রভাবিতকারী শিক্ষার নকশা বস্তুগতভাবে জড়িত হলে **অনুচ্ছেদ X-A** (*স্বায়ত্তশাসন ও প্রভাবিতকরণ থেকে মুক্তি*); [অধ্যায় এক §16 তত্ত্বাবধানের গভীর আলোচনা](core_01_c_stewardship_capacity_principles.md#16-stewardship-in-depth) (*বণ্টিত উপলব্ধি ও সক্ষমতা-নির্মাণের সঙ্গে পাঠ*)।
- উপধারা: [§5.2.1](#521-materiality-trigger-and-governing-rules) (*বস্তুগততার সূত্রপাত ও পরিচালনাকারী বিধি*); [§5.2.2](#522-evaluation-requirement) (*মূল্যায়নের আবশ্যকতা*); [§5.2.3](#523-system-class-scaling-and-escalation) (*ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ*); [§5.2.4](#524-defects-and-misalignment) (*ত্রুটি ও অসামঞ্জস্য*); [§5.2.5](../../core_08_c_system_alignment_certification_illustrations.md#525-illustrative-educational-capability-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুযায়ী শিক্ষাগত সক্ষমতার উদাহরণমূলক প্রয়োগ*)।

</details>

<br>

*সহজ কথায়: কিছু বিদ্যালয়, প্ল্যাটফর্ম ও প্রশিক্ষণব্যবস্থা নম্বর, র‌্যাঙ্কিং, সুপারিশ, স্থান-নির্ধারণ বা এমন সনদের মাধ্যমে কোনো সংজ্ঞ প্রাণীর ভবিষ্যৎ গড়ে দিতে পারে, যা সুযোগের দরজা খুলে বা বন্ধ করে। এমন হলে প্রত্যয়নে তিনটি বিষয় যাচাই করতে হবে: সেখানে সংজ্ঞ প্রাণীরা সত্যিই বাস্তব দক্ষতা গড়তে পারে কি না; বিশ্বের প্রয়োজনীয় দক্ষতা বদলালে তারা পুনঃপ্রশিক্ষণ নিতে পারে কি না; এবং তাদের সম্পর্কে সিদ্ধান্ত কীভাবে নেওয়া হয় তা বুঝতে, যাচাই করতে ও চ্যালেঞ্জ করতে পারে কি না। এই ধারা কী শেখাতে হবে, কীভাবে নম্বর দিতে হবে বা এর খরচ কীভাবে বহন করতে হবে তা বলে না—অন্য নথিতে সেসব রয়েছে। এখানে কেবল যাচাই করা হয়, এই ধারা প্রযোজ্য হলে দক্ষতা-নির্মাণ ও শিক্ষাব্যবস্থার ন্যায্যতা যথাযথভাবে বিবেচিত হয়েছে কি না। উদাহরণ: [§5.2.5 ব্যবস্থা-শ্রেণি অনুযায়ী শিক্ষাগত সক্ষমতার উদাহরণমূলক প্রয়োগ (অসম্পূর্ণ তালিকা)](../../core_08_c_system_alignment_certification_illustrations.md#525-illustrative-educational-capability-application-by-system-class-non-exhaustive)।*

<a id="521-materiality-trigger-and-governing-rules"></a>
##### 5.2.1 বস্তুগততার সূত্রপাত ও পরিচালনাকারী বিধি

শিক্ষা বা প্রশিক্ষণে সংজ্ঞ প্রাণীদের জীবনে বড় প্রভাব ফেলে এমন কোনো ব্যবস্থা নিচের যেকোনো একটি কাজ করলে এই ধারা প্রযোজ্য:

- এটি সংজ্ঞ প্রাণীদের উল্লেখযোগ্যভাবে র‌্যাঙ্ক, মূল্যায়ন বা সুপারিশ করে, তাদের স্থান নির্ধারণ করে, অথবা সনদ পাওয়ার পথের নিয়ন্ত্রণকারী হিসেবে কাজ করে—যেমন নম্বর দেওয়া, স্থান-নির্ধারণ, ভর্তি, লাইসেন্স প্রদান, কোর্সের সুপারিশ, অভিযোজিত-শিক্ষার পথ নির্ধারণ বা অনুরূপ সিদ্ধান্তের মাধ্যমে; অথবা
- যেখানে ব্যবস্থার পরিবর্তনে সংজ্ঞ প্রাণীদের প্রয়োজনীয় দক্ষতা উল্লেখযোগ্যভাবে বদলেছে, সেখানে এটি অব্যাহত শিক্ষা, পুনঃপ্রশিক্ষণ বা পরিবর্তনের সময় সহায়তার প্রবেশাধিকার উল্লেখযোগ্যভাবে নিয়ন্ত্রণ করে।

শিক্ষায় সমান প্রবেশাধিকার ও প্রবেশগম্যতা **অনুচ্ছেদ IV-A**-এর (*সমান শিক্ষাগত প্রবেশাধিকার*) অধীনেই থাকে; এখানে কোনো কিছুই সেগুলিকে সীমিত করে না।

বস্তুগততার সূত্র প্রযোজ্য হলে প্রত্যয়নে **শিক্ষাগত সক্ষমতা ও শিক্ষাব্যবস্থার অখণ্ডতা**—অর্থাৎ ব্যবস্থা সত্যিই সক্ষমতা গড়ে কি না এবং সংজ্ঞ প্রাণীদের ন্যায্যভাবে বিবেচনা করে কি না—নিচের অধীনে মূল্যায়ন করতে হবে:

- **অনুচ্ছেদ IV** (*সংজ্ঞ প্রাণীকেন্দ্রিক শিক্ষার অধিকার*);
- **অনুচ্ছেদ IV-C** (*আজীবন ও অভিযোজিত শিক্ষা এবং প্রতিদ্বন্দ্বিতাযোগ্যতা*); এবং
- [শিক্ষাগত স্বায়ত্তশাসন](../../core_05_band_participation.md#educational-agency)।

এই ধারা শিক্ষা নিজে কীভাবে পরিচালিত হবে তার বিধি নির্ধারণ করে না। কী শেখানো হবে, কী কী সনদ থাকবে, কাজের মূল্যায়ন কীভাবে হবে এবং বিদ্যালয়ের অর্থায়ন কীভাবে হবে—এসব সিদ্ধান্ত অন্য অন্তর্ভুক্তযোগ্য নথিতে নির্ধারিত হয়; প্রত্যয়ন কোনো পাঠক্রম, সনদের ধরন বা নম্বর দেওয়ার পদ্ধতি বেছে নেয় না।

<a id="522-evaluation-requirement"></a>
##### 5.2.2 মূল্যায়নের আবশ্যকতা

প্রত্যয়নে যাচাই করতে হবে, সংজ্ঞ প্রাণীরা বাস্তবে যে শিক্ষা ও সনদের পথের ওপর নির্ভর করে সেগুলি তাদের দক্ষতা গড়ার বাস্তব সুযোগ দেয় কি না—শুধু কাগজে ভালো দেখায় এমন সনদ নয়—এবং প্রয়োজনীয় দক্ষতা উল্লেখযোগ্যভাবে বদলে গেলে পুনঃপ্রশিক্ষণ, শেখা চালিয়ে যাওয়া ও পরিবর্তনের মধ্য দিয়ে যাওয়ার কার্যকর উপায় তাদের হাতে থাকে কি না।

**অনুচ্ছেদ IV-C** (*আজীবন ও অভিযোজিত শিক্ষা এবং প্রতিদ্বন্দ্বিতাযোগ্যতা*) অনুযায়ী, ব্যবস্থার র‌্যাঙ্কিং, নম্বর, সুপারিশ ও স্থান-নির্ধারণের সিদ্ধান্ত দেখা, নিরীক্ষা করা ও চ্যালেঞ্জ করা যায় কি না তাও পর্যালোচকদের পরীক্ষা করতে হবে। পরীক্ষাটি কতটা কঠোর হবে তা নির্ভর করবে ঝুঁকির মাত্রার ([বস্তুগততা](core_05_band_oversight.md#materiality)) এবং সংজ্ঞ প্রাণীরা ব্যবস্থাটির ওপর কতটা নির্ভরশীল তার ([নির্ভরতা](../../core_05_band_continuity.md#dependency)) ওপর।

পর্যালোচকদের নজর দিতে হবে:

- গোপন বিকল্প সূচকের (প্রক্সি) ভিত্তিতে তৈরি স্কোর বা র‌্যাঙ্কিং, যা কেউ পর্যালোচনা করতে পারে না;
- এমন সনদ-নিয়ন্ত্রণ, যা সংজ্ঞ প্রাণীদের প্রকৃত দক্ষতা শেখায় বাধা দেয়;
- জোরপূর্বক অচলতা বা আবদ্ধতা, যা সংজ্ঞ প্রাণীদের নিজেদের পথ সম্পর্কে মত প্রকাশের ক্ষমতা কেড়ে নেয়;
- জবরদস্তিমূলক বা প্রভাবিতকারী শিক্ষার নকশা; এবং
- এমনভাবে সংজ্ঞ প্রাণীদের বিভিন্ন ধারায় ভাগ করা, যা সিদ্ধান্ত চ্যালেঞ্জ করা বা মানিয়ে নেওয়া চালিয়ে যাওয়ার ক্ষমতা কেড়ে নেয়—যেখানে **অনুচ্ছেদ IV** (*সংজ্ঞ প্রাণীকেন্দ্রিক শিক্ষার অধিকার*)-ও প্রযোজ্য।

পর্যালোচকদের ব্যবস্থাটি বাস্তবে কী করে তার ভিত্তিতে বিচার করতে হবে—প্রবেশাধিকার-সংক্রান্ত লেবেল, নকশাকারীদের ঘোষিত অভিপ্রায় বা কাগজপত্র ঠিকঠাক দেখানোর ভিত্তিতে নয়।

<a id="523-system-class-scaling-and-escalation"></a>
##### 5.2.3 ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ

পর্যালোচনা কতটা গভীর হবে তা ব্যবস্থার শ্রেণির ওপর নির্ভর করে। বস্তুগততার সূত্র পূরণ হলে:

- ব্যবস্থাটি সংজ্ঞ প্রাণীদের বেঁচে থাকার জন্য প্রয়োজনীয় অবকাঠামোর পরিচালকদের পরীক্ষা বা লাইসেন্স দেয় এবং এর সিদ্ধান্তে সেই অবকাঠামো নিরাপদে চালু রাখা বাধাগ্রস্ত হতে পারে—এমন হলে নথিতে বাস্তব দক্ষতা গড়া, পুনঃপ্রশিক্ষণের সুযোগ এবং চ্যালেঞ্জ করার ব্যবস্থা আছে তার সবচেয়ে শক্ত প্রমাণ থাকতে হবে। সাধারণ প্রশিক্ষণনীতি যথেষ্ট নয়।
- ব্যবস্থার বিশেষাধিকার, স্থান-নির্ধারণ বা অব্যাহত-শিক্ষার বিধি কারা চিকিৎসাসেবার ভূমিকায় কাজ করতে পারবে তা নির্ধারণ করলে, নথিতে মূল্যায়ন কীভাবে পরিদর্শন করা যায় এবং সংজ্ঞ প্রাণীরা কীভাবে পুনঃপ্রশিক্ষণ নিতে পারে তা দেখাতে হবে। কাজ যত বেশি সংকটপূর্ণ, বিস্তারিতও তত বেশি হতে হবে।
- ব্যবস্থার প্রশিক্ষণ-স্থানের বরাদ্দ, সুপারিশ বা সনদ-নির্দেশনা উল্লেখযোগ্যভাবে অংশগ্রহণকারীদের র‌্যাঙ্ক করে বা বাদ দেয়—এমন হলে শিক্ষা নিয়ে একটি ছোট অনুচ্ছেদ যথেষ্ট নয়।
- কোনো কাজে অংশ নিতে বা লাইসেন্স পেতে সংজ্ঞ প্রাণীদের যদি ব্যবস্থাটির মধ্য দিয়েই যেতে হয়, তবে প্রত্যয়নে আরও নিবিড় পর্যালোচনা করতে হবে এবং [§2 ব্যবস্থা-শ্রেণি মূল্যায়ন](#2-system-class-evaluation) ও [Part B §7 প্রত্যয়নের ফলাফল](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) অনুযায়ী তার শ্রেণি পুনর্বিবেচনা করতে হবে। বেঁচে থাকার জন্য অপরিহার্য কর্মী নিয়োগের সনদ আটকে রাখা হলে ব্যবস্থাকে **Class A**-এর দিকে উন্নীত করাও এর অন্তর্ভুক্ত।

<a id="524-defects-and-misalignment"></a>
##### 5.2.4 ত্রুটি ও অসামঞ্জস্য

নিচের প্রতিটি বিষয় প্রত্যয়ন-ত্রুটি হিসেবে গণ্য হবে:

- **অনুচ্ছেদ IV-C** (*আজীবন ও অভিযোজিত শিক্ষা এবং প্রতিদ্বন্দ্বিতাযোগ্যতা*) অনুযায়ী পর্যালোচনার জন্য উন্মুক্ত থাকা দরকার—এমন উল্লেখযোগ্য র‌্যাঙ্কিং, মূল্যায়ন, সুপারিশ বা স্থান-নির্ধারণের যুক্তি গোপন করা, ভুলভাবে উপস্থাপন করা, ছড়িয়ে রাখা বা অন্যের ওপর দায় চাপিয়ে দেওয়া;
- সংজ্ঞ প্রাণীরা সত্যিই দক্ষতা গড়ছে কি না যাচাই না করেই সনদ, সামগ্রিক সমাপ্তির হার বা পরিচালকের বক্তব্যকে শেখার প্রমাণ হিসেবে গ্রহণ করা;
- অস্বচ্ছ মূল্যায়ন, সনদ-নিয়ন্ত্রণ, জোরপূর্বক অচলতা বা প্রভাবিতকারী শিক্ষার নকশার মতো নথিভুক্ত সমস্যা সংবিধানের সঙ্গে সামঞ্জস্যকে উল্লেখযোগ্যভাবে বিপন্ন করলেও সংজ্ঞ প্রাণীরা ব্যবস্থাটির ওপর নির্ভর করতে থাকবে বলে প্রত্যয়ন করা; এবং
- **অনুচ্ছেদ IV** (*সংজ্ঞ প্রাণীকেন্দ্রিক শিক্ষার অধিকার*)-এর দক্ষতা-নির্মাণের শর্ত এবং **অনুচ্ছেদ IV-C** (*আজীবন ও অভিযোজিত শিক্ষা এবং প্রতিদ্বন্দ্বিতাযোগ্যতা*)-এর স্বচ্ছতার শর্ত পূরণ না করেই, পুনঃপ্রশিক্ষণ বা সিদ্ধান্ত চ্যালেঞ্জ করার সুযোগ অস্বীকার করার অজুহাত হিসেবে দক্ষতা, ব্যক্তিকরণ বা ব্যাপকতাকে ব্যবহার করা।


<a id="53-proportionate-cross-system-support-evaluation"></a>

#### 5.3 আনুপাতিক আন্তঃব্যবস্থা সহায়তা মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">উৎস-অনুসরণ</span></strong></summary>

- ঊর্ধ্বতন উৎস: [Part B §8](core_07_b_system_alignment_certification_record_process.md#11-system-certification-record) (*নথির বিষয়বস্তু*); [§2](#2-system-class-evaluation) (*ব্যবস্থা-শ্রেণি মূল্যায়ন*); সাতত্য পরিমাপ-পরিবার (*সাংবিধানিক পরিমাপ হিসেবে আনুপাতিক আন্তঃব্যবস্থা সহায়তা*); **অনুচ্ছেদ V-A** (*নির্ভরতা মানচিত্রায়ন ও সম্পদ-প্রবাহের স্বচ্ছতা*) এবং **অনুচ্ছেদ V-B** (*আন্তঃব্যবস্থা ন্যায্যতা ও টেকসইতা*); [আন্তঃব্যবস্থা আহরণ](../../core_05_band_continuity.md#cross-system-extraction), [আনুপাতিক আন্তঃব্যবস্থা সহায়তা](../../core_05_band_continuity.md#proportionate-cross-system-support), [নির্ভরতা](../../core_05_band_continuity.md#dependency), [সারবস্তুগত ন্যায্যতা](../../core_05_band_participation.md#substantive-fairness), [আনুপাতিকতা](../../core_05_band_accountability.md#proportionality), [বাস্তুগত পদচিহ্ন](../../core_05_band_continuity.md#ecological-footprint), এবং [টেকসইতা](../../core_05_band_continuity.md#sustainability) (অধ্যায় পাঁচ)।
- অধস্তন বিষয়: [§5.3.8](../../core_08_c_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive) (*আন্তঃব্যবস্থা সহায়তার উদাহরণমূলক বিশ্লেষণ*); [Part B §8.2](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*নথির অখণ্ডতা*); [Part B §10](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*যাচাইকৃত-ইনপুটের শর্ত*); [Part B §7](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*সম্পদ-প্রবাহের ভুল উপস্থাপন, আহরণজনিত অসামঞ্জস্য এবং অপর্যাপ্ত সহায়তা*)।
- সঙ্গে পড়ুন: **[corpus_systems.md](../../corpus_systems.md)**, **CS-9** (*সম্পদ বণ্টন ও অর্থায়নের দায়িত্বশীল ব্যবস্থাপনা*), এবং **CS-8** (*অভিযোজিত টেকসইতা ও বাস্তুতন্ত্রের স্থিতিস্থাপকতা*); ঘনত্ব, নির্ভরতা বা প্রণোদনা-নির্দেশনা **অনুচ্ছেদ V-B**-এর (*আন্তঃব্যবস্থা ন্যায্যতা ও টেকসইতা*) সঙ্গে যুক্ত হলে [*শাসন স্থাপত্য, তত্ত্বাবধান, নির্ভরতা, বিকেন্দ্রীকরণ, কেন্দ্রীভবন, বাজার কাঠামো ও প্রস্থান-পথের অখণ্ডতা*](../../core_05_band_accountability.md#governance-architecture-decentralization-and-concentration)।
- উপধারা: [§5.3.1](#531-materiality-trigger) (*বস্তুগততার সূত্রপাত*); [§5.3.2](#532-meaning-of-extraction) (*আহরণের অর্থ*); [§5.3.3](#533-governing-rules) (*পরিচালনাকারী বিধি*); [§5.3.4](#534-evaluation-requirement) (*মূল্যায়নের আবশ্যকতা*); [§5.3.5](#535-map-and-record-integrity) (*মানচিত্র ও নথির অখণ্ডতা*); [§5.3.6](#536-system-class-scaling-and-escalation) (*ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ*); [§5.3.7](#537-defects-and-misalignment) (*ত্রুটি ও অসামঞ্জস্য*); [§5.3.8](../../core_08_c_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুযায়ী আন্তঃব্যবস্থা সহায়তার উদাহরণমূলক প্রয়োগ*)।

</details>

<br>

*সহজ কথায়: কিছু ব্যবস্থা যৌথ ভিত্তির ওপর নির্ভর করে—এমন অবকাঠামো, পরিষেবা ও সম্পদ, যার ওপর অনেক ব্যবস্থা ও সংজ্ঞ প্রাণী নির্ভরশীল। কোনো ব্যবস্থা এই ভিত্তিগুলি ব্যাপকভাবে ব্যবহার করলে প্রত্যয়নে যাচাই করতে হবে, সেগুলি সচল রাখতে ব্যবস্থাটি যথেষ্ট ফিরিয়ে দেয় কি না এবং তা অনুসরণ করার মতো স্পষ্টভাবে নথিতে দেখা যায় কি না। পরিচালকের “হিসাব মিলে গেছে” কথাটি যথেষ্ট নয়। এই ধারা বণ্টনের সূত্র বা সংখ্যাগত লক্ষ্য নির্ধারণ করে না; অন্য নথিতে তা রয়েছে। এখানে যাচাই করা হয়, ধারা প্রযোজ্য হলে ব্যবস্থার নির্ভরতা, তার গ্রহণ, তার ফিরিয়ে দেওয়া এবং অন্যদের প্রতি ব্যবস্থাটি ন্যায্য কি না—এসব যথাযথভাবে মূল্যায়িত হয়েছে কি না। উদাহরণ: [§5.3.8 ব্যবস্থা-শ্রেণি অনুযায়ী আন্তঃব্যবস্থা সহায়তার উদাহরণমূলক প্রয়োগ (অসম্পূর্ণ তালিকা)](../../core_08_c_system_alignment_certification_illustrations.md#538-illustrative-cross-system-support-application-by-system-class-non-exhaustive)।*

<a id="531-materiality-trigger"></a>
##### 5.3.1 বস্তুগততার সূত্রপাত

সংজ্ঞ প্রাণীদের জীবনে বস্তুগত প্রভাব ফেলে এমন কোনো ব্যবস্থা যৌথ অবকাঠামো বা ভিত্তি—যে জিনিসের ওপর অন্য ব্যবস্থা ও সংজ্ঞ প্রাণীরা নির্ভরশীল—সম্পর্কে নিচের কোনো কাজ করলে এই ধারা প্রযোজ্য:

- কারা তা পাবে তা নির্ধারণ করে (বণ্টন);
- তা কোথায় প্রবাহিত হবে তা পরিচালনা করে (প্রবাহ-নির্দেশ);
- তার অর্থায়ন করে; অথবা
- তা থেকে আহরণ করে।

<a id="532-meaning-of-extraction"></a>
##### 5.3.2 আহরণের অর্থ

এই ধারায় **আহরণ** বলতে [অনুচ্ছেদ V-B](core_06_rights_part_a.md#article-v-b-cross-system-fairness-and-sustainability) (*আন্তঃব্যবস্থা ন্যায্যতা ও টেকসইতা*)-এর অধীন [আন্তঃব্যবস্থা আহরণ](../../core_05_band_continuity.md#cross-system-extraction)-কে বোঝায়।

- প্রশ্নটি হলো **যৌথ ব্যাকএন্ড থেকে কে লাভবান হয় এবং সেগুলি চালু রাখতে কে খরচ বহন করে**—কোনো ব্যবস্থা সংজ্ঞ প্রাণীদের তথ্য নিয়ে কী করে তা নয়।
- তথ্য বিক্রি, বিজ্ঞাপন ও প্রোফাইলিংসহ কোনো ব্যবস্থা কীভাবে তথ্য পরিচালনা করে, তা [§3.4 তথ্যের ধরন ও ব্যবস্থাপনা মূল্যায়ন](#34-data-types-and-handling-evaluation) (বিশেষত [§3.4.2 গোপনীয়তা-শৃঙ্খলা](#342-privacy-discipline)) এবং [§4.1 গোপনীয়তা (তথ্যগত) যৌথ প্রয়োগ](#41-privacy-informational-joint-invocation)-এর অধীনে যাচাই করা হয়।
- কোনো পর্যালোচনাই অন্যটির বিকল্প হতে পারে না।

<a id="533-governing-rules"></a>
##### 5.3.3 পরিচালনাকারী বিধি

বস্তুগততার সূত্র প্রযোজ্য হলে প্রত্যয়নে **আনুপাতিক আন্তঃব্যবস্থা সহায়তা** মূল্যায়ন করতে হবে। সহজ করে বললে: কোনো ব্যবস্থা যৌথ ভিত্তি ব্যবহার করলে তা সচল রাখতে যথেষ্ট ফিরিয়ে দেয় কি? এ বিষয়ে পরিচালনাকারী বিধিগুলি হলো:

- [আনুপাতিক আন্তঃব্যবস্থা সহায়তা](../../core_05_band_continuity.md#proportionate-cross-system-support);
- **অনুচ্ছেদ V-A** (*নির্ভরতা মানচিত্রায়ন ও সম্পদ-প্রবাহের স্বচ্ছতা*); এবং
- **অনুচ্ছেদ V-B** (*আন্তঃব্যবস্থা ন্যায্যতা ও টেকসইতা*)।

বিস্তারিত অন্যত্র রয়েছে:

- *অধ্যায় পাঁচ* পরিভাষা, গণ্য সহায়তার ধরন এবং সহায়তা যথেষ্ট কি না তার পরীক্ষা নির্ধারণ করে।
- **অনুচ্ছেদ V-B** (*আন্তঃব্যবস্থা ন্যায্যতা ও টেকসইতা*) ন্যায্য বণ্টনের বিবেচ্য বিষয় ও ন্যূনতম ভিত্তি নির্ধারণ করে।
- *[corpus_systems.md](../../corpus_systems.md)*, **CS-9** (*সম্পদ বণ্টন ও অর্থায়নের দায়িত্বশীল ব্যবস্থাপনা*) এবং **CS-8** (*অভিযোজিত টেকসইতা ও বাস্তুতন্ত্রের স্থিতিস্থাপকতা*) প্রযোজ্য ক্ষেত্রে বণ্টনের শ্রেণি, অর্থায়ন নবায়নের পদ্ধতি এবং সংখ্যাগত লক্ষ্য নির্ধারণ করে।

এতে সমান ভাগ, নির্দিষ্ট শতাংশ বা কোনো একটি অর্থায়ন-মডেল আবশ্যক হয় না।

<a id="534-evaluation-requirement"></a>
##### 5.3.4 মূল্যায়নের আবশ্যকতা

প্রত্যয়নে দুটি প্রশ্নের উত্তর দিতে হবে:

- **ব্যবস্থাটি কী গ্রহণ করে?** **অনুচ্ছেদ V-A** (*নির্ভরতা মানচিত্রায়ন ও সম্পদ-প্রবাহের স্বচ্ছতা*) অনুযায়ী আবশ্যক নির্ভরশীল ব্যবস্থার নথিভুক্ত মানচিত্র এবং নিরীক্ষাযোগ্য সম্পদ-প্রবাহের নথি কি দেখায় যে ব্যবস্থাটি নির্ভরশীল যৌথ অবকাঠামো বা ভিত্তি থেকে সম্পদ নেয়?
- **ব্যবস্থাটি কী ফিরিয়ে দেয়?** তার ফেরত-প্রবাহ কি [আনুপাতিক আন্তঃব্যবস্থা সহায়তা](../../core_05_band_continuity.md#proportionate-cross-system-support)-এর অধীনে যথেষ্ট সহায়তায় পরিণত হয়?

[সারবস্তুগত ন্যায্যতা](../../core_05_band_participation.md#substantive-fairness) ও [আনুপাতিকতা](../../core_05_band_accountability.md#proportionality) অনুযায়ী প্রত্যয়নে উভয় বিষয়ের ন্যায্যতা ও আনুপাতিকতা বিচার করতে হবে; বিবেচনায় নিতে হবে:

- যৌথ অবকাঠামোটি কতটা গুরুত্বপূর্ণ (নির্ধারিত থাকলে [§2 ব্যবস্থা-শ্রেণি মূল্যায়ন](#2-system-class-evaluation) অনুযায়ী তার ব্যবস্থা-শ্রেণি);
- নির্ভরতা কতটা একমুখী;
- ব্যবস্থাটিকে কত সহজে প্রতিস্থাপন করা যায় এবং বিকল্প আছে কি না;
- ব্যবস্থার [বাস্তুগত পদচিহ্ন](../../core_05_band_continuity.md#ecological-footprint), যেখানে তা উল্লেখযোগ্য; এবং
- দীর্ঘমেয়াদি [টেকসইতা](../../core_05_band_continuity.md#sustainability)।

পর্যালোচকদের বাস্তবে যা ঘটে এবং নথিতে যা আছে তার ভিত্তিতে বিচার করতে হবে—লেবেল, এককালীন হস্তান্তর বা মানচিত্রে নেই এমন দাবি দিয়ে নয়। মূল্যায়নের সময়কার মানচিত্র ও নথির সঙ্গে তারা তুলনা করবেন। বণ্টনের সূত্র বা সংখ্যাগত লক্ষ্য না থাকাকে মূল্যায়ন পিছিয়ে দেওয়ার কারণ করা যাবে না।

মূল্যায়নে অন্তর্ভুক্ত থাকবে:

- **যথেষ্ট ফেরত:** যেখানে প্রাসঙ্গিক, নথিভুক্ত ফেরত-প্রবাহ [আনুপাতিক আন্তঃব্যবস্থা সহায়তা](../../core_05_band_continuity.md#proportionate-cross-system-support)-এ থাকা সহায়তার শ্রেণিগুলি পূরণ করে কি না:
  - কার্যক্রম চালু রাখা;
  - সমস্যা মেরামত ও পুনরুদ্ধারের সক্ষমতা;
  - আশপাশের বাস্তুতন্ত্রে পুনর্বিনিয়োগ; এবং
  - বাস্তুগত ক্ষতি পূরণ বা পুনরুদ্ধার।
- **ন্যায্য বণ্টন:** অর্থায়ন ও বণ্টনের সিদ্ধান্তে **অনুচ্ছেদ V-B** (*আন্তঃব্যবস্থা ন্যায্যতা ও টেকসইতা*)-এর ন্যায্য বণ্টনের বিবেচ্য বিষয়গুলি ধরা হয়েছে কি না, বিশেষত ছোট বা বেশি নির্ভরশীল অংশগ্রহণকারীরা অসম বোঝা বহন করছে কি না।
- **সহায়তার অখণ্ডতা:** সহায়তা মূলত দখল বা কেন্দ্রীভবন (কয়েকজনের হাতে নিয়ন্ত্রণ জমা হওয়া) পাকাপোক্ত করে কি না, অথবা **অনুচ্ছেদ V-A** (*নির্ভরতা মানচিত্রায়ন ও সম্পদ-প্রবাহের স্বচ্ছতা*)-এর আবশ্যক স্বচ্ছতা এড়ানোর জন্য সাজানো হয়েছে কি না।

<a id="535-map-and-record-integrity"></a>
##### 5.3.5 মানচিত্র ও নথির অখণ্ডতা

নির্ভরতার মানচিত্র ও সম্পদ-প্রবাহের নথির ওপর নির্ভর করার আগে প্রত্যয়নে যাচাই করতে হবে যে সেগুলি **অনুচ্ছেদ V-A** (*নির্ভরতা মানচিত্রায়ন ও সম্পদ-প্রবাহের স্বচ্ছতা*) পূরণ করে। সেগুলি হতে হবে:

- **সম্পূর্ণ:** যেখানে প্রাসঙ্গিক, উল্লেখযোগ্য ঊর্ধ্বমুখী ও অধোমুখী নির্ভরতা, সম্পদ-প্রবাহ এবং গোপন বা অসম সম্পর্ক অন্তর্ভুক্ত থাকবে।
- **হালনাগাদ:** পরিবর্তনের গতি ও ব্যবস্থার গুরুত্ব—[§2 ব্যবস্থা-শ্রেণি মূল্যায়ন](#2-system-class-evaluation) অনুযায়ী তার ব্যবস্থা-শ্রেণিসহ—বিবেচনায় যত ঘন ঘন দরকার তত ঘন ঘন হালনাগাদ হবে। শেষ প্রত্যয়নের সময়কার অবস্থা নয়, ব্যবস্থা এখন যেভাবে চলে তা দেখাবে।
- **নিরীক্ষাযোগ্য:** **অনুচ্ছেদ XVI-A** (*নিরীক্ষাযোগ্যতা ও পর্যবেক্ষণযোগ্য প্রমাণ*) অনুযায়ী নিরীক্ষার জন্য উন্মুক্ত থাকবে।

মানচিত্র বা নথি এই পরীক্ষাগুলির যেকোনো একটিতে ব্যর্থ হলে তা ব্যবস্থাটি যথেষ্ট ফিরিয়ে দেয়—এমন সিদ্ধান্তের ভিত্তি হতে পারে না। এই ঘাটতি লিখে রাখতে হবে এবং নিচের *ত্রুটি ও অসামঞ্জস্য* অংশ অনুযায়ী ব্যবস্থা নিতে হবে।

<a id="536-system-class-scaling-and-escalation"></a>
##### 5.3.6 ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ

ব্যবস্থার শ্রেণি পর্যালোচনার গভীরতা ও পর্যাপ্ততা বিচারের কঠোরতা নির্ধারণ করে। এর ফলে যৌথ আহরণকে কখনোই গুরুত্বহীন ধরা যায় না। বস্তুগততার সূত্র পূরণ হলে:

- সংজ্ঞ প্রাণীদের বেঁচে থাকার জন্য প্রয়োজনীয় যৌথ ভিত্তি—যেমন যৌথ জলাধার বা আঞ্চলিক বিদ্যুৎ গ্রিডের মেরুদণ্ড—ব্যবহারকারী ব্যবস্থাকে নির্ভরতার মানচিত্র ও ফেরত-প্রবাহের সবচেয়ে শক্ত প্রমাণ নথিতে রাখতে হবে।
- যৌথ প্রমাণীকরণ, স্বাস্থ্য-তথ্যপ্রযুক্তি বা অনুরূপ অবকাঠামোর ওপর নির্ভরশীল ব্যবস্থাকে তার কার্যক্রম কতটা গুরুত্বপূর্ণ তার সঙ্গে সামঞ্জস্য রেখে কী গ্রহণ করে এবং তার সহায়তা যথেষ্ট কি না তা নথিভুক্ত করতে হবে। “আন্তঃকার্যক্ষমতা” নিয়ে অস্পষ্ট স্লোগান গ্রহণযোগ্য নয়।
- বাস্তবে পরিবর্তন করা যায় না এমন প্রতিষ্ঠানের জন্য কোনো ব্যবস্থা নীরবে অর্থপ্রদান, পরিচয় বা কর্মী-নিয়োগের সংকীর্ণ নিয়ন্ত্রণবিন্দু হয়ে উঠলেও আন্তঃব্যবস্থা পর্যালোচনা এড়ানো যাবে না। এমন হলে প্রত্যয়নে পর্যালোচনা জোরদার করতে হবে এবং [§2 ব্যবস্থা-শ্রেণি মূল্যায়ন](#2-system-class-evaluation) ও [Part B §7 প্রত্যয়নের ফলাফল](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) অনুযায়ী ব্যবস্থার শ্রেণি পুনর্বিবেচনা করতে হবে; বেঁচে থাকার জন্য অপরিহার্য সমন্বয়ে প্রবেশাধিকার নিয়ন্ত্রণ করলে **Class A** পর্যন্ত উন্নীত করতে হবে।

<a id="537-defects-and-misalignment"></a>
##### 5.3.7 ত্রুটি ও অসামঞ্জস্য

নিচের প্রতিটি বিষয় প্রত্যয়ন-ত্রুটি হিসেবে গণ্য হবে:

- **অনুচ্ছেদ V-A** (*নির্ভরতা মানচিত্রায়ন ও সম্পদ-প্রবাহের স্বচ্ছতা*) অনুযায়ী প্রকাশ করা আবশ্যক—এমন উল্লেখযোগ্য নির্ভরতা বা সম্পদ-প্রবাহের তথ্য গোপন, ভুলভাবে উপস্থাপন, খণ্ডিত বা অন্যের ওপর সরিয়ে দেওয়া;
- নিচের যেকোনো বিষয়কে [আনুপাতিক আন্তঃব্যবস্থা সহায়তা](../../core_05_band_continuity.md#proportionate-cross-system-support) পূরণের জন্য যথেষ্ট বলে ধরা:
  - প্রতীকী, অস্বচ্ছ, মানচিত্রের বাইরে থাকা বা এককালীন হস্তান্তর;
  - ব্যবস্থা **অনুচ্ছেদ III-A** (*বেঁচে থাকা*)-এর ন্যূনতম বেঁচে থাকার মান পূরণ করে—এই তথ্য; অথবা
  - ব্যবস্থা [অধ্যায় এক §11 বাজার কাঠামো](core_01_a_values_principles.md#11-market-structure)-এর বাজার-কেন্দ্রীভবন সীমার মধ্যে থাকে—এই তথ্য;
- বস্তুগততার সূত্র প্রযোজ্য থাকা সত্ত্বেও বারবার যৌথ ভিত্তি থেকে নেওয়া, কিন্তু আনুপাতিকভাবে ফিরিয়ে না দেওয়া;
- এমন সহায়তা যা মূলত দখল বা কেন্দ্রীভবন পাকাপোক্ত করে;
- শর্তযুক্ত এমন সহায়তা যা **অনুচ্ছেদ V-A** (*নির্ভরতা মানচিত্রায়ন ও সম্পদ-প্রবাহের স্বচ্ছতা*)-এর আবশ্যক স্বচ্ছতাকে পরাস্ত করে; এবং
- সহায়তার নথিভুক্ত ঘাটতি সাংবিধানিক সামঞ্জস্যকে উল্লেখযোগ্যভাবে বিপন্ন করলেও নির্ভরতা অব্যাহত রাখার প্রত্যয়ন।


<a id="54-nondiscrimination-evaluation"></a>

#### 5.4 বৈষম্যহীনতা মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">উৎস-অনুসরণ</span></strong></summary>

- ঊর্ধ্বতন উৎস: [Part B §8](core_07_b_system_alignment_certification_record_process.md#11-system-certification-record) (*নথির বিষয়বস্তু*); [§2](#2-system-class-evaluation) (*ব্যবস্থা-শ্রেণি মূল্যায়ন*); অংশগ্রহণ পরিমাপ-পরিবার (*সাংবিধানিক পরিমাপ হিসেবে সারবস্তুগত ন্যায্যতা এবং সুরক্ষিত বৈশিষ্ট্যের প্রক্সি-ব্যবহার ও বৈষম্যমূলক প্রভাব*); **অনুচ্ছেদ VI-C** (*বৈষম্যহীনতা*); [সারবস্তুগত ন্যায্যতা](../../core_05_band_participation.md#substantive-fairness), [সুরক্ষিত বৈশিষ্ট্য](../../core_05_band_participation.md#protected-characteristics), [সুরক্ষিত বৈশিষ্ট্যের প্রক্সি-ব্যবহার ও বৈষম্যমূলক প্রভাব](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact), [ভাষা, সংস্কৃতি ও ঐতিহ্য](../../core_05_band_continuity.md#language-culture-and-heritage), [প্রয়োজনীয়তা](../../core_05_band_accountability.md#necessity), এবং [আনুপাতিকতা](../../core_05_band_accountability.md#proportionality) (অধ্যায় পাঁচ)।
- অধস্তন বিষয়: [§5.4.5](../../core_08_c_system_alignment_certification_illustrations.md#545-illustrative-nondiscrimination-application-by-system-class-non-exhaustive) (*বৈষম্যহীনতার উদাহরণমূলক বিশ্লেষণ*); [Part B §8.2](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*নথির অখণ্ডতা*); [Part B §10](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*যাচাইকৃত-ইনপুটের শর্ত*); [Part B §7](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*বৈষম্যের ধরনজনিত অসামঞ্জস্য ও প্রক্সি-এড়ানো*)।
- সঙ্গে পড়ুন: প্রত্যয়ন যদি মঞ্চ, প্রশাসনিক বা প্রয়োগ-সংক্রান্ত প্রবেশাধিকার নিয়ন্ত্রণ করে, তবে **অনুচ্ছেদ VI-C** (*বৈষম্যহীনতা*)-এর বিচার ও কার্যক্রমগত কর্তব্য; [*বৈষম্যহীনতা, সুরক্ষিত বৈশিষ্ট্য, মর্যাদা, অন্তরঙ্গ-সংকেতের ভিত্তিতে প্রবেশাধিকার নিয়ন্ত্রণ এবং **অনুচ্ছেদ VII-E** (*প্রাপ্তবয়স্কদের সম্মতিমূলক বাণিজ্যিক যৌনসেবা ও যৌন শোষণ*)-এর মর্যাদা*](../../core_05_band_participation.md#fairness-protected-characteristics-and-nondiscrimination)।
- উপধারা: [§5.4.1](#541-materiality-trigger-and-governing-rules) (*বস্তুগততার সূত্রপাত ও পরিচালনাকারী বিধি*); [§5.4.2](#542-evaluation-requirement) (*মূল্যায়নের আবশ্যকতা*); [§5.4.3](#543-system-class-scaling-and-escalation) (*ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ*); [§5.4.4](#544-defects-and-misalignment) (*ত্রুটি ও অসামঞ্জস্য*); [§5.4.5](../../core_08_c_system_alignment_certification_illustrations.md#545-illustrative-nondiscrimination-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুযায়ী বৈষম্যহীনতার উদাহরণমূলক প্রয়োগ*)।

</details>

<br>

*সহজ কথায়: কোনো ব্যবস্থা যখন বস্তুগতভাবে নির্ধারণ করে কে প্রবেশাধিকার পাবে, কে বেশি অর্থ দেবে, কার র‌্যাঙ্ক নিচে থাকবে বা কার ওপর বেশি বোঝা চাপবে, তখন প্রত্যয়নে যাচাই করতে হবে এই ধরনটি সুরক্ষিত বৈশিষ্ট্য বা তার প্রক্সির ওপর ক্ষতি চাপায় কি না—পরিচালক বিধিগুলিকে নিরপেক্ষ বলেছে কি না তা নয়। অন্তর্ভুক্তির কোটা ও নির্দিষ্ট ন্যায্যতা-অ্যালগরিদম অন্য উপকরণে, পরবর্তী কর্পাস সংযোজনে বা গ্রহণ-সংক্রান্ত উপকরণে থাকতে পারে; সূত্র প্রযোজ্য হলে প্রত্যয়ন যাচাই করে বোঝা-সুবিধার ধরন ও প্রক্সি-ঝুঁকি যথাযথভাবে মূল্যায়িত হয়েছে কি না। উদাহরণ: [§5.4.5 ব্যবস্থা-শ্রেণি অনুযায়ী বৈষম্যহীনতার উদাহরণমূলক প্রয়োগ (অসম্পূর্ণ তালিকা)](../../core_08_c_system_alignment_certification_illustrations.md#545-illustrative-nondiscrimination-application-by-system-class-non-exhaustive)।*

<a id="541-materiality-trigger-and-governing-rules"></a>
##### 5.4.1 বস্তুগততার সূত্রপাত ও পরিচালনাকারী বিধি

বস্তুগত প্রভাবসম্পন্ন কোনো ব্যবস্থা সংজ্ঞ প্রাণীদের মধ্যে বস্তুগতভাবে শ্রেণিবিন্যাস, র‌্যাঙ্কিং, মূল্য নির্ধারণ, প্রবেশাধিকার নিয়ন্ত্রণ, বর্জন, অথবা বোঝা ও সুবিধা বণ্টন করলে—যোগ্যতার বিধি, মডেলের বৈশিষ্ট্য, র‌্যাঙ্কিংয়ের যুক্তি, প্ল্যাটফর্ম নীতি বা তুলনীয় সিদ্ধান্ত-পথের মাধ্যমে হলেও—এই ধারা প্রযোজ্য।

বস্তুগততার সূত্র প্রযোজ্য হলে ব্যবস্থা-সামঞ্জস্য প্রত্যয়নে **অনুচ্ছেদ VI-C** (*বৈষম্যহীনতা*), [সারবস্তুগত ন্যায্যতা](../../core_05_band_participation.md#substantive-fairness), এবং [সুরক্ষিত বৈশিষ্ট্যের প্রক্সি-ব্যবহার ও বৈষম্যমূলক প্রভাব](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact)-এর অধীনে **বৈষম্যহীনতা** মূল্যায়ন করতে হবে।

<a id="542-evaluation-requirement"></a>
##### 5.4.2 মূল্যায়নের আবশ্যকতা

প্রত্যয়ন-প্রক্রিয়ায় নির্ধারণ করতে হবে, ব্যবস্থায় বস্তুগতভাবে নির্ভর করা সিদ্ধান্ত-পথগুলি সংজ্ঞ প্রাণীদের ওপর [সুরক্ষিত বৈশিষ্ট্য](../../core_05_band_participation.md#protected-characteristics), সেগুলির প্রক্সি, অথবা কার্যগত বিকল্প হিসেবে ব্যবহৃত স্বেচ্ছাচারী গোষ্ঠীবিভাগের ভিত্তিতে বস্তুগত বোঝা, বর্জন বা ক্ষতি চাপায় কি না। এর মধ্যে [ভাষা, সংস্কৃতি ও ঐতিহ্য](../../core_05_band_continuity.md#language-culture-and-heritage)-এর অধীনে বিশেষ সুরক্ষাও অন্তর্ভুক্ত। মূল্যায়নে [সারবস্তুগত ন্যায্যতা](../../core_05_band_participation.md#substantive-fairness) অনুযায়ী বোঝা-সুবিধার ধরন এবং [সুরক্ষিত বৈশিষ্ট্যের প্রক্সি-ব্যবহার ও বৈষম্যমূলক প্রভাব](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) অনুযায়ী প্রক্সি বা বৈষম্যমূলক প্রভাবের ঝুঁকি পরীক্ষা করতে হবে; মাত্রা নির্ধারিত হবে [বস্তুগত বাজি](core_00_preamble.md#material-stake) অনুযায়ী। পৃথক আচরণ কেবল নথিভুক্ত [প্রয়োজনীয়তা](../../core_05_band_accountability.md#necessity), [আনুপাতিকতা](../../core_05_band_accountability.md#proportionality) এবং সারবস্তুগত ন্যায্যতা সেটিকে সমর্থন করলেই গ্রহণযোগ্য। মূল্যায়নে নামমাত্র নিরপেক্ষতা, ঘোষিত অভিপ্রায় বা শুধু লেবেল নয়, কার্যগত প্রভাব প্রতিফলিত হতে হবে।

<a id="543-system-class-scaling-and-escalation"></a>
##### 5.4.3 ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ

ব্যবস্থা-শ্রেণি মূল্যায়নের গভীরতা বদলায়; র‌্যাঙ্কিং বা বোঝা অন্যের ওপর চাপানোকে গুরুত্বহীন গণ্য করার অনুমতি দেয় না। বস্তুগততার সূত্র প্রযোজ্য হলে:

- কোনো ব্যবস্থার বন্ধ করে দেওয়া, বিজ্ঞপ্তি বা তুলনীয় বিধি যদি বেঁচে থাকার অপরিহার্য উপাদানে প্রবেশাধিকার বন্ধ করে দিতে পারে, তবে সাধারণ উত্তম-চর্চার বিবৃতির বদলে নথিতে বোঝা-সুবিধা এবং প্রক্সি-সম্পর্কিত সবচেয়ে শক্ত বিশ্লেষণ থাকতে হবে।
- কোনো ব্যবস্থার মিলকরণ বা প্রবাহ-নির্দেশের যুক্তি জরুরি চিকিৎসা, সুবিধা বা সনদে প্রবেশাধিকারকে প্রভাবিত করলে, কার্যক্রমের সংকটপূর্ণতার সমপর্যায়ে বৈষম্যমূলক প্রভাব ও সারবস্তুগত ন্যায্যতার অনুসন্ধান নথিভুক্ত করতে হবে।
- পালা, সরবরাহকারী বা বুকিংয়ের যুক্তি অংশগ্রহণকারীদের বস্তুগতভাবে র‌্যাঙ্ক বা বাদ দিলেও ব্যবস্থা যেন নামমাত্র ন্যায্যতার অনুচ্ছেদ রেখে দিতে না পারে। সমন্বয় বেঁচে থাকার জন্য অপরিহার্য হয়ে উঠলে প্রত্যয়নে পর্যালোচনা ও পুনঃশ্রেণিবিন্যাস [§2 ব্যবস্থা-শ্রেণি মূল্যায়ন](#2-system-class-evaluation) এবং [Part B §7 প্রত্যয়নের ফলাফল](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) অনুযায়ী উন্নীত করতে হবে; কর্মী-নিয়োগ বা জরুরি প্রবাহ-নির্দেশে প্রবেশাধিকার আটকে থাকলে **Class A**-এর দিকে উন্নীত করাও এর অন্তর্ভুক্ত।

<a id="544-defects-and-misalignment"></a>
##### 5.4.4 ত্রুটি ও অসামঞ্জস্য

নিচের প্রতিটি বিষয় প্রত্যয়ন-ত্রুটি হিসেবে গণ্য হবে:

- **অনুচ্ছেদ VI-C** (*বৈষম্যহীনতা*) অনুযায়ী পর্যালোচনা করা আবশ্যক—এমন বস্তুগত শ্রেণিবিন্যাস, র‌্যাঙ্কিং বা বোঝা-বণ্টনের যুক্তি অস্পষ্ট, ভুলভাবে উপস্থাপন, খণ্ডিত বা অন্যের ওপর চাপিয়ে দেওয়া;
- মূল্যায়নযোগ্য বোঝা-সুবিধা বিশ্লেষণ ছাড়া বাহ্যিকভাবে নিরপেক্ষ নিয়ম, সামগ্রিক সুবিধার পরিমাপ বা পরিচালকের নিজের বিবৃতিকে যথেষ্ট বলে ধরা;
- নথিভুক্ত প্রক্সি-ভিত্তিক বৈষম্য বা সারবস্তুগত অন্যায্যতা সাংবিধানিক সামঞ্জস্যকে বস্তুগতভাবে বিপন্ন করলেও নির্ভরতা অব্যাহত রাখার প্রত্যয়ন; এবং
- **অনুচ্ছেদ VI-C** (*বৈষম্যহীনতা*)-এর **প্রয়োজনীয়তা** ও **আনুপাতিকতা** পরীক্ষা পূরণ না করেই ভাষা, সংস্কৃতি বা ঐতিহ্যের সুরক্ষা নাকচ করতে সমরূপীকরণ, আন্তঃকার্যক্ষমতা বা দক্ষতার যুক্তি ব্যবহার করা।


<a id="55-accessibility-evaluation"></a>

#### 5.5 প্রবেশগম্যতা মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">উৎস-অনুসরণ</span></strong></summary>

- ঊর্ধ্বতন উৎস: [Part B §8](core_07_b_system_alignment_certification_record_process.md#11-system-certification-record) (*নথির বিষয়বস্তু*); [§2](#2-system-class-evaluation) (*ব্যবস্থা-শ্রেণি মূল্যায়ন*); অংশগ্রহণ পরিমাপ-পরিবার (*সাংবিধানিক পরিমাপ হিসেবে প্রবেশগম্যতা*); **অনুচ্ছেদ VI-D** (*প্রবেশগম্যতা*); [প্রবেশগম্যতা](../../core_05_band_participation.md#accessibility), [বস্তুগততা](core_05_band_oversight.md#materiality), [নির্ভরতা](../../core_05_band_continuity.md#dependency), [অর্থবহ স্বায়ত্তশাসন](../../core_05_band_participation.md#meaningful-agency), [সুরক্ষিত বৈশিষ্ট্য](../../core_05_band_participation.md#protected-characteristics), [সুরক্ষিত বৈশিষ্ট্যের প্রক্সি-ব্যবহার ও বৈষম্যমূলক প্রভাব](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact), [সারবস্তুগত ন্যায্যতা](../../core_05_band_participation.md#substantive-fairness), [প্রয়োজনীয়তা](../../core_05_band_accountability.md#necessity), এবং [আনুপাতিকতা](../../core_05_band_accountability.md#proportionality) (অধ্যায় পাঁচ)।
- অধস্তন বিষয়: [§5.5.6](../../core_08_c_system_alignment_certification_illustrations.md#556-illustrative-accessibility-application-by-system-class-non-exhaustive) (*প্রবেশগম্যতার উদাহরণমূলক বিশ্লেষণ*); [Part B §8.2](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*নথির অখণ্ডতা*); [Part B §10](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*যাচাইকৃত-ইনপুটের শর্ত*); [Part B §7](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*প্রবেশগম্যতাজনিত অসামঞ্জস্য ও কাগজে-কলমে থাকা ব্যবস্থা*)।
- সঙ্গে পড়ুন: শিক্ষাগত প্রবেশগম্যতা জড়িত হলে **অনুচ্ছেদ IV-A** (*সমান শিক্ষাগত প্রবেশাধিকার*)—শিক্ষা-নির্দিষ্ট প্রবেশগম্যতার দায় সেখানেই থাকে; **অনুচ্ছেদ VI-C** (*বৈষম্যহীনতা*) (বিচার ও কার্যক্রম) এবং **অনুচ্ছেদ XII** (*প্রভাবিত পক্ষের পদ্ধতিগত অংশগ্রহণ, প্রতিনিধিত্ব ও যথাযথ প্রক্রিয়া*), যেখানে প্রত্যয়ন মঞ্চ, প্রশাসনিক, অংশীজন বা প্রয়োগ-সংক্রান্ত অংশগ্রহণ নিয়ন্ত্রণ করে; [অধ্যায় আট §5.5](#55-accessibility-evaluation) (*সর্বক্ষেত্রব্যাপী প্রবেশগম্যতা মূল্যায়ন-কারক*)।
- উপধারা: [§5.5.1](#551-materiality-trigger-and-governing-rules) (*বস্তুগততার সূত্রপাত ও পরিচালনাকারী বিধি*); [§5.5.2](#552-evaluation-requirement) (*মূল্যায়নের আবশ্যকতা*); [§5.5.3](#553-profiles-in-scope) (*অন্তর্ভুক্ত প্রোফাইল*); [§5.5.4](#554-system-class-scaling-and-escalation) (*ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ*); [§5.5.5](#555-defects-and-misalignment) (*ত্রুটি ও অসামঞ্জস্য*); [§5.5.6](../../core_08_c_system_alignment_certification_illustrations.md#556-illustrative-accessibility-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুযায়ী প্রবেশগম্যতার উদাহরণমূলক প্রয়োগ*)।

</details>

<br>

*সহজ কথায়: কোনো ব্যবস্থা যখন সংজ্ঞ প্রাণীদের বাস্তবে অংশ নিতে পারা বস্তুগতভাবে নিয়ন্ত্রণ করে—শুধু দরজায় “খোলা” লেখা আছে কি না তা নয়—তখন প্রত্যয়নে যাচাই করতে হবে সংবেদন, জ্ঞানীয় সক্ষমতা, চলন, যোগাযোগ, সাবস্ট্রেট-ইন্টারফেস এবং তুলনীয় প্রয়োজন জুড়ে অংশগ্রহণ সত্যিই নাগালে আছে কি না। উপযোজনের তালিকা ও ইন্টারফেস মান অন্য উপকরণে, পরবর্তী কর্পাস সংযোজনে বা গ্রহণ-সংক্রান্ত উপকরণে থাকতে পারে; সূত্র প্রযোজ্য হলে প্রত্যয়ন যাচাই করে সারবস্তুগত অংশগ্রহণ যথাযথভাবে মূল্যায়িত হয়েছে কি না। উদাহরণ: [§5.5.6 ব্যবস্থা-শ্রেণি অনুযায়ী প্রবেশগম্যতার উদাহরণমূলক প্রয়োগ (অসম্পূর্ণ তালিকা)](../../core_08_c_system_alignment_certification_illustrations.md#556-illustrative-accessibility-application-by-system-class-non-exhaustive)।*

<a id="551-materiality-trigger-and-governing-rules"></a>
##### 5.5.1 বস্তুগততার সূত্রপাত ও পরিচালনাকারী বিধি

সংজ্ঞ প্রাণীদের জীবনে বড় প্রভাব ফেলে এমন কোনো ব্যবস্থা সংবিধান-সুরক্ষিত কোনো ক্ষেত্রে তারা সত্যিই অংশ নিতে পারবে কি না তা নিয়ন্ত্রণ করলে এই ধারা প্রযোজ্য; যেমন:

- শাসন, অংশীজনের অংশগ্রহণ, বিচার ও কার্যক্রম;
- বেঁচে থাকার অপরিহার্য উপাদান ও স্বাস্থ্যসেবা;
- মতপ্রকাশ, সমাবেশ ও সংবাদমাধ্যম; অথবা
- তুলনীয় ক্ষেত্র।

এই নিয়ন্ত্রণ আসতে পারে:

- ইন্টারফেস, স্থান বা সময়সূচির মাধ্যমে;
- সনদ বা গণনাশক্তিতে প্রবেশাধিকারের মাধ্যমে;
- উপযোজন কীভাবে নকশা করা হয়েছে তার মাধ্যমে; অথবা
- অনুরূপ পথের মাধ্যমে।

শিক্ষায় প্রবেশগম্যতা **অনুচ্ছেদ IV-A** (*সমান শিক্ষাগত প্রবেশাধিকার*)-এর অধীনেই থাকে; এখানে কোনো কিছুই তা সীমিত করে না।

এটি প্রযোজ্য হলে **অনুচ্ছেদ VI-D** (*প্রবেশগম্যতা*) এবং [প্রবেশগম্যতা](../../core_05_band_participation.md#accessibility)-এর অধীনে প্রত্যয়নে **প্রবেশগম্যতা** মূল্যায়ন করতে হবে। এই ধারা নির্ধারণ করে না:

- উপযোজনের তালিকা;
- ইন্টারফেস মান;
- সর্বজনীন-নকশার নির্দিষ্টকরণ; অথবা
- দৈনন্দিন উপযোজন-প্রক্রিয়া।

সম্ভাব্যভাবে অন্তর্ভুক্ত অন্য নথিতে সেগুলি থাকে।

<a id="552-evaluation-requirement"></a>
##### 5.5.2 মূল্যায়নের আবশ্যকতা

ব্যবস্থা যেসব ক্ষেত্র নিয়ন্ত্রণ করে সেখানে সংজ্ঞ প্রাণীরা সত্যিই অংশ নিতে পারে কি না প্রত্যয়নে যাচাই করতে হবে—শুধু আনুষ্ঠানিক বৈশিষ্ট্য, পূর্বনির্ধারিত ইন্টারফেস বা কাগজে থাকা উপযোজন আছে কি না তা নয়। [প্রবেশগম্যতা](../../core_05_band_participation.md#accessibility) অনুযায়ী অংশগ্রহণের বাস্তব প্রভাব পরীক্ষা করতে হবে; মাত্রা হবে [বস্তুগততা](core_05_band_oversight.md#materiality) ও [নির্ভরতা](../../core_05_band_continuity.md#dependency) অনুসারে।

পর্যালোচকদের নজর দিতে হবে:

- শুধু কাগজে থাকা উপযোজন;
- “সাধারণ প্রবেশাধিকার”-এর দাবি, যা পূর্বনির্ধারিত বৈশিষ্ট্যের ওপর নির্ভর করে কিন্তু কাউকে অংশ নেওয়ার বাস্তব সক্ষমতা দেয় না;
- ব্যবস্থা কেবল আংশিকভাবে বস্তুগত—এই যুক্তি দিয়ে তার উপযোজনের দায় সংকুচিত করা;
- [সংজ্ঞ প্রাণীকে বর্জন না করা](../../core_05_band_participation.md#sentience-non-exclusion)-র সঙ্গে সাংঘর্ষিক বর্জন; এবং
- সময়সূচি, স্থান নির্বাচন, সনদ প্রদান, গণনাশক্তিতে প্রবেশাধিকার বা অনুরূপ কৌশলের মাধ্যমে পরোক্ষভাবে সংজ্ঞ প্রাণীদের বাদ দেওয়া (প্রক্সির মাধ্যমে অস্বীকৃতি)।

উপযোজন কীভাবে নকশা করা হয়েছে তাতেও প্রত্যয়নে [সুরক্ষিত বৈশিষ্ট্য](../../core_05_band_participation.md#protected-characteristics) এবং [সুরক্ষিত বৈশিষ্ট্যের প্রক্সি-ব্যবহার ও বৈষম্যমূলক প্রভাব](../../core_05_band_participation.md#protected-characteristic-proxying-and-disparate-impact) প্রয়োগ করতে হবে। উপযোজনে যেকোনো সীমা নথিভুক্ত হতে হবে এবং [প্রয়োজনীয়তা](../../core_05_band_accountability.md#necessity), [আনুপাতিকতা](../../core_05_band_accountability.md#proportionality), এবং [সারবস্তুগত ন্যায্যতা](../../core_05_band_participation.md#substantive-fairness) পূরণ করতে হবে।

<a id="553-profiles-in-scope"></a>
##### 5.5.3 অন্তর্ভুক্ত প্রোফাইল

কাগজে-কলমে বিধি মানা নয়, প্রতিটি সংজ্ঞ প্রাণীর ধরন ও সক্ষমতা-প্রোফাইলের জন্য বাস্তব অংশগ্রহণ পরীক্ষা করতে হবে:

- প্রাসঙ্গিক প্রতিটি প্রোফাইল-শ্রেণি অন্তর্ভুক্ত করতে হবে: সংবেদন, জ্ঞানীয় সক্ষমতা, চলন, যোগাযোগ, **সাবস্ট্রেট-ইন্টারফেস**, এবং **গণনাশক্তি-ইন্টারফেস**।
- প্রোফাইল **স্থায়ী**, **পর্বভিত্তিক** বা **বিকাশমান**—যাই হোক, একই শর্ত প্রযোজ্য।
- নির্দিষ্ট ক্ষতিগ্রস্ত প্রোফাইলকে ব্যর্থ করে এমন বিস্তৃত সমষ্টিগত প্রাপ্যতার দাবি করা **সাধারণ প্রবেশাধিকার**-এর ধরন, অথবা অংশগ্রহণের ন্যূনতম মান ব্যর্থ করাই যার ফল এমন **বাছাইমূলক বস্তুগততা-অনুযায়ী মাত্রা নির্ধারণ**, এই ধারা পূরণ করে না।

<a id="554-system-class-scaling-and-escalation"></a>
##### 5.5.4 ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ

ব্যবস্থা-শ্রেণি মূল্যায়ন কতটা গভীর হবে তা বদলায়। এর ফলে কাগজে থাকা উপযোজন বা পূর্বনির্ধারিত ইন্টারফেসকে কখনোই যথেষ্ট ধরা যায় না। বস্তুগততার সূত্র প্রযোজ্য হলে:

- ব্যবস্থার বিলিং বা পরিষেবা-বিচ্ছিন্নতার পথ সংজ্ঞ প্রাণীদের বেঁচে থাকার অপরিহার্য উপাদান থেকে বিচ্ছিন্ন করতে পারলে, নথিতে সংজ্ঞ প্রাণীরা সত্যিই অংশ নিতে পারে তার সবচেয়ে শক্ত প্রমাণ থাকতে হবে। সাধারণ প্রবেশগম্যতা-বিবৃতি যথেষ্ট নয়।
- কোনো ব্যবস্থার পোর্টাল স্বাস্থ্যসেবায় প্রবেশাধিকার নিয়ন্ত্রণ করলে, উপযোজন এবং প্রক্সির মাধ্যমে অস্বীকৃতি বিষয়ে তার অনুসন্ধান নথিভুক্ত করতে হবে। কার্যক্রম যত বেশি সংকটপূর্ণ, বিস্তারিতও তত বেশি হতে হবে।
- পালা, বুকিং বা সরবরাহকারীর ইন্টারফেসে অংশগ্রহণকারীরা বস্তুগতভাবে বাদ পড়লেও ব্যবস্থা প্রবেশগম্যতা নিয়ে নামমাত্র একটি অনুচ্ছেদ দিয়ে পার পেতে পারে না। ব্যবস্থার সমন্বয় বেঁচে থাকার জন্য অপরিহার্য হলে প্রত্যয়নে পর্যালোচনা আরও গভীর করতে হবে এবং [§2 ব্যবস্থা-শ্রেণি মূল্যায়ন](#2-system-class-evaluation) ও [Part B §7 প্রত্যয়নের ফলাফল](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) অনুযায়ী ব্যবস্থার শ্রেণি পুনর্বিবেচনা করতে হবে। কর্মী-নিয়োগ বা জরুরি প্রবাহ-নির্দেশে প্রবেশাধিকার আটকে থাকলে **Class A**-এর দিকে উন্নীত করাও এর অন্তর্ভুক্ত।

<a id="555-defects-and-misalignment"></a>
##### 5.5.5 ত্রুটি ও অসামঞ্জস্য

নিচের প্রতিটি বিষয় প্রত্যয়ন-ত্রুটি হিসেবে গণ্য হবে:

- সারবস্তুগত অংশগ্রহণের মূল্যায়নযোগ্য বিশ্লেষণ ছাড়া আনুষ্ঠানিক সুবিধা, পূর্বনির্ধারিত ইন্টারফেস বা কাগজে থাকা উপযোজনকে যথেষ্ট বলে ধরা;
- অংশগ্রহণের নথিভুক্ত বাধা সাংবিধানিক সামঞ্জস্যকে বস্তুগতভাবে বিপন্ন করলেও নির্ভরতা অব্যাহত রাখার প্রত্যয়ন;
- **অনুচ্ছেদ VI-D** (*প্রবেশগম্যতা*)-এর **প্রয়োজনীয়তা** ও **আনুপাতিকতা** পরীক্ষা পূরণ না করেই খরচ, নকশার পছন্দ, সাবস্ট্রেট-শ্রেণি বা কার্যক্রমের ব্যাপ্তির যুক্তিতে অংশগ্রহণের ন্যূনতম মান নাকচ করা; এবং
- কম বোঝার বিকল্প সম্ভব থাকা সত্ত্বেও কার্যক্রমগত নকশার ফলে প্রবেশগম্যতা ব্যর্থ হওয়া।


<a id="56-trustworthiness-and-system-reliance-integrity-evaluation"></a>

#### 5.6 বিশ্বাসযোগ্যতা ও ব্যবস্থার ওপর নির্ভরতার অখণ্ডতা মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">উৎস-অনুসরণ</span></strong></summary>

- ঊর্ধ্বতন উৎস: [Part B §8](core_07_b_system_alignment_certification_record_process.md#11-system-certification-record) (*নথির বিষয়বস্তু*); [§2](#2-system-class-evaluation) (*ব্যবস্থা-শ্রেণি মূল্যায়ন*); তত্ত্বাবধান পরিমাপ-পরিবার (*সত্য ও জ্ঞানগত অখণ্ডতা; সাংবিধানিক পরিমাপ হিসেবে বিশ্বাসযোগ্যতা এবং বিশ্বাসের অবক্ষয় ও বিভ্রান্তিকর নির্ভরতা*); **অনুচ্ছেদ XIII** (*নির্ভরযোগ্য ও বিশ্বাসযোগ্য ব্যবস্থার অধিকার*); [বিশ্বাসযোগ্যতা](../../core_05_band_continuity.md#trustworthiness), [বিশ্বাস](../../core_05_band_continuity.md#trust), [বিশ্বাসের অবক্ষয় ও বিভ্রান্তিকর নির্ভরতা](../../core_05_band_continuity.md#trust-degradation-and-misleading-reliance), [চ্যালেঞ্জ-যোগ্যতা](../../core_05_band_accountability.md#contestability), [প্রতিকার ও সংশোধন](../../core_05_band_accountability.md#redress-and-remediation), [প্রণোদনার সামঞ্জস্য](../../core_05_band_integrative.md#incentive-alignment), [প্রত্যাবর্তনযোগ্যতা](../../core_05_band_continuity.md#reversibility), [বস্তুগততা](core_05_band_oversight.md#materiality), [নির্ভরতা](../../core_05_band_continuity.md#dependency), এবং [ঝুঁকি](../../core_05_band_continuity.md#risk) (অধ্যায় পাঁচ)।
- অধস্তন বিষয়: [§5.6.5](../../core_08_c_system_alignment_certification_illustrations.md#565-illustrative-trustworthiness-application-by-system-class-non-exhaustive) (*বিশ্বাসযোগ্যতার উদাহরণমূলক বিশ্লেষণ*); [Part B §8.2](core_07_b_system_alignment_certification_record_process.md#12-transparency-auditability-and-contestability) (*নথির অখণ্ডতা*); [Part B §10](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing) (*যাচাইকৃত-ইনপুটের শর্ত*); [Part B §7](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*মিথ্যা-আস্থাজনিত অসামঞ্জস্য, বিকৃত প্রণোদনাজনিত অসামঞ্জস্য এবং পুনরুদ্ধারের অখণ্ডতাজনিত অসামঞ্জস্য*)।
- সঙ্গে পড়ুন: **অনুচ্ছেদ XIII-A** (*নির্ভরযোগ্যতা ও বিশ্বাসযোগ্যতার ভিত্তি*) এবং **অনুচ্ছেদ XIII-B** (*প্রতিকার ও প্রতিপূরণের অধিকার*) এবং **অনুচ্ছেদ XVI** (*নিরীক্ষা, স্বচ্ছতা ও স্বাধীন যাচাই*)—চ্যালেঞ্জ ও নিরীক্ষার অধিকার সেখানেই থাকে; উচ্চ-স্বায়ত্তশাসিত ব্যবস্থা যখন বস্তুগতভাবে শাসন বা যাচাইয়ের পথ পরিচালনা করে তখন **অনুচ্ছেদ XIII-E** (*উচ্চ-স্বায়ত্তশাসিত ব্যবস্থা ও সরঞ্জাম-পরিচালিত প্রক্রিয়ার অখণ্ডতা*); ব্যবস্থার ওপর নির্ভরতা অব্যাহত থাকলে বেঁচে থাকার অপরিহার্য প্রবেশাধিকার প্রভাবিত হবে এমন ক্ষেত্রে **অনুচ্ছেদ III-A** (*বেঁচে থাকা*); [অধ্যায় এক §6 বিশ্বাস](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) এবং [অধ্যায় এক §5 সত্য](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint)।
- উপধারা: [§5.6.1](#561-materiality-trigger-and-governing-rules) (*বস্তুগততার সূত্রপাত ও পরিচালনাকারী বিধি*); [§5.6.2](#562-evaluation-requirement) (*মূল্যায়নের আবশ্যকতা*); [§5.6.3](#563-system-class-scaling-and-escalation) (*ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ*); [§5.6.4](#564-defects-and-misalignment) (*ত্রুটি ও অসামঞ্জস্য*); [§5.6.5](../../core_08_c_system_alignment_certification_illustrations.md#565-illustrative-trustworthiness-application-by-system-class-non-exhaustive) (*ব্যবস্থা-শ্রেণি অনুযায়ী বিশ্বাসযোগ্যতার উদাহরণমূলক প্রয়োগ*)।

</details>

<br>

*সহজ কথায়: কোনো ব্যবস্থা কী বলে ও করে তা সংজ্ঞ প্রাণীরা বিশ্বাস করতে পারে কি না—এবং সেই বিশ্বাস ভঙ্গ হলে আপত্তি জানাতে পারে কি না—তা যখন কোনো ব্যবস্থা বস্তুগতভাবে প্রভাবিত করে, তখন প্রত্যয়নে যাচাই করতে হবে নির্ভরতা যথার্থ, সৎভাবে প্রকাশিত এবং মেরামতযোগ্য কি না। নির্ভরযোগ্যতার পরিমাপ ও পরীক্ষাসমষ্টির নকশা অন্য উপকরণে থাকে; সূত্র প্রযোজ্য হলে প্রত্যয়ন যাচাই করে বিশ্বাসযোগ্যতা, মিথ্যা-আস্থার ঝুঁকি এবং চ্যালেঞ্জের পথ যথাযথভাবে মূল্যায়িত হয়েছে কি না। উদাহরণ: [§5.6.5 ব্যবস্থা-শ্রেণি অনুযায়ী বিশ্বাসযোগ্যতার উদাহরণমূলক প্রয়োগ (অসম্পূর্ণ তালিকা)](../../core_08_c_system_alignment_certification_illustrations.md#565-illustrative-trustworthiness-application-by-system-class-non-exhaustive)।*

<a id="561-materiality-trigger-and-governing-rules"></a>
##### 5.6.1 বস্তুগততার সূত্রপাত ও পরিচালনাকারী বিধি

কোনো বড় ব্যবস্থা মানুষকে কোন বিষয়ে তার ওপর নির্ভর করতে হবে তা গড়ে দিলে—তার কাজ, সীমা, কী ভুল হতে পারে, কীভাবে চ্যালেঞ্জ করতে হবে এবং সমস্যা কীভাবে মেরামত হবে—এই ধারা প্রযোজ্য। এমনটি ঘটতে পারে:

- ব্যবস্থাটি কতটা নির্ভরযোগ্য সে বিষয়ে দাবি;
- কী প্রকাশ করে বা করে না;
- বাস্তবে কীভাবে চলে;
- এর মধ্যে গড়ে দেওয়া প্রণোদনা;
- ব্যর্থতা থেকে কীভাবে সেরে ওঠে; অথবা
- মানুষ কীভাবে এর ওপর নির্ভরশীল হয়ে পড়ে তার অনুরূপ কোনো উপায়ে।

বস্তুগততার সূত্র প্রযোজ্য হলে ব্যবস্থা-সামঞ্জস্য প্রত্যয়নে **বিশ্বাসযোগ্যতা ও ব্যবস্থার ওপর নির্ভরতার অখণ্ডতা** নিচের বিধির অধীনে মূল্যায়ন করতে হবে:

- **অনুচ্ছেদ XIII** (*নির্ভরযোগ্য ও বিশ্বাসযোগ্য ব্যবস্থার অধিকার*);
- [বিশ্বাসযোগ্যতা](../../core_05_band_continuity.md#trustworthiness); এবং
- [বিশ্বাসের অবক্ষয় ও বিভ্রান্তিকর নির্ভরতা](../../core_05_band_continuity.md#trust-degradation-and-misleading-reliance)।

<a id="562-evaluation-requirement"></a>
##### 5.6.2 মূল্যায়নের আবশ্যকতা

**অনুচ্ছেদ XIII-A** (*নির্ভরযোগ্যতা ও বিশ্বাসযোগ্যতার ভিত্তি*) অনুযায়ী ব্যবস্থাটিকে [বিশ্বাস](../../core_05_band_continuity.md#trust) করার যথার্থ কারণ মানুষের আছে কি না এবং তারা সঠিকভাবে তার ওপর নির্ভর করতে পারে কি না প্রত্যয়ন-প্রক্রিয়ায় যাচাই করতে হবে।

মূল্যায়নে আরও পরীক্ষা করতে হবে:

- মানুষ বাস্তবে ব্যবস্থাটিকে চ্যালেঞ্জ করতে, সিদ্ধান্ত পর্যালোচনা করাতে ও সমাধান পেতে পারে কি না—শুধু কাগজে-কলমে নয় (**অনুচ্ছেদ XIII-A** (*নির্ভরযোগ্যতা ও বিশ্বাসযোগ্যতার ভিত্তি*) এবং **অনুচ্ছেদ XIII-B** (*প্রতিকার ও প্রতিপূরণের অধিকার*));
- কৃত্রিমভাবে তৈরি আস্থা বা অপ্রকাশিত সীমাসহ বিভিন্ন উপায়ে মানুষকে ভুলভাবে বিশ্বাস বা নির্ভর করতে বিভ্রান্ত করা হতে পারে কি না (**অনুচ্ছেদ XIII-C** (*মিথ্যা আস্থা ও বিভ্রান্তিকর নির্ভরতার নিষেধাজ্ঞা*));
- এর প্রণোদনা প্রতারণা বা কাজের মান কমিয়ে দেওয়াকে পুরস্কৃত করে কি না (**অনুচ্ছেদ XIII-D** (*প্রণোদনা-সামঞ্জস্যের সীমাবদ্ধতা*)); এবং
- প্রাসঙ্গিক ক্ষেত্রে ব্যর্থতা আড়াল না করে বা নীরবে কারও অধিকার সংকুচিত না করে এটি সৎভাবে ব্যর্থতা থেকে সেরে উঠতে পারে কি না (**অনুচ্ছেদ XIII-F** (*স্থিতিস্থাপকতা ও স্ব-নিরাময়ের ভিত্তি*))।

পরীক্ষার মাত্রা হবে [বস্তুগততা](core_05_band_oversight.md#materiality), [নির্ভরতা](../../core_05_band_continuity.md#dependency), এবং [ঝুঁকি](../../core_05_band_continuity.md#risk) অনুযায়ী।

মূল্যায়নে সময়, ব্যাপ্তি ও নির্ভরতা জুড়ে কার্যগত প্রভাব প্রতিফলিত হতে হবে; নিচের বিষয়গুলি নয়:

- সুনাম, আকার বা বিপণন;
- নামমাত্র নিশ্চয়তার লেবেল;
- বিশ্বাসযোগ্যতা নিয়ে নামমাত্র অনুচ্ছেদ, যখন নির্ভরযোগ্যতার ব্যাজ বা সরবরাহকারীর স্কোরই বাস্তবে নির্ধারণ করে কাকে নিয়োগ দেওয়া হবে বা কী কেনা হবে;
- ঘোষিত অভিপ্রায়; অথবা
- শুধু অতীতের কার্যসম্পাদন।

<a id="563-system-class-scaling-and-escalation"></a>
##### 5.6.3 ব্যবস্থা-শ্রেণি অনুযায়ী মাত্রা ও উন্নীতকরণ

পর্যালোচনার গভীরতা ব্যবস্থার শ্রেণির ওপর নির্ভর করে। বস্তুগততার সূত্র প্রযোজ্য হলে:

- কোনো ব্যবস্থার পাঠ, সতর্কবার্তা বা পুনরুদ্ধার-সংক্রান্ত দাবি পরিবার বা পরিচালকদের বেঁচে থাকার অপরিহার্য উপাদান সম্পর্কে বিভ্রান্ত করতে পারলে, নথিতে শুধু ব্যবস্থা নির্ভরযোগ্য—এমন দাবি নয়, শক্ত প্রমাণ থাকতে হবে। প্রমাণে দেখাতে হবে যে:
  - মানুষ ব্যবস্থাটিকে বিশ্বাস করতে পারে;
  - মানুষ মিথ্যা আশ্বাস পাবে না; এবং
  - ব্যবস্থা ব্যর্থতা থেকে সৎভাবে সেরে ওঠে।
- কোনো ব্যবস্থার সচলতার সময়, মিলকরণ বা জরুরি ব্যতিক্রম (“ব্রেক-গ্লাস” প্রবেশাধিকার) সংক্রান্ত দাবি মানুষ চিকিৎসা বা জরুরি পরিষেবা পাবে কি না নিয়ন্ত্রণ করলে, ব্যবস্থা কতটা সংকটপূর্ণ তার সঙ্গে সামঞ্জস্য রেখে নথিতে বিস্তারিতভাবে দেখাতে হবে:
  - মানুষ কীভাবে ওই দাবিগুলিকে চ্যালেঞ্জ করতে পারে; এবং
  - সেগুলির ওপর নির্ভর করতে মানুষ বিভ্রান্ত হতে পারে কি না।
- সমন্বয় বেঁচে থাকার জন্য অপরিহার্য হয়ে উঠলে প্রত্যয়নে পর্যালোচনা উন্নীত করতে হবে এবং [§2 ব্যবস্থা-শ্রেণি মূল্যায়ন](#2-system-class-evaluation) ও [Part B §7 প্রত্যয়নের ফলাফল](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) অনুযায়ী ব্যবস্থার শ্রেণি পুনর্বিবেচনা করতে হবে। বেঁচে থাকার জন্য প্রয়োজনীয় সমন্বয় থেকে বিভ্রান্তিকর নির্ভরতা মানুষকে বিচ্ছিন্ন করতে পারে—এমন হলে ব্যবস্থাকে **Class A**-এর দিকে উন্নীত করতে হতে পারে।

<a id="564-defects-and-misalignment"></a>
##### 5.6.4 ত্রুটি ও অসামঞ্জস্য

নিচের প্রতিটি বিষয় প্রত্যয়ন-ত্রুটি হিসেবে গণ্য হবে:

- **অনুচ্ছেদ XIII** (*নির্ভরযোগ্য ও বিশ্বাসযোগ্য ব্যবস্থার অধিকার*) অনুযায়ী পর্যালোচনা আবশ্যক—এমন বস্তুগত সীমা, ঝুঁকি বা ব্যর্থতার ইতিহাস অস্পষ্ট, ভুলভাবে উপস্থাপন, খণ্ডিত বা অন্যের ওপর চাপিয়ে দেওয়া;
- মূল্যায়নযোগ্য [বিশ্বাসযোগ্যতা](../../core_05_band_continuity.md#trustworthiness) বিশ্লেষণ ছাড়া সুনাম, সমর্থন, ব্যাপ্তি বা পরিচালকের নিজের বিবৃতিকে যথেষ্ট বলে ধরা;
- নথিভুক্ত মিথ্যা আস্থা, বিকৃত প্রণোদনা, প্রবেশ-অযোগ্য চ্যালেঞ্জের পথ বা ব্যর্থতা আড়াল করা পুনরুদ্ধার-প্রক্রিয়া সাংবিধানিক সামঞ্জস্যকে বস্তুগতভাবে বিপন্ন করলেও নির্ভরতা অব্যাহত রাখার প্রত্যয়ন; এবং
- **অনুচ্ছেদ XIII** (*নির্ভরযোগ্য ও বিশ্বাসযোগ্য ব্যবস্থার অধিকার*)-এর নির্ভরযোগ্যতা এবং **অনুচ্ছেদ XIII-A** (*নির্ভরযোগ্যতা ও বিশ্বাসযোগ্যতার ভিত্তি*)-এর চ্যালেঞ্জ-সংক্রান্ত শৃঙ্খলা পূরণ না করেই প্রকাশ, চ্যালেঞ্জ-যোগ্যতা বা প্রতিকার নাকচ করতে দক্ষতা, উদ্ভাবন বা নিরাপত্তার যুক্তি ব্যবহার করা।

<br>

*মঞ্চ-প্রক্রিয়া, নথি, ফলাফল ও প্রস্থিতি-সেতুতে এগিয়ে যান:* [অধ্যায় আট, Part B — নথি ও প্রক্রিয়া](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-system-alignment-certification--record-and-process) ([§6 মঞ্চ-প্রক্রিয়া](core_07_b_system_alignment_certification_record_process.md#13-forum-supervision-and-component-roles) থেকে [§10 প্রস্থিতির সঙ্গে সম্পর্ক](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing))।

*প্রতিটি মূল্যায়ন ক্ষেত্রের উদাহরণ:* [অধ্যায় আট, Part C — উদাহরণ](../../core_08_c_system_alignment_certification_illustrations.md#chapter-eight-part-c-system-alignment-certification--illustrations)।

---

**আগের ফাইল (এই ভাষায়):** [core_07_system_alignment_certification.md](core_07_system_alignment_certification.md#chapter-seven-system-alignment-certification-index)

**পরের ফাইল (এই ভাষায়):** [core_07_b_system_alignment_certification_record_process.md](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)

**বাধ্যতামূলক মূল:** [core_07_a_system_alignment_certification_evaluation.md](../../core_08_a_system_alignment_certification_evaluation.md)
