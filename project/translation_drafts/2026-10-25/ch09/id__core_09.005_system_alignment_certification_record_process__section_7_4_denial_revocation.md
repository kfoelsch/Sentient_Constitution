#### 7.4 Penolakan dan Pencabutan

*Secara sederhana: penolakan dan pencabutan adalah hasil nyata, bukan ancaman. Jika sistem belum disertifikasi dan operator tidak bersedia atau tidak mampu memperbaiki masalah, sertifikasi ditolak. Jika sistem memegang sertifikasi dan operator tidak bersedia atau tidak mampu memperbaiki masalah, sertifikasinya dicabut. Dalam kedua hal tersebut, makhluk sadar terdampak diberi tahu, ketergantungan dibatasi, dan tidak seorang pun diputus dari kebutuhan esensial untuk bertahan hidup sebelum ada pengganti.*

<a id="741-what-denial-and-revocation-are"></a>

##### 7.4.1 Arti penolakan dan pencabutan

**Penolakan** ([Penolakan Sertifikasi](core_05.040_band_continuity.md#certification-denial)) adalah hasil tidak disertifikasi ([§7 Hasil Sertifikasi](#7-certification-outcomes)), yang dicapai dengan menolak sertifikasi. **Pencabutan** ([Pencabutan Sertifikasi](core_05.040_band_continuity.md#certification-revocation)) adalah hasil pencabutan, yang dicapai dengan menarik kembali sertifikasi yang telah dimiliki. Ini adalah nama sederhana bagi hasil yang telah dicantumkan dalam [§7 Hasil Sertifikasi](#7-certification-outcomes).

<a id="742-when-denial-or-revocation-is-required"></a>

##### 7.4.2 Kapan penolakan atau pencabutan diwajibkan

**Penolakan diwajibkan** pada sertifikasi pertama, peninjauan baru, atau putaran untuk sistem yang tidak memegang status, apabila:

1. pemeriksaan menyatakan operator mampu tetapi tidak bersedia, atau tidak bersedia maupun mampu;
2. pemeriksaan menyatakan operator bersedia tetapi tidak mampu, dan penyempitan lingkup, dukungan, atau pengalihan tanggung jawab tidak menutup kesenjangan dalam jendela waktu terpanjang yang diizinkan kelas sistem; atau
3. satu kali penangguhan berdasarkan [§7.3 Kesiapan Remediasi: Kesediaan dan Kapasitas untuk Mengoreksi](#73-remediation-readiness-willingness-and-capacity-to-correct) telah berakhir dan temuan masih belum terbukti.

**Pencabutan diwajibkan** bagi sistem yang memegang sertifikasi, pada saat sertifikasi ulang atau peninjauan yang dibuka kembali, apabila:

1. setelah pemberitahuan dan kesempatan untuk menjawab, pemeriksaan menyatakan operator mampu tetapi tidak bersedia, atau tidak bersedia maupun mampu;
2. tenggat suatu persyaratan telah terlewati tanpa dipenuhi dua kali, atau persyaratan berkelanjutan telah dilanggar secara material, dan operator tidak dapat menunjukkan penyebab terverifikasi yang berada di luar kendalinya;
3. bukti yang diajukan untuk kesiapan, koreksi, atau pelepasan persyaratan terbukti palsu, direkayasa, atau disembunyikan;
4. langkah pembuktian yang diwajibkan forum tidak dilakukan dalam jendela waktunya saat ketidakselarasan masih berlangsung; atau
5. pemeriksaan menyatakan operator bersedia tetapi tidak mampu, dan kesenjangan tidak ditutup dalam jendela waktu yang ditetapkan forum setelah perlindungan sementara berlaku.

Forum tidak boleh memenuhi satu pun persyaratan ini dengan memberikan sertifikasi atau melanjutkan sertifikasi dengan persyaratan.

<a id="743-protection-first"></a>

##### 7.4.3 Perlindungan didahulukan

Penolakan dan pencabutan mengubah status sertifikasi. Keduanya tidak dengan sendirinya mematikan sistem.

- **Sebelum salah satunya berlaku:** forum menyatakan perlindungan sementara dan batas ketergantungan ([§7.2 Cacat Sertifikasi dan Koreksi](#72-certification-defects-and-correction), *Perlindungan, koreksi, dan verifikasi*).
- **Sistem Kelas A yang gangguannya akan memutus kebutuhan esensial untuk bertahan hidup sebelum tersedia pengganti:** status berubah segera. Operasi hanya berlanjut sebagai ketergantungan sementara yang diotorisasi secara terpisah berdasarkan [Bagian C §9.2 Sertifikasi Sementara dan Penuh](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) (*Ketergantungan Kelas A*), dengan rencana bertanggal untuk menyediakan pengganti atau pengelola yang mampu.

<a id="744-process"></a>

##### 7.4.4 Proses

Sebelum penolakan atau pencabutan, operator diberi:

- pemberitahuan tentang temuan dan buktinya;
- jendela waktu singkat yang dinyatakan untuk menjawab atau menunjukkan langkah pembuktian (ditetapkan berdasarkan tingkat dalam [Bagian C §9.2 Sertifikasi Sementara dan Penuh](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification)); dan
- kesempatan menggugat temuan melalui [rantai dapat-digugat](#63-contestability-chain), yaitu jalur untuk menggugat catatan sertifikasi.

Keputusan menyatakan alasannya dalam catatan, termasuk temuan tentang kesediaan dan kapasitas ([Bagian C §8.1 Isi minimum catatan](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)). Perlindungan mendesak tidak menunggu semua proses ini ([§6.2 Urutan Pengawasan](#62-supervisory-sequence)).

<a id="745-effect"></a>

##### 7.4.5 Dampak

Penolakan atau pencabutan menimbulkan dampak berikut:

- **Status:** sistem berstatus Tidak Disertifikasi. Sistem tidak boleh go-live atau berkembang secara material, serta tidak boleh menyatakan dirinya tersertifikasi.
- **Pemberitahuan:** pihak yang mengandalkan sistem dan setiap Institusi yang mengoperasikan atau mengelolanya diberi tahu.
- **Operasi:** ketergantungan yang berlanjut diputuskan secara terpisah berdasarkan perlindungan kebutuhan esensial untuk bertahan hidup dalam [Bagian C §9.2 Sertifikasi Sementara dan Penuh](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification).
- **Institusi:** pencabutan sertifikasi yang dikutip oleh Institusi dianggap sebagai pencabutan sertifikasi untuk kaskade dalam [Bagian E §14.3 Kaskade dari Sertifikasi Sistem](core_09.020_institutional_alignment_certification.md#143-cascade-from-system-certifications).
- **Kedudukan:** penolakan atau pencabutan tidak dengan sendirinya mengubah kedudukan siapa pun. Hanya [Bab Sepuluh](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) dan [Bab Sebelas](core_12.000_standing_integration.md#chapter-twelve-standing-effects-and-integration) yang memutuskan hal itu. Fakta di baliknya dapat menjadi masukan ke catatan kedudukan pelanggaran, tetapi hanya melalui [Bagian C §10 Hubungan dengan Kedudukan](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) dan gerbang masukan terverifikasinya:
  - Pencabutan karena penyembunyian, bukti palsu, pelanggaran persyaratan material, atau operasi di luar lingkup sertifikasi dapat menjadi masukan tersebut.
  - Temuan “bersedia, tidak mampu” tidak menjadi masukan apa pun.
  - Penolakan terhadap sistem yang belum pernah memegang sertifikasi tidak menjadi masukan melalui bab ini.

<a id="746-not-a-permanent-bar"></a>

##### 7.4.6 Bukan larangan permanen

Operator yang ditolak atau dicabut sertifikasinya dapat mengajukan permohonan kembali.

- **Hal yang harus ditunjukkan dalam permohonan baru:** apa yang telah berubah.
  - bukti kesiapan yang baru, dengan langkah pembuktian yang telah dilakukan dan diverifikasi; dan
  - jika penyebabnya adalah tata kelola atau insentif, perubahan struktur yang telah diterapkan.
- **Yang bukan hal baru:** badan penerus, berganti nama, terpecah, atau dialihkan yang membawa operator, kendali, atau sistem yang sama ([Bagian C §9.3 Anti-Pengelakan](core_09.010_system_alignment_certification_record_recertification.md#93-non-evasion); [Bab Tiga §2.1 Pola Pengelakan Umum](core_03.000_definition_integrity.md#21-common-evasion-patterns)).
- **Masa tunggu:** forum tidak boleh menetapkan masa tunggu tanpa tujuan substantif.

---

**Berkas sebelumnya:** [core_09.000_system_alignment_certification_evaluation.md](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-part-a-certification-evaluation)

**Berkas berikutnya:** [core_09.010_system_alignment_certification_record_recertification.md](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-certification-record-recertification-and-standing)
