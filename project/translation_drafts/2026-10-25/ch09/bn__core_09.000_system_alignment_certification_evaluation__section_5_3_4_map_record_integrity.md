<!-- AI-assisted translation draft; unreviewed. §5.3.4 map and record integrity, source lines 1209–1215; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §5.3.4 map and record integrity (bn)

## English source (lines 1209–1215)

Before relying on dependency maps and resource-flow records, certification must check that they meet **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*). They must be:

- **Complete:** they cover significant upstream and downstream dependencies, resource flows, and any relationships that are hidden or lopsided, where those matter.
- **Current:** they are updated often enough given how fast things change and how critical the system is, including its system class under [§2 System Class Evaluation](#2-system-class-evaluation). They show the system as it runs now, not as it ran at the last certification.
- **Auditable:** they are open to audit under **Article XVI-A** (*Auditability and Observable Evidence*).

A map or record that fails any of these tests cannot support a finding that the system gives back enough. The gap must be written down and handled under *Defects and misalignment* below.

## Translation draft

##### 5.3.4 মানচিত্র ও নথির অখণ্ডতা

নির্ভরতা-মানচিত্র ও সম্পদ-প্রবাহের নথির ওপর নির্ভর করার আগে সার্টিফিকেশনকে যাচাই করতে হবে যে সেগুলো **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*) পূরণ করে। সেগুলো হতে হবে:

- **সম্পূর্ণ:** গুরুত্বপূর্ণ উজান ও ভাটির নির্ভরতা, সম্পদ প্রবাহ এবং প্রাসঙ্গিক ক্ষেত্রে গোপন বা একতরফা সম্পর্ক অন্তর্ভুক্ত করবে।
- **হালনাগাদ:** পরিবর্তনের গতি ও ব্যবস্থার গুরুত্ব—[§2 System Class Evaluation](#2-system-class-evaluation)-এর অধীনে তার শ্রেণিসহ—অনুযায়ী যথেষ্ট ঘন ঘন আপডেট হবে। সর্বশেষ সার্টিফিকেশনের সময় যেমন ছিল তা নয়, এখন যেভাবে ব্যবস্থা চলে তা দেখাবে।
- **নিরীক্ষাযোগ্য:** **Article XVI-A** (*Auditability and Observable Evidence*) অনুসারে নিরীক্ষার জন্য উন্মুক্ত থাকবে।

কোনো মানচিত্র বা নথি এই পরীক্ষাগুলোর একটিতেও ব্যর্থ হলে, ব্যবস্থা যথেষ্ট ফিরিয়ে দেয়—এমন সিদ্ধান্তে তা সমর্থন দিতে পারে না। ঘাটতি লিখে রাখতে হবে এবং নিচের *Defects and misalignment* অনুযায়ী ব্যবস্থা নিতে হবে।
