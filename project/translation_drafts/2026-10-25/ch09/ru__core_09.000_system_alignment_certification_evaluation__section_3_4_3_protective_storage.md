<!-- AI-assisted translation draft; unreviewed. §3.4.3 protective storage and key custody, source lines 684–691; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4.3 protective storage and key custody (ru)

## English source (lines 684–691)

##### 3.4.3 Protective Storage and Key Custody

For data in the restricted-by-default and non-accessible bands, certification must verify that the system meets the protective storage and key-custody minimum in [CS-6.305 Part A §5.0 Access-posture bands](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands). The record must show:
- where restricted data and its keys actually sit, including backups, caches, logs, and swap;
- that plaintext is confined to the processes that need it; and
- that audit, export, and lawful-override paths still work.

A claim of encryption without that evidence does not satisfy this check.

## Translation draft

##### 3.4.3 Защищенное хранение и управление ключами

Для данных в полосах с ограниченным по умолчанию и недоступным доступом сертификация должна проверить, что система соблюдает минимальные требования к защищенному хранению и управлению ключами, установленные [CS-6.305, часть A, §5.0, полосы режимов доступа](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands). В записи должно быть указано:

- где фактически находятся данные с ограниченным доступом и их ключи, включая резервные копии, кэши, журналы и файл подкачки;
- что открытый текст доступен только процессам, которым он необходим; и
- что пути аудита, экспорта и законного переопределения продолжают работать.

Одного заявления о шифровании без этих доказательств недостаточно для прохождения проверки.
