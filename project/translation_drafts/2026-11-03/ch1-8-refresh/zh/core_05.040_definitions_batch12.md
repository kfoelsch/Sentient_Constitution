# Chapter Five definition batch 12 — Clean Recertification (zh)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Clean Recertification; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### 无问题的重新认证

<details>
<summary><strong>溯源</strong></summary>

- 规范归属：第九章C部分§9.3.1两种状态。与重新认证、临时认证及完整认证合读。集群组成：无。

</details>

*通俗地说，当前没有不一致，监测指标也未显示不一致即将发生时，该次重新认证才算无问题。只有无问题的重新认证计入完整认证。*

- **What it is**
  - **In scope / out of scope / dependencies:** 范围：未发现当前不一致或即将发生不一致指标的重新认证。达到规定数量的连续、无问题临时重新认证是完整认证的一个条件。范围外：发现当前不一致并将计数归零的失败重新认证；或未发现当前不一致但有临近指标的重新认证（不算失败，但也不干净）。依赖重新认证、临时认证和完整认证。数量及完整认证要求见第九章C部分§9.3.1；本条仅定义第五章含义。
<a id="clean-recertification-a"></a>
- **How to measure and assess**
  - 按连续性测量族评估：是否只有无问题的重新认证才增加计数；失败的重新认证是否将计数重置为零。
<a id="clean-recertification-c"></a>
- **What must hold**
  - **Primary failure:** 主要失败：仍有未解决的不一致、缺陷、逾期检查或失败的回归测试却计为无问题；存在即将不一致的指标仍增加计数。
