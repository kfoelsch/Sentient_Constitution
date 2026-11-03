<!-- AI-assisted translation draft; unreviewed. §3.4.3 protective storage and key custody, source lines 684–691; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4.3 protective storage and key custody (tr)

## English source (lines 684–691)

##### 3.4.3 Protective Storage and Key Custody

For data in the restricted-by-default and non-accessible bands, certification must verify that the system meets the protective storage and key-custody minimum in [CS-6.305 Part A §5.0 Access-posture bands](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands). The record must show:
- where restricted data and its keys actually sit, including backups, caches, logs, and swap;
- that plaintext is confined to the processes that need it; and
- that audit, export, and lawful-override paths still work.

A claim of encryption without that evidence does not satisfy this check.

## Translation draft

##### 3.4.3 Koruyucu Depolama ve Anahtarların Muhafazası

Varsayılan olarak kısıtlı ve erişilemez bantlardaki veriler için sertifikasyon, sistemin [CS-6.305 Bölüm A §5.0 Erişim duruşu bantları](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands) kapsamındaki koruyucu depolama ve anahtar muhafazası asgari koşulunu karşıladığını doğrulamalıdır. Kayıt şunları göstermelidir:

- kısıtlı verilerin ve anahtarlarının yedekler, önbellekler, günlükler ve takas alanı dâhil gerçekte nerede bulunduğunu;
- açık metnin yalnızca ona ihtiyaç duyan süreçlerle sınırlandığını; ve
- denetim, dışa aktarma ve hukuka uygun geçersiz kılma yollarının çalışmaya devam ettiğini.

Bu kanıtlar olmadan şifreleme iddiası bu kontrolü karşılamaz.
