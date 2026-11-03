<!-- AI-assisted translation draft; unreviewed. §3.4 data-types introduction and evaluation requirement, source lines 636–650; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §3.4 data types and handling introduction (id)

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

*Dalam istilah sederhana: sertifikasi juga harus melihat jenis data yang disentuh sistem dan apakah sistem menanganinya dengan tepat—termasuk apakah jenisnya masih tepat dalam siklus tinjauan saat ini dan apakah infrastruktur dasarnya cukup kuat untuk data tersebut pada kelas sistem itu. Aturan jenis dan [Catatan Jenis Data Sistem](core_05.040_band_continuity.md#system-data-types-record) terdapat dalam korpus sistem; sertifikasi memeriksa apakah aturan benar-benar diterapkan dan catatannya jujur.*

Sertifikasi penyelarasan sistem harus mengevaluasi **jenis dan penanganan data** sebagai bagian dari setiap catatan sertifikasi berdampak material. Bagian ini menetapkan hal yang wajib diverifikasi oleh sertifikasi. Taksonomi jenis dan mekanisme penanganan terdapat dalam **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Jenis dan penanganan informasi*) dan [CS-6.310 — Klasifikasi data](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, bersama dengan:

- definisi baku jenis informasi;
- aturan penanganan dan persyaratan pemisahan;
- perincian siklus hidup; dan
- [Catatan Jenis Data Sistem](core_05.040_band_continuity.md#system-data-types-record) yang tahan lama.

**Persyaratan evaluasi.** Proses sertifikasi harus menentukan apakah sistem:

- mengidentifikasi jenis data yang secara material berada dalam cakupan; dan
- menanganinya menurut klasifikasi **paling ketat yang berlaku**, termasuk selama transformasi, agregasi, delegasi, penyimpanan, retensi, dan pengaitan lintas ranah.

Evaluasi harus mencerminkan dampak fungsional, bukan label, format, atau tahap alur pemrosesan saja.
