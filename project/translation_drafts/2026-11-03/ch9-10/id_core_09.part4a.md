##### 5.3.4 Integritas Peta dan Catatan

Sebelum mengandalkan peta ketergantungan dan catatan arus sumber daya, sertifikasi wajib memeriksa apakah keduanya memenuhi **Pasal V-A** (*Pemetaan Ketergantungan dan Transparansi Arus Sumber Daya*). Keduanya wajib:

- **Lengkap:** mencakup ketergantungan signifikan di hulu dan hilir, aliran sumber daya, serta hubungan yang tersembunyi atau timpang jika hal itu penting.
- **Mutakhir:** diperbarui cukup sering sesuai kecepatan perubahan dan tingkat kekritisan sistem, termasuk kelas sistemnya berdasarkan [§2 Evaluasi Kelas Sistem](#2-system-class-evaluation). Peta dan catatan menunjukkan sistem yang beroperasi saat ini, bukan saat sertifikasi terakhir.
- **Dapat diaudit:** terbuka untuk diaudit berdasarkan **Pasal XVI-A** (*Kemampuan Diaudit dan Bukti yang Dapat Diamati*).

Peta atau catatan yang gagal memenuhi salah satu pengujian ini tidak dapat mendukung temuan bahwa sistem memberi pengembalian yang cukup. Kesenjangannya wajib dicatat dan ditangani berdasarkan *Cacat dan ketidakselarasan* di bawah.

<a id="535-system-class-scaling-and-escalation"></a>
##### 5.3.5 Penskalaan dan Eskalasi Kelas Sistem

Kelas sistem menentukan kedalaman tinjauan dan ketatnya penilaian kecukupan. Kelas sistem tidak pernah membuat ekstraksi dari sumber daya bersama terlalu kecil untuk diperhitungkan; ekstraksi yang dipecah di antara badan, catatan, atau periode dinilai sebagai satu kesatuan berdasarkan [Bab Satu §15.1.1 Prinsip Anti-Segmentasi](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle). Setiap kali pemicu materialitas terpenuhi:

- Sistem yang mengambil dari fondasi bersama yang dibutuhkan makhluk sadar untuk bertahan hidup — misalnya daerah aliran sungai bersama atau tulang punggung jaringan listrik regional — wajib mencatat bukti peta ketergantungan dan aliran pengembalian yang paling kuat. Kapasitas berkelanjutan sistem bersama inilah yang dilindungi [Bab Satu §9 Kapasitas Sistem Bersama](core_01.000_values_principles.md#9-shared-system-capacity), dan **Pasal III-A** (*Kelangsungan Hidup*) menjadi alasan bukti paling kuat diperlukan di sini.
- Sistem yang bergantung pada autentikasi bersama, teknologi informasi kesehatan, atau infrastruktur sejenis wajib mendokumentasikan apa yang diambilnya dan apakah dukungannya memadai, dengan kedalaman yang sesuai dengan tingkat kekritisan operasinya. Slogan kabur tentang "interoperabilitas" tidak diperhitungkan: ketergantungan itu wajib tampak dalam peta dan catatan, sebagaimana diwajibkan [Bab Satu §18.5 Arsitektur Modular dan Disiplin Ketergantungan](core_01.010_stewardship_capacity_principles.md#185-modular-architecture-and-dependency-discipline).
- Sistem tidak boleh menghindari tinjauan lintas sistem sambil diam-diam menjadi titik hambat pembayaran, identitas, atau kepegawaian bagi institusi yang secara realistis tidak dapat beralih.
  - **Siapa yang tidak dapat beralih:** dinilai berdasarkan faktor kemudahan penggantian dalam [§5.3.3 Persyaratan Evaluasi](#533-evaluation-requirement).
  - **Mengapa ini penting:** ini adalah jenis konsentrasi yang dijelaskan [Bab Satu §11.4 Konsentrasi Sumber Daya dan Ketergantungan](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable). Bagian itu mengarahkan pengadopsi untuk menetapkan tingkat konsentrasi, misalnya berapa banyak makhluk sadar atau sistem yang bergantung pada satu penyedia tanpa alternatif nyata, atau siapa yang mengendalikan antarmuka dan titik akses ke infrastruktur bersama. Sertifikasi tidak menunggu tingkat yang ditetapkan pengadopsi terlampaui sebelum meningkatkan tinjauannya (lihat di bawah).
  - **Tindakan sertifikasi:** sertifikasi meningkatkan tinjauan dan mempertimbangkan ulang kelas sistem berdasarkan [§2.2 Bagaimana kelas sistem mengatur setiap evaluasi](#22-how-system-class-scales-every-evaluation), sampai **Kelas A** jika sistem mengendalikan akses ke koordinasi yang penting bagi kelangsungan hidup.

Peningkatan tahap tidak menunggu ambang konsentrasi berdasarkan [Bab Satu §11.4 Konsentrasi Sumber Daya dan Ketergantungan](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable). Ambang yang ditetapkan pengadopsi dan telah dilampaui sistem merupakan bukti tambahan. Ambang yang belum ditetapkan atau terlalu tinggi tidak menunda peningkatan tahap, dan melampaui ambang bukan dengan sendirinya temuan pelanggaran.

<a id="536-defects-and-misalignment"></a>
##### 5.3.6 Cacat dan Ketidakselarasan

Cacat dalam [§5](#5-rights-floor-and-domain-evaluations) (*Evaluasi Lantai Hak dan Ranah*) berlaku untuk evaluasi ini, termasuk informasi ketergantungan atau arus sumber daya yang wajib diungkapkan sistem berdasarkan **Pasal V-A** (*Pemetaan Ketergantungan dan Transparansi Arus Sumber Daya*). Selain itu, setiap hal berikut dihitung sebagai cacat sertifikasi:

- menganggap salah satu hal berikut cukup untuk memenuhi [Dukungan Lintas Sistem yang Proporsional](core_05.040_band_continuity.md#proportionate-cross-system-support):
  - transfer simbolis, tidak transparan, di luar peta, atau satu kali;
  - fakta bahwa sistem memenuhi lantai kelangsungan hidup dalam **Pasal III-A** (*Kelangsungan Hidup*); atau
  - fakta bahwa sistem tetap berada dalam batas konsentrasi pasar di [Bab Satu §11 Struktur Pasar](core_01.000_values_principles.md#11-market-structure);
- berulang kali mengambil dari fondasi bersama tanpa pengembalian yang proporsional, ketika pemicu materialitas berlaku;
- dukungan yang terutama memperkuat penguasaan atau konsentrasi; dan
- dukungan bersyarat yang menggagalkan transparansi yang diwajibkan **Pasal V-A** (*Pemetaan Ketergantungan dan Transparansi Arus Sumber Daya*).

Kesenjangan dukungan yang terdokumentasi diperhitungkan berdasarkan [Bab Satu §6 Kepercayaan dan Keterpercayaan](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity).

<a id="54-nondiscrimination-evaluation"></a>

#### 5.4 Evaluasi Nondiskriminasi

<details>
<summary><strong><span style="color: #2563eb;">Jejak</span></strong></summary>

- Hulu:
  - [Bagian C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*isi catatan*);
  - [§2](#2-system-class-evaluation) (*evaluasi kelas sistem*); keluarga pengukuran Partisipasi (*Keadilan Substantif serta Proksi Karakteristik yang Dilindungi dan Dampak yang Tidak Proporsional sebagai pengukuran konstitusional*); **Pasal VI-C** (*Nondiskriminasi*);
  - [Keadilan Substantif](core_05.055_band_participation.md#substantive-fairness),
  - [Karakteristik yang Dilindungi](core_05.055_band_participation.md#protected-characteristics),
  - [Proksi Karakteristik yang Dilindungi dan Dampak yang Tidak Proporsional](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact),
  - [Bahasa, Budaya, dan Warisan](core_05.040_band_continuity.md#language-culture-and-heritage),
  - [Keniscayaan](core_05.035_band_accountability.md#necessity), dan
  - [Proporsionalitas](core_05.035_band_accountability.md#proportionality) (Bab Lima).
- Hulu: Prinsip Bab Satu
  - [§3.1 Keadilan](core_01.000_values_principles.md#31-fairness) (terutama [§3.1.2 Manfaat dan Beban](core_01.000_values_principles.md#312-benefits-and-burdens)) dan
  - [§11.4 Konsentrasi Sumber Daya dan Ketergantungan](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*pengendalian akses; peningkatan tahap di §5.4.2*).
- Hilir:
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*Penerapan ilustratif nondiskriminasi menurut kelas sistem*);
  - [Bagian C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*integritas catatan*);
  - [Bagian C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*gerbang masukan terverifikasi*);
  - [Bagian B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*ketidakselarasan pola diskriminasi dan pengelakan melalui proksi*).
- Baca bersama: kewajiban adjudikasi dan operasi **Pasal VI-C** (*Nondiskriminasi*) jika sertifikasi menjadi gerbang bagi akses forum, administrasi, atau penegakan; [*Status Nondiskriminasi, Karakteristik yang Dilindungi, Martabat, Pengendalian Sinyal Intim, dan **Pasal VII-E** (*Layanan seksual komersial dengan persetujuan orang dewasa dan eksploitasi seksual*)*](core_05.055_band_participation.md#fairness-protected-characteristics-and-nondiscrimination).
- Subbagian:
  - [§5.4.1](#541-evaluation-requirement) (*persyaratan evaluasi*);
  - [§5.4.2](#542-system-class-scaling-and-escalation) (*penskalaan dan eskalasi kelas sistem*);
  - [§5.4.3](#543-defects-and-misalignment) (*cacat dan ketidakselarasan*);
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*Penerapan ilustratif nondiskriminasi menurut kelas sistem*).

</details>

<br>

*Dalam bahasa sederhana: beberapa sistem menentukan siapa yang diterima. Beberapa menentukan siapa yang membayar lebih mahal. Beberapa menentukan siapa yang mendapat peringkat lebih rendah atau menanggung beban lebih berat. Jika sistem membuat keputusan seperti ini dengan dampak berarti, sertifikasi mengajukan satu pertanyaan: apakah bahaya terutama menimpa makhluk sadar dengan karakteristik yang dilindungi, atau sifat yang menjadi proksi karakteristik itu? Pernyataan operator bahwa aturannya netral tidak menjawab pertanyaan tersebut. Contoh terapan: [CS-9.320 §9 Penerapan ilustratif nondiskriminasi menurut kelas sistem](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class).*

Bagian ini berlaku jika sistem yang berdampak material secara material mengklasifikasikan, memeringkat, menetapkan harga, menjadi gerbang, mengecualikan, atau mengalokasikan beban dan manfaat di antara makhluk sadar — termasuk melalui aturan kelayakan, fitur model, logika pemeringkatan, kebijakan platform, atau jalur keputusan sebanding.

Sertifikasi keselarasan sistem wajib mengevaluasi **nondiskriminasi** berdasarkan **Pasal VI-C** (*Nondiskriminasi*), [Keadilan Substantif](core_05.055_band_participation.md#substantive-fairness), dan [Proksi Karakteristik yang Dilindungi dan Dampak yang Tidak Proporsional](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact) jika pemicu materialitas berlaku.

<a id="541-evaluation-requirement"></a>
##### 5.4.1 Persyaratan Evaluasi

*Dalam bahasa sederhana: bab ini tidak menetapkan kuota inklusi. Bab ini tidak memilih rumus keadilan. Dokumen lain mungkin mengaturnya, demikian pula tambahan korpus pada masa mendatang atau dokumen yang dibuat pengadopsi. Sertifikasi hanya memeriksa apakah seseorang benar-benar menilai siapa yang menerima manfaat, siapa yang menanggung beban, dan apakah proksi untuk sifat yang dilindungi digunakan. Evaluasi itu berlaku setiap kali pemicunya berlaku.*

Proses sertifikasi wajib menentukan apakah jalur keputusan yang secara material diandalkan sistem membebankan beban, pengecualian, atau bahaya material kepada makhluk sadar berdasarkan salah satu dari hal berikut:

- [Karakteristik yang Dilindungi](core_05.055_band_participation.md#protected-characteristics);
- proksinya; atau
- pengelompokan sewenang-wenang yang digunakan sebagai pengganti fungsional, termasuk spesialisasi bahasa, budaya, dan warisan berdasarkan [Bahasa, Budaya, dan Warisan](core_05.040_band_continuity.md#language-culture-and-heritage).

Evaluasi, yang diskalakan menurut [taruhan material](core_00.000_preamble.md#material-stake), wajib:

- menguji pola beban dan manfaat berdasarkan [Keadilan Substantif](core_05.055_band_participation.md#substantive-fairness); dan
- menguji risiko proksi atau dampak yang tidak proporsional berdasarkan [Proksi Karakteristik yang Dilindungi dan Dampak yang Tidak Proporsional](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact).

Perlakuan berbeda hanya dapat diterima jika dibenarkan oleh [Keniscayaan](core_05.035_band_accountability.md#necessity), [Proporsionalitas](core_05.035_band_accountability.md#proportionality), dan keadilan substantif yang terdokumentasi. Evaluasi wajib mencerminkan dampak fungsional, bukan netralitas nominal, niat yang dinyatakan, atau label saja.

<a id="542-system-class-scaling-and-escalation"></a>
##### 5.4.2 Penskalaan dan Eskalasi Kelas Sistem

Kelas sistem menentukan kedalaman evaluasi. Kelas itu tidak membolehkan siapa pun menganggap pemeringkatan atau pengalihan beban sebagai hal yang tidak material. Setiap kali pemicu materialitas terpenuhi, hal-hal berikut berlaku:

- **Sistem yang aturan penghentian, pemberitahuan, atau aturan sebandingnya dapat menutup akses ke kebutuhan pokok kelangsungan hidup:**
  - catatan wajib memuat analisis beban-manfaat dan proksi yang paling kuat, bukan pernyataan umum tentang praktik terbaik; dan
  - pengalihan biaya tersembunyi tidak memenuhi [Bab Satu §3.1.2 Manfaat dan Beban](core_01.000_values_principles.md#312-benefits-and-burdens).
- **Sistem yang logika pencocokan atau peruteannya memengaruhi layanan darurat, tunjangan, atau akses kredensial:**
  - catatan wajib mendokumentasikan temuan dampak yang tidak proporsional dan keadilan substantif pada tingkat kekritisan operasional; dan
  - alasannya adalah bahwa keadilan menurut [Bab Satu §3.1 Keadilan](core_01.000_values_principles.md#31-fairness) berarti makhluk sadar tidak diperlakukan berdasarkan aturan tanpa penjelasan atau dibiarkan menanggung biaya yang dihindari pihak lain.
- **Sistem yang logika giliran kerja, vendor, atau pemesanannya secara material memeringkat atau mengecualikan peserta:**
  - sistem tidak boleh mengganti analisis nyata dengan paragraf keadilan sekadarnya;
  - ketika koordinasi menjadi penting bagi kelangsungan hidup, sertifikasi wajib meningkatkan tinjauan dan reklasifikasi berdasarkan [§2.2 Bagaimana kelas sistem mengatur setiap evaluasi](#22-how-system-class-scales-every-evaluation), termasuk reklasifikasi ke **Kelas A** jika sistem menjadi gerbang bagi kepegawaian atau perutean darurat; dan
  - pengendalian akses semacam itu merupakan indikator konsentrasi berdasarkan [Bab Satu §11.4 Konsentrasi Sumber Daya dan Ketergantungan](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable), karena banyak makhluk sadar atau sistem bergantung pada satu penyedia tanpa alternatif nyata; karena itu sertifikasi meningkatkan tinjauan di sini.

<a id="543-defects-and-misalignment"></a>
##### 5.4.3 Cacat dan Ketidakselarasan

Dua kelompok cacat berlaku pada evaluasi ini:

- **Cacat yang berlaku di seluruh bagian:**
  - cacat dalam [§5](#5-rights-floor-and-domain-evaluations) (*Evaluasi Lantai Hak dan Ranah*) berlaku bagi evaluasi ini; dan
  - cacat tersebut berlaku untuk logika klasifikasi, pemeringkatan, atau alokasi beban material jika **Pasal VI-C** (*Nondiskriminasi*) mewajibkan peninjauan.
- **Cacat nondiskriminasi:** setiap hal berikut juga wajib diperlakukan sebagai cacat sertifikasi:
  - menganggap netralitas pada tampilan, metrik kemudahan agregat, atau laporan mandiri operator sudah cukup tanpa analisis beban-manfaat yang dapat dievaluasi; dan
  - menggunakan pembingkaian homogenisasi, interoperabilitas, atau efisiensi untuk mengalahkan perlindungan bahasa, budaya, atau warisan tanpa memenuhi pengujian **Keniscayaan** dan **Proporsionalitas** dalam **Pasal VI-C** (*Nondiskriminasi*).

Diskriminasi melalui proksi atau ketidakadilan substantif yang terdokumentasi diperhitungkan berdasarkan [Bab Satu §6 Kepercayaan dan Keterpercayaan](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity).

<a id="55-accessibility-evaluation"></a>
