# Chapter Five definition batch 14 — Full Certification (zh)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Full Certification; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### 完整认证

<details>
<summary><strong>溯源</strong></summary>

- 规范归属：第九章C部分§9.3临时与完整认证。本条位于系统一致性认证主题组旁边，但不属于该组。与临时认证、重新认证、系统/分类记录及代理偏差合读。

</details>

*通俗地说，系统在连续通过无问题的临时重新认证后获得更长周期的状态，当前没有问题，也没有迹象预示问题将至。该状态并非永久；评估失败或监测指标警告会使其失去。*

- **What it is**
  - **In scope / out of scope / dependencies:** 范围：系统曾获临时认证，完成规定次数的连续无问题临时重新认证，并且最近一次未显示当前不一致或即将不一致的指标。认证周期按类别设定，有期限且可重启审查。范围外：临时认证；可附加于任一状态的附条件认证；永久许可、声誉分数或地位效应（仅第十一章决定）。依赖临时认证和重新认证。无问题次数下限、降级和层级窗口见第九章C部分§9.3。本条仅定义第五章含义。
<a id="full-certification-a"></a>
- **How to measure and assess**
  - 按连续性测量族评估：是否完成类别要求的连续无问题临时重新认证次数；是否没有未解决不一致、未修复缺陷、逾期检查或失败回归测试；记录中的监测触发与趋势是否未越过/接近阈值、可独立复核且未被设得过窄以致问题无法显现。
<a id="full-certification-c"></a>
- **What must hold**
  - **Primary failure:** 主要失败：未达最低次数或存在当前问题/临近指标仍授予完整认证；重新认证失败或重启审查发现不一致后仍保留；指标狭窄到无法指示问题；以完整状态为由跳过或延迟重启触发。
