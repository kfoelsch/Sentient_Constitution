##### 5.3.4 মানচিত্র ও নথির অখণ্ডতা

নির্ভরতার মানচিত্র ও সম্পদ-প্রবাহের নথির ওপর নির্ভর করার আগে, সেগুলো **Article V-A** (*নির্ভরতার মানচিত্র ও সম্পদ-প্রবাহের স্বচ্ছতা*) পূরণ করে কি না প্রত্যয়নে যাচাই করতে হবে। সেগুলো হতে হবে:

- **সম্পূর্ণ:** যেখানে প্রাসঙ্গিক, সেখানে উল্লেখযোগ্য ঊর্ধ্বমুখী ও নিম্নমুখী নির্ভরতা, সম্পদ-প্রবাহ এবং গোপন বা একপেশে সম্পর্ক অন্তর্ভুক্ত করবে।
- **হালনাগাদ:** পরিস্থিতি কত দ্রুত বদলায় এবং সিস্টেম কতটা গুরুত্বপূর্ণ তার সঙ্গে সামঞ্জস্য রেখে যথেষ্ট ঘন ঘন হালনাগাদ হবে; [§2 System Class Evaluation](#2-system-class-evaluation)-এর অধীনে সিস্টেম শ্রেণিও বিবেচ্য। এতে শেষ প্রত্যয়নের সময়কার অবস্থা নয়, সিস্টেমটি এখন যেভাবে চলছে তা দেখাবে।
- **নিরীক্ষাযোগ্য:** **Article XVI-A** (*নিরীক্ষাযোগ্যতা ও পর্যবেক্ষণযোগ্য প্রমাণ*)-এর অধীনে নিরীক্ষার জন্য উন্মুক্ত থাকবে।

এই পরীক্ষার যেকোনো একটিতে ব্যর্থ মানচিত্র বা নথির ভিত্তিতে সিস্টেম যথেষ্ট ফিরিয়ে দেয় বলে সিদ্ধান্ত নেওয়া যাবে না। ঘাটতিটি লিখে রাখতে হবে এবং নিচের *ত্রুটি ও অসামঞ্জস্য* অনুযায়ী ব্যবস্থা নিতে হবে।

<a id="535-system-class-scaling-and-escalation"></a>
##### 5.3.5 সিস্টেম শ্রেণি অনুযায়ী মাপ ও ধাপে উন্নীতকরণ

পর্যালোচনার গভীরতা এবং পর্যাপ্ততা কত নিবিড়ভাবে বিচার হবে তা সিস্টেমের শ্রেণি নির্ধারণ করে। ভাগ করা অবকাঠামো থেকে নেওয়া কিছুই এত ছোট হয়ে যায় না যে তা হিসাবের বাইরে থাকবে; এবং একাধিক সত্তা, নথি বা সময়কালে ভাগ করা আহরণকে [Chapter One §15.1.1 Anti-Segmentation Principle](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle) অনুযায়ী একত্রে বিচার করা হবে। বস্তুগততার শর্ত পূরণ হলেই:

- সংবেদনশীল সত্তাদের বেঁচে থাকার জন্য প্রয়োজনীয় ভাগ করা ভিত্তির ওপর নির্ভরশীল সিস্টেম — যেমন ভাগ করা জলাধার বা আঞ্চলিক বিদ্যুৎ-গ্রিডের প্রধান সংযোগব্যবস্থা — নির্ভরতার মানচিত্র ও ফিরতি প্রবাহের সবচেয়ে শক্তিশালী প্রমাণ নথিতে দেবে। এগুলোই ভাগ করা সিস্টেম, যেগুলোর দীর্ঘস্থায়ী সক্ষমতা [Chapter One §9 Shared-System Capacity](core_01.000_values_principles.md#9-shared-system-capacity) সুরক্ষিত করে; আর এখানেই **Article III-A** (*জীবনধারণ*)-এর কারণে শক্ত প্রমাণ বিশেষভাবে জরুরি।
- ভাগ করা authentication, health-IT বা অনুরূপ অবকাঠামোর ওপর নির্ভরশীল সিস্টেম কী নিচ্ছে এবং তার সহায়তা পর্যাপ্ত কি না, তা কার্যক্রমের গুরুত্বের সঙ্গে সামঞ্জস্যপূর্ণ গভীরতায় নথিভুক্ত করবে। “interoperability” নিয়ে অস্পষ্ট স্লোগান গণ্য হবে না: [Chapter One §18.5 Modular Architecture and Dependency Discipline](core_01.010_stewardship_capacity_principles.md#185-modular-architecture-and-dependency-discipline) অনুযায়ী মানচিত্র ও নথিতে নির্ভরতাটি দৃশ্যমান হতে হবে।
- যে প্রতিষ্ঠানগুলো বাস্তবে সহজে বদলাতে পারে না, তাদের জন্য কোনো সিস্টেম নীরবে অর্থপরিশোধ, পরিচয় বা কর্মী-নিয়োগের সংকীর্ণ মুখ হয়ে উঠলেও আন্তঃসিস্টেম পর্যালোচনা এড়াতে পারবে না।
  - **কারা বদলাতে পারে না:** [§5.3.3 মূল্যায়নের শর্ত](#533-evaluation-requirement)-এর প্রতিস্থাপনযোগ্যতার উপাদান অনুযায়ী বিচার হবে।
  - **কেন তা গুরুত্বপূর্ণ:** [Chapter One §11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)-এ বর্ণিত কেন্দ্রীভবনের এটিই ধরন। এতে গ্রহণকারীদের এ ধরনের কেন্দ্রীভবনের মাত্রা নির্ধারণ করতে বলা হয়েছে; যেমন বাস্তব বিকল্প ছাড়া একটি provider-এর ওপর কত sentient বা সিস্টেম নির্ভরশীল, অথবা ভাগ করা অবকাঠামোর interface ও প্রবেশপথ কে নিয়ন্ত্রণ করে। গ্রহণকারীর নির্ধারিত মাত্রা অতিক্রম না করা পর্যন্ত প্রত্যয়ন পর্যালোচনা উন্নীত করার জন্য অপেক্ষা করে না (নিচে দেখুন)।
  - **প্রত্যয়ন কী করে:** [§2.2 How system class scales every evaluation](#22-how-system-class-scales-every-evaluation)-এর অধীনে পর্যালোচনা উন্নীত করে এবং সিস্টেমের শ্রেণি পুনর্বিবেচনা করে; জীবনধারণ-অপরিহার্য সমন্বয়ে প্রবেশাধিকার সিস্টেম নিয়ন্ত্রণ করলে **Class A** পর্যন্ত উন্নীত হতে পারে।

উন্নীতকরণ [Chapter One §11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)-এর অধীনে নির্ধারিত কেন্দ্রীভবনের সীমার অপেক্ষা করে না। গ্রহণকারী সীমা নির্ধারণ করেছে এবং সিস্টেম তা অতিক্রম করেছে—এটি আরও প্রমাণ। সীমা নির্ধারণ না করা বা অতিরিক্ত উঁচু করে নির্ধারণ করা উন্নীতকরণ বিলম্বিত করে না; আবার সীমা অতিক্রম করাই একা অসদাচরণের সিদ্ধান্ত নয়।

<a id="536-defects-and-misalignment"></a>
##### 5.3.6 ত্রুটি ও অসামঞ্জস্য

[§5](#5-rights-floor-and-domain-evaluations) (*Rights-Floor and Domain Evaluations*)-এর ত্রুটিগুলো এই মূল্যায়নে প্রযোজ্য; **Article V-A** (*নির্ভরতার মানচিত্র ও সম্পদ-প্রবাহের স্বচ্ছতা*) অনুযায়ী সিস্টেমকে যে নির্ভরতা বা সম্পদ-প্রবাহের তথ্য প্রকাশ করতে হবে তাতেও প্রযোজ্য। এ ছাড়া, নিচের প্রতিটি বিষয় প্রত্যয়নের ত্রুটি:

- নিচের যেকোনো বিষয়কে [Proportionate Cross-System Support](core_05.040_band_continuity.md#proportionate-cross-system-support) পূরণের জন্য যথেষ্ট বলে ধরা:
  - প্রতীকী, অস্বচ্ছ, মানচিত্রের বাইরে, বা এককালীন হস্তান্তর;
  - সিস্টেম **Article III-A** (*জীবনধারণ*)-এর জীবনধারণের ন্যূনতম শর্ত পূরণ করে—এই তথ্য; অথবা
  - সিস্টেম [Chapter One §11 Market Structure](core_01.000_values_principles.md#11-market-structure)-এর বাজার-কেন্দ্রীভবনের সীমার মধ্যে আছে—এই তথ্য;
- বস্তুগততার শর্ত প্রযোজ্য থাকা সত্ত্বেও ফিরিয়ে না দিয়ে বারবার ভাগ করা ভিত্তি থেকে নেওয়া;
- মূলত capture বা কেন্দ্রীভবন শক্তিশালী করে এমন সহায়তা; এবং
- এমন শর্তযুক্ত সহায়তা, যা **Article V-A** (*নির্ভরতার মানচিত্র ও সম্পদ-প্রবাহের স্বচ্ছতা*) অনুযায়ী প্রয়োজনীয় স্বচ্ছতা নষ্ট করে।

সহায়তার নথিভুক্ত ঘাটতি [Chapter One §6 Trust and Trustworthiness](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)-এর অধীনে গণ্য হবে।

<a id="54-nondiscrimination-evaluation"></a>

#### 5.4 বৈষম্যহীনতার মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণপথ</span></strong></summary>

- **পূর্ববর্তী ভিত্তি:**
  - [Part C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*নথির বিষয়বস্তু*);
  - [§2](#2-system-class-evaluation) (*সিস্টেম শ্রেণির মূল্যায়ন*); Participation measurement family (*সাংবিধানিক পরিমাপ হিসেবে Substantive Fairness এবং Protected Characteristic Proxying and Disparate Impact*); **Article VI-C** (*বৈষম্যহীনতা*);
  - [Substantive Fairness](core_05.055_band_participation.md#substantive-fairness),
  - [Protected Characteristics](core_05.055_band_participation.md#protected-characteristics),
  - [Protected Characteristic Proxying and Disparate Impact](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact),
  - [Language, Culture, and Heritage](core_05.040_band_continuity.md#language-culture-and-heritage),
  - [Necessity](core_05.035_band_accountability.md#necessity), এবং
  - [Proportionality](core_05.035_band_accountability.md#proportionality) (Chapter Five)।
- **পূর্ববর্তী ভিত্তি: নীতি — Chapter One**
  - [§3.1 Fairness](core_01.000_values_principles.md#31-fairness) (বিশেষত [§3.1.2 Benefits and Burdens](core_01.000_values_principles.md#312-benefits-and-burdens)) এবং
  - [§11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*প্রবেশ নিয়ন্ত্রণ; §5.4.2-এ উন্নীতকরণ*)।
- **পরবর্তী ধাপ:**
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*সিস্টেম শ্রেণি অনুযায়ী বৈষম্যহীনতার উদাহরণমূলক প্রয়োগ*);
  - [Part C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*নথির অখণ্ডতা*);
  - [Part C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*যাচাইকৃত-ইনপুট গেট*);
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*বৈষম্যের ধরনজনিত অসামঞ্জস্য ও proxy-এর মাধ্যমে ফাঁকি*)।
- **এগুলোর সঙ্গে পড়ুন:** **Article VI-C** (*বৈষম্যহীনতা*)-এর বিচার ও পরিচালন-দায়িত্ব, যেখানে প্রত্যয়ন ফোরাম, প্রশাসনিক বা বলবৎকরণে প্রবেশ নিয়ন্ত্রণ করে; [*বৈষম্যহীনতা, সুরক্ষিত বৈশিষ্ট্য, মর্যাদা, অন্তরঙ্গ সংকেতভিত্তিক প্রবেশ-নিয়ন্ত্রণ, এবং **Article VII-E** (*প্রাপ্তবয়স্কদের সম্মতিতে বাণিজ্যিক যৌনসেবা ও যৌন শোষণ*)-এর মর্যাদা*](core_05.055_band_participation.md#fairness-protected-characteristics-and-nondiscrimination)।
- **উপবিভাগসমূহ:**
  - [§5.4.1](#541-evaluation-requirement) (*মূল্যায়নের শর্ত*);
  - [§5.4.2](#542-system-class-scaling-and-escalation) (*সিস্টেম শ্রেণি অনুযায়ী মাপ ও ধাপে উন্নীতকরণ*);
  - [§5.4.3](#543-defects-and-misalignment) (*ত্রুটি ও অসামঞ্জস্য*);
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*সিস্টেম শ্রেণি অনুযায়ী বৈষম্যহীনতার উদাহরণমূলক প্রয়োগ*)।

</details>

<br>

*সহজ ভাষায়: কিছু সিস্টেম ঠিক করে কে প্রবেশাধিকার পাবে। কিছু ঠিক করে কে বেশি দাম দেবে। কিছু ঠিক করে কে নিচে rank হবে বা বেশি ভার বহন করবে। সিস্টেম এমন সিদ্ধান্ত গুরুত্বপূর্ণভাবে নিলে, প্রত্যয়ন একটি প্রশ্ন করে: ক্ষতি কি মূলত সুরক্ষিত বৈশিষ্ট্যসম্পন্ন sentient-দের ওপর, অথবা তার proxy হিসেবে ব্যবহৃত বৈশিষ্ট্যের ওপর পড়ে? নিয়ম নিরপেক্ষ বলে অপারেটরের দাবি এ প্রশ্নের উত্তর নয়। কাজের উদাহরণ: [CS-9.320 §9 Illustrative nondiscrimination application by system class](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class)।*

বস্তুগত প্রভাবসম্পন্ন কোনো সিস্টেম sentient-দের মধ্যে বস্তুগতভাবে শ্রেণিবিন্যাস, rank, মূল্য নির্ধারণ, প্রবেশ নিয়ন্ত্রণ, বর্জন, বা ভার ও সুবিধা বণ্টন করলে — যোগ্যতার নিয়ম, model feature, ranking-এর যুক্তি, platform policy বা তুলনীয় সিদ্ধান্ত-পথসহ — এই বিভাগ প্রযোজ্য।

বস্তুগততার শর্ত প্রযোজ্য হলে, System alignment certification-এ **Article VI-C** (*বৈষম্যহীনতা*), [Substantive Fairness](core_05.055_band_participation.md#substantive-fairness), এবং [Protected Characteristic Proxying and Disparate Impact](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact)-এর অধীনে **বৈষম্যহীনতা** মূল্যায়ন করতে হবে।

<a id="541-evaluation-requirement"></a>
##### 5.4.1 মূল্যায়নের শর্ত

*সহজ ভাষায়: এই অধ্যায় অংশগ্রহণের কোটা নির্ধারণ করে না। কোনো fairness formula বেছে দেয় না। অন্য নথিতে সেসব থাকতে পারে। কর্পাসে পরে সংযোজন বা গ্রহণকারীর তৈরি নথিতেও থাকতে পারে। প্রত্যয়ন কেবল যাচাই করে যে কে সুবিধা পায়, কে ভার বহন করে এবং সুরক্ষিত বৈশিষ্ট্যের proxy ব্যবহৃত হচ্ছে কি না—এগুলো কেউ সত্যিই দেখেছে। শর্তটি প্রযোজ্য হলেই এই মূল্যায়নও প্রযোজ্য।*

প্রত্যয়ন প্রক্রিয়ায় নির্ধারণ করতে হবে, সিস্টেমের ওপর বস্তুগতভাবে নির্ভর করা সিদ্ধান্ত-পথ sentient-দের নিচের কোনো ভিত্তিতে বস্তুগত ভার, বর্জন বা ক্ষতির মুখে ফেলে কি না:

- [Protected Characteristics](core_05.055_band_participation.md#protected-characteristics);
- সেগুলোর proxy; অথবা
- কার্যকরী বিকল্প হিসেবে ব্যবহৃত খেয়ালখুশিমূলক গোষ্ঠীবিভাগ, যার মধ্যে [Language, Culture, and Heritage](core_05.040_band_continuity.md#language-culture-and-heritage)-এর অধীনে ভাষা, সংস্কৃতি ও ঐতিহ্যের বিশেষত্ব রয়েছে।

[material stake](core_00.000_preamble.md#material-stake) অনুযায়ী মাপ নির্ধারণ করে মূল্যায়নে:

- [Substantive Fairness](core_05.055_band_participation.md#substantive-fairness)-এর অধীনে ভার ও সুবিধার ধরন পরীক্ষা করতে হবে; এবং
- [Protected Characteristic Proxying and Disparate Impact](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact)-এর অধীনে proxy বা ভিন্নতর প্রভাবের ঝুঁকি পরীক্ষা করতে হবে।

পার্থক্যমূলক আচরণ গ্রহণযোগ্য কেবল যখন নথিভুক্ত [Necessity](core_05.035_band_accountability.md#necessity), [Proportionality](core_05.035_band_accountability.md#proportionality) এবং প্রকৃত ন্যায্যতা তা সমর্থন করে। কেবল নামমাত্র নিরপেক্ষতা, ঘোষিত উদ্দেশ্য বা লেবেল নয়, কার্যকরী প্রভাব মূল্যায়নে প্রতিফলিত হতে হবে।

<a id="542-system-class-scaling-and-escalation"></a>
##### 5.4.2 সিস্টেম শ্রেণি অনুযায়ী মাপ ও ধাপে উন্নীতকরণ

সিস্টেম শ্রেণি নির্ধারণ করে সিস্টেম কত গভীরভাবে মূল্যায়িত হবে। এটি ranking বা ভার অন্যের ওপর চাপানোকে বস্তুগত নয় বলে দেখার অনুমতি দেয় না। বস্তুগততার শর্ত পূরণ হলেই নিচের বিষয় প্রযোজ্য:

- **যেসব সিস্টেমের বন্ধ করা, notification বা তুলনীয় নিয়ম জীবনধারণের অপরিহার্য উপকরণ বন্ধ করে দিতে পারে:**
  - নথিতে সাধারণ best-practice বিবৃতি নয়, ভার-সুবিধা ও proxy-এর সবচেয়ে শক্তিশালী বিশ্লেষণ থাকতে হবে; এবং
  - গোপনভাবে খরচ অন্যের ওপর চাপানো [Chapter One §3.1.2 Benefits and Burdens](core_01.000_values_principles.md#312-benefits-and-burdens) পূরণ করে না।
- **যেসব সিস্টেমের matching বা routing যুক্তি জরুরি চিকিৎসা, সুবিধা বা credential-এ প্রবেশকে প্রভাবিত করে:**
  - নথিতে পরিচালনগত গুরুত্ব অনুযায়ী ভিন্নতর প্রভাব ও প্রকৃত ন্যায্যতার সিদ্ধান্ত নথিভুক্ত থাকতে হবে; এবং
  - কারণ হলো [Chapter One §3.1 Fairness](core_01.000_values_principles.md#31-fairness)-এর ন্যায্যতা মানে sentient-দের ব্যাখ্যাহীন নিয়মে বিচার না করা বা অন্যেরা যে খরচ এড়ায় তা তাদের ওপর না চাপানো।
- **যেসব সিস্টেমের shift, vendor বা booking-এর যুক্তি অংশগ্রহণকারীদের বস্তুগতভাবে rank করে বা বাদ দেয়:**
  - প্রকৃত বিশ্লেষণের বদলে নামমাত্র fairness অনুচ্ছেদ রেখে দেওয়া যাবে না;
  - সমন্বয় জীবনধারণের জন্য অপরিহার্য হলে, [§2.2 How system class scales every evaluation](#22-how-system-class-scales-every-evaluation)-এর অধীনে প্রত্যয়নে পর্যালোচনা উন্নীত ও পুনঃশ্রেণিবিন্যাস করতে হবে; কর্মী-নিয়োগ বা জরুরি routing নিয়ন্ত্রিত হলে **Class A**-তে পুনঃশ্রেণিবিন্যাসও এর অন্তর্ভুক্ত; এবং
  - [Chapter One §11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)-এর অধীনে এ ধরনের প্রবেশ-নিয়ন্ত্রণ কেন্দ্রীভবনের সূচক, কারণ বাস্তব বিকল্প ছাড়া বহু sentient বা সিস্টেম একটি provider-এর ওপর নির্ভর করে; তাই এখানেও প্রত্যয়ন পর্যালোচনা বাড়ায়।

<a id="543-defects-and-misalignment"></a>
##### 5.4.3 ত্রুটি ও অসামঞ্জস্য

এই মূল্যায়নে দুই ধরনের ত্রুটি প্রযোজ্য:

- **পুরো বিভাগের ত্রুটি:**
  - [§5](#5-rights-floor-and-domain-evaluations) (*Rights-Floor and Domain Evaluations*)-এর ত্রুটি এই মূল্যায়নে প্রযোজ্য; এবং
  - **Article VI-C** (*বৈষম্যহীনতা*)-এর অধীনে পর্যালোচনা আবশ্যক এমন বস্তুগত শ্রেণিবিন্যাস, ranking বা ভার-বণ্টনের যুক্তিতেও প্রযোজ্য।
- **বৈষম্যহীনতা-সংক্রান্ত ত্রুটি:** নিচের প্রতিটি বিষয়কেও প্রত্যয়নের ত্রুটি হিসেবে ধরতে হবে:
  - মূল্যায়নযোগ্য ভার-সুবিধার বিশ্লেষণ ছাড়া বাহ্যিকভাবে নিরপেক্ষ মনে হওয়া, সামষ্টিক সুবিধা-পরিমাপক বা অপারেটরের নিজের প্রতিবেদনকে যথেষ্ট ধরা; এবং
  - **Article VI-C** (*বৈষম্যহীনতা*)-এর **Necessity** ও **Proportionality** পরীক্ষা পূরণ না করেই একরূপীকরণ, interoperability বা দক্ষতার দৃষ্টিভঙ্গি ব্যবহার করে ভাষা, সংস্কৃতি বা ঐতিহ্যের সুরক্ষা নষ্ট করা।

নথিভুক্ত proxy-ভিত্তিক বৈষম্য বা প্রকৃত অন্যায্যতা [Chapter One §6 Trust and Trustworthiness](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)-এর অধীনে গণ্য হবে।

<a id="55-accessibility-evaluation"></a>

#### 5.5 প্রবেশগম্যতার মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণপথ</span></strong></summary>

- **পূর্ববর্তী ভিত্তি:**
  - [Part C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*নথির বিষয়বস্তু*);
  - [§2](#2-system-class-evaluation) (*সিস্টেম শ্রেণির মূল্যায়ন*); Participation measurement family (*সাংবিধানিক পরিমাপ হিসেবে প্রবেশগম্যতা*); **Article VI-D** (*প্রবেশগম্যতা*);
  - [Accessibility](core_05.055_band_participation.md#accessibility),
  - [Materiality](core_05.050_band_oversight.md#materiality),
  - [Dependency](core_05.040_band_continuity.md#dependency),
  - [Meaningful Agency](core_05.055_band_participation.md#meaningful-agency),
  - [Protected Characteristics](core_05.055_band_participation.md#protected-characteristics),
  - [Protected Characteristic Proxying and Disparate Impact](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact),
  - [Substantive Fairness](core_05.055_band_participation.md#substantive-fairness),
  - [Necessity](core_05.035_band_accountability.md#necessity), এবং
  - [Proportionality](core_05.035_band_accountability.md#proportionality) (Chapter Five)।
- **পূর্ববর্তী ভিত্তি: নীতি — Chapter One**
  - [§3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help) (*§5.5.2-তে বদলানো প্রয়োজন; §5.5.3-তে সাড়া না দেওয়ার সুরক্ষা*),
  - [§7.1 Limitation Discipline](core_01.000_values_principles.md#71-limitation-discipline),
  - [§5.2 Plain-Language Accessibility](core_01.000_values_principles.md#52-plain-language-accessibility-participation-and-stewardship-duty), এবং
  - [§11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*প্রবেশ-নিয়ন্ত্রণ; §5.5.3-তে ধাপে উন্নীতকরণ*)।
- **পরবর্তী ধাপ:**
  - [CS-9.320 §10](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-10-illustrative-accessibility-application-by-system-class) (*সিস্টেম শ্রেণি অনুযায়ী প্রবেশগম্যতার উদাহরণমূলক প্রয়োগ*);
  - [Part C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*নথির অখণ্ডতা*);
  - [Part C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*যাচাইকৃত-ইনপুট গেট*);
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*প্রবেশগম্যতার অসামঞ্জস্য ও কেবল কাগজে থাকা সুবিধা*)।
- যেখানে শিক্ষায় প্রবেশগম্যতা প্রাসঙ্গিক, সেখানে **Article IV-A** (*শিক্ষায় সমান প্রবেশাধিকার*)-এর সঙ্গে পড়ুন — শিক্ষা-নির্দিষ্ট প্রবেশগম্যতার দায়িত্ব সেখানেই; **Article III-A** (*জীবনধারণ*)-এর সঙ্গে, যেখানে বিল, আদায় বা বন্ধের ধাপ জীবনধারণের অপরিহার্য উপকরণে প্রবেশ শেষ করে দিতে পারে — [§5.5.3](#553-system-class-scaling-and-escalation)-এর সাড়া না-দেওয়া সংক্রান্ত সুরক্ষার পেছনের অর্থপূর্ণ নোটিশের শর্ত; **Article VI-C** (*বৈষম্যহীনতা*) (বিচার ও পরিচালনা) এবং **Article XII** (*অংশীজনের সিস্টেমে অংশগ্রহণ, প্রতিনিধিত্ব ও যথাযথ প্রক্রিয়া*)-এর সঙ্গে, যেখানে প্রত্যয়ন ফোরাম, প্রশাসনিক, অংশীজন বা বলবৎকরণে অংশগ্রহণ নিয়ন্ত্রণ করে; [Chapter Nine §5.5](#55-accessibility-evaluation) (*সব ক্ষেত্র জুড়ে প্রযোজ্য প্রবেশগম্যতার মূল্যায়ন-উপাদানের সংযোগ*)।
- **উপবিভাগসমূহ:**
  - [§5.5.1](#551-evaluation-requirement) (*মূল্যায়নের শর্ত*);
  - [§5.5.2](#552-profiles-in-scope) (*পরিধিতে থাকা profile*);
  - [§5.5.3](#553-system-class-scaling-and-escalation) (*সিস্টেম শ্রেণি অনুযায়ী মাপ ও ধাপে উন্নীতকরণ*);
  - [§5.5.4](#554-defects-and-misalignment) (*ত্রুটি ও অসামঞ্জস্য*);
  - [CS-9.320 §10](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-10-illustrative-accessibility-application-by-system-class) (*সিস্টেম শ্রেণি অনুযায়ী প্রবেশগম্যতার উদাহরণমূলক প্রয়োগ*)।

</details>

<br>

*সহজ ভাষায়: কোনো সিস্টেম সংবেদনশীল সত্তারা সত্যিই অংশ নিতে পারবে কি না তা বস্তুগতভাবে নিয়ন্ত্রণ করলে — শুধু দরজায় “খোলা” লেখা আছে কি না নয় — সংবেদন, চিন্তা, চলাচল, যোগাযোগ, দেহগত ভিত্তি ও interface, গণনামাধ্যমের interface, এবং তুলনীয় প্রয়োজন জুড়ে অংশগ্রহণ সত্যিই সম্ভব কি না, প্রত্যয়নে যাচাই করতে হবে। সুবিধার তালিকা ও interface-এর মান অন্য নথি, কর্পাসে পরবর্তী সংযোজন, বা গ্রহণের নথিতে থাকতে পারে; শর্ত প্রযোজ্য হলে প্রকৃত অংশগ্রহণ মূল্যায়িত হয়েছে কি না প্রত্যয়ন যাচাই করে। কাজের উদাহরণ: [CS-9.320 §10 Illustrative accessibility application by system class](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-10-illustrative-accessibility-application-by-system-class)।*

সংবেদনশীল সত্তাদের জীবনে বড় প্রভাব ফেলা সিস্টেম সংবিধান-সুরক্ষিত কোনো বিষয়ে তারা সত্যিই অংশ নিতে পারবে কি না নিয়ন্ত্রণ করলে এই বিভাগ প্রযোজ্য, যেমন:

- শাসন, অংশীজনের অংশগ্রহণ, বিচার ও পরিচালনা;
- জীবনধারণের অপরিহার্য উপকরণ ও স্বাস্থ্যসেবা;
- মতপ্রকাশ, সমাবেশ ও সংবাদমাধ্যম; অথবা
- তুলনীয় ক্ষেত্র।

নিয়ন্ত্রণ আসতে পারে:

- interface, স্থান বা সময়সূচি থেকে;
- credential বা গণনাশক্তিতে প্রবেশাধিকার থেকে;
- সুবিধার নকশা থেকে; অথবা
- অনুরূপ পথ থেকে।

শিক্ষায় প্রবেশগম্যতার দায়িত্ব **Article IV-A** (*শিক্ষায় সমান প্রবেশাধিকার*)-এর অধীনে থাকবে; এখানকার কিছুই তা সংকুচিত করে না।

যেখানে তা প্রযোজ্য, **Article VI-D** (*প্রবেশগম্যতা*) এবং [Accessibility](core_05.055_band_participation.md#accessibility)-এর অধীনে প্রত্যয়নে **প্রবেশগম্যতা** মূল্যায়ন করতে হবে। এই বিভাগ নির্ধারণ করে না:

- সুবিধার তালিকা;
- interface-এর মান;
- সর্বজনীন নকশার নির্দিষ্টকরণ; অথবা
- দৈনন্দিন সুবিধা দেওয়ার কার্যপ্রণালি।

সেগুলো থাকতে পারে অন্য অন্তর্ভুক্ত নথিতে।

<a id="551-evaluation-requirement"></a>
##### 5.5.1 মূল্যায়নের শর্ত

আনুষ্ঠানিক বৈশিষ্ট্য, পূর্বনির্ধারিত interface বা কাগজে থাকা সুবিধা আছে কি না কেবল তা নয়, সিস্টেম যে ক্ষেত্রগুলো নিয়ন্ত্রণ করে সেগুলোতে sentient-রা সত্যিই অংশ নিতে পারে কি না প্রত্যয়নে যাচাই করতে হবে। [Accessibility](core_05.055_band_participation.md#accessibility)-এর অধীনে অংশগ্রহণের বাস্তব প্রভাব পরীক্ষা করতে হবে এবং [Materiality](core_05.050_band_oversight.md#materiality) ও [Dependency](core_05.040_band_continuity.md#dependency) অনুযায়ী মাপ নির্ধারণ করতে হবে।

পর্যালোচকদের নজর দিতে হবে:

- কেবল কাগজে থাকা সুবিধা;
- “সাধারণ প্রবেশাধিকার”-এর দাবি, যা পূর্বনির্ধারিত বৈশিষ্ট্যের ওপর নির্ভর করে কিন্তু কাউকে বাস্তবে অংশ নেওয়ার সক্ষমতা দেয় না;
- সিস্টেমটি কেবল আংশিকভাবে বস্তুগত—এমন যুক্তি দেখিয়ে তার দিতে-হওয়া সুবিধা কমানো;
- [Sentience Non-Exclusion](core_05.055_band_participation.md#sentience-non-exclusion)-এর সঙ্গে সাংঘর্ষিক বর্জন; এবং
- সময়সূচি, স্থান নির্বাচন, credential, গণনাশক্তিতে প্রবেশাধিকার বা অনুরূপ কার্যপ্রণালির মাধ্যমে পরোক্ষভাবে sentient-দের বাদ দেওয়া নকশা (proxy-এর মাধ্যমে বঞ্চনা)।

সুবিধার নকশায় [Protected Characteristics](core_05.055_band_participation.md#protected-characteristics) এবং [Protected Characteristic Proxying and Disparate Impact](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact)-ও প্রত্যয়নে প্রয়োগ করতে হবে। সুবিধার যেকোনো সীমা নথিভুক্ত হতে হবে এবং [Necessity](core_05.035_band_accountability.md#necessity), [Proportionality](core_05.035_band_accountability.md#proportionality), ও [Substantive Fairness](core_05.055_band_participation.md#substantive-fairness) পূরণ করতে হবে।

<a id="552-profiles-in-scope"></a>
##### 5.5.2 পরিধিতে থাকা profile

[Accessibility](core_05.055_band_participation.md#accessibility)-এর অধীনে পরিধিতে থাকা প্রতিটি sentient-এর ধরন ও সক্ষমতা-profile-এর ক্ষেত্রে কাগজে নিয়ম মানা নয়, বাস্তব অংশগ্রহণ পরীক্ষা করতে হবে:

- **যে profile-গুলো গণ্য:** সংবেদন, চিন্তা, চলাচল ও যোগাযোগের profile; কোনো sentient তার দেহগত ভিত্তির (**substrate-interface**) মাধ্যমে বা গণনামাধ্যমের (**compute-interface**) মাধ্যমে কীভাবে যুক্ত হয় সে-সংক্রান্ত profile; এবং তুলনীয় profile।
- **সময়ের সঙ্গে প্রয়োজন বদলানো:** profile **স্থায়ী** (একই থাকে), **পর্বভিত্তিক** (আসে ও যায়), অথবা **বিকাশভিত্তিক** (sentient-এর বিকাশের সঙ্গে বদলায়) হতে পারে। তিনটিই একইভাবে অন্তর্ভুক্ত; আর [Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help)-এর অধীনে, sentient আগে কী পারত বা তার label কী, তা নয়—এখন সে কী করতে পারে তার ভিত্তিতে বিচার হবে।
- **যা এই বিভাগ পূরণ করে না:**
  - **সাধারণ প্রবেশাধিকার**-এর দাবি, যেখানে সামগ্রিক প্রবেশাধিকার বিস্তৃত মনে হলেও প্রভাবিত sentient-দের নির্দিষ্ট একটি গোষ্ঠী বাস্তব প্রবেশাধিকার পায় না; এবং
  - **বেছে বেছে বস্তুগততা মাপা**, যেখানে সিস্টেমটি কেবল আংশিক বস্তুগত বলা হয় তার দিতে-হওয়া সুবিধা কমাতে, ফলে sentient-রা **Article VI-D** (*প্রবেশগম্যতা*)-এর সুরক্ষিত অংশগ্রহণের নিচে নেমে যায়।

<a id="553-system-class-scaling-and-escalation"></a>
##### 5.5.3 সিস্টেম শ্রেণি অনুযায়ী মাপ ও ধাপে উন্নীতকরণ

সিস্টেম শ্রেণি মূল্যায়নের গভীরতা বদলায়। কিন্তু কাগজে থাকা সুবিধা বা পূর্বনির্ধারিত interface যথেষ্ট বলে ধরার অনুমতি কখনো দেয় না। বস্তুগততার শর্ত পূরণ হলেই:

- সিস্টেমের bill বা outage-এর পথ sentient-দের জীবনধারণের অপরিহার্য উপকরণ থেকে বিচ্ছিন্ন করতে পারে, এমন হলে নথিতে দেখাতে হবে sentient-রা বাস্তবে অংশ নিতে পারে—এর সবচেয়ে শক্ত প্রমাণ। সাধারণ প্রবেশগম্যতার বিবৃতি যথেষ্ট নয়। sentient-দের বাদ দেয় এমন বাধার জন্য [Chapter One §7.1 Limitation Discipline](core_01.000_values_principles.md#71-limitation-discipline)-এর অধীনে যুক্তি দিতে হবে; এবং বিল ও outage-এর notice এমনভাবে লিখতে হবে যাতে sentient-রা [Chapter One §5.2 Plain-Language Accessibility](core_01.000_values_principles.md#52-plain-language-accessibility-participation-and-stewardship-duty)-এর অধীনে তা পড়ে পদক্ষেপ নিতে পারে।
- sentient-রা অর্থ দেওয়া বা উত্তর দেওয়া বন্ধ করলে সিস্টেমের bill, আদায় বা সংযোগ বন্ধের প্রক্রিয়া তাদের জীবনধারণের অপরিহার্য উপকরণ থেকে বিচ্ছিন্ন করতে পারে, এমন হলে কারণ যাই হোক উত্তর দিতে না-পারা sentient-দের কীভাবে সুরক্ষা দেয় তা নথিতে দেখাতে হবে; গুরুতর বিষণ্নতার মতো চিন্তা বা মানসিক স্বাস্থ্যের অবস্থাও অন্তর্ভুক্ত। sentient কেন নীরব তা সিস্টেমের জানার প্রয়োজন হওয়া চলবে না। এটি [Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help)-কে bill, আদায় ও সংযোগ বন্ধে প্রয়োগ করে। নীরবতা সম্মতি নয়, এবং সেবাটি ছেড়ে দেওয়ার সিদ্ধান্তও নয়। যে notice-এর ভিত্তিতে sentient পদক্ষেপ নিতে পারে না তা অপরিহার্য সম্পর্ক শেষ করার আগে **[Article III-A** (*জীবনধারণ*)](core_06.000_rights_part_a.md#article-iii-a-survival) যে অর্থপূর্ণ notice চায় তা নয়। নথিতে দেখাতে হবে:
  - sentient-এর সঙ্গে যোগাযোগের একাধিক উপায়, এবং আগে উত্তরহীন থাকা মাধ্যমের ওপর নির্ভর না করে পরবর্তী যোগাযোগ;
  - সংযোগ বন্ধ করার আগে যোগাযোগ করার জন্য, আগেই কোনো বিশ্বস্ত sentient বা উকিল বেছে নেওয়ার উপায়; কেবল উত্তর পাওয়ার জন্য প্রয়োজনীয় তথ্যই ভাগ করা হবে;
  - সংযোগ বন্ধ করার আগে সক্রিয়ভাবে যোগাযোগের চেষ্টা, যেখানে সিস্টেম sentient-কে সাহায্যের সঙ্গে যুক্ত করার চেষ্টা করবে (যেমন সহায়তা বা যত্নের সেবা, অথবা তার বেছে নেওয়া যোগাযোগ), sentient নিজে এগিয়ে আসা পর্যন্ত অপেক্ষা করবে না;
  - উত্তর না দেওয়ার কারণে জীবনধারণের অপরিহার্য উপকরণ বন্ধ করার আগে sentient পর্যালোচক দ্বারা পর্যালোচনা, কেবল automated process নয়; পর্যালোচনা হবে সিস্টেম যা পর্যবেক্ষণ করতে পারে (উত্তরহীন যোগাযোগ এবং কী ঝুঁকিতে আছে) তার ভিত্তিতে, sentient-এর স্বাস্থ্য বা মানসিক অবস্থা সম্পর্কে অনুমানের ভিত্তিতে নয়; এবং
  - দ্রুত ও কম বাধার প্রত্যাবর্তন-পথ (সেবা পুনরুদ্ধার ও অর্থপ্রদানের ব্যবস্থা), যাতে একবারের নীরবতা স্থায়ী ক্ষতিতে পরিণত না হয়।
- সিস্টেমের portal স্বাস্থ্যসেবায় প্রবেশ নিয়ন্ত্রণ করলে, সুবিধা এবং proxy-এর মাধ্যমে বঞ্চনা সম্পর্কে সিদ্ধান্ত নথিভুক্ত করতে হবে। কার্যক্রম যত গুরুত্বপূর্ণ, বিশদ তত বেশি দরকার।
- shift, booking বা vendor interface অংশগ্রহণকারীদের বস্তুগতভাবে বাদ দিলেও সিস্টেম প্রবেশগম্যতা নিয়ে নামমাত্র অনুচ্ছেদ রেখে পার পাবে না। সিস্টেমের সমন্বয় জীবনধারণের জন্য অপরিহার্য হলে, প্রত্যয়নে নিবিড়তর পর্যালোচনা এবং [§2.2 How system class scales every evaluation](#22-how-system-class-scales-every-evaluation)-এর অধীনে তার শ্রেণি পুনর্বিবেচনা করতে হবে। কর্মী-নিয়োগ বা জরুরি routing নিয়ন্ত্রিত হলে **Class A**-এর দিকে উন্নীতকরণও এর মধ্যে পড়ে। sentient-রা বাস্তবে এড়াতে পারে না এমন interface-ই [Chapter One §11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)-এ বলা প্রবেশ-নিয়ন্ত্রণ।

<a id="554-defects-and-misalignment"></a>
##### 5.5.4 ত্রুটি ও অসামঞ্জস্য

[§5](#5-rights-floor-and-domain-evaluations) (*Rights-Floor and Domain Evaluations*)-এর ত্রুটিগুলো এই মূল্যায়নে প্রযোজ্য। এ ছাড়া, নিচের প্রতিটি বিষয়কে প্রত্যয়নের ত্রুটি হিসেবে ধরতে হবে:

- প্রকৃত অংশগ্রহণের মূল্যায়ন ছাড়া আনুষ্ঠানিক সুবিধা, পূর্বনির্ধারিত interface বা কাগজে থাকা সুবিধাকে যথেষ্ট ধরা;
- **Article VI-D** (*প্রবেশগম্যতা*)-এর **Necessity** ও **Proportionality** পরীক্ষা পূরণ না করে অংশগ্রহণের ন্যূনতম মান নষ্ট করতে খরচ, নকশা-পছন্দ, দেহগত ভিত্তির শ্রেণি বা কার্যক্রমের মাত্রাকে যুক্তি হিসেবে ব্যবহার করা;
- কম ভারসৃষ্টিকারী বিকল্প বাস্তবসম্মত হলেও কার্যক্রমের নকশায় প্রবেশগম্যতা নষ্ট করা; এবং
- [§5.5.3 System Class Scaling and Escalation](#553-system-class-scaling-and-escalation)-এর অধীনে নথিতে দেখাতে-হওয়া সুরক্ষা ছাড়া, sentient-এর নীরবতা বা অর্থ না দেওয়াকে সম্মতি, প্রত্যাখ্যান বা সেবা ছেড়ে দেওয়ার সিদ্ধান্ত ধরে জীবনধারণের অপরিহার্য উপকরণ বন্ধ করা।

অংশগ্রহণের নথিভুক্ত বাধা [Chapter One §6 Trust and Trustworthiness](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)-এর অধীনে গণ্য হবে।

<a id="56-trustworthiness-and-system-reliance-integrity-evaluation"></a>

#### 5.6 বিশ্বস্ততা ও সিস্টেমের ওপর নির্ভরতার অখণ্ডতার মূল্যায়ন

<details>
<summary><strong><span style="color: #2563eb;">অনুসরণপথ</span></strong></summary>

- **পূর্ববর্তী ভিত্তি:**
  - [Part C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*নথির বিষয়বস্তু*);
  - [§2](#2-system-class-evaluation) (*সিস্টেম শ্রেণির মূল্যায়ন*); Oversight measurement family (*Truth ও জ্ঞানগত অখণ্ডতা; সাংবিধানিক পরিমাপ হিসেবে Trustworthiness এবং Trust Degradation and Misleading Reliance*); **Article XIII** (*নির্ভরযোগ্য ও বিশ্বস্ত সিস্টেমের অধিকার*);
  - [Trustworthiness](core_05.040_band_continuity.md#trustworthiness),
  - [Trust](core_05.040_band_continuity.md#trust),
  - [Trust Degradation and Misleading Reliance](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance),
  - [Contestability](core_05.035_band_accountability.md#contestability),
  - [Redress and Remediation](core_05.035_band_accountability.md#redress-and-remediation),
  - [Incentive Alignment](core_05.045_band_integrative.md#incentive-alignment),
  - [Reversibility](core_05.040_band_continuity.md#reversibility),
  - [Materiality](core_05.050_band_oversight.md#materiality),
  - [Dependency](core_05.040_band_continuity.md#dependency), এবং
  - [Risk](core_05.040_band_continuity.md#risk) (Chapter Five)।
- **পূর্ববর্তী ভিত্তি: নীতি — Chapter One**
  - [§3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help) (*sentient-রা এখন যেমন, তাদের জন্য কার্যকর চ্যালেঞ্জ ও পর্যালোচনার পথ; যারা নির্ভর করে সেই sentient-দের ভিত্তিতে বিভ্রান্তিকর নির্ভরতা বিচার; সাড়া না-দেওয়া sentient-দের কাছে জীবনধারণ-সংক্রান্ত জরুরি সতর্কতা পৌঁছানো*),
  - [§4 Safety](core_01.000_values_principles.md#4-safety-harm-constraint),
  - [§6 Trust](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity),
  - [§10 Resilience and Self-Healing Design](core_01.000_values_principles.md#10-resilience-and-self-healing-design), এবং
  - [§11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*যে নির্ভরতা বাস্তবে এড়ানো যায় না; §5.6.2-তে ধাপে উন্নীতকরণ*)।
- **পরবর্তী ধাপ:**
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*সিস্টেম শ্রেণি অনুযায়ী বিশ্বস্ততার উদাহরণমূলক প্রয়োগ*);
  - [Part C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*নথির অখণ্ডতা*);
  - [Part C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*যাচাইকৃত-ইনপুট গেট*);
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*মিথ্যা বিশ্বাস, বিকৃত প্রণোদনা ও পুনরুদ্ধারের অখণ্ডতাজনিত অসামঞ্জস্য*)।
- **এগুলোর সঙ্গে পড়ুন:** **Article XIII-A** (*নির্ভরযোগ্যতা ও বিশ্বস্ততার ভিত্তি*), **Article XIII-B** (*প্রতিকার ও প্রতিকার-লাভের অধিকার*) এবং **Article XVI** (*Audit, Transparency, and Independent Verification*) — চ্যালেঞ্জ ও নিরীক্ষার অধিকারের দায়িত্ব সেখানেই; উচ্চ-স্বায়ত্তশাসিত সিস্টেম শাসন বা যাচাইয়ের পথ বস্তুগতভাবে চালালে **Article XIII-E** (*উচ্চ-স্বায়ত্তশাসিত সিস্টেম ও tool-মাধ্যমে প্রক্রিয়ার অখণ্ডতা*)-এর সঙ্গে; সিস্টেমের ওপর অব্যাহত নির্ভরতা জীবনধারণ-অপরিহার্য প্রবেশকে প্রভাবিত করলে **Article III-A** (*জীবনধারণ*)-এর সঙ্গে; দেহ, স্বাস্থ্য বা নিরাপত্তাকে প্রভাবিত করতে পারে এমন পণ্য বা সেবা সিস্টেম সরবরাহ, তালিকাভুক্ত, সুপারিশ বা পরামর্শ দিলে **Article III-F** (*নিরাপদ পণ্য ও স্বাস্থ্য-তথ্য*)-এর সঙ্গে; স্বাস্থ্য ও নিরাপত্তা-সংক্রান্ত তথ্যের ওপর নির্ভরশীল প্রত্যেক sentient-এর জন্য তা ব্যবহারযোগ্য হওয়া দরকার হলে **Article VI-D** (*প্রবেশগম্যতা*)-এর সঙ্গে; [Chapter One §6 Trust](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) (1.000 §6) এবং [Chapter One §5 Truth](core_01.000_values_principles.md#5-truth-epistemic-integrity-constraint) (1.000 §5)-এর সঙ্গে।
- **কার্যকরী পরিভাষা:** পণ্য ও সেবার স্বাস্থ্য ও নিরাপত্তা-তথ্য এবং rating, ranking ও অর্থপ্রদত্ত প্রচারের জন্য [CJS-5.120 §10](corpus_joint_structure/cjs_05.120_participation_operations.md#product-and-service-health-and-safety-information) (*Participation: প্রকাশের পর্যাপ্ততা ও পর্যবেক্ষণযোগ্যতার শর্ত*); ক্ষতির প্রতিবেদন ও সংশোধনী নোটিশের জন্য [CJS-5.125 §15](corpus_joint_structure/cjs_05.125_accountability_operations.md#harm-reports-and-corrective-notices) (*Accountability: কাঠামোগত পর্যালোচনা, সংশোধনের জরুরিতা ও প্রকাশের শর্ত*)।
- **উপবিভাগসমূহ:**
  - [§5.6.1](#561-evaluation-requirement) (*মূল্যায়নের শর্ত*);
  - [§5.6.2](#562-system-class-scaling-and-escalation) (*সিস্টেম শ্রেণি অনুযায়ী মাপ ও ধাপে উন্নীতকরণ*);
  - [§5.6.3](#563-defects-and-misalignment) (*ত্রুটি ও অসামঞ্জস্য*);
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*সিস্টেম শ্রেণি অনুযায়ী বিশ্বস্ততার উদাহরণমূলক প্রয়োগ*)।

</details>

<br>

*সহজ ভাষায়: কোনো সিস্টেম সংবেদনশীল সত্তারা তার কথা ও কাজে ভরসা করতে পারে কি না — এবং সেই বিশ্বাস ভেঙে গেলে আপত্তি জানাতে পারে কি না — তা বস্তুগতভাবে প্রভাবিত করলে, নির্ভরতা ন্যায্য কি না, সততার সঙ্গে প্রকাশিত হয়েছে কি না এবং সমস্যা সারানো যায় কি না, প্রত্যয়নে যাচাই করতে হবে। নির্ভরযোগ্যতার পরিমাপক ও test-suite-এর নকশা অন্য নথিতে রয়েছে; শর্ত প্রযোজ্য হলে বিশ্বস্ততা, মিথ্যা বিশ্বাসের ঝুঁকি ও চ্যালেঞ্জের পথ সত্যিই মূল্যায়িত হয়েছে কি না, প্রত্যয়ন তা যাচাই করে। কাজের উদাহরণ: [CS-9.320 §11 Illustrative trustworthiness application by system class](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class)।*

কোনো বড় সিস্টেম সংবেদনশীল সত্তারা কোন বিষয়ে তার ওপর নির্ভর করে তা গঠন করলে এই বিভাগ প্রযোজ্য: সিস্টেম কী করে, তার সীমা কোথায়, কী ভুল হতে পারে, কীভাবে চ্যালেঞ্জ করা যায়, এবং সমস্যা কীভাবে ঠিক হয়। এমন প্রভাব আসতে পারে:

- তার নির্ভরযোগ্যতা সম্পর্কে দাবি;
- কী প্রকাশ করে বা করে না;
- বাস্তবে কীভাবে চলে;
- এর মধ্যে থাকা প্রণোদনা;
- ব্যর্থতা থেকে কীভাবে পুনরুদ্ধার করে; অথবা
- sentient-দের তার ওপর নির্ভরশীল করে এমন অনুরূপ কোনো পথ।

বস্তুগততার শর্ত প্রযোজ্য হলে, নিচের বিষয় অনুযায়ী System alignment certification-এ **বিশ্বস্ততা ও সিস্টেম-নির্ভরতার অখণ্ডতা** মূল্যায়ন করতে হবে:

- **Article XIII** (*নির্ভরযোগ্য ও বিশ্বস্ত সিস্টেমের অধিকার*);
- [Trustworthiness](core_05.040_band_continuity.md#trustworthiness); এবং
- [Trust Degradation and Misleading Reliance](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance)।

<a id="561-evaluation-requirement"></a>
##### 5.6.1 মূল্যায়নের শর্ত

**Article XIII-A** (*নির্ভরযোগ্যতা ও বিশ্বস্ততার ভিত্তি*) অনুযায়ী, sentient-দের সিস্টেমটিকে [বিশ্বাস](core_05.040_band_continuity.md#trust) করার যথেষ্ট কারণ আছে কি না এবং তারা সঠিকভাবে তার ওপর নির্ভর করতে পারে কি না, প্রত্যয়ন প্রক্রিয়ায় যাচাই করতে হবে।

মূল্যায়নে আরও পরীক্ষা করতে হবে:

- sentient-রা বাস্তবে সিস্টেমকে চ্যালেঞ্জ করতে পারে, সিদ্ধান্ত পুনর্বিবেচনা করাতে পারে, এবং সমস্যা সারাতে পারে কি না — কেবল কাগজে নয়। বর্তমান অবস্থায় sentient-দের জন্য এটি কার্যকর হতে হবে, যাদের সহজে উত্তর দেওয়া বা দীর্ঘ প্রক্রিয়া পার হওয়া সম্ভব নয় তারাও অন্তর্ভুক্ত ([Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **Article XIII-A** (*নির্ভরযোগ্যতা ও বিশ্বস্ততার ভিত্তি*) এবং **Article XIII-B** (*প্রতিকার ও প্রতিকার-লাভের অধিকার*));
- সিস্টেমটি প্রাপ্যতার চেয়ে বেশি বিশ্বাস বা নির্ভরতা অর্জন করেছে বলে sentient-দের বিভ্রান্ত করা হতে পারে কি না — অর্জন না-করা বিশ্বাসের মাধ্যমে, অথবা তার অপ্রকাশিত সীমার কারণে। গড় sentient নয়, যারা বাস্তবে সিস্টেমটি ব্যবহার করে তাদের ভিত্তিতে তা বিচার হবে (**Article XIII-C** (*মিথ্যা বিশ্বাস ও বিভ্রান্তিকর নির্ভরতা নিষিদ্ধকরণ*));
- স্বাস্থ্য বা নিরাপত্তাকে প্রভাবিত করতে পারে এমন পণ্য ও সেবা সম্পর্কে সিস্টেম যে তথ্য দেয় তা সঠিক, পদক্ষেপ নেওয়ার মতো যথেষ্ট সম্পূর্ণ, এবং প্রয়োজন আছে এমন sentient-এর পক্ষে খুঁজে পাওয়া ও বোঝা সহজ কি না। নিরাপত্তা-সতর্কতা, স্বাস্থ্য-সংক্রান্ত দাবি, পুষ্টির তথ্য, উপাদান ও allergen-এর তথ্য এর অন্তর্ভুক্ত। কিছু অজানা বা পরীক্ষা না করা হলে “নিরাপদ” বোঝায় এমন ফাঁক না রেখে তা স্পষ্ট করে বলাও এর অন্তর্ভুক্ত (**Article III-F** (*নিরাপদ পণ্য ও স্বাস্থ্য-তথ্য*), এবং সিস্টেম-স্তরের সংযোগ হিসেবে **Article XIII-A** (*নির্ভরযোগ্যতা ও বিশ্বস্ততার ভিত্তি*) ও **Article XIII-C** (*মিথ্যা বিশ্বাস ও বিভ্রান্তিকর নির্ভরতা নিষিদ্ধকরণ*));
- ভিন্ন সংবেদন, চিন্তা ও ভাষাগত প্রয়োজনসম্পন্ন sentient-রা স্বাস্থ্য ও নিরাপত্তার তথ্য ব্যবহার করতে পারে কি না এবং সিদ্ধান্ত নেওয়ার সময় তা তাদের কাছে পৌঁছায় কি না; ছোট অক্ষরে লুকানো বা একটিমাত্র format-এ দেওয়া হয় কি না (**Article III-F** (*নিরাপদ পণ্য ও স্বাস্থ্য-তথ্য*); **Article VI-D** (*প্রবেশগম্যতা*); [Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help));
- ওই তথ্য ভুল প্রমাণিত হলে, বা পণ্য অনিরাপদ হলে, ক্ষতির জরুরিতার সঙ্গে সামঞ্জস্যপূর্ণ notice window-র মধ্যে (NU-1 থেকে NU-3) এর ওপর নির্ভরশীল সবাইকে জানানো এবং তারা যেখানে আছে সেখানে পৌঁছানো হয় কি না; এবং ক্ষতির জরুরিতার জন্য নির্ধারিত containment ও correction window-র মধ্যে (CU-1 থেকে CU-4) অনিরাপদ পণ্য বা ভুল তথ্য যেখানেই আছে তা আটকে ও সংশোধন করা হয় কি না ([Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **Article XIII-B** (*প্রতিকার ও প্রতিকার-লাভের অধিকার*));
- সিস্টেমের ভেতরের পুরস্কার কি প্রতারণা বা শর্টকাটকে উৎসাহিত করে (**Article XIII-D** (*প্রণোদনা-সামঞ্জস্যের সীমা*)); এবং
- প্রাসঙ্গিক হলে, ব্যর্থতা আড়াল না করে বা নীরবে কারও অধিকার কেড়ে না নিয়ে সিস্টেম সততার সঙ্গে ব্যর্থতা থেকে পুনরুদ্ধার করতে পারে কি না (**Article XIII-F** (*স্থিতিস্থাপকতা ও স্ব-পুনরুদ্ধারের ভিত্তি*))।

পরীক্ষার মাত্রা [Materiality](core_05.050_band_oversight.md#materiality), [Dependency](core_05.040_band_continuity.md#dependency) এবং [Risk](core_05.040_band_continuity.md#risk) অনুযায়ী নির্ধারিত হবে।

সময়, মাত্রা ও নির্ভরতা জুড়ে কার্যকরী প্রভাব মূল্যায়নে প্রতিফলিত হতে হবে, কেবল নিচের কোনো বিষয় নয়:

- সুনাম, আকার বা বিপণন;
- নামমাত্র নিশ্চয়তার label;
- বিশ্বস্ততা নিয়ে নামমাত্র অনুচ্ছেদ, যখন reliability badge বা vendor score-ই বাস্তবে নির্ধারণ করে কাকে কাজ দেওয়া হবে বা কী কেনা হবে;
- ঘোষিত উদ্দেশ্য; অথবা
- কেবল অতীতের কর্মদক্ষতা।

<a id="562-system-class-scaling-and-escalation"></a>
##### 5.6.2 সিস্টেম শ্রেণি অনুযায়ী মাপ ও ধাপে উন্নীতকরণ

পর্যালোচনার গভীরতা সিস্টেমের শ্রেণির ওপর নির্ভর করে। বস্তুগততার শর্ত পূরণ হলেই:

- সিস্টেমের reading, alert বা পুনরুদ্ধারের দাবি পরিবার বা অপারেটরকে জীবনধারণের অপরিহার্য উপকরণ (সংবেদনশীল সত্তাদের বেঁচে থাকার জন্য প্রয়োজনীয় বিষয়) সম্পর্কে বিভ্রান্ত করতে পারে, এমন হলে নথিতে কেবল সিস্টেম নির্ভরযোগ্য—এমন দাবি নয়, শক্ত প্রমাণ থাকতে হবে; কারণ নির্ভরতা অর্জন করতে হয় সিস্টেমের বাস্তব আচরণ দিয়ে ([Chapter One §6 Trust](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity))। প্রমাণে দেখাতে হবে:
  - sentient-রা সিস্টেমটিকে বিশ্বাস করতে পারে;
  - sentient-রা মিথ্যা আশ্বাস পাবে না;
  - [Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help)-এর শর্ত অনুযায়ী, সাড়া না-দেওয়া sentient-দের কাছেও জীবনধারণ-সংক্রান্ত জরুরি alert ও পরামর্শ পৌঁছায় এবং উত্তর না পেলে পরবর্তী যোগাযোগ হয়; এবং
  - [Chapter One §10 Resilience and Self-Healing Design](core_01.000_values_principles.md#10-resilience-and-self-healing-design)-এর শর্ত অনুযায়ী, সিস্টেম ব্যর্থতা থেকে সততার সঙ্গে পুনরুদ্ধার করে।
- সিস্টেমের uptime, matching বা জরুরি override (“break-glass” access) নিয়ে দাবি sentient-রা চিকিৎসা বা জরুরি সেবা পাবে কি না নিয়ন্ত্রণ করে, এমন হলে ([Chapter One §4 Safety](core_01.000_values_principles.md#4-safety-harm-constraint)-এ উল্লিখিত ঝুঁকি), সিস্টেমের গুরুত্বের সঙ্গে সামঞ্জস্যপূর্ণ বিশদে নথিতে দেখাতে হবে:
  - sentient-রা কীভাবে ওই দাবিকে চ্যালেঞ্জ করতে পারে; এবং
  - সেগুলোর ওপর নির্ভর করতে গিয়ে sentient-রা বিভ্রান্ত হতে পারে কি না।
- সমন্বয় জীবনধারণের জন্য অপরিহার্য হলে, [§2.2 How system class scales every evaluation](#22-how-system-class-scales-every-evaluation)-এর অধীনে প্রত্যয়নে পর্যালোচনা উন্নীত ও সিস্টেমের শ্রেণি পুনর্বিবেচনা করতে হবে। বিভ্রান্তিকর নির্ভরতা sentient-দের বেঁচে থাকার জন্য দরকারি সমন্বয় বন্ধ করতে পারে, এমন হলে **Class A**-এর দিকে উন্নীতকরণ হতে পারে। যে নির্ভরতা sentient-রা বাস্তবে এড়াতে পারে না, তা [Chapter One §11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)-এর নির্ধারিত dependency।

<a id="563-defects-and-misalignment"></a>
##### 5.6.3 ত্রুটি ও অসামঞ্জস্য

[§5](#5-rights-floor-and-domain-evaluations) (*Rights-Floor and Domain Evaluations*)-এর ত্রুটিগুলো এই মূল্যায়নে প্রযোজ্য; **Article XIII** (*নির্ভরযোগ্য ও বিশ্বস্ত সিস্টেমের অধিকার*) অনুযায়ী পর্যালোচনা দরকার এমন বস্তুগত সীমা, ঝুঁকি বা ব্যর্থতার ইতিহাসও এর অন্তর্ভুক্ত। এ ছাড়া, নিচের প্রতিটি বিষয়কে প্রত্যয়নের ত্রুটি হিসেবে ধরতে হবে:

- মূল্যায়নযোগ্য [Trustworthiness](core_05.040_band_continuity.md#trustworthiness) বিশ্লেষণ ছাড়া সুনাম, সমর্থন, মাত্রা বা অপারেটরের নিজের প্রতিবেদনকে যথেষ্ট ধরা;
- **Article III-F** (*নিরাপদ পণ্য ও স্বাস্থ্য-তথ্য*)-এর অধীনে, সতর্কতা না থাকা বা ফাঁকা ঘরকে পণ্য বা সেবা নিরাপদ হওয়ার প্রমাণ হিসেবে ধরা, “অজানা” বা “পরীক্ষিত নয়” স্পষ্টভাবে বলার বদলে; এবং
- **Article XIII** (*নির্ভরযোগ্য ও বিশ্বস্ত সিস্টেমের অধিকার*)-এর নির্ভরযোগ্যতা এবং **Article XIII-A** (*নির্ভরযোগ্যতা ও বিশ্বস্ততার ভিত্তি*)-এর চ্যালেঞ্জ-সংক্রান্ত শর্ত পূরণ না করে, প্রকাশ, আপত্তিযোগ্যতা বা প্রতিকার ব্যর্থ করার জন্য দক্ষতা, উদ্ভাবন বা নিরাপত্তার দৃষ্টিভঙ্গি ব্যবহার করা।

নথিভুক্ত মিথ্যা বিশ্বাস, বিকৃত প্রণোদনা, প্রবেশগম্য নয় এমন চ্যালেঞ্জের পথ, এবং ব্যর্থতা আড়াল করা পুনরুদ্ধার-পদ্ধতি [Chapter One §6 Trust and Trustworthiness](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)-এর অধীনে গণ্য হবে।

<br>

*ফোরাম প্রক্রিয়া ও ফলাফলে এগিয়ে যান:* [Chapter Nine, Part B — Forum Process and Outcomes](core_09.005_system_alignment_certification_record_process.md#chapter-nine-part-b-system-alignment-certification--forum-process-and-outcomes) ([§6 Forum Process](core_09.005_system_alignment_certification_record_process.md#6-forum-process) এবং [§7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes))। *তারপর নথি, পুনঃপ্রত্যয়ন ও অবস্থানের সংযোগে যান:* [Chapter Nine, Part C — Record, Recertification, and Standing](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-system-alignment-certification--record-recertification-and-standing) ([§8 System Certification Record](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) থেকে [§11 Relationship to Standing](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing) পর্যন্ত)।

*প্রতিটি মূল্যায়ন ক্ষেত্রের কাজের উদাহরণ:* [CS-9.320 System alignment certification illustrations](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-system-alignment-certification-illustrations)।
