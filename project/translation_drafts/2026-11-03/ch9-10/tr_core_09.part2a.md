#### 2.2 Sistem Sınıfının Her Değerlendirmeyi Nasıl Ölçeklediği

Sistem sınıfı, bu bölümdeki her değerlendirmenin ne derinlikte yapılacağını — [§3 Bütün-Sistem Sertifikasyon Değerlendirmesi](#3-whole-system-certification-evaluation) içindeki bütün-sistem etkenlerini, [§3.4 Veri Türleri ve İşleme Değerlendirmesi](#34-data-types-and-handling-evaluation) içindeki veri işlemeyi ve [§5 Hak Tabanı ve Alan Değerlendirmeleri](#5-rights-floor-and-domain-evaluations) içindeki her Hak Tabanı ve alan değerlendirmesini — ve ne sıklıkla tekrarlanacağını belirler:

- Daha yüksek sınıflı sistemler, uygulanabilir her değerlendirmenin yalnızca ileri sürülmediğini, gerçekten yapıldığını gösteren orantılı biçimde daha güçlü kanıt gerektirir. Hiçbir sistem sınıfı, yalnızca kâğıt üzerinde var olan kimlik bilgileri, etiketler veya düzenlemelerle ya da içine kimsenin bakamadığı inceleme ve kararlarla yetinemez.
- Daha düşük sistem sınıfları da tetikleyici koşulun bulunduğu her yerde dürüst ve orantılı değerlendirme gerektirir.
- Sistem sınıfı, gerekli bir değerlendirmenin atlanmasına hiçbir zaman izin vermez. Gerçek rolü sistem sınıfını aşan bir sistem yeniden sınıflandırılmalı ve daha yüksek derinlikte yeniden değerlendirilmelidir. Ölçek, erişim veya benimsenmedeki büyüme ve güçlenen, yayılan ya da ikamesi zorlaşan bağımlılık, **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Yeniden sınıflandırma gerekliliği*) uyarınca yeniden değerlendirme tetikleyicileridir; ayrıca [§9.2 Yeniden açma tetikleyicileri](core_09.010_system_alignment_certification_record_recertification.md#92-reopening-triggers) kapsamında incelemeyi yeniden açar. Bir evlat edinenin [Birinci Bölüm §11.4 Kaynak ve Bağımlılık Yoğunlaşması](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) uyarınca belirlediği eşiğin aşılması, bu büyümenin ek kanıtıdır. Yeniden değerlendirme eşik aşılana kadar beklemez; hiç belirlenmemiş veya fazla yüksek belirlenmiş bir eşik de yeniden değerlendirmeyi geciktirmez.

Katılım ve orantılılık gereklilikleri de aynı şekilde ölçeklenir:

- **A Sınıfı** sistemler, hata giderim mümkün olmadan önce hayatta kalma temel ihtiyaçlarını engelleyebileceğinden, uygulamada mümkün olan en güçlü katılım yollarını gerektirir. Bunlar şunları içerir:
  - erişilebilir itiraz；
  - paydaş incelemesi；ve
  - etkilenen payın atandığı forum ailesinden bulgular; [B Kısmı §6.1 Forum gözetimi ve bileşen rolleri](core_09.005_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles) uyarınca gereken Kurum veya Algılayan Forumlar dâhil。
- **B Sınıfı** sistemler aşağıdakilere erişimi koşula bağladığında sağlam katılım yolları gerektirir:
  - sağlık hizmeti；
  - eğitim；
  - yardımlar；
  - çalışma；veya
  - karşılaştırılabilir gündelik yaşam alanları。
- **C Sınıfı** sistemler de itiraz edilebilir kayıtlar ve orantılı açıklama gerektirir; özellikle koordinasyon etkileri:
  - korunan gruplara daha ağır yük bindirdiğinde；
  - çok sayıda algılayanın aynı sisteme bağımlı kalmasına yol açtığında；veya
  - sistemin yakında B veya A Sınıfına geçebileceğine işaret ettiğinde。

<a id="23-pilot-certification"></a>

#### 2.3 Pilot sertifikasyon

Bir **[pilot](core_05.040_band_continuity.md#pilot)** bir [devreye almadır](core_05.040_band_continuity.md#go-live); bu nedenle [B Kısmı §7.1 Devreye Alma Kapısı](core_09.005_system_alignment_certification_record_process.md#71-go-live-gate) içindeki devreye alma kuralı uyarınca başlamadan önce kendine ait sertifikasyonu gerektirir.

- Herhangi bir sistem sınıfındaki sistemin tam devreye almadan önce pilot yürütmesi beklenir; yürütmeyen sistem bunun nedenini kaydeder.
- Bir pilotta da dürüst sınıflandırma ve tetikleyici koşulu karşılanan her değerlendirme gerekir; kapsamı, nüfusu ve süresi kaydında belirtilir.
- Pilot kendi kaydı üzerinden, sistem sınıfına ve sistemin ikame edilebilirliğine göre ölçeklenen derinlikte değerlendirilir: etkileyeceği veya ona bağımlı olacak algılayanlar için uygulanabilir bir alternatif bulunup bulunmadığı; varsa bunun ne kadar maliyet, gecikme ve işlev kaybı getirdiği incelenir ([Bağımlılık](core_05.040_band_continuity.md#dependency) bölümüne bakın).
  - Sistem ne kadar kolay ikame edilebiliyorsa ve sistem sınıfı ne kadar düşükse pilotun değerlendirmesi o kadar hafif olabilir.
  - Kolayca ikame edilemeyen bir sistemin pilotu, tam devreye alma için sistem sınıfının gerektirdiği derinlikte değerlendirilir。

<a id="3-whole-system-certification-evaluation"></a>

### 3. Bütün-Sistem Sertifikasyon Değerlendirmesi

<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Üst akış:
  - [Birinci Bölüm §12 Sistemik Değerlendirme Gerekliliği](core_01.000_values_principles.md#12-systemic-evaluation-requirement) (1.000 §12); Gelişim ölçüm ailesi (*İyi oluş, güvenlik, zarar ve hayatta kalma tabanına erişim*); Anayasal Performans ölçüm ailesi (*Anayasal Verimlilik, Önlenebilir Yük ve Üretken Kapasite*)；
  - [Anayasal Dörtlü](core_00.000_preamble.md#constitutional-tetrad)；
  - [İki Anayasal Amaç](core_00.000_preamble.md#two-constitutional-aims)；
  - [maddi pay](core_00.000_preamble.md#material-stake)；
  - [§1 Amaç ve Rol](#1-purpose-and-role)。
- Alt akış:
  - [CS-9.320 §4](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class) (*Sistem sınıfına göre örnek bütün-sistem uygulaması*)；
  - [§3.4](#34-data-types-and-handling-evaluation) ile
  - [§5.6](#56-trustworthiness-and-system-reliance-integrity-evaluation) arası (*alan değerlendirmeleri*)；
  - [CS-9.320 §2](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-2-illustrative-system-class-profiles) (*Örnek sistem sınıfı profilleri*)；
  - [C Kısmı §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*kayıt içeriği*)；
  - [C Kısmı §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*kayıt bütünlüğü*)；
  - [B Kısmı §6](core_09.005_system_alignment_certification_record_process.md#6-forum-process) (9.005 §6) (*itiraz edilebilirlik zinciri*)；
  - [B Kısmı §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*sertifikasyon sonuçları*)。
- Birlikte okunmalı:
  - [Birinci Bölüm §16](core_01.010_stewardship_capacity_principles.md#16-stewardship-in-depth) (1.010 §16),
  - [§18](core_01.010_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline) ve
  - [§19](core_01.010_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture)；
  - [Birinci Bölüm §7.4 Gönüllü Bırakma, Önemli Öz-Değişiklik ve Çıkış Hakları](core_01.000_values_principles.md#74-voluntary-discontinuation-and-exit-rights) (1.000 §7.4)；
  - [Birinci Bölüm §7.2 Toplanma, Kolektif Örgütlenme ve Kurumsal Oluşum](core_01.000_values_principles.md#72-assembly-collective-organization-and-institutional-formation) (1.000 §7.2); denetim, şeffaflık veya bağımsız doğrulamaya ilişkin Hak Tabanları maddi biçimde söz konusu olduğunda **Article XVI** (*Denetim, Şeffaflık ve Bağımsız Doğrulama*); Süreklilik ölçüm ailesi (
  - [§3.2](#32-systemic-scope-and-risk-factors) — dayanıklılık, geri döndürülebilirlik ve sistemik risk)；
  - [Risk Değerlendirmesi](core_05.040_band_continuity.md#risk-evaluation)；
  - [Risk Açıklaması](core_05.050_band_oversight.md#risk-disclosure)；
  - [Kamusal Gözetim Tabanı Açıklaması](core_05.050_band_oversight.md#public-oversight-baseline-disclosure); Katılım ölçüm ailesi (
  - [§4.1](#41-privacy-informational-joint-invocation) — mahremiyet ve veri sorumlu yönetimi); Hesap Verebilirlik ölçüm ailesi (
  - [§3.1](#31-governance-incentive-and-contestability-discipline) — teşvik uyumu ve pazarda itiraz edilebilirlik)；
  - [Sistem Sınırları](core_05.040_band_continuity.md#system-boundaries)；
  - [Sistem Beyannamesi](core_05.040_band_continuity.md#system-charter)。
- Alt bölümler:
  - [§3.1](#31-governance-incentive-and-contestability-discipline) ile
  - [§3.4](#34-data-types-and-handling-evaluation) arası (*her zaman: yönetişim, sistemik etkenler, zaman ufku, veri türleri ve işleme*). II. Aşama [§4 Konunun Gündeme Geldiği Yerde Yapılan Değerlendirmeler](#4-evaluations-where-implicated) (*konu gündeme geldiğinde: mahremiyet alanları, çıkış hakları, toplanma ve muhalefet*) ve [§5 Hak Tabanı ve Alan Değerlendirmeleri](#5-rights-floor-and-domain-evaluations) (*tetikleyici koşul bulunduğunda*) bölümlerinde sürer。

</details>

<br>

*Yalın dille: Sistemin tek bir parçasına onay verip geri kalanını görmezden gelemezsiniz. İncelemeyi yapanların bütün resmi görmesi gerekir — sistemin neye bağımlı olduğu, üst akışta bir şey bozulursa neyin bozulacağı, daha sonra ortaya çıkan veya zaman içinde biriken zararlar, algılayanların sistemi gerçekten kullanıp kullanamadığı (yalnızca kâğıt üzerinde değil), özel bilgilerin uygun biçimde ayrılıp ayrılmadığı, algılayanların tuzağa düşmeden ayrılıp ayrılamadığı, grupların sistem tarafından bölünmeden örgütlenip örgütlenemediği, kısa vadeli kazanımların uzun vadeli zararı gizleyip gizlemediği ve büyük çıkarlar söz konusu olduğunda gerçek gözetim ile hesap verebilirliğin işlemeye devam edip etmeyeceği.*

*Uygulamalı örnekler: [CS-9.320 §4 Sistem sınıfına göre örnek bütün-sistem uygulaması](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class), bu bölümün uygulamada nasıl işlediğini gösterir. Her sistem sınıfından birer örnek sistem seçip yukarıdaki değerlendirmelerden geçirir.*

Bir sertifikasyon değerlendirmesi, [Anayasal Dörtlünün](core_00.000_preamble.md#constitutional-tetrad) (Katılım, Gözetim, Hesap Verebilirlik ve Zamanındalık), incelenen sistemin [maddi payını](core_00.000_preamble.md#material-stake) karşılayacak kadar güçlü olacağını doğrulamalıdır.

Sistem Sertifikasyon Kayıtları, bu bölümdeki, [§4 Konunun Gündeme Geldiği Yerde Yapılan Değerlendirmeler](#4-evaluations-where-implicated) ve [§5 Hak Tabanı ve Alan Değerlendirmeleri](#5-rights-floor-and-domain-evaluations) içindeki her etkenin, aşağıdakilerden herhangi biri bakımından maddi olduğu yerlerde değerlendirildiğini göstermelidir:

- sertifikasyon；
- doğrulama；
- yeniden sertifikasyon；
- süregelen güven；
- devreye alma；veya
- sertifikasyon koşulunun kaldırılması。

Yalnızca sistemin hemen ortaya çıkan veya yerel etkilerini değerlendirmek yeterli değildir. II. Aşama olan bütün-sistem değerlendirmesi bu boşluğu aşağıdaki tabloda listelenen üç parçayla doldurur. Bu bölüm **IIa** parçasını kapsar. [§4 Konunun Gündeme Geldiği Yerde Yapılan Değerlendirmeler](#4-evaluations-where-implicated) **IIb**’yi, [§5 Hak Tabanı ve Alan Değerlendirmeleri](#5-rights-floor-and-domain-evaluations) ise **IIc**’yi kapsar. Tablo yalnızca rehber niteliğindedir; hiçbir bölümün gerekliliklerini değiştirmez.

| Ne zaman | Alt aşama | Bölümler | Uygulanma alanı |
|------|-----------|----------|---------|
| **Her zaman** | IIa | [§3.1 Yönetişim, Teşvik ve İtiraz Edilebilirlik Disiplini](#31-governance-incentive-and-contestability-discipline); [§3.2 Sistemik Kapsam ve Risk Etkenleri](#32-systemic-scope-and-risk-factors); [§3.3 Zaman Tutarlılığı Kısıtı](#33-time-consistency-constraint); [§3.4 Veri Türleri ve İşleme Değerlendirmesi](#34-data-types-and-handling-evaluation) | maddi etkisi olan her Sistem Sertifikasyon Kaydı |
| **Konu gündeme geldiğinde** | IIb | [§4.1 Mahremiyetin (Bilgisel) Birlikte Uygulanması](#41-privacy-informational-joint-invocation); [§4.2 Gönüllü Bırakma, Önemli Öz-Değişiklik ve Çıkış Hakları](#42-voluntary-discontinuation-major-self-modification-and-exit-rights); [§4.3 Toplanma, Kolektif Örgütlenme ve Kurumsal Oluşum](#43-assembly-collective-organization-and-institutional-formation), [§4.3.1](#431-dissent-and-peaceful-protest) dâhil | sertifikasyon konusu, alt bölümün belirttiği alan veya ilkeyi maddi biçimde ilgilendirdiğinde |
| **Tetikleyici koşul bulunduğunda** | IIc | [§5 Hak Tabanı ve Alan Değerlendirmeleri](#5-rights-floor-and-domain-evaluations) | §5 tablosundaki bir tetikleyici koşul karşılandığında |

<a id="31-governance-incentive-and-contestability-discipline"></a>
