<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (tr)

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

*Basitçe: sertifikasyon, sistemin hangi tür verilere dokunduğunu ve bunları uygun şekilde işleyip işlemediğini de incelemelidir. Buna türlerin mevcut inceleme döngüsünde hâlâ doğru olup olmadığı ve temel altyapının o sistem sınıfındaki bu veriler için yeterince güçlü olup olmadığı da dâhildir. Tür kuralları ve [Sistem Veri Türleri Kaydı](core_05.040_band_continuity.md#system-data-types-record) sistemler külliyatında yer alır; sertifikasyon kuralların gerçekten uygulandığını ve kaydın dürüst olduğunu denetler.*

Sistem uyum sertifikasyonu, maddi etkisi olan her sertifikasyon kaydının parçası olarak **veri türlerini ve işlenmesini** değerlendirmelidir. Bu bölüm, sertifikasyonun neleri doğrulaması gerektiğini belirtir. Tür taksonomisi ve işleme mekanizmaları **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Bilgi türleri ve işlenmesi*) ve [CS-6.310 — Veri sınıflandırmaları](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** içinde yer alır; ayrıca şunları kapsar:

- bilgi türlerinin kanonik tanımları;
- işleme kuralları ve ayırma gereklilikleri;
- yaşam döngüsü ayrıntıları; ve
- kalıcı [Sistem Veri Türleri Kaydı](core_05.040_band_continuity.md#system-data-types-record).

**Değerlendirme gerekliliği.** Sertifikasyon süreci, sistemin:

- maddi ölçüde kapsamda olan veri türlerini belirleyip belirlemediğini; ve
- dönüştürme, toplulaştırma, devretme, depolama, saklama ve alanlar arası bağlantı dâhil **uygulanabilir en kısıtlayıcı** sınıflandırmaya göre işleyip işlemediğini;

belirlemelidir. Değerlendirme yalnızca etiketi, biçimi veya işlem hattı aşamasını değil, işlevsel etkiyi yansıtmalıdır.
