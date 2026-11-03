<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (ur)

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
    Rec -.->|VIb, §10 —<br/>صرف تصدیق شدہ معلومات؛<br/>موجودہ تصدیق یا تصدیق کے دوران<br/>سامنے آنے والے حقائق| S
    G --->|ہاں: ریکارڈ کی<br/>حدود میں چلائیں| Ch
    G --->|تصدیق شدہ،<br/>پیشگی شرائط باقی| Hold
    Ch -->|اہم نقص:<br/>تحفظ کریں اور درست کریں| Rm
    Ch -->|مقررہ وقت پر، یا<br/>اہم تبدیلی یا<br/>معتبر چیلنج جائزہ<br/>لازم کرے تو| Re
    Ch -.->|VIb, §10 —<br/>صرف تصدیق شدہ معلومات؛<br/>عمل کے دوران شراکت اور<br/>خلاف ورزی کے ریکارڈ کے لیے<br/>حقائق سامنے آ سکتے ہیں| S2
    Rm -->|اصلاح کے ثبوت کی<br/>اگلے جائزے کے دور میں<br/>جانچ ہوتی ہے| Re
    G -->|تصدیق شدہ نہیں| Rm
```
