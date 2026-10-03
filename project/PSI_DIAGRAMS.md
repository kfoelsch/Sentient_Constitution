# Process, system, institution: diagrams

**Status:** working visuals for author review. Mermaid renders on GitHub and in most Markdown viewers. A PNG of each chart is in `diagrams/`.

**Conventions.** Charts here follow the rules in [`doc_architecture.md`](../doc_architecture.md): top to bottom (**VIS-CHART-ORIENT-04**), a blank line between box title and content (**VIS-CHART-READABILITY-01**), and unfilled nodes with white text and palette outlines (**VIS-CHART-THEME-02**). White labels need a dark canvas, so the PNGs are rendered on one. In a light-mode viewer the labels may be hard to read.

## 1. Top level

```mermaid
flowchart TB
  subgraph V["VALUES<br/>bind every object<br/>(Chapter One)"]
    direction LR
    aims["Two aims<br/><br/>Flourishing + Continuity"]
    tetrad["Tetrad<br/><br/>Participation · Oversight<br/>Accountability · Timeliness"]
    floors["Floors<br/><br/>Safety · Truth<br/>Wellbeing · Freedom"]
  end

  subgraph L["GOVERNANCE LAYERS<br/>who holds authority<br/>(Preamble 3.3, adopted)"]
    direction LR
    ccl["Constitutional Contract Layer<br/><br/>who may govern"]
    ssp["Stakeholder System Participation<br/><br/>voice inside authorized systems"]
  end

  subgraph O["OBJECTS GOVERNED<br/>what the problem is about<br/>(proposed index)"]
    direction LR
    inst["Institution<br/><br/>mandate, offices, stewards"]
    proc["Process<br/><br/>steps, records, clocks"]
    sys["System<br/><br/>boundaries, capture, capacity"]
  end

  subgraph R["ROUTING AND FLOORS"]
    direction LR
    sod["Segregation of duties (Chapter Seven)<br/><br/>act · check · record · hear challenge"]
    rule["Process-ownership dispute rule<br/><br/>draft, not adopted"]
    forum["Forums (Chapter Twelve)<br/><br/>independent review and certification"]
  end

  impl["Implementation corpus: CJS · CS · CI · CF<br/><br/>operational detail;<br/>implements, never narrows"]

  V -->|"served by"| L
  L -->|"act on all three"| O
  impl -->|"holds the how"| O
  O -->|"disputes; binding process acts need four seats"| R

  inst <==>|"16 items overlap"| proc
  proc <-->|"8"| sys
  inst <-.->|"5"| sys
  aims ~~~ tetrad ~~~ floors
  sod ~~~ rule
  rule -.-> forum

  style aims fill:none,stroke:#64748b,color:#ffffff
  style tetrad fill:none,stroke:#64748b,color:#ffffff
  style floors fill:none,stroke:#64748b,color:#ffffff
  style ccl fill:none,stroke:#2563eb,color:#ffffff
  style ssp fill:none,stroke:#0f766e,color:#ffffff
  style inst fill:none,stroke:#64748b,color:#ffffff,stroke-dasharray:5 3
  style proc fill:none,stroke:#64748b,color:#ffffff,stroke-dasharray:5 3
  style sys fill:none,stroke:#64748b,color:#ffffff,stroke-dasharray:5 3
  style sod fill:none,stroke:#2563eb,color:#ffffff
  style rule fill:none,stroke:#ea580c,color:#ffffff,stroke-dasharray:5 3
  style forum fill:none,stroke:#ea580c,color:#ffffff
  style impl fill:none,stroke:#16a34a,color:#ffffff
  style V fill:none,stroke:#334155,color:#ffffff
  style L fill:none,stroke:#334155,color:#ffffff
  style O fill:none,stroke:#334155,color:#ffffff
  style R fill:none,stroke:#334155,color:#ffffff
```

**How to read it**

- **Bands, top to bottom:** values bind everything; the two governance layers (authority questions) act on the three objects (what the problem is about); disputes and the separation-of-duties floor sit at the bottom. The implementation corpus feeds the objects from the side.
- **Outline colors** follow the shared palette: blue is authority (the Constitutional Contract Layer and segregation of duties), teal is participation, orange is forum review, green is the implementation corpus, slate is neutral context (values and the three objects).
- **Dashed outline** means proposed or draft: the object index and the process-ownership dispute rule. Solid outline is adopted text.
- **Overlap numbers** come from [the crosswalk](PROCESS_SYSTEM_INSTITUTION_CROSSWALK.md): how many of the 55 object-tagged items in Chapter One and Chapter Seven also touch a second object.
- **Process is the hub:** it overlaps both other objects, and Chapter Seven's floor attaches to it.

**Simplifications to check**

- "Act on all three" is a summary, not a verified rule. I did not check which layer reaches which object in practice, and a later chart could split it.
- The arrow into the bottom band covers both disputes and the four-seat floor. In the earlier version, Process pointed straight at the segregation-of-duties box and the dispute rule. Band-to-band links keep each band a horizontal row, so those two pointers are now in the label.
- Chapter Seven is drawn as a floor on binding process acts. Its text also covers institutional seats (placement, vacancy, independence lines), so it touches Institution too.
- The Forums box stands for the whole of Chapter Twelve, not just dispute routing.
- Objects are a proposed index, not adopted structure.
