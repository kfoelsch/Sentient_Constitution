<!-- Locale: id | Source: origin/main current working copy | AI-drafted, unreviewed | Terjemahan lengkap §9.3 saat ini; sumber Inggris mengendalikan. -->

<a id="93-provisional-and-full-certification"></a>
#### 9.3 Sertifikasi Sementara dan Penuh

*Secara sederhana: sistem memperoleh kepercayaan secara bertahap. Sistem baru dan sistem yang gagal dalam evaluasi memulai dengan masa sertifikasi sementara yang singkat dan diperiksa lebih sering. Hanya sistem yang kini tidak memiliki masalah dan tidak menunjukkan tanda masalah yang akan datang yang beralih ke sertifikasi penuh dengan interval lebih panjang. Kegagalan evaluasi mengembalikannya ke masa sementara.*

<a id="931-the-two-statuses"></a>
##### 9.3.1 Dua status

Sertifikasi memiliki salah satu dari dua status. Masing-masing memiliki interval sertifikasi sendiri, yang dicantumkan dalam Catatan Sertifikasi Sistem berdasarkan [§8.1 Isi minimum catatan](#81-minimum-record-contents):

- **[Sertifikasi sementara](core_05.040_band_continuity.md#provisional-certification)** adalah status:
  - sertifikasi pertama suatu sistem, termasuk sistem yang baru diterapkan; dan
  - sistem yang disertifikasi setelah sertifikasi ulang gagal, atau setelah tinjauan yang dibuka kembali atau tinjauan baru menemukan ketidakselarasan.

  Interval sertifikasi sementara lebih singkat daripada interval penuh untuk kelas sistem yang sama. Batas ketergantungan dicantumkan dalam Catatan Sertifikasi Sistem.
- **[Sertifikasi penuh](core_05.040_band_continuity.md#full-certification)** hanya dapat diperoleh pada sertifikasi ulang sistem yang berstatus sementara, dan hanya jika ketiga hal berikut terpenuhi:
  1. sistem menyelesaikan jumlah sertifikasi ulang sementara bersih yang diwajibkan secara berurutan: sekurang-kurangnya satu, dan lebih banyak untuk kelas sistem yang lebih tinggi sebagaimana ditetapkan dokumen yang diadopsi;
  2. tidak ada ketidakselarasan saat ini: Catatan Sertifikasi Sistem tidak menunjukkan ketidakselarasan terbuka, cacat yang belum dipulihkan, pemeriksaan yang terlambat, atau pengujian regresi yang gagal; dan
  3. tidak ada indikator pemantauan yang menunjukkan ketidakselarasan akan segera terjadi: pemicu pemantauan dan ukuran tren dalam Catatan tidak menunjukkan ambang terlampaui ataupun tren menuju ambang.

Sertifikasi penuh menggunakan interval yang disesuaikan dengan kelas sistem. Statusnya tetap berbatas waktu, bukan persetujuan permanen.

Sertifikasi ulang disebut **bersih** jika memenuhi persyaratan 2 dan 3.

<details><summary><strong>Panduan pembaca (non-operatif): status sertifikasi</strong></summary>

> Tabel ini merangkum §9.3. Jika berbeda, teks utama yang berlaku.
>
> | | Sertifikasi sementara | Sertifikasi penuh |
> |---|---|---|
> | **Pemegangnya** | Sertifikasi pertama, termasuk sistem baru; atau sistem yang disertifikasi setelah gagal atau tinjauan dibuka kembali/baru menemukan ketidakselarasan | Sistem yang memperolehnya saat sertifikasi ulang dalam status sementara |
> | **Cara memperolehnya** | Diberikan bersama hasil sertifikasi | Jumlah sertifikasi ulang sementara bersih berurutan yang diwajibkan (sekurang-kurangnya satu), tanpa ketidakselarasan kini dan tanpa indikator ketidakselarasan mendatang |
> | **Interval** | Interval sementara, lebih singkat daripada interval penuh untuk kelas yang sama | Interval sesuai kelas sistem; tetap berbatas waktu |
> | **Jika sertifikasi ulang gagal** | Konsekuensi Bagian B §7 berlaku; sertifikasi berikutnya sementara dan hitungan bersih kembali ke nol | Konsekuensi Bagian B §7 berlaku; sertifikasi berikutnya sementara dan hitungan bersih kembali ke nol |
> | **Jika indikator ketidakselarasan mendatang muncul** | Tetap sementara; hitungan tidak bertambah | Turun ke status sementara |

</details>

<a id="932-failure-and-step-down"></a>
##### 9.3.2 Kegagalan dan penurunan status

Hasil sertifikasi ulang, tinjauan yang dibuka kembali, atau tinjauan baru menentukan dampaknya terhadap status sistem:

- Sertifikasi ulang yang menemukan ketidakselarasan saat ini adalah sertifikasi ulang yang **gagal**. Konsekuensi dalam [Bagian B §7 Hasil Sertifikasi](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) berlaku. Sertifikasi berikutnya yang dapat diperoleh hanya sementara, sebersih apa pun pemeriksaan berikutnya; hitungan sertifikasi ulang bersih dimulai lagi dari nol.
- Jika tidak ditemukan ketidakselarasan saat ini tetapi terdapat indikator ketidakselarasan yang akan datang, sertifikasi ulang tidak gagal dan juga tidak bersih. Sistem sementara tetap sementara dan hitungannya tidak maju; sistem penuh turun menjadi sementara.
- Tinjauan yang dibuka kembali berdasarkan [§9 Sertifikasi Ulang dan Pembukaan Kembali](#9-recertification-and-reopening) dan menemukan ketidakselarasan memiliki dampak yang sama dengan sertifikasi ulang gagal.
- Tinjauan baru atas sistem bersertifikasi yang menemukan ketidakselarasan saat ini juga berdampak sama. Jika sistem tidak memiliki status sertifikasi, aturan penolakan dalam [Bagian B §7.4 Penolakan dan Pencabutan](core_09.005_system_alignment_certification_record_process.md#74-denial-and-revocation) berlaku.

<a id="933-cause-of-misalignment"></a>
##### 9.3.3 Penyebab ketidakselarasan

Jika evaluasi, sertifikasi ulang, tinjauan yang dibuka kembali, atau tinjauan baru menemukan ketidakselarasan, Catatan Sertifikasi Sistem menyatakan salah satu penyebab berikut:

- **disebabkan desain:** sistem atau prosesnya dibangun sehingga menghasilkan keluaran tidak selaras walaupun dijalankan sebagaimana mestinya;
- **disebabkan operasi:** desain tampak baik, tetapi cara sistem dioperasikan, diberi masukan, atau dipelihara membuat hasilnya tidak selaras; atau
- **belum ditentukan:** pemulihan desain dan operasi sama-sama tetap terbuka sampai forum menentukan penyebabnya.

Penetapan penyebab dibatasi sebagai berikut:

- Jika sistem terus menghasilkan keluaran tidak selaras, sistem itu tidak selaras sekalipun desainnya tampak baik di atas kertas. Desain yang tampak baik bukan pembelaan.
- Desain yang akan menghasilkan keluaran tidak selaras merupakan ketidakselarasan sebelum keluaran itu muncul.
- Penetapan penyebab menentukan pemulihan yang dicari dan cakupan tinjauan yang dibuka kembali. Penetapan itu tidak pernah menentukan apakah sistem tidak selaras.

Jika penyebabnya desain:

- hitungan sertifikasi ulang bersih tetap nol sampai desain ulang diterapkan dan diverifikasi;
- forum yang menetapkan penyebab, atau forum berikutnya yang ditugaskan menurut [Bagian B §6.2 Urutan Supervisi](core_09.005_system_alignment_certification_record_process.md#62-supervisory-sequence), memverifikasi desain ulang dalam [sasaran penerimaan yang sesuai](core_05.040_band_continuity.md#tier-window), dan dapat melakukannya pada sertifikasi ulang sementara pertama;
- **evaluasi komponen** sebelum desain ulang diverifikasi (bagian satu komponen dalam suatu putaran sertifikasi, sebagaimana didefinisikan [Bagian B §6.1 Supervisi Forum dan Peran Komponen](core_09.005_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles)) tidak dihitung sebagai hasil bersih, sebersih apa pun hasilnya; dan
- perubahan cara sistem dioperasikan tidak memenuhi langkah ini.

Ketentuan ini melengkapi, bukan mengganti, aturan penurunan status di atas. Operator atau sentient terdampak dapat meminta forum meninjau penetapan penyebab. Jika penyebab diubah, aturan ini tidak lagi berlaku.

<a id="934-tier-windows"></a>
##### 9.3.4 Jangka waktu tingkat

Jika evaluasi awal, sertifikasi ulang, tinjauan yang dibuka kembali, atau tinjauan baru menemukan ketidakselarasan:

- perkara diklasifikasikan menurut tingkat materialitas dalam [Bab Lima Belas §6 Penyelesaian tepat waktu, tingkat materialitas, dan disiplin anti-penundaan](core_15.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline);
- perkara secara presumtif ditempatkan pada tingkat yang sesuai dengan kelas sistemnya (misalnya sistem Kelas A yang tidak selaras secara presumtif berada pada Tingkat A);
- penerimaan, pengamanan bukti, perlindungan sementara, dan putusan mengikuti jangka waktu dan batas luar tingkat tersebut; dan
- keterlambatan ditinjau sebagaimana diwajibkan bagian itu.

<a id="935-class-a-reliance"></a>
##### 9.3.5 Ketergantungan Kelas A

Dibanding sertifikasi penuh, sertifikasi sementara memiliki interval lebih singkat sehingga sertifikasi ulang lebih cepat ([§9.3.1 Dua status](#931-the-two-statuses)); batas ketergantungan dicantumkan dalam Catatan Sertifikasi Sistem ([§8.1 Isi minimum catatan](#81-minimum-record-contents)). Jika penghentian sistem akan memutus kebutuhan esensial untuk bertahan hidup sebelum pengganti tersedia:

- sertifikasi sementara saja tidak mewajibkan penghentian sistem tersebut;
- perlindungan sementara dan syarat sertifikasi dalam [Bagian B §7 Hasil Sertifikasi](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) menangani keadaan itu;
- aturan yang sama berlaku selama hitungan ditahan setelah temuan ketidakselarasan desain: penahanan hitungan tidak pernah dengan sendirinya menghentikan sistem yang diandalkan sentient; dan
- selama penahanan berlangsung, forum menetapkan perlindungan sementara, syarat sertifikasi atas ketergantungan, dan pemberitahuan kepada pihak yang bergantung.

<a id="936-verification-not-assertion"></a>
##### 9.3.6 Verifikasi, bukan pernyataan

Status sistem, hitungan sertifikasi ulang bersih, dan indikator pemantauan harus diverifikasi, dan verifikasi terbuka untuk tinjauan independen. Pernyataan sistem sendiri tidak cukup:

- indikator tidak boleh dipilih atau ditetapkan dengan cara yang membuat ketidakselarasan mustahil terlihat;
- desain ulang diverifikasi dengan cara yang sama, berdasarkan bukti yang dapat diperiksa pihak lain;
- sertifikasi penuh tidak menutup alasan apa pun untuk membuka kembali tinjauan. Setiap pemicu dalam [§9 Sertifikasi Ulang dan Pembukaan Kembali](#9-recertification-and-reopening) tetap berlaku; dan
- pengelakan ditangani berdasarkan [§9.4 Anti-pengelakan](#94-non-evasion).
