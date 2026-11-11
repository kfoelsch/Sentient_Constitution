<!-- AI-assisted translation draft; unreviewed. Complete current-source Chapter Nine Part C §§8–11. Source SHA-256 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Baseline commit 247e2180509e5e029c1106878cf225067339e010; baseline SHA-256 faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Draft only; do not synchronize into translations/. -->

<a id="chapter-nine-part-c-certification-record-recertification-and-standing"></a>

# CHAPTER NINE, PART C: SYSTEM ALIGNMENT CERTIFICATION — RECORD, RECERTIFICATION, AND STANDING

<a id="8-system-certification-record"></a>

### 8. 系统认证记录

<details>
<summary><strong>追溯</strong></summary>

- 上游:
  - [B部分 §6](core_09.005_system_alignment_certification_record_process.md#6-论坛程序) (*论坛组成部分的认定结果纳入系统认证记录*);
  - [B部分 §7](core_09.005_system_alignment_certification_record_process.md#7-认证结果) (*认证结果及作出结果时提出的关切*);
  - [A部分 §1](core_09.000_system_alignment_certification_evaluation.md#1-目的与作用) (9.000 §1) (*认证目的与流程概览*);
  - [A部分 §2](core_09.000_system_alignment_certification_evaluation.md#2-系统类别评估) (*系统类别评估*) (9.000 §2) 至
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-权利底线与领域评估) (*反映在系统认证记录中的评估结果*);
  - [第二至第四章](../../core_04.000_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) (*定义、举证责任、可追溯性和核验基础*);
  - [系统认证记录](../../core_05.040_band_continuity.md#system-certification-record) (*第五章中的含义*);
  - [实质约束性行为记录](../../core_05.035_band_accountability.md#materially-binding-act-record);
  - [记录完整性](../../core_05.035_band_accountability.md#record-integrity) (*适用于系统认证记录的可靠性规则*);
  - [第八章 §8 行为记录与可归责交接](../../core_08.000_functional_independence_separation_of_duties.md#8-act-records-and-attributable-handoffs) (8.000 §8); 监督测量系列：作为宪法测量的真实与认识论完整性;
  - [**Def.O1** *第XVI条：审计、透明度与独立核验*](../../core_05.050_band_oversight.md#defo1-transparency-auditability-and-verification).
- 下游: [§9](#9-再认证与重新开启) (*重新认证与重新开启*); [§11.3](#113-经核实输入门-一份认证记录仅当其有界可追溯可质疑并在下列项下经核实时才可以向第八章轨迹供料) (*已核验输入门槛*); [第十五章 §2.3](../../core_15.000_forum.md#23-forum-case-records-standing-records-and-contests) (*论坛案件记录与 standing 记录争议*) (15.000 §2.3).
- 一并阅读:
  - [第XVI条：审计、透明度与独立核验](../../core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [证据保存](../../core_05.050_band_oversight.md#evidence-preservation);
  - **[CS-6.305](../../corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*信息类型与处理*) 并且 [CS-6.310 — 数据分类](../../corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**;
  - **[CS-9.305](../../corpus_systems/cs_09.305_system_classification_machinery.md#cs-9305-part-a-system-classification-machinery) (*系统分类机制*) 并且 [CS-9.310 — 系统影响分类](../../corpus_systems/cs_09.310_system_impact_classifications.md#cs-9310-part-b-system-impact-classifications)**;
  - **CS-6.345** (*系统生命周期*);
  - **CJS-5.110 §4** (*透明度级别与审计访问条件*).
- 子节:
  - [§8.1](#81-记录最低内容) (*记录最低内容*), 与
  - [§8.1.1](#811-系统身份范围与既往系统认证记录) (*系统身份、范围及此前记录*);
  - [§8.1.2](#812-分类与全系统认定) (*分类与全系统认定*);
  - [§8.1.3](#813-系统数据类型记录) (*系统数据类型记录*);
  - [§8.1.4](#814-权利底线与领域认定) (*权利底线与领域认定*);
  - [§8.1.5](#815-技术证据与审查认定) (*技术证据与审查认定*);
  - [§8.1.6](#816-监督独立性与质疑路径) (*监督、独立性与质疑途径*);
  - [§8.1.7](#817-关切原因与补救准备度) (*关切、原因与补救准备度*);
  - [§8.1.8](#818-结果与依赖限制) (*结果与依赖限制*);
  - [§8.1.9](#819-运行计划) (*运行计划*); 并且
  - [§8.1.10](#8110-完整性) (*完整性*);
  - [§8.2](#82-系统认证记录的透明度与可审计性) (*系统认证记录的透明度与可审计性*).

</details>


*用直白的话说：认证记录是一份受审系统的可审计案卷 — 谁在运行它、查了什么、发现了什么、决定了什么，以及如何质疑。它不是营销材料，也不是一行批准印章。记录深度、披露与质疑负担按 [§2.1](core_07_a_system_alignment_certification_evaluation.md) 随系统类缩放 — **Class A** 生存关键系统需要比 **Class C** 协调层更完整、更可质疑的案卷，尽管两者都必须诚实陈述类别并反映所要求的评价。*

一份**系统认证记录**是关于某一系统、版本、运营者或尽责管理者、范围、时间窗、实质影响画像与决定语境的有界、可审查记录 — 范围有界、时间有界，并在第五章 [系统认证记录](../../core_05.040_band_continuity.md#system-certification-record) 的含义下可质疑。

<a id="81-minimum-record-contents"></a>

#### 8.1 记录最低内容

<a id="811-system-identity-scope-and-prior-system-certification-record"></a>
##### 8.1.1 系统身份、范围与既往系统认证记录

记录至少须说明系统、系统版本、运营者或管理者、认证范围；适用的System Charter（或说明其缺失为何不重要）；受影响的社区与依赖关系；审查状态，以及存在Charter时认证范围是否与其所述范围一致。若运营者/管理者是持有Institutional Certification Record的Institution，须按版本链接该记录，以便追溯所依据的机构事实，并说明系统状态。后续认证轮次须链接依照第八章§8保存的上一份已完成系统认证记录，并说明此后变化。

<a id="812-classification-and-whole-system-findings"></a>
##### 8.1.2 分类与全系统认定

记录须列明系统分类记录（或CS-9.305与CS-9.310要求的内容）以及依照 [Part A §3 Whole-System Certification Evaluation](core_09.000_system_alignment_certification_evaluation.md#3-全系统认证评估) 得出的认定：所分配类别、分类理由、关键假设（含重大影响假设）、存在的依赖类型、重大时的运行关键性评估、不确定性、各认证状态适用的类别分级认证周期；若分类不确定或有争议，还须列出所依据的预防性类别及待解决期间的认证条件。

记录全系统评估和适用的第4节评估中的重大认定，包括系统性范围、隐私联合调用、退出、集会与异议、时间一致性、治理、激励，以及适用时的可质疑性。系统性风险属于评估范围时，列出风险评估及所依据假设；披露安排（对象或路由方式、相对于重大决定的时点、配有可用替代物的正当暂缓披露）；以及评估或披露未完成时的缺陷/认证条件。这些风险认定留在本系统认证记录中，不另建单独命名的风险披露记录，也不形成第五份强制组成记录。

<a id="813-system-data-types-record"></a>
##### 8.1.3 系统数据类型记录

列明依照[第一部分§3.4 数据类型与处理评估](core_09.000_system_alignment_certification_evaluation.md#34-数据类型与处理评估)制定或核验的系统数据类型记录（或CS-6.305、CS-6.310要求的内容），包括重大范围内的数据类型；模糊或多类型数据的分类理由；所依据的分隔与跨域关联控制；处理、保留、生命周期及基础设施保障情况；支持Attributable Action和Attribution Integrity所需的归因能力；以及CS-6.305 §§5、8项下最近一次定期复评（日期/周期标识、按类别与影响确定的频率、重大重新定型）。还须说明正当披露/审计访问限制及所需公开替代物。若适用Type O基线，说明Public Oversight Baseline Disclosure如何覆盖认证范围、所依据的System Charter字段、边界认定、覆盖缺口和条件。

<a id="814-rights-floor-and-domain-findings"></a>
##### 8.1.4 权利底线与领域认定

对于[第一部分§5 权利底线与领域评估](core_09.000_system_alignment_certification_evaluation.md#5-权利底线与领域评估)表中触发条件适用的每项保护，列出所依据的重大性触发条件与评估范围及该保护的认定：认证或持续依赖是否排除或实质削弱生存必需品、教育机会或Safe Conditions；生态足迹（归因假设、生命周期/依赖边界、重大负担、披露安排及所需环境论坛认定）；跨系统支持（依赖系统图/资源流范围、图与记录的完整性/时效/可审计性、提取和回流、支持充分性、公平分配）；不歧视（负担/利益模式、受保护特征和代理歧视、实质公平）；无障碍（实质参与、便利安排、反代理拒绝）；教育能力（能力建设、再培训、评估透明与可质疑性、重大时反代理/反操纵）；可信性（虚假信任、逆向激励、质疑渠道和恢复完整性）。另列不确定性、必需的Sentient论坛或指定组成部分认定、正当披露限制及公开替代物，以及与持续伤害有关的认证条件、依赖限制或重启触发条件。

<a id="815-technical-evidence-and-review-findings"></a>
##### 8.1.5 技术证据与审查认定

列明实质依赖的技术标准、测试、测量、不确定性、安全裕度、失效模式、安全测试结果及证据基础。包括每次再认证的回归测试（范围、运行的标准/定制测试套件、结果、已知失败、补救及有理由接受的剩余风险）和CS-6.345要求的认证周期证据包：范围、分类、测试、剩余风险、补救准备度、监测，以及适用时与既往记录相比的重大变化。还要记录利益相关方、权利底线、无障碍、依赖和参与方面的考量；重大时的生态暴露/归因、环境前提依赖、生命周期负担、恢复义务和环境一致性组成部分审查；以及被俘获、自我审查、激励错位、证据控制和阻碍质疑的风险。

<a id="816-supervision-independence-and-challenge-paths"></a>
##### 8.1.6 监督、独立性与质疑路径

列明对每个组成部分作出发布、采纳、转交、提交裁决、暂缓或审查的论坛家族/权限主体，以及B部分§6.2的监督顺序。记录第八章要求的四个席位（发起、核验/授权、记录、质疑）、各持有人与权限及任职时有效的Charter Role Map版本；每次回避、委托、替代、允许合并或紧急偏离；并提供足够的控制线信息，证明运营方/提案方没有核验自己的认证主张，也没有控制对该主张的质疑。列出§10指定的可质疑路径与B部分§6.3链条，说明受影响方如何在各阶段提出质疑。

<a id="817-concerns-cause-and-remediation-readiness"></a>
##### 8.1.7 关切、原因与补救准备度

记录论坛审查或形成结果时提出的每一项异议、不同意见、关切与质疑，无论提出者或渠道为何。逐项说明提出者（或匿名/保密状态）、内容、如何处理或仍未解决的原因，以及产生的认证条件、依赖限制或重启触发条件；并公布B部分§6.2.4的审查意见日志。发现不一致/缺陷时，列明设计所致、运行所致或尚未确定的原因及所依据证据。若发现补救事项，列出意愿/能力认定及证据、要求的证明步骤、期限、独立核验和§7.3认定。拒绝/撤销时，列明理由、临时保护及§7.4依赖限制。

<a id="818-outcome-and-reliance-limits"></a>
##### 8.1.8 结果与依赖限制

至少列明：依照{link8}作出的认证结果；系统处于临时或完整认证状态，还是Not Certified；适用的认证周期；重新开启审查的触发条件；依赖限制。

<a id="819-operating-plan"></a>
##### 8.1.9 运行计划

同一记录须包含按系统类别和重大影响调整的简明运行计划，无须另立文件。计划说明获准运行的认证范围、人口与期限；认证到期日、下次再认证到期日和中期审计完成日（{link91}）；首次上线或重大扩张获准的最早日期、通知期限及理由（{link71}）；每项认证条件的时限、负责者、完成/持续遵守证据、独立核验主体及违反后果；谁监测实际结果和保障措施、使用哪些证据/指标、检查频率，以及哪些认定/阈值要求行动或重新开启审查；谁回应事故、质疑和未满足的条件、适用时限及临时保护、遏止、回退或依赖限制的权限；发现缺陷时的纠正工作、核验标准/结果、剩余不确定性和获准的临时依赖。对于Not Certified系统，说明禁止上线、另行获准的临时持续依赖、纠正要求和重新审查前提；不得暗示已获认证运行许可。

运行证据及后来认定条件已满足的材料，按{act}作为链接加入；不得就地改动已完成的记录。详细测试/监测方法仍由其指定负责人掌握，包括{cs}。

<a id="8110-completeness"></a>
##### 8.1.10 完整性

记录遗漏任何适用评估的认定即不完整：对每个有重大影响的系统，须有Part A §§2、3、3.4的认定；须有locus或principle受到影响的每个§4小节；以及触发条件成立的每个§5领域。认定须反映评估实际发现，而非小节标题或运营者自己的证明。即使没有改变结果，遗漏审查或形成结果时提出的关切、异议或不同意见，也会使记录不完整。

<a id="82-transparency-and-auditability-of-the-system-certification-record"></a>
#### 8.2 系统认证记录的透明度与可审计性
*通俗地说：系统认证记录只有在感知者能够阅读和核查时才有用。本节把透明度和可审计性落实为系统认证记录自身的具体要求，而非抽象理想。在四元组的**监督**支柱下，监督要求审计。系统一致性认证是规模尤其大的审计程序之一，必须达到此处的底线。它不拥有也不取代[第XVI条](../../core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification)（*审计、透明度与独立核验*）或其他审计模式。感知者能够提出异议的第三项要求见[§10 质疑认证](#10-对认证提出质疑)。*
本节将[透明度](../../core_05.050_band_oversight.md#transparency)和[可审计性](../../core_05.050_band_oversight.md#auditability)适用于系统认证记录。它们是[记录完整性](../../core_05.035_band_accountability.md#record-integrity)中“可查阅”和“可重构”的部分；记录完整性涵盖整份系统认证记录（[§8 系统认证记录](#8-系统认证记录)）。规范术语的归属及责任边界见[序言——宪法责任登记册](../../core_00.000_preamble.md#4-principles-definitions-and-rights)和[权限层级与内部序列](../../core_05.045_band_integrative.md#owner-non-relocation)。依照[宪法四元组](../../core_00.000_preamble.md#constitutional-tetrad)：
**可审计性**——感知者必须能够重构并核查系统认证记录：
  - 记录版本之间发生了什么变化、由谁作出每项变更、依据何种权限、应谁请求；对于新系统认证记录，还须说明它相较于所承接的已完成系统认证记录发生了什么变化；
  - [§8](#8-系统认证记录)（*每次再认证或重新开启审查所承接的已完成系统认证记录*）；
- 下游：[§11.3](#113-经核实输入门-一份认证记录仅当其有界可追溯可质疑并在下列项下经核实时才可以向第八章轨迹供料)和[§11.5 违规地位记录](#115-违规资格记录)（*事实支持不利认定时适用的已核实输入门槛*）；[第十五章](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction)（15.000）（*重新开启的论坛监督*）；[第十一章](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened)（11.000）。
  - [§9.1](#91-再认证计划与新系统认证记录)（*再认证计划与新系统认证记录*）；

<a id="9-recertification-and-reopening"></a>

### 9. 再认证与重新开启

<details>
<summary><strong><span style="color: #2563eb;">追溯</span></strong></summary>

- 上游依据：
  - [B部分§7](core_09.005_system_alignment_certification_record_process.md#7-认证结果)（*现行结果*）；
  - [§8](#8-系统认证记录)（*每次再认证或重新开启的审查都遵循的已完成系统认证记录*）；
  - [A部分§2](core_09.000_system_alignment_certification_evaluation.md#2-系统类别评估)（9.000 §2）至
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-权利底线与领域评估)（*评估中发现的错误分类、不一致和缺陷*）；
  - [§10](#10-对认证提出质疑)（*可信质疑*）；
  - [两项宪法目标](../../core_00.000_preamble.md#two-constitutional-aims)；
  - [第三章§1](../../core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints)（3.000 §1）和
  - [§2](../../core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior)（*定义完整性与规避*）；
  - [系统章程](../../core_05.040_band_continuity.md#system-charter)（*系统章程与行为不一致，以及逾期审查*）。
- 下游影响：[§11.3](#113-经核实输入门-一份认证记录仅当其有界可追溯可质疑并在下列项下经核实时才可以向第八章轨迹供料)和[§11.5](#115-违规资格记录)（*当事实支持不利认定时使用已核实输入门槛*）；[第十五章](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction)（15.000）（*重新开启后的论坛监督*）；[第十一章](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened)（11.000）。
- 配合阅读：**[CS-6.305 §5](../../corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)**（*重新分类与生命周期治理*）和**[CS-9.305 §3](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)**（*重新分类要求*）。
- 小节：
  - [§9.1](#91-再认证计划与新系统认证记录)（*再认证计划与新的系统认证记录*）；
  - [§9.2](#92-重新开启的触发事项)（*重新开启触发条件*）；
  - [§9.3](#93-临时与完整认证)（*临时和完整认证*，包括
  - [§9.3.1 两种状态](#931-两种状态)，
  - [§9.3.2 失败与降级](#932-失败与降级)，
  - [§9.3.3 不一致的原因](#933-不一致的原因)，
  - [§9.3.4 分级期限](#934-分级时限)，
  - [§9.3.5 对A类的依赖](#935-a类系统依赖)，以及
  - [§9.3.6 核验，而非声称](#936-核验而非自我声明))；
  - [§9.4](#94-不得规避)（*禁止规避*）。

</details>


*通俗地说：没有任何结果是永久的。系统运行期间，指定责任人须监测实际结果与保障措施、回应事件和质疑，并履行系统认证记录中的认证条件。认证系统须依照系统类别所定计划进行再认证，并在每个间隔中点接受审计。重大事实变化或可信质疑要求时，须重新开启审查。缺陷应引发保护、纠正和独立核验。每轮审查都开启一份链接至上一份的新系统认证记录；新记录不会抹去旧记录或对旧记录提出的质疑。旧批准不能代替当前的权利底线合规。*
**核验。**第十五章将对现有系统进行的论坛审查称为*持续一致性核验*。在本章中，核验不是独立程序，而是针对已运行系统的一轮认证：再认证、重新开启审查或新审查。它与其他认证轮次一样，经过[B部分§6 论坛程序](core_09.005_system_alignment_certification_record_process.md#6-论坛程序)，并依照[B部分§7 认证结果](core_09.005_system_alignment_certification_record_process.md#7-认证结果)以某项结果结束。
**监测与回应。**运营者和管护者必须依照[§8.1 最低记录内容](#81-记录最低内容)执行系统认证记录中的运行计划。指定责任人必须：

- 保存监测证据；
- 调查重大事件与指标；
- 将质疑转交给指定主管机关；并且
- 执行必要的临时保护和纠正工作。

以下任何事项如对一致性构成重大疑问，都须依本节及时提交论坛审查，不得等到下一次预定再认证：

- 事件；
- 未满足的认证条件；
- 未按[B部分§7.3 补救准备度：纠正的意愿与能力](core_09.005_system_alignment_certification_record_process.md#73-补救准备度纠正意愿与能力)完成证明步骤；
- 虚假的准备度证据；或
- 可信的质疑。

认证条件的纠正、履行与解除须遵守[B部分§7 认证结果](core_09.005_system_alignment_certification_record_process.md#7-认证结果)中的独立核验要求。

<a id="91-recertification-schedule-and-the-new-system-certification-record"></a>
#### 9.1 再认证计划与新系统认证记录
*通俗地说：认证不会永远有效。系统须按其类别设定的计划接受再认证，并在每个间隔中点接受审计。每轮认证都会开启一份链接至上一份的新系统认证记录。*
系统认证记录必须依照[第十五章§6 及时解决、重要性层级与反拖延纪律](../../core_15.000_forum.md#review-cadence)（*审查周期*）规定的系统类别节奏进行再认证，并在该周期中点接受审计。
**每轮认证须建立新记录。**每次后续认证轮次（再认证、重新开启的审查或新审查）都开启一份新的系统认证记录。新系统认证记录须：
- 链接至其所承接的已完成系统认证记录，并说明此后发生的变化（[§8.1.1 系统身份、范围与既往系统认证记录](#811-系统身份范围与既往系统认证记录)）；并且
已完成的系统认证记录须保持原样（[§8 系统认证记录](#8-系统认证记录)）。它仍是其所覆盖期间的记录，并继续接受[B部分§6.3 可质疑性链条](core_09.005_system_alignment_certification_record_process.md#63-可争议性链条)下的质疑。认证状态、无问题再认证次数和监测指标通过链接延续，并依据[§9.3 临时与完整认证](#93-临时与完整认证)在新系统认证记录中核验。

<a id="92-reopening-triggers"></a>

#### 9.2 重新开启的触发事项

一份**系统认证记录**是**范围有界**且**时间有界**的。当下列任一项具有实质性时，审查在第十五章与被纳入的系统实施义务下重开：

- **一般触发：**
  - 系统、其使用或其运行语境的实质性变化；
  - 被掩盖的行为；
  - 依赖增长，包括对系统的依赖增加、从共同基础中提取增加，以及超过接受方依 [第一章§11.4](../../core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) 设阈值的集中（级别上调不等待达到阈值；A部分§2.2）；
  - 按比例跨系统支持要求，系统回馈共同基础的流量显著下降;
  - 新风险；
  - 事件史；
  - 受影响方证据；
  - [§14](#10-对认证提出质疑) 下的可信质疑；
  - 生态异议；
  - **[CS-3 §3.5](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** 下的系统类错位或逾期再评估；
  - 数据类型或处理错位，以及 **[CS-2 §5.2](../../corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** 下逾期或跳过的定期数据类型再评价；
  - 分类错位；
  - [章程](../../core_05.040_band_continuity.md) 修订、章程—行为不匹配、实质在章程范围之外运行，或逾期的定期章程审查；
  - 其组合中包含该系统的机构发生治理违规（认定治理失败、基于治理理由拒绝或撤销，或认定另一系统的错位由该机构造成）；仅在具有实质性时重新开启，依 [第十章§9.6](../../core_10.000_institutional_alignment_certification.md#96-reopening-the-institutions-systems);
- **反映在认证记录上的域错位**，包括：
  - [§3.1](core_07_a_system_alignment_certification_evaluation.md#31-系统范围与风险因素) 下的实质性风险评价或风险披露缺陷或错位；
  - [§5](core_07_a_system_alignment_certification_evaluation.md#51-生态足迹评价) 下的实质性足迹虚假陈述或错位；
  - [§7](core_07_a_system_alignment_certification_evaluation.md#54-不歧视评价) 下的实质性歧视模式错位或代理规避；
  - [§8](core_07_a_system_alignment_certification_evaluation.md#55-无障碍评价) 下的实质性可及性错位或仅纸面便利安排；
  - [§9](core_07_a_system_alignment_certification_evaluation.md#52-教育能力与学习系统完整性评价) 下的实质性评估不透明、凭证设门或强加过时错位；
  - [§10](core_07_a_system_alignment_certification_evaluation.md#56-可信度与系统依赖完整性评价) 下的实质性虚假信任、扭曲激励或恢复完整性错位；
  - 对应实质性触发适用时的其他 A 部分评价错位 — 包括 [§2](core_07_a_system_alignment_certification_evaluation.md#2-系统类别评估)、[§4](core_07_a_system_alignment_certification_evaluation.md#34-数据类型与处理评价) 与 [§6](core_07_a_system_alignment_certification_evaluation.md#53-比例适当的跨系统支持评价)。

**为何重开要紧。** 因错位、依赖增长或可信质疑而重开，在共享系统设门生存必需、教育通路、能力建设路径、可信依赖或安全的持久供给之处，保护 [两项宪法宗旨](core_00_preamble.md#two-constitutional-aims) 下的**延续**宗旨。过期认证不得顶替当前的权利底线遵从。

<a id="93-provisional-and-full-certification"></a>
#### 9.3 临时与完整认证

*简言之：系统逐步赢得信任。新系统和评估未通过的系统先受更严格限制并频繁复查。只有当前没有问题、也没有问题将至的系统，才能升为完整认证并采用更长周期。评估未通过会使其回到严格限制。*

<a id="931-the-two-statuses"></a>
##### 9.3.1 两种状态

认证有两种状态，每种都有自己的认证周期，并按[§8.1 Minimum record contents](#81-记录最低内容)载于系统认证记录：

- **[Provisional certification](../../core_05.040_band_continuity.md#provisional-certification)**：系统首次认证（包括新部署系统）；或系统在再认证未通过、重新开启审查或新审查发现不一致后取得认证。临时周期短于同一系统类别的完整认证周期，依赖限制列于记录。
- **[Full certification](../../core_05.040_band_continuity.md#full-certification)**：只有持有临时认证的系统在再认证时，且同时满足以下条件才能取得：
  1. 完成规定数量连续、无问题的临时再认证，至少一次；较高类别须依采纳文件规定完成更多次；
  2. 当前没有不一致：记录中没有未解决的不一致、未补救缺陷、逾期检查或未通过的回归测试；以及
  3. 监测指标没有指向即将发生的不一致：记录所列触发条件/趋势指标没有越过阈值，也没有朝阈值发展的趋势。

完整认证按系统类别确定周期，仍有期限，不是永久批准。符合条件2和3的再认证才是**无问题**再认证。

<details>
<summary><strong>读者指南（不具操作效力）：认证状态</strong></summary>

> 本表概述§9.3；如有不同，以正文为准。
>
> | | 临时认证 | 完整认证 |
> |---|---|---|
> | **持有者** | 首次认证（含新部署系统）；或再认证失败/审查发现不一致后获认证的系统 | 持临时认证并在再认证时取得完整认证的系统 |
> | **取得方式** | 随认证结果授予 | 达到规定的连续无问题次数，当前无不一致且无迫近指标 |
> | **认证周期** | 短于同类系统完整周期 | 按系统类别确定，仍有期限 |
> | **再认证失败时** | 适用B部分§7；下次为临时认证，连续无问题计数归零 | 同左 |
> | **出现迫近指标时** | 保持临时，计数不增加 | 降为临时 |
>
</details>

<a id="932-failure-and-step-down"></a>
##### 9.3.2 失败与降级

再认证、重新开启审查或新审查的发现决定系统状态：
- 再认证发现当前不一致即为**失败**；适用[Part B §7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-认证结果)。下次认证只能为临时认证，不论下一次检查多么干净；无问题计数归零。
- 没有当前不一致但有迫近指标时，不算失败，也不算无问题。临时状态保持且计数不增加；完整状态降为临时。
- 依照[§9 Recertification and Reopening](#9-再认证与重新开启)重新开启审查并发现不一致，效果等同再认证失败。
- 已认证系统的新审查发现当前不一致，效果相同。若系统没有认证状态，适用[Part B §7.4 Denial and Revocation](core_09.005_system_alignment_certification_record_process.md#74-拒绝与撤销)。

<a id="933-cause-of-misalignment"></a>
##### 9.3.3 不一致的原因

评估、再认证、重新开启或新审查发现不一致时，记录须说明原因属于：**设计所致**（系统/流程即使按预期运行也会产生不一致结果）；**运行所致**（设计表面合理，但运行、输入或维护方式导致不一致）；或**尚未确定**（论坛查明原因前，设计和运行两方面的补救均保持开放）。

原因认定受以下限制：系统持续产生不一致结果即属不一致，纸面设计看似合理不是抗辩；会产生不一致结果的设计在结果出现前已构成不一致；原因认定决定寻求的补救和重新审查范围，但不决定系统是否不一致。

设计所致时：重新设计实施并核验前，无问题再认证计数保持零；查明原因的论坛或依[Part B §6.2 Supervisory sequence](core_09.005_system_alignment_certification_record_process.md#62-监督顺序)指定的后续论坛，在[matching intake target](../../core_05.040_band_continuity.md#tier-window)期限内核验重新设计，最早可在首次临时再认证时进行；重新设计核验前的组成部分评估不计入无问题总数；改变运行方式不满足此步骤。

这些规则补充但不取代上述降级规则。运营者或受影响的sentient可请求论坛复核原因认定；若原因改变，本组规则停止适用。

<a id="934-tier-windows"></a>
##### 9.3.4 分级时限

初评、再认证、重新开启审查或新审查发现不一致时：按[Chapter Fifteen §6 Timely resolution, materiality tiers, and anti-delay discipline](../../core_15.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline)的重大性等级分类；推定采用与系统类别相应的等级（例如不一致的A类系统推定为A级）；受理、证据保存、临时保护和决定均遵守该等级时限及外限；逾期依该节审查。

<a id="935-class-a-reliance"></a>
##### 9.3.5 A类系统依赖

临时认证周期短于完整认证，因此更早再认证（[§9.3.1 两种状态](#931-两种状态)）；依赖限制记在系统认证记录（[§8.1 Minimum record contents](#81-记录最低内容)）。中断处理如下：
- 临时认证本身不要求中断会在替代方案到位前切断生存必需资源的系统；
- B部分§7的临时保护和认证条件处理此类情况；
- 因设计所致的不一致而暂停计数时同样如此：暂停计数本身不得中断sentient所依赖的系统；以及
- 暂停期间，论坛须说明临时保护、依赖认证条件和对依赖者的通知。

<a id="936-verification-not-assertion"></a>
##### 9.3.6 核验而非自我声明

系统状态、无问题再认证计数和监测指标都必须核验并接受独立审查；系统自己的说法不够：
- 不得设定使不一致永远不可能显现的指标；
- 重新设计也须用他人可核查的证据核验；
- 完整认证不消除重新开启审查的理由，[§9 Recertification and Reopening](#9-再认证与重新开启)的所有触发条件仍适用；以及
- 规避依[§9.4 Non-evasion](#94-不得规避)处理。

<a id="94-non-evasion"></a>

#### 9.4 不得规避

**反规避。** 对本义务的规避由第三章统管 — 本章不重述那套纪律：

- [第三章 §1 — 定义完整性与反规避约束](core_03_definition_integrity.md#1-定义完整性与反规避约束)；
- [第三章 §2 — 来自可观察系统行为的不合规](core_03_definition_integrity.md#2-来自可观察系统行为的不合规)；
- 包括 [§2.1 常见规避模式](core_03_definition_integrity.md#21-常见规避模式) 下的范围与边界规避。

*收束说明：* B 部分过程中没有任何单一步骤就其本身是新的或激进的 — 记录、披露、审查、质疑、评议所角色、重开与轨迹输入都是熟悉的治理工具。不同之处在于把它们一并驱动的**一致性**、**监督**与**问责**，在 [宪法四元](core_00_preamble.md#constitutional-tetrad) 下：同一纪律跨系统类与评议所族系适用，工作保持可见、可重建，而当认证错误、过期或规避时，行动者仍须被问责。

<a id="10-challenging-a-certification"></a>

### 10. 对认证提出质疑

<details>
<summary><strong><span style="color: #2563eb;">追溯</span></strong></summary>

- 上游：
  - [B部分§6.3 可质疑性链条](core_09.005_system_alignment_certification_record_process.md#63-可争议性链条) (*质疑路径的运行顺序*);
  - [B部分§7](core_09.005_system_alignment_certification_record_process.md#7-认证结果) (*质疑可能涉及的结果*);
  - [§8](#8-系统认证记录) (*列明质疑路径的系统认证记录*);
  - [宪法四元](../../core_00.000_preamble.md#constitutional-tetrad);
  - [第二十六-C条](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*及时解决与反拖延底线*).
- 下游： [§9](#9-再认证与重新开启) (*可信质疑会重新开启审查*); [第十五章](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (15.000) (*争议事项对应的论坛路径*).
- 分节：
  - [§10.1](#101-何时开启该途径) (*路径何时开启*); and
  - [§10.2](#102-可质疑途径) (*质疑路径*).

</details>

<details>
<summary><strong><span style="color: #2563eb;">定义 · 评估 · 合规</span></strong></summary>

- [可质疑性](../../core_05.035_band_accountability.md#contestability) · [O](../../core_05.035_band_accountability.md#contestability) · [M](../../core_05.035_band_accountability.md#contestability-a) · [A](../../core_05.035_band_accountability.md#contestability-a) · [C](../../core_05.035_band_accountability.md#contestability-c)

</details>


系统认证记录只有在感知者能够纠正其错误时才有用。质疑必须真实有效：能够重新开启审查、暂停依赖，并到达对争议事项有权限的论坛。毫无改变的意见箱不算数。

本节属于第六阶段（运行）的子阶段VIa，并与[§9 再认证与重新开启](#9-再认证与重新开启)配套。它规定受影响方如何质疑系统认证记录。已公布记录的质疑路径在结果公布时开启，见[§10.1 路径何时开启](#101-何时开启该途径)。

依照[宪法四元](../../core_00.000_preamble.md#constitutional-tetrad)，[可质疑性](../../core_05.035_band_accountability.md#contestability)落实**问责**并保持挑战路径中的**参与**。依据[第二十六-C条](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor)的质疑期限落实及时性。

受影响方必须有真实的质疑方式。记录须列明§10.2的质疑路径，足以质疑记录内容、范围、分类假设、对证据的依赖、监督完整性、结果及持续依赖。机制须有效且可及，不得流于仪式。质疑必须能够重新开启审查；在可信地证明重大错误或完整性风险时暂停或限制依赖；并转交给对争议事项有合法管辖权的论坛家族。义务随系统类别和重大影响而定；存在重大影响时，称系统为实验性、内部、个人、孤立或仅技术用途不能免除义务。

<a id="101-when-the-path-opens"></a>

#### 10.1 何时开启该途径

*简而言之：在要求任何人依赖认证之前，质疑途径必须已经开放。对于尚未运行的系统，首次结果公布时途径开启；对于已经运行的系统，途径早已开放。*

途径何时开启、开放多久：

- 对于尚未运行的系统，无论结果如何，首次认证结果公布时，已公布记录质疑途径即开启。因此可以在系统上线前提出质疑并暂停依赖，见 [Part B §7.1 Go-Live Gate](core_09.005_system_alignment_certification_record_process.md#71-上线门槛)。
- 已运行的系统已有利益相关者。因此其途径已经开放，或在系统记录开启时开放。这包括处于 [Article XXVIII-A](../../core_06.020_rights_part_e.md#xxviii-a-existing-instantiations-adoption-transition-window)（*分阶段采用与权利底线连续性*）过渡窗口的系统以及后续认证。
- **利益相关者**是受到系统重大影响或对系统有重大依赖的 sentients，由评估认定，而非由运营者指定。
- 对尚未运行的系统，在途径开启前，《系统认证记录》仍会列明该系统（[Part B §6.2 Supervisory sequence](core_09.005_system_alignment_certification_record_process.md#62-监督顺序)）。[§10.2 Contestability paths](#102-可质疑途径)中的组成部分、主导诚信和升级途径在整个审查期间均可使用。
- 只要系统仍有利益相关者，该途径就保持开放。认证后出现利益相关者时，依照 [§9 Recertification and Reopening](#9-再认证与重新开启) 重新开启审查。
- 若系统仍有利益相关者，却没有可质疑《系统认证记录》的开放途径，则关于系统一致的主张没有依据。

<a id="102-contestability-paths"></a>

#### 10.2 可质疑途径

*简而言之：《系统认证记录》必须说明应到何处提出异议。先走通常的第一步，再进入对争议结论有权限的论坛；若主导论坛本身受到质疑，则使用备用途径；必要时升级。等待可能造成损害时，质疑者可直接诉诸论坛。*

《系统认证记录》必须列明以下四条质疑途径，让受影响者知道争议应提交何处。这些途径将 Chapter Fifteen 的 [Dispute sequencing](../../core_15.000_forum.md#dispute-sequencing) 应用于《系统认证记录》。它们是通往论坛的路线，并非新设论坛；论坛权限仍由 Chapter Fifteen 决定。顺序见 [Part B §6.3 Contestability chain](core_09.005_system_alignment_certification_record_process.md#63-可争议性链条)。

- **已公布记录质疑途径**——针对《系统认证记录》一般争议的通常第一步。记录须说明质疑受理席位（[§6.1.1 Four seats in a certification](core_09.005_system_alignment_certification_record_process.md#611-认证中的四个席位)：
  - 谁接收质疑；
  - 如何提交；以及
  - [Article XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor)（*及时解决与反拖延底线*）的期限从收到时起算。

  运营者内部审查、供应商证明或技术签核不属于此途径。
- **组成部分论坛途径**——针对《系统认证记录》中的单项结论提出质疑，并提交给 Chapter Fifteen 中对该结论有权限的论坛家族。
- **主导诚信途径**——质疑主导论坛的程序处理，例如被俘获、隐瞒信息、审查自身工作或过早宣布认证完成。该途径通过 Integrity routing 并设有备用论坛，避免主导论坛自行裁判。
- **升级途径**——根据 Chapter Fifteen 将争议转至其他或更高层级论坛，包括移交、将问题提交另一论坛裁定、备用路由，或在论坛家族之间升级。当主要利益归属其他领域、宪法效力受到质疑、需要结构性补救、两个论坛家族陷入僵局，或论坛可能自行裁判时适用。

若延误可能对权利、证据、独立性或实际恢复造成重大危险，仍可直接使用论坛途径。尚未完成已公布记录质疑途径，不得阻滞论坛途径，也不得耗尽 [Article XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) 的期限。

<a id="11-relationship-to-standing"></a>

### 11. 与轨迹的关系

<details>
<summary><strong>追溯</strong></summary>

- 上游：
  - [Part B §6](core_09.005_system_alignment_certification_record_process.md#6-论坛程序) through
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-认证结果) (*论坛程序、系统认证记录与结果*);
  - [Constitutional Tetrad](../../core_00.000_preamble.md#constitutional-tetrad);
  - [Two Constitutional Aims](../../core_00.000_preamble.md#two-constitutional-aims);
  - [Verified Inputs for Standing](../../core_05.035_band_accountability.md#verified-inputs-for-standing).
- 下游： [第十一章](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (*轨迹记录与经核实输入门*); [第十三章](../../core_13.000_standing_integration.md#chapter-thirteen-standing-effects-and-integration) (*轨迹效果与整合*).
- 配合阅读： **Article III-A** (*认证限制交付时获取生存必需品*).
- 分节：
  - [§11.1](#111-认证可以提供什么--在-两项宪法宗旨-下并且仅通过下方第八章的经核实输入门) (*系统认证记录可向轨迹提供什么*);
  - [§11.2](#112-无论认证结果如何系统都通过其系统认证记录提供轨迹输入临时或完整认证附带或不附带条件有条件或延期认证拒绝撤回到期或其他结果这包括首次认证的系统以及从未获得认证的系统认证过程中的发现无论首次还是后续认证轮次都按相同条件输入轨迹撤回到期或以其他方式失去认证不会排除系统持有认证期间产生的已核实事实所有输入仍须通过下文的经核实输入门) (*每一种认证结果*);
  - [§11.3](#113-经核实输入门-一份认证记录仅当其有界可追溯可质疑并在下列项下经核实时才可以向第八章轨迹供料) (*经核实输入门*);
  - [§11.4](#114-贡献资格记录) (*贡献轨迹记录*); 并且
  - [§11.5](#115-违规资格记录) (*违规轨迹记录*).

</details>


*用直白的话说：认证可以向轨迹供料，但它不是轨迹。一份好的或坏的认证记录可以通过一道严格的门向第八章提供经核实事实 — 只有第八章与第九章决定轨迹记录与效果。*

<a id="111-what-a-system-certification-record-can-pass-on-to-standing"></a>

#### 11.1 **认证可以提供什么** — 在 [两项宪法宗旨](core_00_preamble.md#two-constitutional-aims) 下，并且仅通过下方第八章的经核实输入门：

- 核验与权利底线相容之对齐的记录，可以提供经核实的**繁盛**侧输入；
- 记载错分类、被掩盖缺陷或击败底线之运行的记录，可以提供经核实的**问责**侧输入。

<a id="112-every-certification-outcome"></a>

#### 11.2 无论认证结果如何，系统都通过其系统认证记录提供轨迹输入：临时或完整认证（附带或不附带条件）、有条件或延期认证、拒绝、撤回、到期或其他结果。这包括首次认证的系统以及从未获得认证的系统。认证过程中的发现，无论首次还是后续认证轮次，都按相同条件输入轨迹。撤回、到期或以其他方式失去认证，不会排除系统持有认证期间产生的已核实事实。所有输入仍须通过下文的经核实输入门。

认定系统尚未一致，本身不构成违规。认证轮次的目的正是发现并纠正问题。如果运营者持续、诚实地努力实现一致且没有过失，认定违规的可能性很低。轨迹输入须有事实支持不利分类和对特定行动者的归因（[§11.5 违规轨迹记录](#115-违规资格记录)）；认定运营者愿意但无力纠正问题的准备度结论不提供此类事实（[B部分§7.5 拒绝与撤销的后果](core_09.005_system_alignment_certification_record_process.md#75-拒绝与撤销的效果)）。这不涵盖过失、隐瞒或虚假证据。

<a id="113-verified-input-gate"></a>

#### 11.3 **经核实输入门。** 一份认证记录仅当其有界、可追溯、可质疑，并在下列项下经核实时，才可以向第八章轨迹供料：

- [§2](core_07_a_system_alignment_certification_evaluation.md#2-系统类别评估)（*系统类*）；
- [§4](core_07_a_system_alignment_certification_evaluation.md#34-数据类型与处理评价)（*数据类型与处理*）；
- 在具实质性时的 [§5](core_07_a_system_alignment_certification_evaluation.md#51-生态足迹评价)；
- 在 **Article IV**（《资源分配、依赖与生态系统资金》）实质性触发适用时的 [§6](core_07_a_system_alignment_certification_evaluation.md#53-比例适当的跨系统支持评价)；
- 在 **Article V-B**（《不歧视》）实质性触发适用时的 [§7](core_07_a_system_alignment_certification_evaluation.md#54-不歧视评价)；
- 在 **Article V-G**（《可及性》）实质性触发适用时的 [§8](core_07_a_system_alignment_certification_evaluation.md#55-无障碍评价)；
- 在 **Article VI**（《以感知者为中心的教育权》）实质性触发适用时的 [§9](core_07_a_system_alignment_certification_evaluation.md#52-教育能力与学习系统完整性评价)；
- 在 **Article XIII**（《可靠可信系统权》）实质性触发适用时的 [§10](core_07_a_system_alignment_certification_evaluation.md#56-可信度与系统依赖完整性评价)；
- [§12](#82-系统认证记录的透明度与可审计性) 与 [§14](#10-对认证提出质疑)；
- 第二至四章，以及适用的第十一章过程。

<a id="114-contribution-standing-record"></a>

#### 11.4 贡献资格记录

正面认证、验证、再认证、完成补救，或履行认证条件或获准免除该条件，在表明以下事项时，可以为**贡献资格记录**提供经核实的输入：

- 宪法利益；
- 有能力的管理；
- 安全授权的准备度；
- 系统优化；
- 勤勉；或
- 宪法一致性。

<a id="115-violation-standing-record"></a>

#### 11.5 违规资格记录

当事实支持不利分类并可归因于特定行为者时，系统认证记录中的以下事项可以为**违规资格记录**提供经核实的输入：

- 撤销认证；
- 隐瞒错误分类；
- 再认证未通过；
- 在要求进行再认证时，回归测试未通过或未进行；
- 伪造认证证据；
- 实质性违反认证条件；
- 经核实在认证范围以外运行；
- 不适合该系统类别的基础设施脆弱性；以及
- 在要求进行的A部分评估中发现的实质性缺陷，包括：
  - [§3.4 Data Types and Handling Evaluation](core_09.000_system_alignment_certification_evaluation.md#34-数据类型与处理评估)项下的数据处理缺陷；
  - 系统性风险属于评估范围时，[§3.2.2 Defects and Misalignment](core_09.000_system_alignment_certification_evaluation.md#322-缺陷与不一致)项下的风险评估或风险披露缺陷；
  - 必须披露时，[§5.1 Ecological Footprint Evaluation](core_09.000_system_alignment_certification_evaluation.md#51-生态足迹评估)项下的生态足迹误报；
  - [§5.4 Nondiscrimination Evaluation](core_09.000_system_alignment_certification_evaluation.md#54-不歧视评估)项下的不歧视或代理歧视缺陷；
  - [§5.5 Accessibility Evaluation](core_09.000_system_alignment_certification_evaluation.md#55-无障碍评估)项下的无障碍或实质参与缺陷；
  - [§5.2 Educational Capability and Learning-System Integrity Evaluation](core_09.000_system_alignment_certification_evaluation.md#52-教育能力与学习系统完整性评估)项下的教育能力、评估不透明、凭证把关或强加过时缺陷；或
  - [§5.6 Trustworthiness and System-Reliance Integrity Evaluation](core_09.000_system_alignment_certification_evaluation.md#56-可信度与系统依赖完整性评估)项下的可信度、虚假信任、逆向激励、不可访问的质疑渠道或恢复完整性缺陷。
