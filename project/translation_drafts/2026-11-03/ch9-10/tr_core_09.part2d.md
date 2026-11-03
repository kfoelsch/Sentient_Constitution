##### 3.4.2 Mahremiyet Disiplini

Sertifikasyon, veri işlemeyi aşağıdaki mahremiyet disiplinine tabi tutmalıdır:

- *H, I, N, S ve Y Türleri.* **H**, **I**, **N**, **S** ve **Y Türü** verilerde sertifikasyon, **CS-6.305 (*Bilgi türleri ve işleme*) ile CS-6.310** (*Veri sınıflandırmaları*) içinde her türün belirttiği [mahremiyet düzenlemelerine](corpus_systems/cs_06.310_data_classifications.md#privacy-link) uygun işleme yapıldığını doğrulamalıdır. Buna [Gereklilik](core_05.035_band_accountability.md#necessity), [Orantılılık](core_05.035_band_accountability.md#proportionality), veri minimizasyonu ve rıza ya da başka yeterli yetki dâhildir。
- *Birlikte uygulama.* Birden fazla mahremiyet alanı söz konusu olduğunda, [§4.1 Mahremiyetin (Bilgisel) Birlikte Uygulanması](#41-privacy-informational-joint-invocation) da geçerlidir。
- *Etiketler tek başına yetmez.* Doğru tür etiketi tek başına mahremiyet kurallarına uyulduğunu göstermez。
- *W, U ve T Türleri.* **W**, **U** ve **T Türü** eserlerde sertifikasyon, aşağıdakiler dâhil yaratıcının denetimine saygı gösterildiğini doğrulamalıdır:
  - [CS-6.310 Part B §9.9](corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published) (*W Türü: Yayımlanmış Eserler*) uyarınca kamusal yayımlamanın geri çekilmesi；
  - [CS-6.310 Part B §9.13](corpus_systems/cs_06.310_data_classifications.md#913-commercial-grants) (*Ticari izinler*) uyarınca kayıtlı her iznin sınırları；ve
  - yaratıcının [saklı tuttuğu haklar](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights)。
- *Zımni rıza yoktur.* Bir izin yalnızca belirttiği kullanımları, kapsamı, süreyi, bölgeyi ve ortamı içinde kapsar. Belirtmediği her şey yaratıcının denetiminde kalır. Sertifikasyon; varsayılan bir ayarı, paketlenmiş koşulları, sessizliği veya daha geniş bir izni, izinde belirtilmeyen bir kullanıma rıza olarak değerlendirmemelidir. Örneğin, bir eseri yayımlamak veya satmak için verilen genel lisans, eseri eğitim verisi olarak kullanmaya rıza sayılmaz; bunun için yaratıcının kendi özel rızası gerekir ([saklı tutulan haklar](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights) bölümüne bakın)。

<a id="343-protective-storage-and-key-custody"></a>
##### 3.4.3 Koruyucu Depolama ve Anahtarların Muhafazası

Varsayılan olarak erişimi kısıtlı ve erişilemez katmanlardaki veriler için sertifikasyon, sistemin [CS-6.305 Part A §5.0 Erişim duruşu katmanları](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands) içindeki koruyucu depolama ve anahtar muhafazası asgari koşulunu karşıladığını doğrulamalıdır. Kayıt şunları göstermelidir:

- yedekler, önbellekler, günlükler ve takas alanları dâhil, kısıtlı verilerin ve anahtarlarının fiilen nerede bulunduğunu；
- açık metnin yalnızca buna ihtiyaç duyan süreçlerle sınırlı olduğunu；ve
- denetim, dışa aktarma ve hukuka uygun geçersiz kılma yollarının hâlâ çalıştığını。

Bu kanıt olmadan yalnızca şifreleme iddiasında bulunmak gerekliliği karşılamaz。

<a id="344-scheduled-data-type-re-evaluation"></a>
<a id="344-periodic-data-type-re-evaluation"></a>
##### 3.4.4 Planlı Veri Türü Yeniden Değerlendirmesi

Maddi etkisi olan bir sistem her sertifikalandırıldığında veya yeniden sertifikalandırıldığında inceleme, önemli veri kümelerinin:

- **[CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Yeniden sınıflandırma ve yaşam döngüsü yönetişimi*) ile **CJS-5.130 §18** (*veri saklama ve yaşam döngüsü bütünlüğü koşulları*) uyarınca uygun sınıflandırma bakımından **yeniden değerlendirilip değerlendirilmediğini**；ve
- inceleme gerektirmişse **yeniden sınıflandırılıp sınıflandırılmadığını**

kontrol etmelidir。

**CS-6.305** (*Bilgi türleri ve işleme*) ile **CS-6.310** (*Veri sınıflandırmaları*) kapsamındaki olay tetiklemeli yeniden türlendirme, bu planlı sertifikasyon kontrolünün yerini almaz。

<a id="345-system-class-scaled-infrastructure-assurance"></a>
##### 3.4.5 Sistem Sınıfına Göre Ölçeklenen Altyapı Güvencesi

[§2.2 Sistem sınıfının her değerlendirmeyi nasıl ölçeklediği](#22-how-system-class-scales-every-evaluation) ile **CS-9.305** (*Sistem sınıflandırma mekanizması*) ve **CS-9.310** (*Sistem etki sınıflandırmaları*) uyarınca daha yüksek sınıflı sistemler, aşağıdaki unsurların baskı altında korunabileceğini gösteren orantılı biçimde daha güçlü kanıt gerektirir: işleme, depolama, veri işleme, iletim, yedekleme, kurtarma ve izleme altyapısı:

- sınıflandırma bütünlüğü；
- isnat edilebilirlik；ve
- itiraz edilebilirlik。

**CS-6.305** (*Bilgi türleri ve işleme*) ile **CS-6.310** (*Veri sınıflandırmaları*) kapsamındaki kamusal yarar görünürlüğü varsayılanları uygulandığında, sertifikasyon kısıtlamaların:

- dar kapsamlı；
- belgelenmiş ve denetlenebilir；ve
- makul biçimde mümkün olan en güçlü kamusal ikameyle desteklenmiş olduğunu

doğrulamalıdır. Böylece saklanan bilgi basitçe gizlenmek yerine açıklanır. İkameye özet, toplam değer, kimliksizleştirilmiş sürüm, gecikmeli yayımlama veya koşullu denetim erişimi örnek verilebilir。

<a id="346-infrastructure-robustness-for-data"></a>
##### 3.4.6 Veri İçin Altyapı Sağlamlığı

Sertifikasyon, veri işleme altyapısının söz konusu veri türleri ve sistem sınıfı için uygun olup olmadığını değerlendirmelidir. Bu altyapı şunları içerir:

- kalıcılık katmanları ve işlem hatları；
- erişim kontrolleri；
- şifreleme veya yalıtım sınırları；
- yedekleme ve geri yükleme yolları；ve
- işletmeci veya tedarikçi yetki devri zincirleri。

Yaşam döngüsü bütünlüğü, hasmane dayanıklılık, taşınabilirlik veya kurtarılabilirlik bakımından maddi açıklar kayda geçirilmeli ve sertifikasyon sonucuna, sertifikasyon koşullarına ya da güven sınırlarına yansıtılmalıdır。

<a id="347-defects-and-misalignment"></a>
##### 3.4.7 Kusurlar ve Uyumsuzluk

Aşağıdakilerin her biri sertifikasyon kusuru sayılmalıdır:

- verilerin yanlış sınıflandırılması；
- kaçınmaya yönelik yeniden yapılandırma；
- güvenli olmayan alanlar arası bağlantı；
- doğru tür etiketini taşıdığı hâlde o türün gerektirdiği mahremiyet korumalarını bozan işleme；
- veriye kimin eriştiği, veriyi kimin işlediği veya değiştirdiğine ilişkin kayıt bulunmaması ve bu nedenle önemli bir zararın soruşturulamaması；
- **planlı veri türü yeniden değerlendirmesinin gecikmesi veya atlanması**；
- kısıtlı verilerin depolamada veya yetkili işleme sınırının ötesinde açık metin olarak tutulması ya da anahtarlara bunlara ihtiyaç duymayan süreçlerin erişebilmesi；ve
- **CS-6.305** (*Bilgi türleri ve işleme*) ile **CS-6.310** (*Veri sınıflandırmaları*) korumalarını öngörülebilir biçimde boşa çıkaran altyapı kırılganlığı。

Bu kusurların sonuçları [§7 Sertifikasyon Sonuçları](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) bölümünde belirlenir。

<a id="4-evaluations-where-implicated"></a>
