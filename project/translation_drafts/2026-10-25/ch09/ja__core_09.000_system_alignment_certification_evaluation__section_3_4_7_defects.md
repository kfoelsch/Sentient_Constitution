<!-- AI-assisted translation draft; unreviewed. §3.4.7 defects and misalignment, source lines 733–746; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4.7 defects and misalignment (ja)

## English source (lines 733–746)

##### 3.4.7 Defects and Misalignment

Each of the following must be treated as a certification defect:

- misclassification of data;
- evasive restructuring;
- unsafe cross-domain linkage;
- handling that carries the right type label but still breaks the privacy protections that type requires;
- no record of who accessed, processed, or changed data, so a significant harm could not be investigated;
- **overdue or skipped scheduled data-type re-evaluation**;
- restricted data held as plaintext in storage or beyond its authorized processing boundary, or keys reachable by processes that do not need them; and
- infrastructure fragility that foreseeably defeats CS-6.305 (*Information types and handling*) and CS-6.310 (*Data classifications*) protections.

Their consequences are set in [§7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes).

## Translation draft

##### 3.4.7 欠陥と不整合

次の各項目は認証上の欠陥として扱わなければならない。

- データの誤分類；
- 規則を回避するための再構成；
- ドメインをまたぐ安全でない連結；
- 正しい種類ラベルが付いていても、その種類に必要なプライバシー保護を損なう取扱い；
- 誰がデータにアクセスし、処理し、変更したかの記録がなく、重大な損害を調査できないこと；
- 予定されたデータ種類の再評価の遅延または省略；
- 制限データを保存時に平文で保持すること、または許可された処理境界を越えて保持すること、あるいは不要なプロセスから鍵にアクセスできること；
- CS-6.305 (*Information types and handling*) および CS-6.310 (*Data classifications*) の保護を予見可能な形で損なうインフラの脆弱性。

その帰結は [§7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes).
