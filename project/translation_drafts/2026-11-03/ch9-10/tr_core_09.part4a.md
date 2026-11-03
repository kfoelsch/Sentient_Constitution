##### 5.3.4 Harita ve Kayıt Bütünlüğü

Bağımlılık haritalarına ve kaynak akışı kayıtlarına dayanmadan önce sertifikasyon, bunların **Madde V-A** (*Bağımlılık Haritalama ve Kaynak Akışı Şeffaflığı*) gereklerini karşılayıp karşılamadığını denetlemelidir. Bunlar:

- **Eksiksiz:** önemli oldukları yerlerde, önemli üst ve alt kaynak bağımlılıklarını, kaynak akışlarını ve gizli ya da dengesiz ilişkileri kapsamalıdır.
- **Güncel:** değişimin hızına ve sistemin kritikliğine, [§2 Sistem Sınıfı Değerlendirmesi](#2-system-class-evaluation) kapsamındaki sistem sınıfı dâhil, uygun sıklıkta güncellenmelidir. Sistemin son sertifikasyonda nasıl çalıştığını değil, şimdi nasıl çalıştığını göstermelidir.
- **Denetlenebilir:** **Madde XVI-A** (*Denetlenebilirlik ve Gözlemlenebilir Kanıt*) uyarınca denetime açık olmalıdır.

Bu sınamalardan herhangi birini geçemeyen bir harita veya kayıt, sistemin yeterince geri katkı sağladığı sonucunu destekleyemez. Eksiklik yazılı olarak kaydedilmeli ve aşağıdaki *Kusurlar ve uyumsuzluk* bölümü uyarınca ele alınmalıdır.

<a id="535-system-class-scaling-and-escalation"></a>
##### 5.3.5 Sistem Sınıfına Göre Ölçeklendirme ve Yükseltme

Sistemin sınıfı, incelemenin derinliğini ve yeterliliğin ne kadar yakından değerlendirileceğini belirler. Ortak kaynaklardan çekilen bir katkıyı önemsiz kılmaz; farklı kuruluşlara, kayıtlara veya dönemlere bölünmüş kaynak çekme, [Birinci Bölüm §15.1.1 Bölümlere Ayırmayı Önleme İlkesi](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle) uyarınca tek bir bütün olarak değerlendirilir. Esaslılık tetikleyicisi karşılandığında:

- Algılayanların hayatta kalmak için ihtiyaç duyduğu ortak bir temelden — örneğin ortak bir havzadan veya bölgesel elektrik şebekesinin ana omurgasından — yararlanan bir sistem, bağımlılık haritası ve geri akışlara ilişkin en güçlü kanıtı kayda koymalıdır. Bunlar, [Birinci Bölüm §9 Paylaşılan Sistem Kapasitesi](core_01.000_values_principles.md#9-shared-system-capacity) ilkesinin kalıcı kapasitesini koruduğu ortak sistemlerdir; kanıtın burada en güçlü olmasının nedeni **Madde III-A** (*Hayatta Kalma*) ilkesidir.
- Ortak kimlik doğrulama, sağlık bilişimi veya benzer altyapıya dayanan bir sistem, aldığı şeyleri ve desteğinin yeterli olup olmadığını, operasyonlarının kritikliğine uygun derinlikte belgelemelidir. “Birlikte işlerlik” konulu belirsiz sloganlar sayılmaz: [Birinci Bölüm §18.5 Modüler Mimari ve Bağımlılık Disiplini](core_01.010_stewardship_capacity_principles.md#185-modular-architecture-and-dependency-discipline) uyarınca bağımlılık haritalarda ve kayıtlarda görünür olmalıdır.
- Bir sistem, gerçekçi biçimde başka bir seçeneğe geçemeyen kurumlar için ödeme, kimlik veya personel darboğazına sessizce dönüşürken sistemler arası incelemeden kaçmamalıdır.
  - **Kim geçiş yapamaz:** [§5.3.3 Değerlendirme Gerekliliği](#533-evaluation-requirement) kapsamındaki ikame edilebilirlik etkenlerine göre değerlendirilir.
  - **Neden önemli:** bu, [Birinci Bölüm §11.4 Kaynak ve Bağımlılık Yoğunlaşması](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) ilkesinin tarif ettiği türden bir yoğunlaşmadır. Bu ilke, benimseyenlere; gerçek bir alternatifi olmadan kaç algılayanın veya sistemin tek bir sağlayıcıya bağımlı olduğu ya da ortak altyapının arayüz ve erişim noktalarını kimin kontrol ettiği gibi düzeyler belirlemelerini söyler. Sertifikasyon, incelemesini yükseltmeden önce benimseyenin belirlediği düzeyin aşılmasını beklemez (aşağıya bakın).
  - **Sertifikasyon ne yapar:** incelemeyi yükseltir ve [§2.2 Sistem sınıfı her değerlendirmeyi nasıl ölçeklendirir](#22-how-system-class-scales-every-evaluation) uyarınca sistemin sınıfını, sistemin hayatta kalmak için vazgeçilmez koordinasyona erişimi kontrol ettiği durumlarda **A Sınıfı** düzeyine kadar yeniden değerlendirir.

Üst düzeye geçiş, [Birinci Bölüm §11.4 Kaynak ve Bağımlılık Yoğunlaşması](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) uyarınca belirlenen bir yoğunlaşma eşiğini beklemez. Benimseyenin belirlediği ve sistemin aştığı eşik, ek kanıttır. Belirlenmemiş veya çok yüksek belirlenmiş bir eşik, üst düzeye geçişi geciktirmez; bir eşiğin aşılması da kendi başına uygunsuzluk tespiti değildir.

<a id="536-defects-and-misalignment"></a>
##### 5.3.6 Kusurlar ve Uyumsuzluk

[§5](#5-rights-floor-and-domain-evaluations) (*Hak Tabanı ve Alan Değerlendirmeleri*) kapsamındaki kusurlar, sistemin **Madde V-A** (*Bağımlılık Haritalama ve Kaynak Akışı Şeffaflığı*) uyarınca açıklaması gereken bağımlılık veya kaynak akışı bilgileri dâhil, bu değerlendirme için de geçerlidir. Ayrıca aşağıdakilerin her biri sertifikasyon kusuru sayılır:

- aşağıdakilerden herhangi birini [Orantılı Sistemler Arası Destek](core_05.040_band_continuity.md#proportionate-cross-system-support) gereklerini karşılamaya yeterli saymak:
  - simgesel, kapalı, harita dışında kalan veya tek seferlik aktarımlar;
  - sistemin **Madde III-A** (*Hayatta Kalma*) kapsamındaki hayatta kalma tabanını karşıladığı gerçeği; veya
  - sistemin [Birinci Bölüm §11 Piyasa Yapısı](core_01.000_values_principles.md#11-market-structure) kapsamındaki piyasa yoğunlaşması sınırları içinde kaldığı gerçeği;
- esaslılık tetikleyicisinin geçerli olduğu durumlarda, orantılı biçimde geri katkı sağlamadan ortak temellerden tekrar tekrar kaynak çekmek;
- esas olarak ele geçirmeyi veya yoğunlaşmayı pekiştiren destek; ve
- **Madde V-A** (*Bağımlılık Haritalama ve Kaynak Akışı Şeffaflığı*) uyarınca gereken şeffaflığı boşa çıkaran koşullara bağlanmış destek.

Destekteki belgelenmiş eksiklikler [Birinci Bölüm §6 Güven ve Güvenilirlik](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) uyarınca sayılır.

<a id="54-nondiscrimination-evaluation"></a>

#### 5.4 Ayrımcılık Yapmama Değerlendirmesi

<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Üst kaynaklar:
  - [Kısım C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*kayıt içeriği*);
  - [§2](#2-system-class-evaluation) (*sistem sınıfı değerlendirmesi*); Katılım ölçüm ailesi (*anayasal ölçüm olarak Özlü Adalet ve Korunan Özelliklerin Dolaylı Göstergelerle Kullanımı ve Farklı Etki*); **Madde VI-C** (*Ayrımcılık Yapmama*);
  - [Özlü Adalet](core_05.055_band_participation.md#substantive-fairness),
  - [Korunan Özellikler](core_05.055_band_participation.md#protected-characteristics),
  - [Korunan Özelliklerin Dolaylı Göstergelerle Kullanımı ve Farklı Etki](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact),
  - [Dil, Kültür ve Miras](core_05.040_band_continuity.md#language-culture-and-heritage),
  - [Gereklilik](core_05.035_band_accountability.md#necessity) ve
  - [Orantılılık](core_05.035_band_accountability.md#proportionality) (Beşinci Bölüm).
- Üst kaynaklar: İlkeler: Birinci Bölüm
  - [§3.1 Adalet](core_01.000_values_principles.md#31-fairness) (özellikle [§3.1.2 Yararlar ve Yükler](core_01.000_values_principles.md#312-benefits-and-burdens)) ve
  - [§11.4 Kaynak ve Bağımlılık Yoğunlaşması](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*kapı bekçiliği; §5.4.2'deki üst düzeye geçiş*).
- Alt kaynaklar:
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*Sistem sınıfına göre ayrımcılık yapmamanın örnek uygulaması*);
  - [Kısım C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*kayıt bütünlüğü*);
  - [Kısım C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*doğrulanmış girdi kapısı*);
  - [Kısım B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*ayrımcılık örüntüsünden kaynaklanan uyumsuzluk ve dolaylı göstergelerle kaçınma*).
- Şunlarla birlikte okuyun: sertifikasyon forum, idari veya yaptırım erişimine koşul koyduğunda **Madde VI-C** (*Ayrımcılık Yapmama*) kapsamındaki hükme bağlama ve işleyiş yükümlülüğü; [*Ayrımcılık Yapmama, Korunan Özellikler, Haysiyet, Mahrem Sinyallere Dayalı Erişim Koşulları ve **Madde VII-E** (*Yetişkinlerin rızaya dayalı ticari cinsel hizmetleri ve cinsel sömürü*) Durumu*](core_05.055_band_participation.md#fairness-protected-characteristics-and-nondiscrimination).
- Alt bölümler:
  - [§5.4.1](#541-evaluation-requirement) (*değerlendirme gerekliliği*);
  - [§5.4.2](#542-system-class-scaling-and-escalation) (*sistem sınıfına göre ölçeklendirme ve yükseltme*);
  - [§5.4.3](#543-defects-and-misalignment) (*kusurlar ve uyumsuzluk*);
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*Sistem sınıfına göre ayrımcılık yapmamanın örnek uygulaması*).

</details>

<br>

*Yalın dille: bazı sistemler kimin içeri alınacağına karar verir. Bazıları kimin daha fazla ödeyeceğine. Bazıları kimin daha alt sıraya konacağına veya daha ağır yük taşıyacağına. Bir sistem bu tür kararları önemli sonuçlar doğuracak biçimde verdiğinde sertifikasyon tek bir soru sorar: zarar çoğunlukla korunan özelliklere sahip algılayanlara mı, yoksa onların yerine kullanılan özelliklere mi düşüyor? İşletmecinin kurallarının tarafsız olduğunu söylemesi bu soruyu yanıtlamaz. Örnekler: [CS-9.320 §9 Sistem sınıfına göre ayrımcılık yapmamanın örnek uygulaması](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class).*

Bu bölüm, esaslı etki yaratan bir sistemin uygunluk kuralları, model özellikleri, sıralama mantığı, platform politikası veya benzer karar yolları aracılığıyla algılayanları esaslı biçimde sınıflandırdığı, sıraladığı, fiyatlandırdığı, erişime koşul koyduğu, dışladığı veya aralarında yük ve yarar tahsis ettiği durumlarda uygulanır.

Esaslılık tetikleyicisi geçerliyse sistem uyumu sertifikasyonu, **Madde VI-C** (*Ayrımcılık Yapmama*), [Özlü Adalet](core_05.055_band_participation.md#substantive-fairness) ve [Korunan Özelliklerin Dolaylı Göstergelerle Kullanımı ve Farklı Etki](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact) uyarınca **ayrımcılık yapmamayı** değerlendirmelidir.

<a id="541-evaluation-requirement"></a>
##### 5.4.1 Değerlendirme Gerekliliği

*Yalın dille: bu bölüm kapsayıcılık kotaları belirlemez. Bir adalet formülü seçmez. Başka belgeler bunları ele alabilir; corpus'a daha sonra eklenecek metinler veya benimseyenin yazdığı belgeler de. Sertifikasyon yalnızca birinin yararları kimin elde ettiğine, yükleri kimin taşıdığına ve korunan özelliklerin yerine kullanılan ikame özelliklerin etkili olup olmadığına gerçekten bakıp bakmadığını denetler. Tetikleyicinin geçerli olduğu her yerde bu değerlendirme uygulanır.*

Sertifikasyon süreci, sistemin esaslı biçimde dayandığı karar yollarının aşağıdakilerden herhangi birine dayanarak algılayanlara esaslı yükler, dışlama veya zarar getirip getirmediğini belirlemelidir:

- [Korunan Özellikler](core_05.055_band_participation.md#protected-characteristics);
- bunların ikame özellikleri; veya
- [Dil, Kültür ve Miras](core_05.040_band_continuity.md#language-culture-and-heritage) kapsamında uzmanlaşmalar dâhil, işlevsel ikame olarak kullanılan keyfî gruplamalar.

Değerlendirme, [maddi pay](core_00.000_preamble.md#material-stake) ölçüsünde ölçeklendirilerek şunları yapmalıdır:

- [Özlü Adalet](core_05.055_band_participation.md#substantive-fairness) uyarınca yük ve yarar örüntülerini sınamak; ve
- [Korunan Özelliklerin Dolaylı Göstergelerle Kullanımı ve Farklı Etki](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact) uyarınca ikame özellik veya farklı etki riskini sınamak.

Farklı muameleye yalnızca belgelenmiş [Gereklilik](core_05.035_band_accountability.md#necessity), [Orantılılık](core_05.035_band_accountability.md#proportionality) ve özlü adalet gerekçe oluşturduğunda izin verilir. Değerlendirme, görünürdeki tarafsızlığı, açıklanan niyeti veya etiketi tek başına değil işlevsel etkiyi yansıtmalıdır.

<a id="542-system-class-scaling-and-escalation"></a>
##### 5.4.2 Sistem Sınıfına Göre Ölçeklendirme ve Yükseltme

Sistem sınıfı, sistemin ne derinlikte değerlendirileceğini belirler. Sıralamayı veya yük aktarmayı önemsiz saymaya izin vermez. Esaslılık tetikleyicisinin geçerli olduğu her yerde aşağıdakiler uygulanır:

- **Kapatma, bildirim veya benzer kuralları hayatta kalmak için temel gereksinimleri ortadan kaldırabilecek sistemler:**
  - kayıt genel bir iyi uygulama beyanını değil, yük ve yararlarla ikame özelliklere ilişkin en güçlü çözümlemeyi içermelidir; ve
  - gizli maliyet aktarma, [Birinci Bölüm §3.1.2 Yararlar ve Yükler](core_01.000_values_principles.md#312-benefits-and-burdens) gereklerini karşılamaz.
- **Eşleştirme veya yönlendirme mantığı acil sağlık hizmetlerini, yardımları veya yeterlilik belgesi erişimini etkileyen sistemler:**
  - kayıt, operasyonel kritiklik düzeyinde farklı etki ve özlü adalet bulgularını belgelemelidir; ve
  - bunun nedeni, [Birinci Bölüm §3.1 Adalet](core_01.000_values_principles.md#31-fairness) uyarınca adaletin, algılayanlara açıklanmamış kurallarla davranılmaması veya başkalarının kaçındığı maliyetleri onların üstlenmek zorunda bırakılmaması anlamına gelmesidir.
- **Vardiya, tedarikçi veya rezervasyon mantığı katılımcıları esaslı biçimde sıralayan ya da dışlayan sistemler:**
  - sistem, gerçek bir çözümleme yerine göstermelik bir adalet paragrafı koymamalıdır;
  - koordinasyon hayatta kalmak için vazgeçilmez hâle geldiğinde sertifikasyon, [§2.2 Sistem sınıfı her değerlendirmeyi nasıl ölçeklendirir](#22-how-system-class-scales-every-evaluation) uyarınca incelemeyi ve yeniden sınıflandırmayı yükseltmelidir; buna sistemin personel alımına veya acil durum yönlendirmesine erişimi koşullandırdığı durumlarda **A Sınıfına** yeniden sınıflandırma da dahildir; ve
  - bu tür kapı bekçiliği, gerçek bir alternatif olmaksızın çok sayıda algılayanın veya sistemin tek bir sağlayıcıya bağımlı olması nedeniyle [Birinci Bölüm §11.4 Kaynak ve Bağımlılık Yoğunlaşması](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) uyarınca bir yoğunlaşma göstergesidir; sertifikasyonun burada incelemeyi yükseltmesinin nedeni de budur.

<a id="543-defects-and-misalignment"></a>
##### 5.4.3 Kusurlar ve Uyumsuzluk

Bu değerlendirmeye iki kusur kümesi uygulanır:

- **Bölüm genelindeki kusurlar:**
  - [§5](#5-rights-floor-and-domain-evaluations) (*Hak Tabanı ve Alan Değerlendirmeleri*) kapsamındaki kusurlar bu değerlendirme için de geçerlidir; ve
  - **Madde VI-C** (*Ayrımcılık Yapmama*) inceleme gerektirdiğinde esaslı sınıflandırma, sıralama veya yük tahsis mantığı için de geçerlidir.
- **Ayrımcılık yapmama kusurları:** aşağıdakilerin her biri ayrıca sertifikasyon kusuru sayılmalıdır:
  - değerlendirilebilir bir yük ve yarar çözümlemesi olmaksızın görünürdeki tarafsızlığı, toplulaştırılmış kolaylık ölçütlerini veya işletmecinin öz bildirimini yeterli saymak; ve
  - **Madde VI-C** (*Ayrımcılık Yapmama*) kapsamındaki **Gereklilik** ve **Orantılılık** sınamalarını karşılamadan dil, kültür veya miras korumalarını boşa çıkarmak için tekbiçimlilik, birlikte işlerlik veya verimlilik çerçevelerini kullanmak.

Belgelenmiş ikame özellikler yoluyla ayrımcılık veya özlü adaletsizlik [Birinci Bölüm §6 Güven ve Güvenilirlik](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) uyarınca sayılır.

<a id="55-accessibility-evaluation"></a>
