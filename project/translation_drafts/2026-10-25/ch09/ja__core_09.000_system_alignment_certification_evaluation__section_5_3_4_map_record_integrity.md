<!-- AI-assisted translation draft; unreviewed. §5.3.4 map and record integrity, source lines 1209–1215; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §5.3.4 map and record integrity (ja)

## English source (lines 1209–1215)

Before relying on dependency maps and resource-flow records, certification must check that they meet **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*). They must be:

- **Complete:** they cover significant upstream and downstream dependencies, resource flows, and any relationships that are hidden or lopsided, where those matter.
- **Current:** they are updated often enough given how fast things change and how critical the system is, including its system class under [§2 System Class Evaluation](#2-system-class-evaluation). They show the system as it runs now, not as it ran at the last certification.
- **Auditable:** they are open to audit under **Article XVI-A** (*Auditability and Observable Evidence*).

A map or record that fails any of these tests cannot support a finding that the system gives back enough. The gap must be written down and handled under *Defects and misalignment* below.

## Translation draft

##### 5.3.4 地図と記録の完全性

依存関係の地図と資源フローの記録に依拠する前に、認証ではそれらが**Article V-A** (*Dependency Mapping and Resource-Flow Transparency*)を満たすことを確認しなければならない。次の要件を満たす必要がある。

- **完全であること：**重要な上流・下流の依存関係、資源フロー、重要な隠れた関係や偏った関係を網羅する。
- **最新であること：**変化の速さとシステムの重要性に見合う頻度で更新され、[§2 System Class Evaluation](#2-system-class-evaluation)-におけるシステムクラスも考慮する。最終認証時の姿ではなく、現在の運用を示す。
- **監査可能であること：****Article XVI-A** (*Auditability and Observable Evidence*)に基づく監査に開かれている。

これらのいずれかの要件を満たさない地図または記録は、システムが十分な支援を返しているとの認定を支えることができない。欠落を記録し、以下の*Defects and misalignment*に従って対処しなければならない。
