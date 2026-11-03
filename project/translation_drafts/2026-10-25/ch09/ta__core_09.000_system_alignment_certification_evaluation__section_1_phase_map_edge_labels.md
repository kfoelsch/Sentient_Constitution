<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (ta)

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
    Rec -.->|VIb, §10 —<br/>சரிபார்க்கப்பட்ட உள்ளீடுகள் மட்டும்;<br/>தற்போதைய சான்றளிப்பு அல்லது அதன்போது<br/>உருவான உண்மைகள்| S
    G --->|ஆம்: பதிவின்<br/>வரம்பிற்குள் செயல்படுத்து| Ch
    G --->|சான்றளிக்கப்பட்டது,<br/>முன்நிபந்தனைகள் நிலுவையில்| Hold
    Ch -->|முக்கிய குறைபாடு:<br/>பாதுகாத்து சரிசெய்| Rm
    Ch -->|அட்டவணைப்படி, அல்லது<br/>முக்கிய மாற்றம் /<br/>நம்பத்தகுந்த சவால்<br/>மதிப்பாய்வைக் கோரும்போது| Re
    Ch -.->|VIb, §10 —<br/>சரிபார்க்கப்பட்ட உள்ளீடுகள் மட்டும்;<br/>செயல்பாடு பங்களிப்பு மற்றும்<br/>மீறல் பதிவுகளுக்கான<br/>உண்மைகளை வழங்கலாம்| S2
    Rm -->|சரிசெய்ததற்கான சான்று<br/>அடுத்த மதிப்பாய்வுச் சுற்றில்<br/>சரிபார்க்கப்படும்| Re
    G -->|சான்றளிக்கப்படவில்லை| Rm
```
