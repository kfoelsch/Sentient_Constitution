#### 7.2 認証の欠陥と是正

*平易に言えば、欠陥への対応には条件の付加、延期、拒否、取消し、または新たな審査があり得る。是正を許可の根拠としたり条件解除につなげたりする前に、独立に検証しなければならない。運営者が是正する意思と能力を備えているかによって、フォーラムが選ぶべき対応が決まる（[§7.3 是正の準備態勢：是正する意思と能力](#73-remediation-readiness-willingness-and-capacity-to-correct)、[§7.4 拒否と取消し](#74-denial-and-revocation)）。*

パートAのいずれかの評価で見つかる認証上の欠陥は、軽微な書類上の誤りではない。次を含む。

- [§2 システムクラス評価](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation)に基づく誤分類；
- [§3.2.2 欠陥と不整合](core_09.000_system_alignment_certification_evaluation.md#322-defects-and-misalignment)に基づくリスク評価およびリスク開示の欠陥；
- [§3.4 データ種別と取扱いの評価](core_09.000_system_alignment_certification_evaluation.md#34-data-types-and-handling-evaluation)に基づくデータ取扱いの欠陥；および
- [§5.1 生態学的フットプリント評価](core_09.000_system_alignment_certification_evaluation.md#51-ecological-footprint-evaluation)から[§5.6 信頼性とシステム依拠の完全性の評価](core_09.000_system_alignment_certification_evaluation.md#56-trustworthiness-and-system-reliance-integrity-evaluation)までに挙げられた領域上の欠陥。

そのような欠陥が見つかった場合、フォーラムは次の対応をとることができる。

- 条件付きで認証する；
- 認証を延期する；
- 認証を拒否する；
- 認証を取り消す；
- 認証期間を変更する；または
- [パートC §9 再認証および再開](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening)に基づいて審査を再開するか、新たな審査を命じる。

どの対応を選ぶかは、運営者または管理者に欠陥を是正する意思と能力があるかによる。[§7.3 是正の準備態勢：是正する意思と能力](#73-remediation-readiness-willingness-and-capacity-to-correct)はその確認方法を定め、[§7.4 拒否と取消し](#74-denial-and-revocation)は拒否または取消しが必要となる場合を定める。

**保護、是正、および検証。** 欠陥が見つかった場合、フォーラムは次を明示しなければならない。

- 影響を受ける範囲；
- 暫定保護および依拠の制限；および
- 必要な是正作業。

フォーラムは、[パートC §9.2 暫定認証と完全認証](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification)に基づく原因の所見と階層別の期間を用いる。

運営者または管理者は是正の証拠を提出する。指定された権限者は、証拠が当該範囲の許可または条件解除の根拠となる前に、独立に検証しなければならない。是正は次を満たす必要がある。

- 欠陥と特定された原因に対処する；および
- 影響を受ける保護措置が維持されることを示す。[CS-6.345 §10 再認証、回帰試験、および認証の欠陥](corpus_systems/cs_06.345_design_testing_verification_deployment.md#cs-6345-10-recertification-regression-testing-and-certification-defects)が求める場合は、回帰確認も行う。

是正するとの約束や、作業が完了したという運営者の申告だけでは足りない。運営者は、個々の是正が特定された問題に直接対処していることを示す検証済みの証拠を提出しなければならない。運営者が作業した証拠や、システムが現在稼働している事実だけでは、特定された問題が実際に解決されたことを示さない限り、この要件を満たさない。

未認証のシステムは、新たな運用を開始できない。その間も稼働中のシステムに依拠し続ける場合は、適用されるフォーラム手続と、[パートC §9.2 暫定認証と完全認証](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification)に基づく生存に不可欠な保護措置に従って、別途決定する。

<a id="73-remediation-readiness-willingness-and-capacity-to-correct"></a>

