# Chapter Five definition batch 22 — Pilot (zh)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Pilot; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### 试点

<details>
<summary><strong>溯源</strong></summary>

- 规范归属：第九章A部分§2.3试点认证；B部分§7.1上线门槛。下游：CS-6.345系统生命周期。与上线、临时认证、系统认证/分类记录、依赖、系统锁定及可逆性合读。

</details>

*通俗地说，这是有意限制范围的真实发布。感知者确实受到影响或开始依赖，因此不是沙盒测试；范围、人群和期限必须预先确定。因其真实运行，开始前须单独认证，不得悄然超过认证限度。*

- **What it is**
  - **In scope / out of scope / dependencies:** 范围：全面部署前、在独立系统认证记录中预先限定范围/人群/期限且产生真实影响或依赖的上线。认证仅覆盖记录限度；超出限度的运行是因重大扩展产生的另一次上线，须事先单独认证。beta/试用/预览等名称不决定性质。无真实影响的沙盒测试或不符合定义的过渡阶段不在范围内。依赖上线定义及系统认证记录。评估深度及不进行试点的理由见第九章A部分§2.3。本条仅定义第五章含义。
<a id="pilot-a"></a>
- **How to measure and assess**
  - 按连续性测量族评估：是否在开始前取得独立认证并记录限度；试点是否保持在限度内；超出部分是否在运行前单独认证；是否将改名的真实运行按试点或全面部署进行认证。
<a id="pilot-c"></a>
- **What must hold**
  - **Primary failure:** 主要失败：把试点当作无需认证的测试；试点没有范围/人群/终止日期而实为全面部署；未经新认证即超限；建立依赖或锁定，使日后拒绝、附条件或撤销认证令受影响者付出高昂代价。
