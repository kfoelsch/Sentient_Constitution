<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (mr)

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
    Rec -.->|VIb, §10 —<br/>फक्त पडताळलेले इनपुट;<br/>चालू प्रमाणन किंवा प्रमाणनादरम्यान<br/>उद्भवलेली तथ्ये| S
    G --->|होय: नोंदीच्या<br/>व्याप्तीत कार्य करा| Ch
    G --->|प्रमाणित,<br/>पूर्वअटी प्रलंबित| Hold
    Ch -->|महत्त्वाचा दोष:<br/>संरक्षण करा आणि दुरुस्त करा| Rm
    Ch -->|वेळापत्रकानुसार, किंवा<br/>महत्त्वाचा बदल अथवा<br/>विश्वसनीय आव्हानामुळे<br/>पुनरावलोकन आवश्यक असल्यास| Re
    Ch -.->|VIb, §10 —<br/>फक्त पडताळलेले इनपुट;<br/>कार्यवाहीमुळे Contribution व<br/>Violation नोंदींसाठी<br/>तथ्ये मिळू शकतात| S2
    Rm -->|दुरुस्तीचा पुरावा<br/>पुढील पुनरावलोकन फेरीत<br/>तपासला जातो| Re
    G -->|प्रमाणित नाही| Rm
```
