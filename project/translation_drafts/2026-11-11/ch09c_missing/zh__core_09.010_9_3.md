<!-- AI-assisted translation draft; unreviewed. Current-source Chapter Nine Part C §9.3; source SHA-256 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Baseline commit 247e2180509e5e029c1106878cf225067339e010; baseline SHA-256 faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Draft only; do not synchronize into translations/. -->

<a id="93-provisional-and-full-certification"></a>
#### 9.3 临时与完整认证

*简言之：系统逐步赢得信任。新系统和评估未通过的系统先受更严格限制并频繁复查。只有当前没有问题、也没有问题将至的系统，才能升为完整认证并采用更长周期。评估未通过会使其回到严格限制。*

<a id="931-the-two-statuses"></a>
##### 9.3.1 两种状态

认证有两种状态，每种都有自己的认证周期，并按[§8.1 Minimum record contents](#81-minimum-record-contents)载于系统认证记录：

- **[Provisional certification](core_05.040_band_continuity.md#provisional-certification)**：系统首次认证（包括新部署系统）；或系统在再认证未通过、重新开启审查或新审查发现不一致后取得认证。临时周期短于同一系统类别的完整认证周期，依赖限制列于记录。
- **[Full certification](core_05.040_band_continuity.md#full-certification)**：只有持有临时认证的系统在再认证时，且同时满足以下条件才能取得：
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
- 再认证发现当前不一致即为**失败**；适用[Part B §7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)。下次认证只能为临时认证，不论下一次检查多么干净；无问题计数归零。
- 没有当前不一致但有迫近指标时，不算失败，也不算无问题。临时状态保持且计数不增加；完整状态降为临时。
- 依照[§9 Recertification and Reopening](#9-recertification-and-reopening)重新开启审查并发现不一致，效果等同再认证失败。
- 已认证系统的新审查发现当前不一致，效果相同。若系统没有认证状态，适用[Part B §7.4 Denial and Revocation](core_09.005_system_alignment_certification_record_process.md#74-denial-and-revocation)。

<a id="933-cause-of-misalignment"></a>
##### 9.3.3 不一致的原因

评估、再认证、重新开启或新审查发现不一致时，记录须说明原因属于：**设计所致**（系统/流程即使按预期运行也会产生不一致结果）；**运行所致**（设计表面合理，但运行、输入或维护方式导致不一致）；或**尚未确定**（论坛查明原因前，设计和运行两方面的补救均保持开放）。

原因认定受以下限制：系统持续产生不一致结果即属不一致，纸面设计看似合理不是抗辩；会产生不一致结果的设计在结果出现前已构成不一致；原因认定决定寻求的补救和重新审查范围，但不决定系统是否不一致。

设计所致时：重新设计实施并核验前，无问题再认证计数保持零；查明原因的论坛或依[Part B §6.2 Supervisory sequence](core_09.005_system_alignment_certification_record_process.md#62-supervisory-sequence)指定的后续论坛，在[matching intake target](core_05.040_band_continuity.md#tier-window)期限内核验重新设计，最早可在首次临时再认证时进行；重新设计核验前的组成部分评估不计入无问题总数；改变运行方式不满足此步骤。

这些规则补充但不取代上述降级规则。运营者或受影响的sentient可请求论坛复核原因认定；若原因改变，本组规则停止适用。

<a id="934-tier-windows"></a>
##### 9.3.4 分级时限

初评、再认证、重新开启审查或新审查发现不一致时：按[Chapter Fifteen §6 Timely resolution, materiality tiers, and anti-delay discipline](core_15.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline)的重大性等级分类；推定采用与系统类别相应的等级（例如不一致的A类系统推定为A级）；受理、证据保存、临时保护和决定均遵守该等级时限及外限；逾期依该节审查。

<a id="935-class-a-reliance"></a>
##### 9.3.5 A类系统依赖

临时认证周期短于完整认证，因此更早再认证（[§9.3.1 两种状态](#931-the-two-statuses)）；依赖限制记在系统认证记录（[§8.1 Minimum record contents](#81-minimum-record-contents)）。中断处理如下：
- 临时认证本身不要求中断会在替代方案到位前切断生存必需资源的系统；
- B部分§7的临时保护和认证条件处理此类情况；
- 因设计所致的不一致而暂停计数时同样如此：暂停计数本身不得中断sentient所依赖的系统；以及
- 暂停期间，论坛须说明临时保护、依赖认证条件和对依赖者的通知。

<a id="936-verification-not-assertion"></a>
##### 9.3.6 核验而非自我声明

系统状态、无问题再认证计数和监测指标都必须核验并接受独立审查；系统自己的说法不够：
- 不得设定使不一致永远不可能显现的指标；
- 重新设计也须用他人可核查的证据核验；
- 完整认证不消除重新开启审查的理由，[§9 Recertification and Reopening](#9-recertification-and-reopening)的所有触发条件仍适用；以及
- 规避依[§9.4 Non-evasion](#94-non-evasion)处理。
