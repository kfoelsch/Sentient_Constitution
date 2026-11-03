<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (te)

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
    Rec -.->|VIb, §10 —<br/>ధృవీకరించిన ఇన్‌పుట్‌లు మాత్రమే;<br/>ప్రస్తుత ధృవీకరణ లేదా ధృవీకరణ సమయంలో<br/>తలెత్తిన వాస్తవాలు| S
    G --->|అవును: రికార్డు<br/>పరిధిలో పనిచేయండి| Ch
    G --->|ధృవీకరించబడింది,<br/>ముందస్తు షరతులు పెండింగ్‌లో| Hold
    Ch -->|ముఖ్యమైన లోపం:<br/>రక్షించి సరిచేయండి| Rm
    Ch -->|షెడ్యూల్ ప్రకారం, లేదా<br/>ముఖ్యమైన మార్పు లేదా<br/>నమ్మదగిన సవాలు<br/>సమీక్షను కోరినప్పుడు| Re
    Ch -.->|VIb, §10 —<br/>ధృవీకరించిన ఇన్‌పుట్‌లు మాత్రమే;<br/>ఆపరేషన్ Contribution మరియు<br/>Violation రికార్డులకు సంబంధించిన<br/>వాస్తవాలను అందించవచ్చు| S2
    Rm -->|సవరణకు సంబంధించిన ఆధారాలు<br/>తదుపరి సమీక్ష చక్రంలో<br/>తనిఖీ చేయబడతాయి| Re
    G -->|ధృవీకరించబడలేదు| Rm
```
