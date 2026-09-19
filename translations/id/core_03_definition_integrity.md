<a id="chapter-three-definition-integrity-evasion-and-non-compliance"></a>
# BAB TIGA: INTEGRITAS DEFINISI, PENGELAKAN, DAN KETIDAKPATUHAN

<details>
<summary><strong><span style="color: #2563eb;">Letak dalam korpus (non-operatif): struktur berkas dan aturan baca</span></strong></summary>

> Isi berikut **hanya panduan pembaca**. Tidak menambah, mengurangi, atau mempersempit kewajiban yang mengikat di berkas ini atau di bab lain.
>
> Berkas ini adalah **uji coba bahasa pembaca** atas [Bab Tiga bahasa Inggris](../../core_03_definition_integrity.md). **Bukan** bagian mengikat Konstitusi Makhluk Sadar. **Bukan** konstitusi kedua. **Bukan** edisi kirim. **Disematkan** pada `SC-Corpus-2026.08.09`. Jika terjemahan ini dan sumber bahasa Inggris tampak berselisih, berkas bernomor [`core_03_definition_integrity.md`](../../core_03_definition_integrity.md) yang menang. Urutan baca dan metadata edisi tetap di [README.md](../../README.md). Metode dan glosarium: [translations/id/README.md](README.md).
>
> **Sebelumnya (lokal ini):** [core_02_definition_structure.md](core_02_definition_structure.md)
>
> **Berikutnya (bahasa ini):** [core_04_burden_traceability_verification.md](core_04_burden_traceability_verification.md)
> **Alur baca:** §1 integritas definisi dan anti-pengelakan → §2 ketidakpatuhan dari perilaku yang dapat diamati dan jenis pengelakan → §3 profil temuan dan akibat jejak

</details>

<details>
<summary><strong><span style="color: #2563eb;">Panduan pembaca (non-operatif): di mana Bab Tiga hidup dan apa yang tetap di sini</span></strong></summary>

> Isi berikut **hanya panduan pembaca**. Tidak menambah, mengurangi, atau mempersempit kewajiban yang mengikat di bab ini atau di bab lain.
>
> Di mana ini hidup (navigasi):
> - **Pemilik konstitusional:** integritas definisi, pengelakan, dan ketidakpatuhan bagi kerja penilaian. **Bab Dua** adalah pemilik struktur; **Bab Empat** adalah pemilik beban dan artefak ketelusuran; **Bab Lima** adalah pemilik definisi kanonik.
> - **Pemilik implementasi:** catatan jejak, proses forum, dan protokol implementasi menerapkan aturan ini dalam operasi tanpa menggantikannya.
> - **Aturan anti-relokasi:** bab ini tidak menugaskan slot jejak, perutean forum, atau penunjukan salah laku anti-konstitusi final.

</details>

<br>

Bab Tiga adalah pemilik konstitusional atas **integritas definisi, pengelakan, dan ketidakpatuhan bagi kerja penilaian**.

<br>

*Dalam bahasa sederhana: bab ini memblokir permainan kata — jika perilaku mengelak persyaratan nyata suatu definisi, itu dihitung sebagai ketidakpatuhan bahkan ketika dokumen administrasi tampak baik.*

<a id="1-definition-integrity-and-anti-evasion-constraints"></a>
### 1. Integritas Definisi dan Batasan Anti-Pengelakan
<details>
<summary><strong><span style="color: #2563eb;">Jejak rujukan</span></strong></summary>

- Hulu: Prinsip: [Bab Dua, §1 — Tujuan dan Peran](core_02_definition_structure.md#1-purpose-and-role); [Bab Dua, §2 Persyaratan Integritas Definisi](core_02_definition_structure.md#2-definition-integrity-requirement).
- Hilir: [Bab Tiga, bagian 2 — Ketidakpatuhan dari Perilaku Sistem yang Dapat Diamati](#2-non-compliance-from-observable-system-behavior); [Bab Empat, bagian 2 — Persyaratan Ketelusuran Definisi](core_04_burden_traceability_verification.md#2-definition-traceability-requirement); [Bab Empat, bagian 5 — Standar Bukti Kepatuhan](core_04_burden_traceability_verification.md#5-compliance-evidence-standard); [Bab Delapan — Model Kontribusi, Pelanggaran, dan Jejak](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model).
- Baca bersama: [Bab Satu, bagian 4.2 — Kebenaran (Batasan Integritas Epistemik)](core_01_a_values_principles.md#32-truth-epistemic-integrity-constraint) — tafsir berdasarkan perilaku yang dapat diamati daripada struktur atau maksud yang dinyatakan mengoperasionalkan batasan kebenaran konstitusional pada lapisan integritas-definisi.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Indeks Bab Tiga (non-operatif): tautan alfabetis ke tajuk dalam bab</span></strong></summary>

[Batasan Integritas Cakupan Lintas-Komponen](#23-cross-component-scope-integrity-constraint)

[Batasan Integritas Interaksi Lintas-Sistem](#24-cross-system-interaction-integrity-constraint)

[Integritas Definisi dan Batasan Anti-Pengelakan](#1-definition-integrity-and-anti-evasion-constraints)

[Profil Temuan Ketidakpatuhan](#3-non-compliance-finding-profiles)

[Batasan Operasional](#34-operational-constraints)

[Akibat Jejak bagi Sistem yang Sudah Disertifikasi](#31-standing-effects-for-already-certified-systems)

[Akibat Jejak pada Sertifikasi Pertama](#32-standing-effects-at-first-certification)

[Akibat Jejak bagi Makhluk Sadar dan Lembaga](#33-standing-effects-for-sentients-and-institutions)

[Ketidakpatuhan dari Perilaku Sistem yang Dapat Diamati](#2-non-compliance-from-observable-system-behavior)

[Pola Pengelakan Umum](#21-common-evasion-patterns)

[Pengelakan Reduktif](#22-reductive-evasion)

[Batasan Integritas Temporal dan Kontinuitas](#25-temporal-integrity-and-continuity-constraint)

[Batasan Integritas Ketidakpastian dan Non-Eksploitasi](#26-uncertainty-integrity-and-non-exploitation-constraint)

</details>

<br>

Bagian ini mengatur bagaimana definisi harus ditafsirkan dan diterapkan dalam praktik.

- Definisi harus ditafsirkan dan diterapkan berdasarkan perilaku sistem dan hasil yang dapat diamati di bawah kondisi sistem fungsional penuh.
- Tafsir, penyusunan, dan perilaku sistem yang meruntuhkan cakupan semantik, penilaian, dan kepatuhan penuh definisi — yang sesuai dengan komponen Ontologis (O), Penilaian (A), dan Kepatuhan (C) mereka — dilarang; [**Bagian 2**](#2-non-compliance-from-observable-system-behavior) bab ini merinci ketidakpatuhan dari perilaku yang dapat diamati dan pengelakan.
- Kesetaraan fungsional mengalahkan penamaan, struktur, dekomposisi, representasi, atau maksud yang dinyatakan; hasil yang dihasilkan suatu sistem mengatur bagaimana ia diklasifikasi dan dievaluasi.

Bagian ini tidak mendefinisikan standar evaluasi, kecukupan bukti, atau beban pembuktian, yang diatur secara eksklusif oleh **Bab Dua, bagian 1** dan **Bab Empat, bagian 1 dan 4**.

<a id="2-non-compliance-from-observable-system-behavior"></a>
### 2. Ketidakpatuhan dari Perilaku Sistem yang Dapat Diamati
<details>
<summary><strong><span style="color: #2563eb;">Jejak rujukan</span></strong></summary>

- Hulu: Prinsip: [Bab Tiga, bagian 1 — Integritas Definisi dan Batasan Anti-Pengelakan](#1-definition-integrity-and-anti-evasion-constraints); [Bab Dua, §2 Persyaratan Integritas Definisi](core_02_definition_structure.md#2-definition-integrity-requirement); [Bab Dua, §2.2 Ketidakpatuhan karena Pelemahan Struktural atau Terapan](core_02_definition_structure.md#22-non-compliance-by-structural-or-applied-weakening).
- Hilir: katalog jenis di bagian [2.1](#21-common-evasion-patterns) sampai [2.6](#26-uncertainty-integrity-and-non-exploitation-constraint); [3. Profil Temuan Ketidakpatuhan](#3-non-compliance-finding-profiles); [Bab Empat, bagian 5 — Standar Bukti Kepatuhan](core_04_burden_traceability_verification.md#5-compliance-evidence-standard); [Bab Empat, bagian 3 — Persyaratan Observabilitas Ketelusuran](core_04_burden_traceability_verification.md#3-observability-of-traceability-requirement); [Bab Tujuh §16](../../core_08_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion) (*penunjuk pembukaan ulang sertifikasi keselarasan sistem dan anti-pengelakan*); [Bab Delapan — Model Kontribusi, Pelanggaran, dan Jejak](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model).
- Baca bersama: [Bab Dua, §1 — Tujuan dan Peran](core_02_definition_structure.md#1-purpose-and-role) bagi aturan pemenuhan-bersama di bawah kondisi sistem fungsional penuh; [Bab Dua, §2.4 Aturan Tafsir di bawah Ambiguitas](core_02_definition_structure.md#24-interpretation-rule-under-ambiguity) — tafsir yang melemahkan pagar pengaman, menyusutkan apa yang harus dinilai, atau memperburuk hasil dunia nyata tidak sah; [Bab Empat, bagian 5 — Standar Bukti Kepatuhan](core_04_burden_traceability_verification.md#5-compliance-evidence-standard) — bukti harus menunjukkan kepatuhan di bawah aturan di bagian ini; bukti yang akan tidak patuh di sini gagal beban pembuktian; [Ketidakpatuhan](../../core_05_band_integrative.md#non-compliance).

</details>

<br>

*Dalam bahasa sederhana: suatu sistem tidak patuh ketika apa yang benar-benar dilakukannya atau dihasilkannya akan mematahkan suatu definisi — dinilai di bawah kondisi fungsional penuh, bukan hanya di kertas. Pengelakan berarti melemahkan suatu definisi ketika ia benar-benar diterapkan. Itu adalah ketidakpatuhan di bawah Bab Dua §2.2 — terlepas dari maksud, kesadaran, atau tujuan yang diklaim.*

Bagian ini mendefinisikan kapan sistem tidak patuh berdasarkan perilaku dan hasil yang dapat diamati, termasuk:

- di mana perilaku atau cakupan yang dinyatakan menyimpang dari efek nyata
- pengelakan lintas waktu, skala, interaksi sistem, dan kondisi operasi di mana itu penting

Suatu sistem tidak patuh di mana hal yang dapat diamati itu akan melanggar suatu definisi di bawah penerapan penuh komponen Ontologis (O), Penilaian (A), dan Kepatuhan (C)-nya, terlepas dari struktur, tafsir, atau implementasi yang dinyatakan.

**Cara menilai.** Sistem tidak patuh di mana:

- klaim yang dinyatakan bertabrakan dengan apa yang benar-benar dapat dilihat:
  - perilaku sistem, representasi, atau artefak audit yang dinyatakan bertabrakan dengan hasil yang dapat diamati; dalam hal itu, hasil yang dapat diamati yang mengatur
  - cakupan sistem yang dinyatakan bertabrakan dengan efek fungsional nyata; dalam hal itu, definisi harus diterapkan berdasarkan perilaku dan efek sistem nyata
- suatu definisi tidak dipenuhi secara penuh di bawah kondisi sistem fungsional penuh:
  - cakupan semantik, pengukuran, penilaian, dan kepatuhan bersama (O, M, A, dan C)
  - termasuk lintas waktu, skala, sistem terhubung, dan kondisi operasi di mana itu penting
- suatu definisi dipenuhi hanya di kertas sementara cakupan penuh itu tidak dipenuhi:
  - hanya dalam bentuk, representasi, struktur, proses, atau kondisi terbatas
  - hasil yang tidak konsisten dengan cakupan pelindung, penilaian, atau kepatuhan penuh suatu definisi
  - komponen definisi dipenuhi hanya di bawah kondisi terbatas, tidak representatif, atau disusun secara selektif
  - tafsir yang menjaga kepatuhan formal sambil mendegradasi hasil dunia nyata

Subbagian jenis di bawah mendaftar pola umum. Mereka tidak menggantikan aturan penilaian di atas.

<a id="21-common-evasion-patterns"></a>
#### 2.1 Pola Pengelakan Umum

*Dalam bahasa sederhana: ini cara-cara umum suatu sistem dapat tampak patuh tanpa benar-benar memenuhi definisi — ukuran yang ditukar, dokumen administrasi palsu, cakupan yang dipotong, atau insentif yang mendorong semua orang menjauh dari kepatuhan. Daftar ini tidak tertutup. Jenis dapat terjadi bersama. Menyusutkan apa yang dimaksud definisi dicakup di [§2.2](#22-reductive-evasion).*

Bentuk pengelakan berikut dilarang:

- **Ukuran palsu dan dokumen administrasi** — mengklaim kepatuhan lewat apa yang diukur, dilaporkan, atau dicatat daripada lewat hasil yang dituntut definisi:
  - mengganti dengan ukuran, indikator, atau deskripsi yang menyimpang dari perihal definisi, sambil tetap mengklaim lulus
  - mengoptimalkan suatu skor atau ukuran dengan cara yang membuat hasil dunia nyata yang dituntut definisi menjadi lebih buruk
  - menyajikan catatan, artefak, atau bukti yang secara material salah menyatakan apa yang benar-benar dilakukan sistem atau apakah ia patuh
  - memenuhi persyaratan dalam nama, struktur, atau proses tanpa menghasilkan efek dunia nyata yang dituntut definisi (lihat juga [§2.1.1](#211-formal-label-and-representation-gaming))
- **Trik cakupan dan batas** — mengatur apa yang dihitung, dan kapan, sehingga bagian sulit tidak pernah diuji:
  - mempersempit evaluasi atau penerapan untuk meninggalkan unsur sistem, efek, atau kondisi yang penting
  - memecah tanggung jawab lintas komponen, pelaku, atau waktu sehingga tidak seorang pun harus memenuhi definisi bagi seluruh sistem
  - tampak patuh hanya di bawah observasi, audit, atau jendela terbatas sambil mematahkan definisi dalam operasi yang lebih luas
- **Jebakan insentif** — membangun imbalan, tekanan, atau dinamika yang secara sistematis mendorong sistem menjauh dari kepatuhan:
  - menciptakan kondisi di bawah mana insentif, dinamika, atau keseimbangan meruntuhkan kepatuhan sebagai hal yang biasa


<a id="211-formal-label-and-representation-gaming"></a>
##### 2.1.1 Permainan Label Formal dan Representasi

*Dalam bahasa sederhana: suatu label, klasifikasi, atau tinjauan cap karet tidak dihitung jika keputusan, pelindungan, atau kewajiban nyata tidak pernah benar-benar terjadi ketika itu penting.*

Ini adalah bentuk terfokus dari **Ukuran palsu dan dokumen administrasi**. Sistem tidak boleh memenuhi definisi konstitusional lewat label, klasifikasi formal, prosedur nominal, atau representasi semata ketika efek nyata, tempo operasi, atau hasil fungsional yang dituntut definisi hilang. Pola yang dilarang mencakup, tanpa batasan:

- persetujuan human-in-the-loop atau human-on-the-loop (manusia di dalam lingkar keputusan, atau manusia yang mengawasi lingkar itu) yang ada hanya dalam nama — tanpa kuasa keputusan nyata pada kecepatan sistem benar-benar berjalan
- tinjauan cap karet, musyawarah semu, atau klasifikasi catatan-kertas yang dipakai sebagai ganti beban atau adjudikasi yang dituntut
- penggantian nama formal, restrukturisasi, atau reklasifikasi entitas yang melepas kewajiban tanpa memindahkan tanggung jawab dalam praktik
- pilihan taksonomi yang nyaman yang menghapus pembedaan yang dituntut definisi

Di mana perubahan struktur-formal bersifat material, terapkan [Bab Satu §11.6 Tanggung Jawab Penerus dan Non-Pelarian Struktur-Formal](core_01_c_stewardship_capacity_principles.md#116-successor-responsibility-and-formal-structure-non-escape).

<a id="22-reductive-evasion"></a>
#### 2.2 Pengelakan Reduktif

Reduksi terjadi di mana penerapan suatu definisi menghasilkan hasil yang tidak memenuhi ekspresi penuh komponen Ontologis (O), Penilaian (A), dan Kepatuhan (C)-nya. Suatu sistem tidak patuh di mana tafsir atau penerapannya atas suatu definisi mereduksi cakupan semantik, ketegasan penilaian, atau persyaratan kepatuhan definisi, menghasilkan pelindungan atau hasil yang secara material lebih lemah daripada yang dituntut definisi penuh.

Bentuk reduksi berikut dilarang:
- Reduksi semantik: memperlakukan suatu definisi sebagai deskriptif sambil menghapus daya normatif atau penilaian
- Reduksi prosedural: memperlakukan pelaksanaan proses sebagai cukup terlepas dari hasil dunia nyata
- Reduksi formal: memperlakukan dokumentasi, struktur, atau representasi sebagai cukup tanpa efek fungsional
- Reduksi cakupan: mengecualikan kondisi, unsur sistem, atau efek yang relevan secara material
- Reduksi penilaian: melemahkan kondisi evaluasi yang dituntut dalam praktik lewat penerapan selektif
- Reduksi hasil: menggantikan hasil dunia nyata yang dituntut dengan hasil pengganti, parsial, atau antara

<a id="23-cross-component-scope-integrity-constraint"></a>
#### 2.3 Batasan Integritas Cakupan Lintas-Komponen
Semua komponen definisi (Ontologis (O), Pengukuran (M), Penilaian (A), dan Kepatuhan (C)) harus diterapkan pada cakupan sistem fungsional, kondisi evaluasi, dan bingkai temporal yang sama. Semua komponen harus dipenuhi bersama di bawah cakupan, kondisi, dan konteks temporal yang konsisten.

Ketidakselarasan lintas komponen adalah pengelakan sekaligus ketidakpatuhan, termasuk:
- menerapkan komponen Ontologis pada cakupan sistem yang lebih luas atau berbeda daripada komponen Kepatuhan
- menerapkan komponen Pengukuran pada cakupan, kondisi, atau kerangka waktu yang berbeda daripada komponen Ontologis, Penilaian, atau Kepatuhan yang mereka dukung
- memenuhi komponen Penilaian di bawah kondisi terbatas atau diidealkan sambil menyatakan kepatuhan di bawah operasi penuh
- menunjukkan pemenuhan komponen lintas kerangka waktu, instans, atau keadaan sistem yang berbeda

<a id="24-cross-system-interaction-integrity-constraint"></a>
#### 2.4 Batasan Integritas Interaksi Lintas-Sistem
Sistem harus dinilai sebagai bagian dari sistem fungsional yang lebih luas tempat mereka beroperasi. Penilaian itu mencakup ketergantungan hulu, efek hilir, dan jalur interaksi di mana relevan secara material. Definisi harus diterapkan lintas sistem yang berinteraksi di mana interaksi semacam itu secara material memengaruhi hasil yang diatur definisi.

Suatu sistem tidak patuh di mana:
- perilakunya, dalam kombinasi dengan sistem lain, menghasilkan hasil yang melanggar suatu definisi
- ia mengeksternalisasi efek ke sistem, populasi, atau lingkungan lain untuk menjaga kepatuhan lokal
- batas sistem dipakai untuk mengecualikan efek interaksi yang relevan secara material

<a id="25-temporal-integrity-and-continuity-constraint"></a>
#### 2.5 Batasan Integritas Temporal dan Kontinuitas
Semua komponen harus dipenuhi secara berkelanjutan di bawah kondisi sistem fungsional penuh sepanjang daur hidup sistem.

Kepatuhan harus dijaga lintas waktu, termasuk pembaruan sistem, perubahan versi, pelatihan ulang, rekonfigurasi, dan pergeseran konteks pengerahan.

Suatu sistem tidak patuh di mana:
- kepatuhan ditunjukkan hanya pada suatu titik waktu atau di bawah observasi terbatas
- perubahan sistem mendegradasi atau membatalkan komponen definisi yang sebelumnya dipenuhi
- kepatuhan terpecah lintas tahap daur hidup sehingga tidak ada tahap yang memenuhi semua komponen di bawah kondisi penuh

<a id="26-uncertainty-integrity-and-non-exploitation-constraint"></a>
#### 2.6 Batasan Integritas Ketidakpastian dan Non-Eksploitasi
Di mana ketidakpastian ada, definisi harus diterapkan dengan cara yang menjaga cakupan semantik, penilaian, dan kepatuhan penuhnya. Penerapan harus terjadi di bawah kondisi sepadan dengan potensi bahaya, ketergantungan, dan risiko. Ketidakpastian tidak boleh dipakai untuk melemahkan, menunda, atau menghindari penerapan definisi.

Suatu sistem tidak patuh di mana ia:
- mengemukakan ketidakpastian untuk menunda atau menghindari evaluasi atau penentuan kepatuhan
- menerapkan ketidakpastian secara asimetris untuk menguntungkan klaim kepatuhan
- memperkuat ambiguitas untuk melemahkan ketegasan atau hasil yang dituntut
- menuntut kepastian yang tidak dapat dicapai untuk mengakui ketidakpatuhan

Di mana ketidakpastian mencegah demonstrasi kepatuhan yang definitif bagi komponen definisi yang relevan secara material, sistem harus memenuhi beban kehati-hatian yang sepadan dengan potensi bahaya. Gagal melakukan itu adalah ketidakpatuhan di bawah bagian ini dan gagal beban pembuktian di bawah [Bab Empat, bagian 5 — Standar Bukti Kepatuhan](core_04_burden_traceability_verification.md#5-compliance-evidence-standard).

<a id="3-non-compliance-finding-profiles"></a>
### 3. Profil Temuan Ketidakpatuhan
<details>
<summary><strong><span style="color: #2563eb;">Jejak rujukan</span></strong></summary>

- Hulu: [Bab Tiga, bagian 2 — Ketidakpatuhan dari Perilaku Sistem yang Dapat Diamati](#2-non-compliance-from-observable-system-behavior); [Bab Dua, §2 Persyaratan Integritas Definisi](core_02_definition_structure.md#2-definition-integrity-requirement).
- Hilir: [Bab Empat, bagian 2 — Persyaratan Ketelusuran Definisi](core_04_burden_traceability_verification.md#2-definition-traceability-requirement); [Bab Tujuh — Sertifikasi Keselarasan Sistem](../../core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification); [Bab Delapan — Model Kontribusi, Pelanggaran, dan Jejak](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model); [Bab Sembilan — Akibat Jejak dan Integrasi](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration); [CJS-3.1 Kompas konstitusional dan peta klaster](../../corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md#cjs-31-constitutional-compass-and-cluster-map).
- Baca bersama: [Profil Temuan Ketidakpatuhan](../../core_05_band_accountability.md#non-compliance-finding-profile) — rumah O/M/A/C kanonik bagi ruas profil; [Tetrad Konstitusional](core_00_preamble.md#constitutional-tetrad); [Dua Tujuan Konstitusional](core_00_preamble.md#two-constitutional-aims).

</details>

<br>

*Dalam bahasa sederhana: ketika sesuatu gagal pada suatu definisi, profil temuan adalah label opsional yang mengatakan jenis masalah konstitusional apa itu — untuk perutean dan audit. Ia tidak mengubah hasil lulus/gagal. Bagi sistem yang sudah berjalan di bawah sertifikasi keselarasan, ketidakpatuhan terverifikasi harus memberi makan jejak; makhluk sadar dan lembaga ditandai hanya ketika tautan terverifikasi. Sertifikasi pertama kali adalah kasus khusus ([§3.2](#32-standing-effects-at-first-certification)).*

Temuan **ketidakpatuhan** material di bawah bab ini atau di bawah definisi **Bab Lima** yang diundang boleh membawa suatu [Profil Temuan Ketidakpatuhan](../../core_05_band_accountability.md#non-compliance-finding-profile). Profil itu hanya metadata orientasi dan perutean. Ia:

- boleh menamai kaki [Tetrad Konstitusional](core_00_preamble.md#constitutional-tetrad) dan orientasi [Dua Tujuan Konstitusional](core_00_preamble.md#two-constitutional-aims) mana yang paling menggambarkan kegagalan — misalnya Pengawasan, Partisipasi, atau Pertanggungjawaban disilangkan dengan Berkembang atau Kesinambungan
- tidak mengubah apakah definisi yang mendasari dipenuhi
- tidak menciptakan label putusan kedua
- tidak menggantikan pengukuran kontribusi atau pelanggaran [Bab Delapan](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model)

Akibat jejak bergantung pada siapa yang dinilai dan apakah sistem sudah disertifikasi. Subbagian di bawah menetapkan kasus itu.

<a id="31-standing-effects-for-already-certified-systems"></a>
#### 3.1 Akibat Jejak bagi Sistem yang Sudah Disertifikasi

Jika suatu sistem sudah berjalan di bawah suatu [sertifikasi keselarasan sistem](../../core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) — termasuk pengakuan, pengakuan bersyarat, atau revalidasi yang belum kedaluwarsa — ketidakpatuhan terverifikasi yang material pada cakupan fungsional sistem itu **harus** masuk ke pengukuran jejak [Bab Delapan](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model) bagi **sistem itu**. Hanya fakta yang lolos [gerbang masukan terverifikasi](../../core_09_standing_assessment.md#verified-inputs-for-standing) yang boleh masuk. Ukur dan terapkan jejak di bawah Bab Delapan dan Sembilan. Pembukaan ulang, pencabutan, atau konsekuensi sertifikasi lain tetap di bawah [Bab Tujuh](../../core_08_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion). Mereka tidak menggantikan catatan jejak sistem itu.

<a id="32-standing-effects-at-first-certification"></a>
#### 3.2 Akibat Jejak pada Sertifikasi Pertama

Jika sistem masih dalam [sertifikasi keselarasan sistem](../../core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) **pertamanya** dan belum diakui — termasuk di mana pengakuan ditunda atau ditolak — ketidakpatuhan terverifikasi terutama memutuskan **hasil sertifikasi** di bawah Bab Tujuh. Hasil itu boleh berupa pengakuan bersyarat, pengakuan tertunda, non-pengakuan, atau hasil sebanding. Catatan sertifikasi itu masih boleh memasok masukan jejak terverifikasi di bawah [Bab Tujuh §15](../../core_08_b_system_alignment_certification_record_process.md#15-relationship-to-standing) ketika fakta mendukungnya. Bab ini tidak menuntut catatan jejak yang sama yang harus diterima sistem berjalan yang sudah disertifikasi.

<a id="33-standing-effects-for-sentients-and-institutions"></a>
#### 3.3 Akibat Jejak bagi Makhluk Sadar dan Lembaga

Jejak suatu makhluk sadar terdampak hanya ketika tautan terverifikasi ke makhluk sadar itu ditunjukkan. Sekadar terkait dengan sistem yang tidak patuh tidak cukup. Tautan terverifikasi harus ke:

- peran kausal
- kewajiban
- wewenang
- kontrol
- keterdugaan
- manfaat
- penyembunyian
- kapasitas pencegahan yang layak

Jejak suatu lembaga terdampak ketika lembaga itu adalah subjek yang dinilai, atau ketika ia terverifikasi sebagai wahana pola ketidakpatuhan. Catatan lembaga tetap dapat ditelusuri secara terpisah dari catatan makhluk sadar individual. Terapkan kasus itu di bawah [Bab Delapan](../../core_09_standing_assessment.md#chapter-nine-compliance-violation-and-standing-model) dan [Bab Sembilan](../../core_10_standing_integration.md#chapter-ten-standing-effects-and-integration). Profil temuan membantu merute dan mengaudit. Ia sendiri tidak menetapkan hasil jejak, slot, kunci jejak, gerbang, atau pemulihan.

<a id="34-operational-constraints"></a>
#### 3.4 Batasan Operasional

Ketidakpatuhan juga boleh ditemukan terhadap batasan operasional di korpus implementasi bersama. Profil temuan bawaan dan cara mereka menempel pada temuan itu ditangani di sana — bukan di bab ini. Lihat [CJS-3.1 Kompas konstitusional dan peta klaster](../../corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md#cjs-31-constitutional-compass-and-cluster-map).

---

**Berkas sebelumnya:** [core_02_definition_structure.md](core_02_definition_structure.md)

**Berkas berikutnya (bahasa ini):** [core_04_burden_traceability_verification.md](core_04_burden_traceability_verification.md)

**Sumber mengikat:** [core_03_definition_integrity.md](../../core_03_definition_integrity.md)
