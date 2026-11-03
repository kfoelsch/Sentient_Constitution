<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (bn)

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

*সহজ কথায়: সিস্টেমটি কী ধরনের ডেটা স্পর্শ করে এবং সেগুলো যথাযথভাবে পরিচালনা করে কি না, তা প্রত্যয়নকে দেখতে হবে—বর্তমান পর্যালোচনা-চক্রে ডেটার ধরনগুলো এখনও সঠিক কি না এবং সেই সিস্টেম-শ্রেণিতে সেই ডেটার জন্য অন্তর্নিহিত অবকাঠামো যথেষ্ট শক্তিশালী কি না, তাও অন্তর্ভুক্ত। ধরন-সংক্রান্ত নিয়ম ও [সিস্টেম ডেটা টাইপস রেকর্ড](core_05.040_band_continuity.md#system-data-types-record) সিস্টেমস কর্পাসে রয়েছে; প্রত্যয়ন যাচাই করে নিয়মগুলো সত্যিই প্রয়োগ হয়েছে কি না এবং রেকর্ডটি সঠিক কি না।*

প্রতিটি বস্তুগত প্রভাবসম্পন্ন প্রত্যয়ন রেকর্ডের অংশ হিসেবে সিস্টেম অ্যালাইনমেন্ট প্রত্যয়নকে **ডেটার ধরন ও ব্যবস্থাপনা** মূল্যায়ন করতে হবে। এই বিভাগে বলা হয়েছে প্রত্যয়নকে কী যাচাই করতে হবে। ধরন-শ্রেণিবিন্যাস ও ব্যবস্থাপনার পদ্ধতি রয়েছে **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*তথ্যের ধরন ও ব্যবস্থাপনা*) এবং [CS-6.310 — ডেটা শ্রেণিবিভাগ](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**-এ, সঙ্গে:

- তথ্যের ধরনগুলোর প্রামাণ্য সংজ্ঞা;
- ব্যবস্থাপনা-নিয়ম ও পৃথক রাখার শর্ত;
- জীবনচক্রের বিবরণ; এবং
- স্থায়ী [সিস্টেম ডেটা টাইপস রেকর্ড](core_05.040_band_continuity.md#system-data-types-record)।

**মূল্যায়নের শর্ত।** প্রত্যয়ন প্রক্রিয়ায় নির্ধারণ করতে হবে সিস্টেমটি:

- বস্তুগতভাবে পরিধির মধ্যে থাকা ডেটার ধরনগুলো শনাক্ত করে কি না; এবং
- রূপান্তর, সমষ্টিকরণ, অর্পণ, সংরক্ষণ, ধরে রাখা ও বিভিন্ন ডোমেইনের মধ্যে সংযোগসহ **প্রযোজ্য সবচেয়ে কঠোর** শ্রেণিবিন্যাস অনুযায়ী সেগুলো পরিচালনা করে কি না।

মূল্যায়নে কার্যগত প্রভাব প্রতিফলিত হতে হবে; শুধু লেবেল, বিন্যাস বা পাইপলাইনের ধাপ নয়।
