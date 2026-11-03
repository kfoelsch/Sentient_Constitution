<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (bn)

## English source

```mermaid
    Rec -.->|VIb, §10 —<br/>verified inputs only;<br/>current certification or facts<br/>arising during certification| S
    G --->|Yes: operate<br/>within the record| Ch
    G --->|Certified,<br/>prerequisites pending| Hold
    Ch -->|Material defect:<br/>protect and correct| Rm
    Ch -->|On schedule, or<br/>material change or<br/>credible challenge<br/>requires review| Re
    Ch -.->|VIb, §10 —<br/>verified inputs only;<br/>operation may supply facts<br/>for Contribution and<br/>Violation records| S2
    Rm -->|Correction evidence<br/>is checked in the<br/>next review pass| Re
    G -->|Not Certified| Rm
```

## Translation draft

```mermaid
    Rec -.->|VIb, §10 —<br/>শুধু যাচাইকৃত ইনপুট;<br/>বর্তমান প্রত্যয়ন বা প্রত্যয়নের<br/>সময়ে উদ্ভূত তথ্য| S
    G --->|হ্যাঁ: নথির<br/>সীমার মধ্যে পরিচালনা| Ch
    G --->|প্রত্যয়িত,<br/>পূর্বশর্ত বাকি| Hold
    Ch -->|উল্লেখযোগ্য ত্রুটি:<br/>সুরক্ষা দিন ও সংশোধন করুন| Rm
    Ch -->|সময়সূচি অনুযায়ী, অথবা<br/>গুরুত্বপূর্ণ পরিবর্তন বা<br/>বিশ্বাসযোগ্য চ্যালেঞ্জে<br/>পর্যালোচনা প্রয়োজন হলে| Re
    Ch -.->|VIb, §10 —<br/>শুধু যাচাইকৃত ইনপুট;<br/>পরিচালনা অবদান ও<br/>লঙ্ঘন-নথির জন্য<br/>তথ্য দিতে পারে| S2
    Rm -->|সংশোধনের প্রমাণ<br/>পরবর্তী পর্যালোচনা<br/>পর্বে যাচাই হয়| Re
    G -->|প্রত্যয়িত নয়| Rm
```
