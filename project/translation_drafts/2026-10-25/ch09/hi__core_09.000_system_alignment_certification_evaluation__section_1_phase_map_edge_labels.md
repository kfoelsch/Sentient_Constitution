<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (hi)

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
    Rec -.->|VIb, §10 —<br/>केवल सत्यापित इनपुट;<br/>वर्तमान प्रमाणन या प्रमाणन के दौरान<br/>उभरे तथ्य| S
    G --->|हाँ: अभिलेख<br/>के दायरे में संचालन| Ch
    G --->|प्रमाणित,<br/>पूर्वापेक्षाएँ लंबित| Hold
    Ch -->|महत्वपूर्ण दोष:<br/>सुरक्षा करें और सुधारें| Rm
    Ch -->|निर्धारित समय पर, या<br/>महत्वपूर्ण बदलाव अथवा<br/>विश्वसनीय चुनौती से<br/>समीक्षा आवश्यक होने पर| Re
    Ch -.->|VIb, §10 —<br/>केवल सत्यापित इनपुट;<br/>संचालन Contribution और<br/>Violation अभिलेखों के लिए<br/>तथ्य दे सकता है| S2
    Rm -->|सुधार के साक्ष्य की<br/>अगले समीक्षा-चक्र में<br/>जाँच होती है| Re
    G -->|प्रमाणित नहीं| Rm
```
