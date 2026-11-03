<!-- AI-assisted translation draft; unreviewed. §5.3.4 map and record integrity, source lines 1209–1215; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §5.3.4 map and record integrity (zh)

## English source (lines 1209–1215)

Before relying on dependency maps and resource-flow records, certification must check that they meet **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*). They must be:

- **Complete:** they cover significant upstream and downstream dependencies, resource flows, and any relationships that are hidden or lopsided, where those matter.
- **Current:** they are updated often enough given how fast things change and how critical the system is, including its system class under [§2 System Class Evaluation](#2-system-class-evaluation). They show the system as it runs now, not as it ran at the last certification.
- **Auditable:** they are open to audit under **Article XVI-A** (*Auditability and Observable Evidence*).

A map or record that fails any of these tests cannot support a finding that the system gives back enough. The gap must be written down and handled under *Defects and misalignment* below.

## Translation draft

##### 5.3.4 地图与记录的完整性

在依赖依赖关系地图和资源流记录之前，认证必须检查其是否符合**Article V-A** (*Dependency Mapping and Resource-Flow Transparency*)。它们必须：

- **完整：**在相关情况下，涵盖重要的上游和下游依赖、资源流，以及任何被隐藏或失衡的关系。
- **保持最新：**根据变化速度和系统关键程度（包括其在[§2 System Class Evaluation](#2-system-class-evaluation)-下的类别）及时更新。它们必须反映系统当前的运行状态，而非上次认证时的状态。
- **可审计：**根据**Article XVI-A** (*Auditability and Observable Evidence*)开放审计。

未通过其中任何一项检查的地图或记录，都不能作为系统已提供足够返还支持的依据。必须记录这一缺口，并按照下文的*Defects and misalignment*处理。
