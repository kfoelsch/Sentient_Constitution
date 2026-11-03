#### 2.2 সিস্টেম শ্রেণি কীভাবে প্রতিটি মূল্যায়নের মাত্রা নির্ধারণ করে

সিস্টেম শ্রেণি নির্ধারণ করে এই অধ্যায়ের প্রতিটি মূল্যায়ন কতটা গভীরভাবে করা হবে — [§3 সমগ্র-সিস্টেম প্রত্যয়ন মূল্যায়ন](#3-whole-system-certification-evaluation)-এর উপাদান, [§3.4 তথ্যের ধরন ও ব্যবস্থাপনার মূল্যায়ন](#34-data-types-and-handling-evaluation)-এর তথ্য ব্যবস্থাপনা, এবং [§5 Rights-Floor ও ক্ষেত্রভিত্তিক মূল্যায়ন](#5-rights-floor-and-domain-evaluations)-এর প্রতিটি মূল্যায়ন — এবং কত ঘন ঘন তা পুনরাবৃত্ত হবে:

- উচ্চতর শ্রেণির সিস্টেমে আরও শক্ত প্রমাণ চাই যে প্রতিটি প্রযোজ্য মূল্যায়ন সত্যিই সম্পন্ন হয়েছে, শুধু দাবি করা হয়নি। কোনো সিস্টেম শ্রেণিই কেবল কাগজে থাকা যোগ্যতা, লেবেল বা সুবিধা, অথবা যার ভেতরের মূল্যায়ন ও সিদ্ধান্ত কেউ দেখতে পারে না—এগুলোতে সন্তুষ্ট হতে পারে না।
- নিম্নতর সিস্টেম শ্রেণিতেও যে ক্ষেত্রে কোনো শর্ত প্রযোজ্য হয়, সেখানে সৎ ও সমানুপাতিক মূল্যায়ন আবশ্যক।
- সিস্টেম শ্রেণি কখনোই আবশ্যক মূল্যায়ন বাদ দেওয়ার অনুমতি দেয় না। সিস্টেমের বাস্তব ভূমিকা তার সিস্টেম শ্রেণিকে ছাড়িয়ে গেলে, তাকে পুনঃশ্রেণিবদ্ধ করে উচ্চতর গভীরতায় পুনর্মূল্যায়ন করতে হবে। পরিসর, পৌঁছ, বা গ্রহণের বৃদ্ধি, এবং এমন নির্ভরতা যা শক্তিশালী হয়, বিস্তৃত হয়, বা প্রতিস্থাপন করা কঠিন হয়ে ওঠে — এগুলো **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*পুনঃশ্রেণিবিন্যাসের শর্ত*) অনুযায়ী পুনর্মূল্যায়নের কারণ; এগুলো [§9.2 পুনরায় খোলার কারণ](core_09.010_system_alignment_certification_record_recertification.md#92-reopening-triggers)-এও পর্যালোচনা পুনরায় খোলে। [Chapter One §11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)-এর অধীনে গ্রহণকারী যে সীমা নির্ধারণ করেছে তা ছাড়িয়ে কেন্দ্রীভবনও ওই বৃদ্ধির আরও প্রমাণ। সীমা অতিক্রমের জন্য পুনর্মূল্যায়ন অপেক্ষা করে না; সীমা নির্ধারিত না থাকা বা অতিরিক্ত উঁচু হওয়া তা বিলম্বিত করে না।

অংশগ্রহণ ও সমানুপাতিকতার শর্তও একইভাবে মাপে বাড়ে বা কমে:

- **Class A** সিস্টেমে বাস্তবে সম্ভব সবচেয়ে শক্তিশালী অংশগ্রহণের পথ থাকতে হবে, কারণ প্রতিকার সম্ভব হওয়ার আগেই ত্রুটি জীবনধারণের অপরিহার্য উপকরণ বন্ধ করে দিতে পারে। এর মধ্যে রয়েছে:
  - প্রবেশগম্য চ্যালেঞ্জের পথ;
  - অংশীজনের পর্যালোচনা; এবং
  - [Part B §6.1 ফোরামের তত্ত্বাবধান ও উপাদানগুলোর ভূমিকা](core_09.005_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles)-এর অধীনে প্রভাবিত স্বার্থের জন্য নির্ধারিত ফোরাম পরিবারের সিদ্ধান্ত; ওই বিভাগে যেখানে প্রয়োজন বলা হয়েছে, সেখানে Institutional বা Sentient Forum-ও অন্তর্ভুক্ত।
- **Class B** সিস্টেমে শক্তিশালী অংশগ্রহণ দরকার, যেখানে সিস্টেমটি নিচের বিষয়গুলো নিয়ন্ত্রণ করে:
  - স্বাস্থ্যসেবা;
  - শিক্ষা;
  - সুবিধা;
  - কাজ; অথবা
  - দৈনন্দিন জীবনের তুলনীয় ক্ষেত্র।
- **Class C** সিস্টেমেও আপত্তি জানানো যায় এমন নথি এবং সমানুপাতিক প্রকাশ দরকার, বিশেষত যেখানে সমন্বয়ের প্রভাব:
  - সুরক্ষিত গোষ্ঠীর ওপর বেশি ভার চাপায়;
  - অনেক সংবেদনশীল সত্তাকে একই সিস্টেমের ওপর নির্ভরশীল করে; অথবা
  - ইঙ্গিত করে যে সিস্টেমটি শিগগির Class B বা Class A-তে উঠতে পারে।

<a id="23-pilot-certification"></a>

#### 2.3 পাইলট প্রত্যয়ন

একটি **[pilot](core_05.040_band_continuity.md#pilot)** হলো [go-live](core_05.040_band_continuity.md#go-live); তাই শুরু হওয়ার আগে তার নিজস্ব প্রত্যয়ন লাগবে, [Part B §7.1 Go-Live Gate](core_09.005_system_alignment_certification_record_process.md#71-go-live-gate)-এর কার্যক্রম শুরুর নিয়ম অনুযায়ী।

- প্রত্যেক সিস্টেম শ্রেণির সিস্টেম পূর্ণ স্থাপনের আগে পাইলট চালাবে বলে প্রত্যাশা করা হয়; তা না করলে কারণ নথিতে জানাতে হবে।
- পাইলটেরও সৎ শ্রেণিবিন্যাস এবং প্রযোজ্য শর্তযুক্ত প্রতিটি মূল্যায়ন লাগবে; তার পরিধি, জনগোষ্ঠী ও সময়কাল নথিতে উল্লেখ থাকবে।
- পাইলটকে তার নিজস্ব নথিতে মূল্যায়ন করা হয়; মূল্যায়নের গভীরতা সিস্টেম শ্রেণি এবং সিস্টেমটি কতটা বিকল্পযোগ্য তার সঙ্গে সামঞ্জস্যপূর্ণ হবে: যেসব সংবেদনশীল সত্তা এতে প্রভাবিত হবে বা এর ওপর নির্ভর করবে তাদের জন্য কার্যকর বিকল্প আছে কি না, এবং সেই বিকল্পের মূল্য, বিলম্ব ও কার্যক্ষমতার ক্ষতি কত (দেখুন [Dependency](core_05.040_band_continuity.md#dependency))।
  - সিস্টেম যত সহজে প্রতিস্থাপনযোগ্য, এবং তার শ্রেণি যত নিচু, পাইলটের মূল্যায়ন তত হালকা হতে পারে।
  - সহজে প্রতিস্থাপন করা যায় না এমন সিস্টেমের পাইলটকে পূর্ণ স্থাপনের সময় তার শ্রেণি যে গভীরতা দাবি করে, সেই গভীরতায় মূল্যায়ন করতে হবে।

<a id="3-whole-system-certification-evaluation"></a>

### 3. সমগ্র-সিস্টেম প্রত্যয়ন মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণপথ</span></strong></summary>

- **পূর্ববর্তী ভিত্তি:**
  - [Chapter One §12 Systemic Evaluation Requirement](core_01.000_values_principles.md#12-systemic-evaluation-requirement) (1.000 §12); Flourishing measurement family (*সুস্থতা, নিরাপত্তা, ক্ষতি ও জীবনধারণের ন্যূনতম উপকরণে প্রবেশ*); Constitutional Performance measurement family (*সাংবিধানিক দক্ষতা, এড়ানো যায় এমন ভার, এবং উৎপাদনক্ষমতা*);
  - [Constitutional Tetrad](core_00.000_preamble.md#constitutional-tetrad);
  - [Two Constitutional Aims](core_00.000_preamble.md#two-constitutional-aims);
  - [material stake](core_00.000_preamble.md#material-stake);
  - [§1 উদ্দেশ্য ও ভূমিকা](#1-purpose-and-role)।
- **পরবর্তী ধাপ:**
  - [CS-9.320 §4](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class) (*সিস্টেম শ্রেণি অনুযায়ী সমগ্র-সিস্টেমের উদাহরণমূলক প্রয়োগ*);
  - [§3.4](#34-data-types-and-handling-evaluation) থেকে
  - [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) (*ক্ষেত্রভিত্তিক মূল্যায়ন*);
  - [CS-9.320 §2](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-2-illustrative-system-class-profiles) (*সিস্টেম-শ্রেণির উদাহরণমূলক প্রোফাইল*);
  - [Part C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*নথির বিষয়বস্তু*);
  - [Part C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*নথির অখণ্ডতা*);
  - [Part B §6](core_09.005_system_alignment_certification_record_process.md#6-forum-process) (9.005 §6) (*আপত্তি জানানোর ধারা*);
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*প্রত্যয়নের ফলাফল*)।
- **এগুলোর সঙ্গে পড়ুন:**
  - [Chapter One §16](core_01.010_stewardship_capacity_principles.md#16-stewardship-in-depth) (1.010 §16),
  - [§18](core_01.010_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline), এবং
  - [§19](core_01.010_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture);
  - [Chapter One §7.4 Voluntary Discontinuation, Major Self-Modification, and Exit Rights](core_01.000_values_principles.md#74-voluntary-discontinuation-and-exit-rights) (1.000 §7.4);
  - [Chapter One §7.2 Assembly, Collective Organization, and Institutional Formation](core_01.000_values_principles.md#72-assembly-collective-organization-and-institutional-formation) (1.000 §7.2); যেখানে নিরীক্ষা, স্বচ্ছতা বা স্বাধীন যাচাইয়ের Rights Floor বস্তুগতভাবে ঝুঁকিতে রয়েছে সেখানে **Article XVI** (*Audit, Transparency, and Independent Verification*); Continuity measurement family (
  - [§3.2](#32-systemic-scope-and-risk-factors) — স্থিতিস্থাপকতা, প্রত্যাবর্তনযোগ্যতা ও পদ্ধতিগত ঝুঁকি);
  - [Risk Evaluation](core_05.040_band_continuity.md#risk-evaluation);
  - [Risk Disclosure](core_05.050_band_oversight.md#risk-disclosure);
  - [Public Oversight Baseline Disclosure](core_05.050_band_oversight.md#public-oversight-baseline-disclosure); Participation measurement family (
  - [§4.1](#41-privacy-informational-joint-invocation) — গোপনীয়তা ও তথ্যের তত্ত্বাবধান); Accountability measurement family (
  - [§3.1](#31-governance-incentive-and-contestability-discipline) — প্রণোদনার সামঞ্জস্য ও বাজারে প্রতিযোগিতা/আপত্তির সুযোগ);
  - [System Boundaries](core_05.040_band_continuity.md#system-boundaries);
  - [System Charter](core_05.040_band_continuity.md#system-charter)।
- **উপবিভাগসমূহ:**
  - [§3.1](#31-governance-incentive-and-contestability-discipline) থেকে
  - [§3.4](#34-data-types-and-handling-evaluation) পর্যন্ত (*সর্বদা: শাসন, পদ্ধতিগত উপাদান, সময়সীমা, এবং তথ্যের ধরন ও ব্যবস্থাপনা*)। Phase II চলতে থাকে
  - [§4 প্রাসঙ্গিক হলে প্রযোজ্য মূল্যায়ন](#4-evaluations-where-implicated)-এ (*প্রাসঙ্গিক হলে: গোপনীয়তার ক্ষেত্র, প্রস্থান অধিকার, সমাবেশ ও ভিন্নমত*) এবং
  - [§5 Rights-Floor ও ক্ষেত্রভিত্তিক মূল্যায়ন](#5-rights-floor-and-domain-evaluations)-এ (*শর্ত পূরণ হলে*)।

</details>

<br>

*সহজ ভাষায়: সিস্টেমের একটি অংশকে অনুমোদন দিয়ে বাকি অংশ উপেক্ষা করা যাবে না। পর্যালোচকদের পূর্ণ চিত্র জানতে হবে — সিস্টেমটি কীসের ওপর নির্ভর করে, ওপরের কোনো অংশ ব্যর্থ হলে নিচে কী ভাঙে, কোন ক্ষতি পরে দেখা দেয় বা সময়ের সঙ্গে জমে, সংবেদনশীল সত্তারা বাস্তবে এটি ব্যবহার করতে পারে কি না (শুধু কাগজে নয়), ব্যক্তিগত তথ্য যথাযথভাবে আলাদা রাখা হয় কি না, সংবেদনশীল সত্তারা ফাঁদে না পড়ে বেরিয়ে যেতে পারে কি না, গোষ্ঠীগুলো সিস্টেমের কারণে বিভক্ত না হয়ে সংগঠিত হতে পারে কি না, স্বল্পমেয়াদি সাফল্য দীর্ঘমেয়াদি ক্ষতি আড়াল করছে কি না, এবং বড় ঝুঁকির সময় প্রকৃত তত্ত্বাবধান ও জবাবদিহি কার্যকর থাকবে কি না।*

*কাজের উদাহরণ: [CS-9.320 §4 Illustrative whole-system application by system class](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class) দেখায় এই বিভাগ বাস্তবে কীভাবে প্রয়োগ হয়। এতে প্রতিটি সিস্টেম শ্রেণির একটি করে তিনটি নমুনা সিস্টেম নিয়ে উপরের মূল্যায়নগুলোর মধ্য দিয়ে বিশ্লেষণ করা হয়েছে।*

প্রত্যয়ন মূল্যায়নে নিশ্চিত করতে হবে যে পর্যালোচনাধীন সিস্টেমের [material stake](core_00.000_preamble.md#material-stake) পূরণের জন্য [Constitutional Tetrad](core_00.000_preamble.md#constitutional-tetrad) (Participation, Oversight, Accountability, এবং Timeliness) যথেষ্ট শক্তিশালী থাকবে।

System Certification Record-এ দেখাতে হবে যে নিচের যেকোনো বিষয়ে বস্তুগতভাবে প্রাসঙ্গিক হলে, মূল্যায়নে এই বিভাগের প্রতিটি উপাদান, [§4 প্রাসঙ্গিক হলে প্রযোজ্য মূল্যায়ন](#4-evaluations-where-implicated), এবং [§5 Rights-Floor ও ক্ষেত্রভিত্তিক মূল্যায়ন](#5-rights-floor-and-domain-evaluations) বিবেচনা করা হয়েছে:

- প্রত্যয়ন;
- যাচাইকরণ;
- পুনঃপ্রত্যয়ন;
- নির্ভরতা অব্যাহত রাখা;
- স্থাপন; অথবা
- প্রত্যয়নের কোনো শর্ত প্রত্যাহার।

কেবল সিস্টেমের তাৎক্ষণিক বা স্থানীয় প্রভাব মূল্যায়ন যথেষ্ট নয়। Phase II, অর্থাৎ সমগ্র-সিস্টেম মূল্যায়ন, নিচের সারণিতে দেখানো তিন অংশের মাধ্যমে এই ঘাটতি পূরণ করে। এই বিভাগে অংশ **IIa** রয়েছে। [§4 প্রাসঙ্গিক হলে প্রযোজ্য মূল্যায়ন](#4-evaluations-where-implicated)-এ **IIb**, এবং [§5 Rights-Floor ও ক্ষেত্রভিত্তিক মূল্যায়ন](#5-rights-floor-and-domain-evaluations)-এ **IIc** রয়েছে। সারণিটি কেবল নির্দেশিকা; কোনো বিভাগের আবশ্যকতা বদলায় না।

| কখন | উপধাপ | বিভাগ | প্রযোজ্য ক্ষেত্র |
|------|-----------|----------|---------|
| **সর্বদা** | IIa | [§3.1 শাসন, প্রণোদনা ও আপত্তিযোগ্যতার শৃঙ্খলা](#31-governance-incentive-and-contestability-discipline); [§3.2 পদ্ধতিগত পরিধি ও ঝুঁকির উপাদান](#32-systemic-scope-and-risk-factors); [§3.3 সময়-সামঞ্জস্যের সীমা](#33-time-consistency-constraint); [§3.4 তথ্যের ধরন ও ব্যবস্থাপনার মূল্যায়ন](#34-data-types-and-handling-evaluation) | বস্তুগত প্রভাবসম্পন্ন প্রতিটি System Certification Record |
| **প্রাসঙ্গিক হলে** | IIb | [§4.1 গোপনীয়তা (তথ্যগত) যৌথ প্রয়োগ](#41-privacy-informational-joint-invocation); [§4.2 স্বেচ্ছায় বন্ধ করা, বড় ধরনের স্ব-পরিবর্তন ও প্রস্থানের অধিকার](#42-voluntary-discontinuation-major-self-modification-and-exit-rights); [§4.3 সমাবেশ, যৌথ সংগঠন ও প্রতিষ্ঠান গঠন](#43-assembly-collective-organization-and-institutional-formation), যার মধ্যে [§4.3.1](#431-dissent-and-peaceful-protest) রয়েছে | প্রত্যয়নের বিষয়টি যেখানে উপবিভাগে উল্লিখিত ক্ষেত্র বা নীতিকে বস্তুগতভাবে প্রভাবিত করে |
| **শর্ত পূরণ হলে** | IIc | [§5 Rights-Floor ও ক্ষেত্রভিত্তিক মূল্যায়ন](#5-rights-floor-and-domain-evaluations) | §5-এর সারণির কোনো শর্ত পূরণ হলে |

<a id="31-governance-incentive-and-contestability-discipline"></a>
#### 3.1 শাসন, প্রণোদনা ও আপত্তিযোগ্যতার শৃঙ্খলা

*সহজ ভাষায়: সংশ্লিষ্ট ঝুঁকির মাত্রায় [Tetrad](core_00.000_preamble.md#constitutional-tetrad)-এর চারটি অঙ্গ টিকে থাকবে কি না — অংশগ্রহণ (সংবেদনশীল সত্তারা বাস্তবে অংশ নিতে পারে কি না), তত্ত্বাবধান (কাজ পর্যবেক্ষণ ও যাচাই করা যায় কি না), জবাবদিহি (ভুল কাজের জন্য জবাব চাওয়া যায় কি না), এবং সময়োপযোগিতা (গুরুত্বপূর্ণ সময়ে সিদ্ধান্ত যথেষ্ট দ্রুত হয় কি না) — তা পর্যালোচকরা না জিজ্ঞেস করলে পর্যালোচনা সম্পূর্ণ হয় না। বস্তুগত ক্ষমতা আসলে কার হাতে, এবং কে কোন বিষয়ে জবাবদিহি করে তাও জানতে হবে — “দল” जैसी অস্পষ্ট উত্তর বা দোষ চাপিয়ে পালানোর бүрхүүл নয়। বৈধ প্রত্যয়নের জন্য এসব প্রশ্নের উত্তর থাকা আবশ্যক।*

প্রত্যয়ন মূল্যায়ন অসম্পূর্ণ, যদি তা যাচাই না করে যে নিচের প্রতিটি বিষয় পর্যালোচনাধীন সিস্টেমের [material stake](core_00.000_preamble.md#material-stake) অনুযায়ী মাপ বজায় রাখবে কি না:

- **oversight**;
- **accountability**;
- **participation**; এবং
- **timeliness**।

মূল্যায়নে আরও যাচাই করতে হবে, নিচের প্রতিটি ধরনের বস্তুগত ভূমিকা **আনুষ্ঠানিকভাবে নির্ধারিত, নথিভুক্ত ও অনুসরণযোগ্য** কি না, যাতে সংবেদনশীল সত্তারা বুঝতে পারে কে জবাবদিহি করবে এবং বাস্তবে সিদ্ধান্তকে চ্যালেঞ্জ করতে পারে:

- stewardship-এর ভূমিকা;
- শাসন-সংক্রান্ত ভূমিকা; এবং
- জবাবদিহির ভূমিকা।

এটি **[CS-9.305](corpus_systems/cs_09.305_system_classification_machinery.md#cs-9305-part-a-system-classification-machinery) (*System classification machinery*) এবং [CS-9.310 — System impact classifications](corpus_systems/cs_09.310_system_impact_classifications.md#cs-9310-part-b-system-impact-classifications)** অনুযায়ী সিস্টেম শ্রেণি ও বস্তুগত প্রভাবের সঙ্গে মাপ নির্ধারণ করে। সিস্টেম শ্রেণি পুনরায় যাচাইয়ের সময়সূচিও নির্ধারণ করে ([§2 সিস্টেম শ্রেণির মূল্যায়ন](#2-system-class-evaluation))।

শাসন, প্রণোদনা ও আপত্তিযোগ্যতা মূল্যায়নে প্রত্যয়নকে নিচের বিষয়গুলো প্রয়োগ করতে হবে:

- **[Chapter One §16 Stewardship In Depth](core_01.010_stewardship_capacity_principles.md#16-stewardship-in-depth)** — বণ্টিত বোঝাপড়া, স্বচ্ছতা, নিরীক্ষাযোগ্যতা এবং আপত্তিযোগ্য পর্যবেক্ষণযোগ্যতা;
- **[Chapter One §18 Governance Under Stewardship Discipline](core_01.010_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline)** — অনুমোদিত শাসন ও জবাবদিহি;
- **[Chapter One §19 Incentive Alignment and System Capture](core_01.010_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture)** — proxy-এর অখণ্ডতা, স্বল্প সময়সীমায় ত্রুটি সংশোধন, এবং capture-এ সাড়া, যার মধ্যে রয়েছে:
  - **[Chapter One §19.1.4 Role-Depth and Material-Responsibility Pathways](core_01.010_stewardship_capacity_principles.md#1914-role-depth-and-material-responsibility-pathways)** — বাস্তব পরিণতি বহনকারী ভূমিকা এবং প্রতীকী অংশগ্রহণ ঠেকানোর সুরক্ষা;
- **[Chapter Fifteen §5 Authorized Roles, Competency Development, and Contribution](core_15.000_governance.md#5-authorized-roles-competency-development-and-contribution)** এবং **[CS-15.305 — Critical system stewardship](corpus_systems/cs_15.305_critical_system_stewardship.md#cs-15305-critical-system-stewardship)** — যেখানে বস্তুগতভাবে প্রাসঙ্গিক সেখানে কার্যকরী ভূমিকা-সংজ্ঞা, দক্ষতা ও অনুসরণযোগ্যতার শর্ত;
- **[Article XVI: Audit, Transparency, and Independent Verification](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification)** — যেখানে নিরীক্ষা, স্বচ্ছতা বা স্বাধীন যাচাইয়ের Rights Floor বস্তুগতভাবে ঝুঁকিতে রয়েছে।

**প্রাতিষ্ঠানিক তথ্য।** এই বিভাগে সিস্টেমের অপারেটর বা steward-এর শাসন ও প্রণোদনা সম্পর্কে প্রশ্ন করা হয়েছে। অপারেটর বা steward যদি [Institution](core_05.040_band_continuity.md#institution) হয়, তবে তার চালানো প্রতিটি সিস্টেমের জন্য বারবার না করে এই তথ্য একবার তার Institutional Certification Record-এ রাখা হয়। [Chapter Ten §3 Whole-Institution Certification Evaluation](core_10.000_institutional_alignment_certification.md#3-whole-institution-certification-evaluation)-এর অধীনে Institution-এর বর্তমান নথি থেকে লিংকের মাধ্যমে নিচের তথ্য নেওয়া যেতে পারে:

- Institution-এর নিজস্ব শাসন;
- জবাবদিহিমূলক দপ্তরসমূহ; এবং
- পুরস্কার কাঠামো।

Chapter Ten Institution-এর বক্তব্যের ওপর ভিত্তি করে এসব তথ্য গ্রহণ করে না। প্রমাণ ও পর্যবেক্ষিত কার্যক্রমের সঙ্গে তা যাচাই করে, এবং প্রতিটি সিদ্ধান্তে কোন ভিত্তির ওপর তা দাঁড়িয়েছে তা বলে। বর্তমান Institutional Certification Record না থাকলে, এই বিভাগ অনুযায়ী সরাসরি তথ্য মূল্যায়ন করা হয়।

এই তথ্যগুলোর জন্য, সিস্টেমটির ফোরাম:

- তবুও সিদ্ধান্ত নেবে যে তথ্যগুলো এই সিস্টেমের জন্য যথেষ্ট কি না; এবং
- System Certification Record-এ কারণ না জানিয়ে একই প্রাতিষ্ঠানিক তথ্য সম্পর্কে ভিন্ন সিদ্ধান্ত দিতে পারবে না।

সিস্টেমের নিজস্ব শাসন, প্রণোদনা ও আপত্তিযোগ্যতা এখানেই মূল্যায়ন করা হয়। দেখুন [Chapter Ten §1 Purpose and Role](core_10.000_institutional_alignment_certification.md#1-purpose-and-role)।

**Type O হিসেবে প্রকাশ।** এই বিভাগে যা প্রতিষ্ঠিত হয় তা প্রত্যয়ন-তথ্য, এবং [CS-6.310 Part B §9.3 Type O](corpus_systems/cs_06.310_data_classifications.md#93-type-o-open-public-oversight-baseline-disclosure-data)-এর অধীনে প্রতিটি সিস্টেম শ্রেণির জন্য প্রত্যয়ন-তথ্য হলো **Type O**। এটি ব্যক্তিগত সিদ্ধান্ত নয়। এতে রয়েছে:

- oversight, accountability, participation ও timeliness-এর মূল্যায়ন;
- নির্ধারিত stewardship, governance ও accountability ভূমিকা, এবং বস্তুগত ক্ষমতা কার হাতে ও কে কোন বিষয়ে জবাবদিহি করে; এবং
- যে প্রাতিষ্ঠানিক তথ্যের ওপর নির্ভর করা হয়েছে, যার মধ্যে শাসন, জবাবদিহিমূলক দপ্তর ও পুরস্কার কাঠামো রয়েছে।

**[CS-6.305 §7 Type O baseline](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems)**-এর বিকল্প প্রকাশ ও গোপন রাখার নিয়ম অনুযায়ী, জনসাধারণের জন্য নির্ধারিত ভিত্তিগত বিশদতার স্তরে [System Certification Record](core_05.040_band_continuity.md#system-certification-record)-এর মাধ্যমে এটি প্রকাশ করতে হবে। **Class A**, **Class B**, এবং **Class C** সিস্টেমের ক্ষেত্রে এটি [Public Oversight Baseline Disclosure](core_05.050_band_oversight.md#public-oversight-baseline-disclosure)-এরও অংশ; এবং [§3.4.1 Type O Baseline Disclosure](#341-type-o-baseline-disclosure) যাচাই করে যে এটি বাস্তবে প্রকাশিত হয়েছে।

**Class L** ও **Class P** সিস্টেমে পূর্ণ Public Oversight Baseline Disclosure প্রযোজ্য নয়, তবে এই প্রত্যয়ন-তথ্য তবুও **Type O**। এতে কতটা বিস্তারিত থাকবে তা [CS-9.310 §8.6 Scaled-duties intensity](corpus_systems/cs_09.310_system_impact_classifications.md#86-scaled-duties-intensity)-এর অধীনে সিস্টেম শ্রেণির স্বচ্ছতার দায়িত্ব অনুযায়ী হবে। Class L বা Class P সিস্টেমকে Class C বা তার বেশি শ্রেণিতে পুনঃশ্রেণিবদ্ধ করলে, পুনঃশ্রেণিবিন্যাসের সময় থেকেই পূর্ণ ভিত্তিগত প্রকাশ প্রযোজ্য হবে।

<a id="32-systemic-scope-and-risk-factors"></a>
#### 3.2 পদ্ধতিগত পরিধি ও ঝুঁকির উপাদান

প্রত্যয়ন মূল্যায়নে বিবেচনা করতে হবে:

- **সবচেয়ে বড় পরিসরের ক্ষতি:**
  - **পরিবেশগত পুনরুদ্ধার-সক্ষমতা** — সিস্টেম কোনো প্রাকৃতিক বাস্তুতন্ত্রের [Ecological Recovery Capacity](core_05.040_band_continuity.md#ecological-recovery-capacity), যেকোনো মাত্রায়, এমনভাবে ক্ষতিগ্রস্ত করতে পারে কি না যাতে ক্ষতির পর তা আর পুনরুৎপাদন হতে না পারে;
  - **অস্তিত্বগত ঝুঁকি** — এমন পরিণতি যা সভ্যতা-পর্যায়ে সংবেদনশীল সত্তাদের টিকে থাকা বিপন্ন করতে পারে;
- **প্রভাব কীভাবে ছড়ায় ও জমা হয়:**
  - **নির্ভরতার সম্পর্ক ও ধারাবাহিক প্রভাব** — ওপরের কোনো অংশ ভাঙলে নিচের দিকে কী ব্যর্থ হয়;
  - **সমষ্টি ও মাত্রার প্রভাব** — অনেক ছোট কাজ একত্র হলে কী বদলায়;
  - **বিলম্বিত, ক্রমবর্ধমান ও সম্ভাব্যতার ওপর নির্ভরশীল প্রভাব** — যে ক্ষতি পরে দেখা দেয়, জমতে থাকে, বা দৈব ঘটনার ওপর নির্ভর করে;
- **সিস্টেম কীভাবে অপব্যবহার বা ভুল পরিধিতে ব্যবহার হতে পারে:**
  - **প্রতিপক্ষমূলক অবস্থা ও অপব্যবহারের সম্ভাবনা** — ক্ষতিকর পক্ষ বা পূর্বানুমেয় অপব্যবহার কীভাবে সিস্টেমকে কাজে লাগাতে পারে;
  - **চার্টারে নির্ধারিত পরিধি বনাম কার্যকরী সীমানা** — যেখানে [System Charter](core_05.040_band_continuity.md#system-charter) আছে বা থাকা দরকার, তা পর্যবেক্ষিত [System Boundaries](core_05.040_band_continuity.md#system-boundaries)-এর সঙ্গে মেলে কি না, এবং ঘোষিত পরিধি বস্তুগত প্রভাব বা নির্ভরতাকে কম করে দেখায় কি না।

<a id="321-risk-evaluation-and-disclosure-bridge"></a>
##### 3.2.1 ঝুঁকি মূল্যায়ন ও প্রকাশের সংযোগ

উপরের উপাদান অনুযায়ী পদ্ধতিগত [Risk](core_05.040_band_continuity.md#risk) পরিধির মধ্যে থাকলে, Chapter Five-এর দুই অংশই প্রত্যয়নে যাচাই করতে হবে — ঝুঁকি প্রকাশের জন্য আলাদা কোনো নামযুক্ত নথির ধরন তৈরি না করে:

- **[Risk Evaluation](core_05.040_band_continuity.md#risk-evaluation)** — পদ্ধতিগত ঝুঁকির সত্যিই মূল্যায়ন হয়েছে কি না:
  - প্রাসঙ্গিক অবস্থায় (নির্ভরতা, সময়সীমা, এবং [Adversarial, Scaled, and Exploited Conditions](core_05.050_band_oversight.md#adversarial-scaled-and-exploited-conditions)); এবং
  - সিস্টেম শ্রেণি ও [material stake](core_00.000_preamble.md#material-stake)-এর মাপ অনুযায়ী।
- **[Risk Disclosure](core_05.050_band_oversight.md#risk-disclosure)** — মূল্যায়িত ঝুঁকির তথ্য:
  - যেসব সংবেদনশীল সত্তার তা জানা দরকার তাদের কাছে পৌঁছেছে কি না; এবং
  - বোঝা, চ্যালেঞ্জ করা ও পদক্ষেপ নেওয়ার মতো সময়ে পৌঁছেছে কি না।

<a id="322-defects-and-misalignment"></a>
##### 3.2.2 ত্রুটি ও অসামঞ্জস্য

উপরের দুই অংশের কেবল একটিমাত্র করা ব্যর্থতা:

- মূল্যায়িত হলেও কখনো প্রকাশ না করা ঝুঁকি উত্তীর্ণ হয় না; এবং
- যথাযথ মূল্যায়ন না করেই প্রকাশ করা ঝুঁকিও উত্তীর্ণ হয় না।

অভ্যন্তরীণ নোট, গভীরে লুকোনো পরিশিষ্ট, চেকলিস্ট বা ঘটনার পরে দেওয়া বিবৃতি — কোনোটিই ঝুঁকি মূল্যায়ন বা ঝুঁকি প্রকাশ হিসেবে গণ্য নয়।

নিচের প্রতিটি বিষয়কে প্রত্যয়নের ত্রুটি হিসেবে ধরতে হবে:

- [Transparency](core_05.050_band_oversight.md#transparency) বা [Safety (Constitutional Constraint)](core_05.040_band_continuity.md#safety-constitutional-constraint)-এর শর্তে যেখানে প্রয়োজন সেখানে মূল্যায়িত পদ্ধতিগত ঝুঁকি প্রয়োজনীয় ব্যক্তিদের কাছে প্রকাশ না করা; অথবা
- পরিচিত ঝুঁকি নথিভুক্ত, প্রকাশিত ও সমাধান না করেই সিস্টেমের ওপর নির্ভরতা অব্যাহত রাখতে অনুমোদন দেওয়া।

এসবের পরিণতি নির্ধারিত হয়েছে [§7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)-এ।

<a id="33-time-consistency-constraint"></a>
#### 3.3 সময়-সামঞ্জস্যের সীমা

পূর্বানুমেয় মধ্যম বা দীর্ঘ সময়সীমার লঙ্ঘন অমীমাংসিত থাকলে, প্রত্যয়নে নিচের কোনো বিষয়কে যথেষ্ট বলে ধরা যাবে না:

- নিকট-মেয়াদি পরিমাপক;
- স্থানীয় নিয়ম-মানা; অথবা
- স্বল্প সময়সীমার দক্ষতা।

স্বল্পমেয়াদি ফলের পেছনে ছোটা গ্রহণযোগ্য নয়, যদি যুক্তিসঙ্গতভাবে প্রত্যাশা করা যায় যে তা ভবিষ্যতে নিচের কোনো বিষয় ভেঙে দেবে — ক্ষতি ধীরে জমলেও, দেরিতে দেখা দিলেও, বা বিভিন্ন সিস্টেম জুড়ে ছড়ালেও:

- **Safety**;
- **Truth**; অথবা
- **wellbeing**।

<a id="34-data-types-and-handling-evaluation"></a>

#### 3.4 তথ্যের ধরন ও ব্যবস্থাপনার মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণপথ</span></strong></summary>

- **পূর্ববর্তী ভিত্তি:**
  - [§3](#3-whole-system-certification-evaluation) (*সমগ্র-সিস্টেম মূল্যায়নের উপাদান*);
  - [CS-9.320 §4](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class) (*সিস্টেম শ্রেণি অনুযায়ী সমগ্র-সিস্টেমের উদাহরণমূলক প্রয়োগ*);
  - [Part C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*নথির বিষয়বস্তু*);
  - [§2](#2-system-class-evaluation) (*সিস্টেম শ্রেণির মূল্যায়ন*); Oversight measurement family (*সাংবিধানিক পরিমাপ হিসেবে সত্য ও জ্ঞানগত অখণ্ডতা*);
  - [Article XV: Info-Sphere Integrity](core_06.010_rights_part_c.md#article-xv-info-sphere-integrity);
  - [Article XVI: Audit, Transparency, and Independent Verification](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [Article VII: Self-Ownership](core_06.005_rights_part_b.md#article-vii-self-ownership)।
- **পরবর্তী ধাপ:**
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class) (*সিস্টেম শ্রেণি অনুযায়ী তথ্য ব্যবস্থাপনার উদাহরণমূলক প্রয়োগ*);
  - [§5.1](#51-ecological-footprint-evaluation) এবং
  - [CS-9.320 §6](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-6-illustrative-ecological-footprint-application-by-system-class) (*সিস্টেম শ্রেণি অনুযায়ী পরিবেশগত পদচিহ্নের উদাহরণমূলক প্রয়োগ*);
  - [Part C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*নথির অখণ্ডতা*);
  - [Part C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*যাচাইকৃত-ইনপুট গেট*);
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*পুনঃশ্রেণিবিন্যাস ও ব্যবস্থাপনার অসামঞ্জস্য*)।
- **এগুলোর সঙ্গে পড়ুন:**
  - **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Information types and handling*) এবং [CS-6.310 — Data classifications](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** (এর মধ্যে রয়েছে **
  - [CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*পুনঃশ্রেণিবিন্যাস ও জীবনচক্র পরিচালনা*) এবং **
  - [CS-6.305 §8](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-8-system-data-types-record-governance)** (*System Data Types Record-এর শাসন*));
  - [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record);
  - [Public Oversight Baseline Disclosure](core_05.050_band_oversight.md#public-oversight-baseline-disclosure);
  - বস্তুগতভাবে প্রাসঙ্গিক হলে **CJS-5.130 §18** (*তথ্য ধরে রাখা ও জীবনচক্রের অখণ্ডতার শর্ত*),
  - **CJS-5.130 §21** (*প্রতিপক্ষমূলক পরিস্থিতিতে দৃঢ়তা ও অপব্যবহার-প্রতিরোধের শর্ত*), এবং
  - **CJS-5.130 §17** (*পারস্পরিক কার্যকারিতা, বহনযোগ্যতা ও প্রস্থানের অখণ্ডতার শর্ত*);
  - গোপনীয়তার কোনো ক্ষেত্র প্রাসঙ্গিক হলে [§4.1 Privacy (Informational) Joint Invocation](#41-privacy-informational-joint-invocation)।
- **উপবিভাগসমূহ:**
  - [§3.4.1](#341-type-o-baseline-disclosure) (*Type O ভিত্তিগত প্রকাশ*);
  - [§3.4.2](#342-privacy-discipline) (*গোপনীয়তার শৃঙ্খলা*);
  - [§3.4.3](#343-protective-storage-and-key-custody) (*সুরক্ষিত সংরক্ষণ ও কী-এর হেফাজত*);
  - [§3.4.4](#344-scheduled-data-type-re-evaluation) (*সময়সূচিভিত্তিক তথ্যের ধরন পুনর্মূল্যায়ন*);
  - [§3.4.5](#345-system-class-scaled-infrastructure-assurance) (*সিস্টেম-শ্রেণির মাপে অবকাঠামোর নিশ্চয়তা*);
  - [§3.4.6](#346-infrastructure-robustness-for-data) (*তথ্যের জন্য অবকাঠামোর দৃঢ়তা*);
  - [§3.4.7](#347-defects-and-misalignment) (*ত্রুটি ও অসামঞ্জস্য*);
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class) (*সিস্টেম শ্রেণি অনুযায়ী তথ্য ব্যবস্থাপনার উদাহরণমূলক প্রয়োগ*)।

</details>

<br>

*সহজ ভাষায়: সিস্টেমটি কোন ধরনের তথ্য ব্যবহার করে এবং তা যথাযথভাবে পরিচালনা করে কি না, প্রত্যয়নে তাও দেখতে হবে — বর্তমান পর্যালোচনা-চক্রে তথ্যের ধরনগুলো এখনও সঠিক কি না, এবং সংশ্লিষ্ট সিস্টেম শ্রেণিতে ওই তথ্যের জন্য অন্তর্নিহিত অবকাঠামো যথেষ্ট শক্তিশালী কি না, তাও অন্তর্ভুক্ত। তথ্যের ধরন-সংক্রান্ত নিয়ম ও System Data Types Record সিস্টেম কর্পাসে রয়েছে; প্রত্যয়নে যাচাই হয় নিয়মগুলো বাস্তবে প্রয়োগ হয়েছে এবং নথিটি সৎ কি না।*

System alignment certification-এ বস্তুগত প্রভাবসম্পন্ন প্রত্যেক System Certification Record-এর অংশ হিসেবে **তথ্যের ধরন ও ব্যবস্থাপনা** মূল্যায়ন করতে হবে। এই বিভাগে বলা হয়েছে প্রত্যয়নে কী যাচাই করতে হবে। তথ্যের ধরন-সংক্রান্ত শ্রেণিবিন্যাস ও ব্যবস্থাপনার নিয়ম রয়েছে **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Information types and handling*) এবং [CS-6.310 — Data classifications](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**-এ, সঙ্গে রয়েছে:

- তথ্যের ধরনের প্রামাণ্য সংজ্ঞা;
- ব্যবস্থাপনার নিয়ম ও পৃথক রাখার শর্ত;
- জীবনচক্রের বিস্তারিত নিয়ম; এবং
- স্থায়ী [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record)।

**মূল্যায়নের শর্ত।** প্রত্যয়ন প্রক্রিয়ায় নির্ধারণ করতে হবে সিস্টেমটি:

- বস্তুগতভাবে প্রাসঙ্গিক তথ্যের ধরনগুলো শনাক্ত করে কি না; এবং
- রূপান্তর, একত্রীকরণ, অর্পণ, সংরক্ষণ, ধরে রাখা, এবং এক ক্ষেত্রের তথ্য অন্য ক্ষেত্রের সঙ্গে যুক্ত করা—এসবসহ সর্বত্র **প্রযোজ্য সবচেয়ে কঠোর** শ্রেণিবিন্যাস অনুযায়ী তথ্য পরিচালনা করে কি না।

মূল্যায়নে কেবল লেবেল, বিন্যাস বা প্রক্রিয়া-ধাপ নয়, কার্যকরী প্রভাব প্রতিফলিত হতে হবে।

<a id="341-type-o-baseline-disclosure"></a>
##### 3.4.1 Type O ভিত্তিগত প্রকাশ

**[CS-6.305 §7 Type O baseline](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems)** প্রযোজ্য হলে, প্রকাশিত [Public Oversight Baseline Disclosure](core_05.050_band_oversight.md#public-oversight-baseline-disclosure) (**Type O**) **প্রত্যয়িত পরিধি** জুড়ে আছে কি না তাও প্রত্যয়নে যাচাই করতে হবে; পরিধিটি নিচের বিষয়গুলো থেকে নির্ধারিত:

- প্রযোজ্য [System Charter](core_05.040_band_continuity.md#system-charter);
- নির্ধারিত সিস্টেম শ্রেণি; এবং
- পর্যবেক্ষিত [System Boundaries](core_05.040_band_continuity.md#system-boundaries)।

এই অন্তর্ভুক্তির মধ্যে [§3.1 Governance, Incentive, and Contestability Discipline](#31-governance-incentive-and-contestability-discipline)-এর অধীনে প্রতিষ্ঠিত শাসন, প্রণোদনা ও আপত্তিযোগ্যতা-সংক্রান্ত সিদ্ধান্ত এবং নির্ধারিত ভূমিকাগুলো থাকতে হবে।

Class L ও Class P-সহ প্রত্যেক সিস্টেম শ্রেণির ক্ষেত্রে, [CS-6.310 Part B §9.3 Type O](corpus_systems/cs_06.310_data_classifications.md#93-type-o-open-public-oversight-baseline-disclosure-data)-এর অধীনে System Certification Record-কে **Type O** প্রত্যয়ন-তথ্য হিসেবে প্রকাশ করা হয়েছে কি না, তাও প্রত্যয়নে যাচাই করতে হবে। Class A, B ও C-এর বাইরে প্রকাশের জন্য পূর্ণ Public Oversight Baseline Disclosure আবশ্যক নয়।

পদ্ধতিগত ঝুঁকি থাকলে মূল্যায়িত ঝুঁকি ভাগ করে নেওয়াও এই ভিত্তিগত প্রকাশের অংশ হতে পারে। জনসাধারণের ভিত্তিগত অধিকার প্রত্যয়নের সীমার চেয়ে বিস্তৃত; এবং [System Classification Record](core_05.040_band_continuity.md#system-classification-record) বা [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record)-এর পাশাপাশি আলাদা নথি তৈরির দাবি করে না।

যৌক্তিকভাবে গোপন রাখা প্রতিটি তথ্যের সঙ্গে বাস্তবসম্মতভাবে সম্ভব সবচেয়ে শক্তিশালী জনসমক্ষে বিকল্প দিতে হবে ([§3.4.5 System-Class-Scaled Infrastructure Assurance](#345-system-class-scaled-infrastructure-assurance)-এ উদাহরণ রয়েছে)। পরিভাষাটির দায়িত্ব Chapter Five-এর; ভিত্তিগত প্রকাশের বিষয়বস্তু ও প্রকাশের কার্যপ্রক্রিয়ার দায়িত্ব CS-6.305 (*Information types and handling*) ও CS-6.310 (*Data classifications*)-এর।

<a id="342-privacy-discipline"></a>
##### 3.4.2 গোপনীয়তার শৃঙ্খলা

তথ্য ব্যবস্থাপনায় নিচের গোপনীয়তা-শৃঙ্খলা বজায় রাখতে হবে:

- *Types H, I, N, S ও Y।* **Type H**, **Type I**, **Type N**, **Type S** ও **Type Y** তথ্যের ক্ষেত্রে, **CS-6.305 (*Information types and handling*) ও CS-6.310** (*Data classifications*)-এ প্রতিটি ধরনের জন্য উল্লিখিত [গোপনীয়তার মূল বিধান](corpus_systems/cs_06.310_data_classifications.md#privacy-link) ব্যবস্থাপনা পূরণ করে কি না, প্রত্যয়নে যাচাই করতে হবে; এর মধ্যে রয়েছে [Necessity](core_05.035_band_accountability.md#necessity), [Proportionality](core_05.035_band_accountability.md#proportionality), তথ্য-সীমিতকরণ, এবং সম্মতি বা অন্য পর্যাপ্ত কর্তৃত্ব।
- *যৌথ প্রয়োগ।* একাধিক গোপনীয়তার ক্ষেত্র প্রাসঙ্গিক হলে [§4.1 Privacy (Informational) Joint Invocation](#41-privacy-informational-joint-invocation)-ও প্রযোজ্য।
- *লেবেলই যথেষ্ট নয়।* তথ্যের সঠিক ধরন-লেবেল একাই গোপনীয়তার নিয়ম মানার প্রমাণ নয়।
- *Types W, U ও T।* **Type W**, **Type U** ও **Type T**-এর কাজের ক্ষেত্রে, স্রষ্টার নিয়ন্ত্রণ সম্মান করা হয়েছে কি না প্রত্যয়নে যাচাই করতে হবে; এর মধ্যে রয়েছে:
  - [CS-6.310 Part B §9.9](corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published) (*Type W: প্রকাশিত কাজ*) অনুযায়ী প্রকাশ্য রিলিজ প্রত্যাহার;
  - [CS-6.310 Part B §9.13](corpus_systems/cs_06.310_data_classifications.md#913-commercial-grants) (*বাণিজ্যিক অনুমতি*) অনুযায়ী প্রতিটি নথিভুক্ত অনুমতির সীমা; এবং
  - স্রষ্টার [সংরক্ষিত অধিকার](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights)।
- *ইঙ্গিত থেকে সম্মতি ধরে নেওয়া যাবে না।* কোনো অনুমতি কেবল তাতে নাম করা ব্যবহারগুলোই অন্তর্ভুক্ত করে, এবং তা ঘোষিত পরিধি, মেয়াদ, অঞ্চল ও মাধ্যমে সীমাবদ্ধ। যা এতে উল্লেখ নেই তা স্রষ্টারই থাকে। কোনো পূর্বনির্ধারিত সেটিং, একত্রিত শর্ত, নীরবতা, বা আরও বিস্তৃত অনুমতিকে এমন ব্যবহারের সম্মতি হিসেবে ধরা যাবে না যা অনুমতিতে উল্লেখ নেই। উদাহরণস্বরূপ, কোনো কাজ প্রকাশ বা বিক্রির সাধারণ লাইসেন্স সেটিকে প্রশিক্ষণ-তথ্য হিসেবে ব্যবহারের সম্মতি নয়; এর জন্য স্রষ্টার নিজস্ব নির্দিষ্ট সম্মতি প্রয়োজন (দেখুন [সংরক্ষিত অধিকার](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights))।

<a id="343-protective-storage-and-key-custody"></a>
##### 3.4.3 সুরক্ষিত সংরক্ষণ ও কী-এর হেফাজত

ডিফল্টভাবে সীমাবদ্ধ এবং প্রবেশ-অযোগ্য স্তরের তথ্যের ক্ষেত্রে, [CS-6.305 Part A §5.0 Access-posture bands](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands)-এ নির্ধারিত সুরক্ষিত সংরক্ষণ ও কী-হেফাজতের ন্যূনতম শর্ত সিস্টেম পূরণ করে কি না প্রত্যয়নে যাচাই করতে হবে। নথিতে দেখাতে হবে:

- সীমাবদ্ধ তথ্য এবং তার কী বাস্তবে কোথায় থাকে, ব্যাকআপ, cache, log ও swap-সহ;
- সরলপাঠ্য তথ্য কেবল যেসব process-এর দরকার সেগুলোর মধ্যেই সীমাবদ্ধ; এবং
- নিরীক্ষা, export ও আইনসম্মত override-এর পথ এখনও কাজ করে।

এসব প্রমাণ ছাড়া কেবল encryption-এর দাবি এই শর্ত পূরণ করে না।

<a id="344-scheduled-data-type-re-evaluation"></a>
<a id="344-periodic-data-type-re-evaluation"></a>
##### 3.4.4 সময়সূচিভিত্তিক তথ্যের ধরন পুনর্মূল্যায়ন

বস্তুগত প্রভাবসম্পন্ন কোনো সিস্টেম প্রত্যয়িত বা পুনঃপ্রত্যয়িত হলেই, পর্যালোচনায় যাচাই করতে হবে তার গুরুত্বপূর্ণ dataset-গুলো:

- **পুনর্মূল্যায়িত** হয়েছে, যথাযথ শ্রেণিবিন্যাসের জন্য **[CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*পুনঃশ্রেণিবিন্যাস ও জীবনচক্র পরিচালনা*) এবং **CJS-5.130 §18** (*তথ্য ধরে রাখা ও জীবনচক্রের অখণ্ডতার শর্ত*) অনুযায়ী; এবং
- পর্যালোচনায় প্রয়োজন দেখা দিলে **পুনঃশ্রেণিবদ্ধ** হয়েছে।

CS-6.305 (*Information types and handling*) ও CS-6.310 (*Data classifications*) অনুযায়ী কোনো ঘটনা ঘটলে তথ্যের ধরন পুনর্নির্ধারণ করা এই নির্ধারিত প্রত্যয়ন-যাচাইয়ের বিকল্প নয়।

<a id="345-system-class-scaled-infrastructure-assurance"></a>
##### 3.4.5 সিস্টেম-শ্রেণির মাপে অবকাঠামোর নিশ্চয়তা

[§2.2 সিস্টেম শ্রেণি কীভাবে প্রতিটি মূল্যায়নের মাত্রা নির্ধারণ করে](#22-how-system-class-scales-every-evaluation), CS-9.305 (*System classification machinery*) এবং CS-9.310 (*System impact classifications*) অনুযায়ী উচ্চতর শ্রেণির সিস্টেমে আরও শক্ত প্রমাণ প্রয়োজন যে চাপের মধ্যেও তথ্য ব্যবস্থাপনা, সংরক্ষণ, প্রক্রিয়াকরণ, প্রেরণ, backup, পুনরুদ্ধার ও পর্যবেক্ষণের অবকাঠামো নিচের বিষয়গুলো অক্ষুণ্ণ রাখতে পারে:

- শ্রেণিবিন্যাসের অখণ্ডতা;
- কার কাজ বা তথ্য তা শনাক্ত করার সামর্থ্য; এবং
- আপত্তি জানানোর সুযোগ।

যেখানে CS-6.305 (*Information types and handling*) ও CS-6.310 (*Data classifications*)-এর জনস্বার্থে দৃশ্যমানতার ডিফল্ট নিয়ম প্রযোজ্য, সেখানে সীমাবদ্ধতা:

- সংকীর্ণভাবে নির্ধারিত;
- নথিভুক্ত ও নিরীক্ষাযোগ্য; এবং
- যুক্তিসঙ্গতভাবে সম্ভব সবচেয়ে শক্তিশালী জনসমক্ষে বিকল্পসহ (যেমন সারসংক্ষেপ, সামষ্টিক তথ্য, পরিচয়মুক্ত সংস্করণ, বিলম্বিত প্রকাশ, বা যোগ্য নিরীক্ষা-প্রবেশাধিকার) কি না, প্রত্যয়নে যাচাই করতে হবে; যাতে গোপন রাখা তথ্যের ব্যাখ্যা থাকে, তা শুধু আড়াল না হয়।

<a id="346-infrastructure-robustness-for-data"></a>
##### 3.4.6 তথ্যের জন্য অবকাঠামোর দৃঢ়তা

তথ্য ব্যবস্থাপনার অবকাঠামো সংশ্লিষ্ট তথ্যের ধরন ও সিস্টেম শ্রেণির জন্য যথাযথ কি না, প্রত্যয়নে মূল্যায়ন করতে হবে। অবকাঠামোর মধ্যে রয়েছে:

- স্থায়ী সংরক্ষণ স্তর ও pipeline;
- প্রবেশাধিকার নিয়ন্ত্রণ;
- encryption বা বিচ্ছিন্নতার সীমানা;
- backup ও restore-এর পথ; এবং
- অপারেটর বা vendor-এর কাছে দায়িত্ব অর্পণের ধারা।

জীবনচক্রের অখণ্ডতা, প্রতিপক্ষমূলক পরিস্থিতিতে দৃঢ়তা, বহনযোগ্যতা, বা পুনরুদ্ধারযোগ্যতার বস্তুগত ঘাটতি নথিতে উল্লেখ করতে হবে এবং প্রত্যয়নের ফলাফল, প্রত্যয়নের শর্ত, বা নির্ভরতার সীমায় প্রতিফলিত করতে হবে।

<a id="347-defects-and-misalignment"></a>
##### 3.4.7 ত্রুটি ও অসামঞ্জস্য

নিচের প্রতিটি বিষয়কে প্রত্যয়নের ত্রুটি হিসেবে ধরতে হবে:

- তথ্যের ভুল শ্রেণিবিন্যাস;
- ফাঁকি দেওয়ার উদ্দেশ্যে পুনর্গঠন;
- এক ক্ষেত্রের তথ্য অন্য ক্ষেত্রে অনিরাপদভাবে যুক্ত করা;
- তথ্যের ধরন সঠিকভাবে চিহ্নিত হলেও ওই ধরনের আবশ্যক গোপনীয়তা-সুরক্ষা ভঙ্গ করে এমন ব্যবস্থাপনা;
- কে তথ্য ব্যবহার, প্রক্রিয়াকরণ বা পরিবর্তন করেছে তার নথি না থাকা, ফলে উল্লেখযোগ্য ক্ষতির তদন্ত করা না যাওয়া;
- **তথ্যের ধরন নির্ধারিত সময়ে পুনর্মূল্যায়ন না করা বা বাদ দেওয়া**;
- সীমাবদ্ধ তথ্য সংরক্ষণে বা অনুমোদিত প্রক্রিয়াকরণ-সীমানার বাইরে সরলপাঠ্য অবস্থায় রাখা, অথবা যেসব process-এর দরকার নেই সেগুলোর কাছে key পৌঁছানো; এবং
- অবকাঠামোর দুর্বলতা যা পূর্বানুমেয়ভাবে CS-6.305 (*Information types and handling*) ও CS-6.310 (*Data classifications*)-এর সুরক্ষা নষ্ট করে।

এসবের পরিণতি রয়েছে [§7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)-এ।

<a id="4-evaluations-where-implicated"></a>

### 4. প্রাসঙ্গিক হলে প্রযোজ্য মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণপথ</span></strong></summary>

- **পূর্ববর্তী ভিত্তি:** [§3](#3-whole-system-certification-evaluation) (*সমগ্র-সিস্টেম মূল্যায়ন, সর্বদা-প্রযোজ্য উপধাপসহ*); [§2](#2-system-class-evaluation) (*সিস্টেম শ্রেণির মূল্যায়ন*); [Chapter One §12 Systemic Evaluation Requirement](core_01.000_values_principles.md#12-systemic-evaluation-requirement) (1.000 §12)।
- **পরবর্তী ধাপ:**
  - [§4.1](#41-privacy-informational-joint-invocation) (*গোপনীয়তার ক্ষেত্র*);
  - [§4.2](#42-voluntary-discontinuation-major-self-modification-and-exit-rights) (*প্রস্থানের অধিকার*);
  - [§4.3](#43-assembly-collective-organization-and-institutional-formation) (*সমাবেশ ও ভিন্নমত*);
  - [Part C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*নথির বিষয়বস্তু*)।
- **এগুলোর সঙ্গে পড়ুন:** [§5 Rights-Floor ও ক্ষেত্রভিত্তিক মূল্যায়ন](#5-rights-floor-and-domain-evaluations) (*শর্ত পূরণ হলে প্রযোজ্য উপধাপ*)।

</details>

<br>

*সহজ ভাষায়: তিনটি যাচাই কেবল তখনই প্রযোজ্য, যখন সিস্টেম সত্যিই সংশ্লিষ্ট বিষয়গুলো ছোঁয় — ব্যক্তিগত তথ্য যথাযথভাবে পৃথক থাকে কি না, সংবেদনশীল সত্তারা ফাঁদে না পড়ে বেরিয়ে যেতে পারে কি না, এবং গোষ্ঠীগুলো সংগঠিত হতে ও ভিন্নমত প্রকাশ করতে পারে কি না। সিস্টেম কোনো একটিকে প্রভাবিত করলে প্রত্যয়নে তা দেখতে হবে।*

এই বিভাগ Phase II (Evaluate)-এর **IIb** উপধাপ। কোনো উপবিভাগের নিজস্ব শর্ত পূরণ হলেই প্রযোজ্য সমগ্র-সিস্টেম মূল্যায়নগুলো এতে একত্র করা হয়েছে।

<a id="41-privacy-informational-joint-invocation"></a>
#### 4.1 গোপনীয়তা (তথ্যগত) যৌথ প্রয়োগ

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণপথ</span></strong></summary>

- **এগুলোর সঙ্গে পড়ুন:** Chapter Five-এর [**Def.C3** (*Privacy (Informational)* — সমমর্যাদার গুচ্ছের প্রধান সংজ্ঞা)](core_05.040_band_continuity.md#defc3-privacy-informational--peer-level-cluster-head) এবং [Privacy (Informational)](core_05.040_band_continuity.md#privacy-informational), অর্থের দায়িত্বে থাকা গুচ্ছ-প্রধানের মূল বিধান।

</details>

<br>

*সহজ ভাষায়: Chapter Six-এর বিভিন্ন অনুচ্ছেদে গোপনীয়তার সুরক্ষা ছড়িয়ে আছে — এক জায়গায় গুছিয়ে নয়। প্রত্যয়ন-পর্যালোচনায় একাধিক সুরক্ষা প্রাসঙ্গিক হলে, পর্যালোচকদের প্রতিটি প্রযোজ্য সুরক্ষা যাচাই করতে হবে। সবচেয়ে সহজ শর্তটি পূরণ করে কাজ শেষ বলা যথেষ্ট নয়।*

প্রত্যয়নের কোনো বিষয় Chapter Six-এর একাধিক গোপনীয়তার ক্ষেত্রকে বস্তুগতভাবে প্রভাবিত করলে, প্রত্যয়নে প্রতিটি ক্ষেত্রের ঠিকানা দিতে হবে। কেবল একটি ক্ষেত্রের অধীনে বিষয়টি নিষ্পত্তি করা যথেষ্ট নয়।

**প্রযোজ্য নীতি।** ক্ষেত্রগুলো একসঙ্গে কীভাবে পড়তে হবে, এই নীতিগুলো তা নিয়ন্ত্রণ করে:

- *যৌথ মূল্যায়ন।* একটি ক্ষেত্রের মধ্য দিয়ে বিষয়টি এমনভাবে চালানো যাবে না যাতে অন্য ক্ষেত্র এড়ানো যায় ([§15.1.1 Anti-Segmentation Principle](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle))।
- *এক ক্ষেত্র থেকে অন্য ক্ষেত্রে টেনে এনে শিথিল করা যাবে না।* প্রতিটি গুচ্ছ-সদস্যের নিজস্ব পরিধিতে স্থানীয়ভাবে ঘোষিত মানই নিয়ন্ত্রণ করবে; অন্য সদস্যের শিথিল মান এনে তা হালকা করা যাবে না ([§15.1.1 Anti-Segmentation Principle](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle))।
- *তথ্যের ধরনের ন্যূনতম শর্ত অক্ষুণ্ণ।* এই উপাদান প্রযোজ্য **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Information types and handling*) ও [CS-6.310](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** (*Data classifications*)-এর কোনো তথ্যের ব্যবস্থাপনা সীমিত করে না। প্রযোজ্য প্রতিটি ধরনের প্রবেশ-অবস্থা ও ব্যবস্থাপনার দায়িত্ব [CS-6.310 Part B §9](corpus_systems/cs_06.310_data_classifications.md#cs-6310-9-data-classifications) (*Data classifications*) অনুযায়ী সম্পূর্ণভাবে প্রযোজ্য, ওই ধরনের জন্য উল্লেখিত [গোপনীয়তার মূল বিধান](corpus_systems/cs_06.310_data_classifications.md#privacy-link)-সহ।
- *সবচেয়ে সুরক্ষামূলক ধরনটি প্রাধান্য পায়।* একই তথ্য একাধিক ধরনের হলে [CS-6.305 Part A §2](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-2-determination-of-classification) (*শ্রেণিবিন্যাস নির্ধারণ*) অনুযায়ী প্রযোজ্য সবচেয়ে সুরক্ষামূলক ব্যবস্থাপনা প্রাধান্য পাবে; আর এক ধরনের ব্যবস্থাপনা মানলেই অন্য ধরনের দায়িত্ব মেটে না।

**গুচ্ছের ক্ষেত্রসমূহ।** বিভিন্ন স্থানে থাকা গোপনীয়তা-সুরক্ষা নিচের অনুচ্ছেদগুলোতে রয়েছে, প্রতিটিতে তার আওতাধীন তথ্যের ধরনসহ:

- **Article VII-A** (*নিজ দেহের ওপর স্বত্ব*) — স্বাস্থ্য, জৈব-পরিমিতি ও জীবদেহের ভিত্তির সঙ্গে যুক্ত নথির জন্য [**Type I**](corpus_systems/cs_06.310_data_classifications.md#95-type-i-identity-and-attribution-data);
- **Article VII-B** (*নিজ মনের ওপর স্বত্ব*) — অভ্যন্তরীণ অবস্থা, পুনর্গঠন বা অনুমানসহ, এর জন্য [**Type N**](corpus_systems/cs_06.310_data_classifications.md#96-type-n-neurocognitive-and-internal-data);
- **Article IX** (*সাদৃশ্য, অভিজ্ঞতামূলক তথ্য ও প্রকাশের অধিকার*):
  - [Article IX-A](core_06.005_rights_part_b.md#article-ix-a-self-ownership-of-likeness-and-reputation) (*সাদৃশ্য ও সুনামের ওপর স্বত্ব*) অনুযায়ী সাদৃশ্য ও কণ্ঠের জন্য **Type I**;
  - [Article IX-B](core_06.005_rights_part_b.md#article-ix-b-experiential-and-derived-data-rights) (*অভিজ্ঞতামূলক ও উদ্ভূত তথ্যের অধিকার*) অনুযায়ী অভিজ্ঞতা ও পারস্পরিক ক্রিয়া থেকে উদ্ভূত তথ্যের জন্য [**Type H**](corpus_systems/cs_06.310_data_classifications.md#94-type-h-historical-relational-transactional-and-participation-data); এবং
  - স্রষ্টার কাজের জন্য [Article IX-D](core_06.005_rights_part_b.md#article-ix-d-creative-work-training-data-use-and-anti-displacement) (*সৃজনশীল কাজ, প্রশিক্ষণ-তথ্য হিসেবে ব্যবহার, এবং স্থানচ্যুতি-রোধ*) অনুযায়ী [**Type Y**](corpus_systems/cs_06.310_data_classifications.md#98-type-y-yours); এর সুরক্ষা [**Type W**](corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published), [**Type U**](corpus_systems/cs_06.310_data_classifications.md#911-type-u-use-licensed), ও [**Type T**](corpus_systems/cs_06.310_data_classifications.md#912-type-t-transferred)-তেও প্রযোজ্য, স্রষ্টার [সংরক্ষিত অধিকার](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights)-সহ;
- **Article X-A** (*কর্তৃত্ব ও প্রভাব-প্রয়োগ থেকে স্বাধীনতা*) — অভ্যন্তরীণ অবস্থা, পুনর্গঠন বা অনুমানসহ, এর জন্য [**Type N**](corpus_systems/cs_06.310_data_classifications.md#96-type-n-neurocognitive-and-internal-data); এবং
- **Article XIV-A** (*নিরাপত্তা, গোয়েন্দা কার্যকলাপ ও গোপন ক্ষমতার সীমা*) — সীমাবদ্ধ নিরাপত্তা ও তদন্ত উপকরণের জন্য [**Type S**](corpus_systems/cs_06.310_data_classifications.md#97-type-s-safety-security-and-restricted-investigation-data); সীমাবদ্ধতা উঠে গেলে এর **H**, **I** বা **N** উপাদান ওই ধরনের সুরক্ষা বজায় রাখে।

**প্রত্যয়নে যা দেখাতে হবে:**

- *অংশগ্রহণ সম্ভব করা।* [Privacy (Informational)](core_05.040_band_continuity.md#privacy-informational) প্রকৃত [Participation](core_05.025_apex_participation_leg.md#participation-constitutional) সম্ভব করে। কণ্ঠ, আলোচনা, মেলামেশা ও চ্যালেঞ্জকে সমর্থনকারী গোপনীয়তা-সুরক্ষা বিভাজন, এক ক্ষেত্রের মান অন্য ক্ষেত্রে টেনে আনা, বা প্রকাশের চাপের মাধ্যমে নষ্ট হয়নি — প্রত্যয়নে তা নিশ্চিত করতে হবে।
- *উন্মুক্ত ও নিরীক্ষার জন্য প্রবেশযোগ্য তথ্যের ধরন।* ন্যূনতম সুরক্ষাগুলো দুই দিকেই প্রযোজ্য:
  - **Type E**, **Type G** বা **Type O** উপাদানের ভেতরে থাকা ব্যক্তিগত, সম্পর্কভিত্তিক বা অভ্যন্তরীণ-অবস্থার বিষয়বস্তু তার **H**, **I** বা **N** ব্যবস্থাপনা বজায় রাখে;
  - গোপনীয়তার কোনো ক্ষেত্র নিজে থেকেই **Type O** বা **Type E** তথ্যকে নিজস্ব নিয়মে অনুমোদিত সংকীর্ণ গোপন রাখার সীমার অতিরিক্ত গোপন করার যুক্তি দেয় না; এবং
  - কারও গোপনীয়তা রক্ষা ও জনসাধারণের প্রাপ্য তথ্য প্রকাশের মধ্যে প্রকৃত দ্বন্দ্ব হলে, কোনো পক্ষ স্বয়ংক্রিয়ভাবে জেতে না: [CS-6.305 §7](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems) (*Class A/B/C সিস্টেমের Type O ভিত্তি*) অনুযায়ী দ্বন্দ্বটি খোলাখুলিভাবে ও নথিতে নিষ্পত্তি হয়।
- *তথ্যের ধরন-সংক্রান্ত প্রমাণ।* [§3.4 তথ্যের ধরন ও ব্যবস্থাপনার মূল্যায়ন](#34-data-types-and-handling-evaluation)-এর অধীনে যাচাই করা [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record)-কে প্রতিটি প্রভাবিত গোপনীয়তা-ক্ষেত্রের প্রমাণ হিসেবে ব্যবহার করতে হবে: পরিধির তথ্যের ধরন এবং তার উদ্দেশ্য, প্রাপক, ভিত্তি ও উদ্ভূত তথ্য। ওই নথিতে দেখানো হয়নি এমন ব্যবস্থাপনার ভিত্তিতে কোনো গোপনীয়তার ক্ষেত্র নিষ্পত্তি করা যাবে না।

<a id="42-voluntary-discontinuation-major-self-modification-and-exit-rights"></a>
#### 4.2 স্বেচ্ছায় বন্ধ করা, বড় ধরনের স্ব-পরিবর্তন ও প্রস্থানের অধিকার

[Chapter One §7.4 Voluntary Discontinuation, Major Self-Modification, and Exit Rights](core_01.000_values_principles.md#74-voluntary-discontinuation-and-exit-rights) প্রত্যয়নের কোনো বিষয়ে প্রযোজ্য হলে, প্রত্যয়নের দাবি বহাল হওয়ার আগে প্রত্যয়নে স্বেচ্ছামূলকতা, সম্মতি, জবরদস্তি-রোধ, নির্ভরতার চাপ, তথ্যপ্রাপ্তি ও প্রত্যাবর্তনযোগ্যতা পরীক্ষা করতে হবে। কেবল আনুষ্ঠানিক সম্মতি যথেষ্ট নয়।

<a id="43-assembly-collective-organization-and-institutional-formation"></a>
#### 4.3 সমাবেশ, যৌথ সংগঠন ও প্রতিষ্ঠান গঠন

[Chapter One §7.2 Assembly, Collective Organization, and Institutional Formation](core_01.000_values_principles.md#72-assembly-collective-organization-and-institutional-formation) প্রত্যয়নের কোনো বিষয়ে প্রযোজ্য হলে, [Anti-Segmentation Principle](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle) অনুযায়ী বিষয়টি যৌথভাবে পরীক্ষা করতে হবে। কেবল একটি দৃষ্টিভঙ্গির মধ্য দিয়ে বিষয়টি এমনভাবে পরিচালনা করলে মূল্যায়ন অসম্পূর্ণ হবে, যাতে সমাবেশ বা যৌথ সংগঠনের সুরক্ষা ব্যর্থ হয়।

<a id="431-dissent-and-peaceful-protest"></a>
