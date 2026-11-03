<!-- AI-assisted translation draft; unreviewed. §3.4.3 protective storage and key custody, source lines 684–691; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4.3 protective storage and key custody (ja)

## English source (lines 684–691)

##### 3.4.3 Protective Storage and Key Custody

For data in the restricted-by-default and non-accessible bands, certification must verify that the system meets the protective storage and key-custody minimum in [CS-6.305 Part A §5.0 Access-posture bands](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands). The record must show:
- where restricted data and its keys actually sit, including backups, caches, logs, and swap;
- that plaintext is confined to the processes that need it; and
- that audit, export, and lawful-override paths still work.

A claim of encryption without that evidence does not satisfy this check.

## Translation draft

##### 3.4.3 保護的保管と鍵の管理

デフォルトでアクセス制限され、アクセス不能なバンドのデータについて、認証では、[CS-6.305 Part A §5.0 アクセス態勢バンド](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands)の保護的保管および鍵管理の最低基準をシステムが満たしていることを検証しなければならない。記録には次を示す必要がある。

- 制限対象データとその鍵が実際にどこに置かれているか（バックアップ、キャッシュ、ログ、スワップを含む）。
- 平文が必要とするプロセスだけに限定されていること。
- 監査、エクスポート、適法なオーバーライドの経路が引き続き機能すること。

これらの証拠がなければ、暗号化しているという主張だけではこの確認を満たさない。
