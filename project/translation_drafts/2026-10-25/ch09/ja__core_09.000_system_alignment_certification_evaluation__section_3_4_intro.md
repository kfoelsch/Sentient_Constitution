<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (ja)

## English source (lines 636–650)

*In plain terms: certification also has to look at what kinds of data the system touches and whether it handles them appropriately — including whether types are still right on the current review cycle, and whether the underlying infrastructure is strong enough for that data at that system class. The type rules and the System Data Types Record live in the systems corpus; certification checks that the rules were actually applied and that the record is honest.*

System alignment certification must evaluate **data types and handling** as part of every materially impactful certification record. This section states what certification must verify. The type taxonomy and handling mechanics live in **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Information types and handling*) and [CS-6.310 — Data classifications](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, together with:

- canonical information-type definitions;
- handling rules and separation requirements;
- lifecycle detail; and
- the durable [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record).

**Evaluation requirement.** The certification process must determine whether the system:

- identifies the data types materially in scope; and
- handles them under the **most restrictive applicable** classification, including across transformation, aggregation, delegation, storage, retention, and cross-domain linkage.

Evaluation must reflect functional effect, not label, format, or pipeline stage alone.

## Translation draft

*簡単に言えば、認証ではシステムがどの種類のデータに触れるか、それを適切に扱っているかも確認しなければならない。現在の審査サイクルでもデータ種別が適切か、またそのシステムクラスにおいて当該データを扱う基盤インフラが十分に堅牢かも含まれる。種別規則と[システムデータ種別記録](core_05.040_band_continuity.md#system-data-types-record)はシステム・コーパスにあり、認証では規則が実際に適用され、記録が正確であることを確認する。*

システム整合性認証では、重要な影響を伴うすべての認証記録の一部として、**データの種類と取扱い**を評価しなければならない。本節は認証が何を検証すべきかを定める。種別の分類体系と取扱いの仕組みは、**[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling)（*情報の種類と取扱い*）および[CS-6.310 — データ分類](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**にあり、次も含まれる。

- 情報種別の標準定義
- 取扱規則と分離要件
- ライフサイクルの詳細
- 永続的な[システムデータ種別記録](core_05.040_band_continuity.md#system-data-types-record)

**評価要件。** 認証プロセスでは、システムが次を満たすか判定しなければならない。

- 重要な範囲に含まれるデータ種別を特定すること。
- 変換、集約、委任、保存、保持、領域横断の連結を含め、**適用可能な最も制限的な**分類に従って取り扱うこと。

評価は機能上の効果を反映しなければならず、ラベル、形式、処理パイプラインの段階だけで判断してはならない。
