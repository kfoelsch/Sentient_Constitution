<!-- AI-assisted translation draft; unreviewed. Complete current-source Chapter Nine Part C §§8–11. Source SHA-256 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Baseline commit 247e2180509e5e029c1106878cf225067339e010; baseline SHA-256 faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Draft only; do not synchronize into translations/. -->

<a id="chapter-nine-part-c-certification-record-recertification-and-standing"></a>

# CHAPTER NINE, PART C: SYSTEM ALIGNMENT CERTIFICATION — RECORD, RECERTIFICATION, AND STANDING

<a id="8-system-certification-record"></a>

### 8. Sistem belgelendirme kaydı

<details>
<summary><strong>İzleme</strong></summary>

- Üst bağlantılar:
  - [B Bölümü §6](core_09.005_system_alignment_certification_record_process.md#6-forum-süreci) (*forum bileşeni bulguları Sistem Sertifikasyon Kaydına işlenir*);
  - [B Bölümü §7](core_09.005_system_alignment_certification_record_process.md#7-sertifikasyon-sonuçları) (*sonuç ve sonuca ulaşırken dile getirilen kaygılar*);
  - [A Bölümü §1](core_09.000_system_alignment_certification_evaluation.md#1-amaç-ve-rol) (9.000 §1) (*sertifikasyon amacı ve süreç özeti*);
  - [A Bölümü §2](core_09.000_system_alignment_certification_evaluation.md#2-sistem-sınıfı-değerlendirmesi) (*Sistem Sınıfı Değerlendirmesi*) (9.000 §2) kadar
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-hak-tabanı-ve-alan-değerlendirmeleri) (*Sistem Sertifikasyon Kaydına yansıtılan değerlendirme çıktıları*);
  - [İkinci ila Dördüncü Bölümler](../../core_04.000_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) (*tanım, ispat yükü, izlenebilirlik ve doğrulama temeli*);
  - [Sistem Sertifikasyon Kaydı](../../core_05.040_band_continuity.md#system-certification-record) (*Beşinci Bölümdeki anlamı*);
  - [Maddi Bağlayıcı Eylem Kaydı](../../core_05.035_band_accountability.md#materially-binding-act-record);
  - [Kayıt Bütünlüğü](../../core_05.035_band_accountability.md#record-integrity) (*Sistem Sertifikasyon Kaydına uygulanan güvenilirlik kuralı*);
  - [Sekizinci Bölüm §8 Eylem Kayıtları ve Atfedilebilir Devirler](../../core_08.000_functional_independence_separation_of_duties.md#8-act-records-and-attributable-handoffs) (8.000 §8); anayasal ölçüm olarak doğruluk ve epistemik bütünlük için gözetim ölçüm ailesi;
  - [**Def.O1** *Madde XVI: Denetim, Şeffaflık ve Bağımsız Doğrulama*](../../core_05.050_band_oversight.md#defo1-transparency-auditability-and-verification).
- Alt bağlantılar: [§9](#9-yeniden-sertifikasyon-ve-yeniden-açma) (*yeniden sertifikasyon ve yeniden açılma*); [§11.3](#113-doğrulanmış-girdi-kapısı-bir-belgelendirme-kaydı-yalnızca-sınırlı-izlenebilir-itiraz-edilebilir-ve-şunlar-altında-doğrulanmış-olduğunda-sekizinci-bölüm-güzergâhına-beslenebilir) (*doğrulanmış girdi kapısı*); [On Beşinci Bölüm §2.3](../../core_15.000_forum.md#23-forum-case-records-standing-records-and-contests) (*forum dava kayıtları ve standing kayıtlarına itirazlar*) (15.000 §2.3).
- Birlikte okuyun:
  - [Madde XVI: Denetim, Şeffaflık ve Bağımsız Doğrulama](../../core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [Kanıtın Korunması](../../core_05.050_band_oversight.md#evidence-preservation);
  - **[CS-6.305](../../corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Bilgi türleri ve işleme*) ve [CS-6.310 — Veri sınıflandırmaları](../../corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**;
  - **[CS-9.305](../../corpus_systems/cs_09.305_system_classification_machinery.md#cs-9305-part-a-system-classification-machinery) (*Sistem sınıflandırma mekanizması*) ve [CS-9.310 — Sistem etki sınıflandırmaları](../../corpus_systems/cs_09.310_system_impact_classifications.md#cs-9310-part-b-system-impact-classifications)**;
  - **CS-6.345** (*Sistem yaşam döngüsü*);
  - **CJS-5.110 §4** (*şeffaflık düzeyleri ve denetim erişim koşulları*).
- Alt bölümler:
  - [§8.1](#81-asgari-kayıt-içerikleri) (*Asgari kayıt içeriği*), ile
  - [§8.1.1](#811-sistem-kimliği-kapsam-ve-önceki-sistem-sertifikasyon-kaydı) (*Sistem kimliği, kapsamı ve önceki kayıt*);
  - [§8.1.2](#812-sınıflandırma-ve-bütün-sistem-bulguları) (*Sınıflandırma ve sistem çapındaki bulgular*);
  - [§8.1.3](#813-sistem-veri-türleri-kaydı) (*Sistem Veri Türleri Kaydı*);
  - [§8.1.4](#814-hak-tabanı-ve-alan-bulguları) (*Hak Tabanı ve alan bulguları*);
  - [§8.1.5](#815-teknik-kanıt-ve-inceleme-bulguları) (*Teknik kanıt ve inceleme bulguları*);
  - [§8.1.6](#816-gözetim-bağımsızlık-ve-itiraz-yolları) (*Gözetim, bağımsızlık ve itiraz yolları*);
  - [§8.1.7](#817-kaygılar-neden-ve-düzeltmeye-hazırlık) (*Kaygılar, neden ve iyileştirmeye hazırlık*);
  - [§8.1.8](#818-sonuç-ve-güven-sınırları) (*Sonuç ve güven sınırları*);
  - [§8.1.9](#819-işletim-planı) (*İşletim planı*); ve
  - [§8.1.10](#8110-eksiksizlik) (*Tamlık*);
  - [§8.2](#82-sistem-sertifikasyon-kaydının-şeffaflığı-ve-denetlenebilirliği) (*Sistem Sertifikasyon Kaydının şeffaflığı ve denetlenebilirliği*).

</details>


*Yalın dille: bir belgelendirme kaydı, inceleme altındaki bir sistem için denetlenebilir olay dosyasıdır — kim işletir, ne denetlendi, ne bulundu, ne kararlaştırıldı ve nasıl itiraz edilir. Bir pazarlama paketi ya da tek satırlık onay damgası değildir. Kayıt derinliği, açıklama ve itiraz yükü [§2.1](core_07_a_system_alignment_certification_evaluation.md) altında sistem sınıfına ölçeklenir — hayatta kalmaya kritik bir **Sınıf A** sistemi, bir **Sınıf C** eşgüdüm katmanından daha dolu ve daha itiraz edilebilir bir dosya ister; yine de her ikisi sınıfı dürüstçe belirtmeli ve gereken değerlendirmeleri yansıtmalıdır.*

Bir **Sistem belgelendirme kaydı**, belirli bir sistem, sürüm, işletici ya da sorumlu yönetici, kapsam, zaman penceresi, maddi-etki profili ve karar bağlamı hakkındaki sınırlı, incelenebilir bir kayıttır — [Sistem belgelendirme kaydı](../../core_05.040_band_continuity.md#system-certification-record)ndaki Beşinci Bölüm anlamı altında kapsama-sınırlı, zamana-sınırlı ve itiraz edilebilir.

<a id="81-minimum-record-contents"></a>

#### 8.1 Asgari kayıt içerikleri

<a id="811-system-identity-scope-and-prior-system-certification-record"></a>
##### 8.1.1 Sistem kimliği, kapsam ve önceki Sistem Sertifikasyon Kaydı

Kayıt en azından sistemi, Sistem Sürümünü, işletmeci/emanetçiyi, sertifikalı kapsamı; geçerli System Charter'ı (yokluğu önemsizse gerekçeli yokluğu); etkilenen toplulukları/bağımlılıkları; inceleme durumunu ve varsa sertifikalı kapsamın Charter kapsamıyla uyuşmasını tanımlar. İşletmeci/emanetçi, Institutional Certification Record sahibi bir Institution ise kullanılan kurumsal olguların izlenebilmesi için sürüm bağlantısı ve sistemin durumu eklenir. Sonraki sertifikasyon turunda, tamamlanmış önceki Sistem Sertifikasyon Kaydına Chapter Eight §8 uyarınca tutulan sürüm bağlantısı ve o zamandan beri nelerin değiştiği belirtilir.

<a id="812-classification-and-whole-system-findings"></a>
##### 8.1.2 Sınıflandırma ve bütün-sistem bulguları

Kayıt, Sistem Sınıflandırma Kaydını (veya CS-9.305/CS-9.310 kapsamında gerekli içeriği) ve bütün-sistem ile ilgili §4 değerlendirmelerinin bulgularını belirtir: atanmış sınıf ve gerekçesi; önemli etki varsayımları dahil temel varsayımlar; mevcut bağımlılık türleri; önemli olduğunda operasyonel kritiklik değerlendirmesi; belirsizlik; her sertifikasyon statüsü için sistem sınıfına göre ölçeklenmiş aralık; sınıflandırma belirsiz/itirazlıysa ihtiyaten esas alınan sınıf ve çözüm bekleyen koşullar. Sistemik kapsam, gizliliğin birlikte kullanımı, çıkış, meclis ve muhalefet, zaman tutarlılığı, yönetişim, teşvik ve ilgiliyse itiraz edilebilirlik hakkındaki önemli bulgular dahil edilir. Sistemik risk kapsamdaysa risk değerlendirmesi/varsayımları; açıklamanın kime/yoluyla verildiği, önemli kararlarla zaman ilişkisi, kullanılabilir ikamelerle gerekçeli saklı tutmalar ve eksik değerlendirme/açıklamanın kusur veya koşulları kaydedilir. Bu bulgular bu Sistem Sertifikasyon Kaydında kalır; ayrı adlandırılmış risk açıklama kaydı veya zorunlu beşinci bileşen kaydı oluşturmaz.

<a id="813-system-data-types-record"></a>
##### 8.1.3 Sistem Veri Türleri Kaydı

[§3.4 Data Types and Handling Evaluation](core_09.000_system_alignment_certification_evaluation.md#34-veri-türleri-ve-işleme-değerlendirmesi) uyarınca oluşturulan/doğrulanan Sistem Veri Türleri Kaydı veya CS-6.305/CS-6.310 gerekli içeriği belirtilir: önemli kapsamdaki veri türleri; belirsiz/çok tür içeren verinin sınıflandırma gerekçesi; ayrıştırma ve alanlar arası bağlantı kontrolleri; işleme, saklama, yaşam döngüsü ve altyapı güvencesi; Attributable Action ve Attribution Integrity için yeterli atıf kabiliyeti; CS-6.305 §§5,8 kapsamındaki son planlı yeniden değerlendirme (tarih/döngü, sınıf ve etkiye göre sıklık, önemli yeniden türleme). Gerekçeli açıklama/denetim erişimi sınırları ve gereken kamuya açık ikameler belirtilir. Type O tabanı geçerliyse Public Oversight Baseline Disclosure'ın sertifikalı kapsamı, kullanılan System Charter alanlarını, sınır bulgularını, boşlukları ve koşulları nasıl kapsadığı açıklanır.

<a id="814-rights-floor-and-domain-findings"></a>
##### 8.1.4 Hak tabanı ve alan bulguları

[§5 Rights-Floor and Domain Evaluations](core_09.000_system_alignment_certification_evaluation.md#5-hak-tabanı-ve-alan-değerlendirmeleri) tablosunda tetikleyicisi geçerli olan her koruma için önemlilik tetikleyicisi, değerlendirme kapsamı ve bulgular yazılır: sertifikasyon/devam eden güvenin hayatta kalma gereklerini, eğitime erişimi veya Safe Conditions'ı dışlayıp önemli ölçüde zayıflatıp zayıflatmadığı; ekolojik ayak izi (atıf varsayımları, yaşam döngüsü/bağımlılık sınırları, yükler, açıklama ve gerekli Environment forum bulguları); sistemler arası destek (bağımlı sistem haritası/kaynak akışı kapsamı, harita ve kaydın tamlığı/güncelliği/denetlenebilirliği, çıkarım ve geri dönüş akışları, yeterlilik, dağıtım adaleti); ayrımcılık yapmama (yük/yarar örüntüsü, korunan özellik ve vekil ayrımcılığı, esaslı adalet); erişilebilirlik (esaslı katılım, uyarlamalar, vekil yoluyla reddi önleme); eğitim kapasitesi (kapasite geliştirme/yeniden eğitim, değerlendirme şeffaflığı/itirazı, vekil/manipülasyon önleme); güvenilirlik (sahte güven, ters teşvikler, itiraz yolu, kurtarma bütünlüğü). Belirsizlik, gerekli bileşen bulguları, gerekçeli açıklama sınırları/kamu ikameleri ve süregelen zararla bağlantılı koşul/güven sınırı/yeniden açma tetikleyicileri de yazılır.

<a id="815-technical-evidence-and-review-findings"></a>
##### 8.1.5 Teknik kanıt ve inceleme bulguları

Önemli ölçüde dayanılan teknik standartlar, testler, ölçümler, belirsizlik, güvenlik payları, arıza biçimleri, güvenlik testi sonuçları ve kanıt temeli belirtilir. Her yeniden sertifikasyonun regresyon testleri (kapsam, standart/özel test kümeleri, sonuçlar, bilinen başarısızlıklar, düzeltmeler ve gerekçeli kabul edilen artık risk) ile CS-6.345'in istediği döngü kanıt paketi (kapsam, sınıflandırma, test, artık risk, düzeltmeye hazırlık, izleme, önceki kayıttan beri önemli değişiklikler) eklenir. Paydaş, hak tabanı, erişilebilirlik, bağımlılık ve katılım hususları; önemliyse ekolojik maruziyet/atıf, çevresel önkoşul bağımlılığı, yaşam döngüsü yükü, restorasyon görevi ve çevresel uyum incelemesi; ayrıca ele geçirilme, öz-inceleme, uyumsuz teşvik, kanıt kontrolü ve itirazın engellenmesi riskleri kaydedilir.

<a id="816-supervision-independence-and-challenge-paths"></a>
##### 8.1.6 Gözetim, bağımsızlık ve itiraz yolları

Her bileşeni düzenleyen, benimseyen, sevk eden, karara gönderen, durduran veya inceleyen forum ailesi/yetkili ve Bölüm B §6.2 gözetim sırası belirtilir. Sekizinci Bölümdeki dört koltuk (başlatma, doğrulama/yetkilendirme, kayıt, itiraz), her tutucu ve yetkisi ile o sırada geçerli Charter Role Map sürümü; her çekilme, yetki devri, yedek, izinli birleşme veya acil sapma kaydedilir. İşletmeci/önerenin kendi sertifikasyon iddiasını doğrulamadığını veya itirazını kontrol etmediğini gösterecek yeterli kontrol-hattı bilgisi sağlanır. §10'daki adlandırılmış itiraz yolları ve Bölüm B §6.3 zinciri, etkilenen tarafların her aşamada nasıl itiraz edebildiğini gösterir.

<a id="817-concerns-cause-and-remediation-readiness"></a>
##### 8.1.7 Kaygılar, neden ve düzeltmeye hazırlık

Forum incelemesinde veya sonuca ulaşırken dile getirilen her itiraz, muhalefet, kaygı ve şikâyet, kimden veya hangi yoldan geldiğine bakılmaksızın kaydedilir. Her biri için sunan (veya anonim/gizli olduğu), içerik, çözüm veya açık kalma nedeni ve doğurduğu koşul/güven sınırı/yeniden açma tetikleyicisi belirtilir; Bölüm B §6.2.4 inceleme sunumları günlüğü yayımlanır. Uyumsuzluk/kusur varsa nedenin tasarım, işletim veya henüz belirlenmemiş olduğu ve kanıtı yazılır. Düzeltme gerekiyorsa isteklilik/yeterlilik bulguları ve kanıtları, kanıtlama adımı, süresi, bağımsız doğrulama ve §7.3 kapsamındaki sonuç kaydedilir. Ret/geri almada gerekçe, geçici koruma ve §7.4 güven sınırları belirtilir.

<a id="818-outcome-and-reliance-limits"></a>
##### 8.1.8 Sonuç ve güven sınırları

En azından {link8} kapsamındaki sertifikasyon sonucu; sistemin geçici/tam sertifikalı ya da Not Certified olması; uygulanabilir sertifikasyon aralığı; incelemeyi yeniden açma tetikleyicileri; güven sınırları belirtilir.

<a id="819-operating-plan"></a>
##### 8.1.9 İşletim planı

Aynı kayıtta, sistem sınıfı ve önemli etkiye göre ölçeklenmiş kısa bir işletim planı bulunur; ayrı belge gerekmez. Yetkilendirilmiş işletimin sertifikalı kapsamı/nüfusu/süresi; sertifikasyon bitişi, sonraki yeniden sertifikasyon tarihi ve ara denetim tarihi ({link91}); ilk go-live/önemli genişleme için izin verilen en erken go-live, bildirim aralığı ve gerekçesi ({link71}); her koşul için zamanlama, sorumlu, tamamlanma/sürekli uyum kanıtı, bağımsız doğrulayıcı ve ihlal sonucu; gerçek sonuçları ve korumaları izleyen kişiler, kanıt/göstergeler, kontrol sıklığı ve işlem/yeniden inceleme gerektiren bulgu/eşikler; olay, itiraz ve karşılanmayan koşullara yanıt verecek kişiler, süreler ve gerektiğinde geçici koruma, sınırlama, geri alma veya güven sınırı yetkisi; kusurlar için düzeltme, doğrulama ölçüt/sonuçları, kalan belirsizlik ve izinli geçici güven belirtilir. Not Certified sistem için yasak go-live, ayrıca yetkilendirilmiş geçici güven, düzeltme şartları ve yeni inceleme ön koşulları yazılır; plan sertifikalı işletim izni ima etmez.

İşletim kanıtları ve koşulların sonradan tamamlandığına dair bulgular {act} uyarınca bağlantı olarak eklenir; tamamlanmış kayıt yerinde değiştirilmez. Ayrıntılı test/izleme yöntemleri {cs} dahil ilgili sahiplerinde kalır.

<a id="8110-completeness"></a>
##### 8.1.10 Eksiksizlik

Uygulanan değerlendirmelerin bulguları yoksa kayıt eksiktir: önemli etkisi olan her sistem için Part A §§2, 3, 3.4; locus/principle etkilenen §4 alt bölümlerinin her biri; tetikleyicisi gerçekleşen her §5 alanı. Bulgular bölüm başlıklarını veya işletmecinin kendi beyanını değil, değerlendirmede gerçekten bulunanı yansıtmalıdır. Sonucu değiştirmemiş olsa bile inceleme/karar sırasında ortaya çıkan kaygı, itiraz veya muhalefet atlanırsa kayıt eksiktir.

<a id="82-transparency-and-auditability-of-the-system-certification-record"></a>
#### 8.2 Sistem Sertifikasyon Kaydının Şeffaflığı ve Denetlenebilirliği
*Yalın dille: Sentientler bir Sistem Sertifikasyon Kaydını okuyup kontrol edemiyorsa kayıt işlevini yerine getiremez. Bu bölüm, şeffaflık ve denetlenebilirliği soyut idealler olarak değil, Sistem Sertifikasyon Kaydının somut gereklilikleri olarak düzenler. Dörtlünün **gözetim** ayağı altında gözetim denetimi gerektirir. Sistem uyum sertifikasyonu özellikle büyük bir denetim sürecidir ve burada belirtilen tabanları karşılamalıdır. [Madde XVI](../../core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification) (*Denetim, Şeffaflık ve Bağımsız Doğrulama*) veya diğer denetim biçimlerinin sahibi değildir ve bunların yerini almaz. Sentientlerin itiraz edebilmesi gerekliliği [§10 Sertifikasyona İtiraz](#10-sertifikasyona-itiraz) bölümündedir.*
Bu bölüm [Şeffaflık](../../core_05.050_band_oversight.md#transparency) ve [Denetlenebilirlik](../../core_05.050_band_oversight.md#auditability) gerekliliklerini Sistem Sertifikasyon Kayıtlarına uygular. Bunlar, bütün Sistem Sertifikasyon Kaydını kapsayan [Kayıt Bütünlüğünün](../../core_05.035_band_accountability.md#record-integrity) “erişilebilir” ve “yeniden oluşturulabilir” parçalarıdır ([§8 Sistem Sertifikasyon Kaydı](#8-sistem-belgelendirme-kaydı)). Kanonik terimlerin yeri ve sorumluluk sınırları [Önsöz — anayasal sorumluluk sicilinde](../../core_00.000_preamble.md#4-principles-definitions-and-rights) ve [Yetki Katmanı ve İç Hiyerarşide](../../core_05.045_band_integrative.md#owner-non-relocation) bulunur. [Anayasal Dörtlü](../../core_00.000_preamble.md#constitutional-tetrad) kapsamında:
**Denetlenebilirlik** — sentientler Sistem Sertifikasyon Kaydını yeniden oluşturup kontrol edebilmelidir:
  - Kayıt Sürümleri arasında neyin değiştiği, her değişikliği kimin, hangi yetkiyle ve kimin isteğiyle yaptığı; yeni bir Sistem Sertifikasyon Kaydı içinse, önceki tamamlanmış Sistem Sertifikasyon Kaydından bu yana neyin değiştiği;
  - [§8](#8-sistem-belgelendirme-kaydı) (*her yeniden sertifikasyonun veya yeniden açılan incelemenin izlediği tamamlanmış Sistem Sertifikasyon Kaydı*);
- Alt akış: [§11.3](#113-doğrulanmış-girdi-kapısı-bir-belgelendirme-kaydı-yalnızca-sınırlı-izlenebilir-itiraz-edilebilir-ve-şunlar-altında-doğrulanmış-olduğunda-sekizinci-bölüm-güzergâhına-beslenebilir) ve [§11.5 İhlal statüsü kaydı](#115-ihlal-statüsü-kaydı) (*olgular olumsuz bulguları desteklediğinde doğrulanmış girdi kapısı*); [On Beşinci Bölüm](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (15.000) (*yeniden açılan forum gözetimi*); [On Birinci Bölüm](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (11.000).
  - [§9.1](#91-yeniden-sertifikasyon-takvimi-ve-yeni-sistem-sertifikasyon-kaydı) (*yeniden sertifikasyon takvimi ve yeni Sistem Sertifikasyon Kaydı*);

<a id="9-recertification-and-reopening"></a>

### 9. Yeniden sertifikasyon ve yeniden açma

<details>
<summary><strong><span style="color: #2563eb;">İzleme</span></strong></summary>

- Önceki dayanaklar:
  - [B Bölümü §7](core_09.005_system_alignment_certification_record_process.md#7-sertifikasyon-sonuçları) (*yürürlükteki sonuç*);
  - [§8](#8-sistem-belgelendirme-kaydı) (*her yeniden sertifikasyonun veya yeniden açılan incelemenin izlediği tamamlanmış Sistem Sertifikasyon Kaydı*);
  - [A Bölümü §2](core_09.000_system_alignment_certification_evaluation.md#2-sistem-sınıfı-değerlendirmesi) (9.000 §2) ile
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-hak-tabanı-ve-alan-değerlendirmeleri) (*değerlendirmede bulunan yanlış sınıflandırma, uyumsuzluk ve kusurlar*);
  - [§10](#10-sertifikasyona-itiraz) (*inandırıcı itiraz*);
  - [İki Anayasal Amaç](../../core_00.000_preamble.md#two-constitutional-aims);
  - [Üçüncü Bölüm §1](../../core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) ve
  - [§2](../../core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*tanım bütünlüğü ve kaçınma*);
  - [Sistem Şartı](../../core_05.040_band_continuity.md#system-charter) (*Sistem Şartı-davranış uyuşmazlığı ve süresi geçmiş inceleme*).
- Sonraki etkiler: [§11.3](#113-doğrulanmış-girdi-kapısı-bir-belgelendirme-kaydı-yalnızca-sınırlı-izlenebilir-itiraz-edilebilir-ve-şunlar-altında-doğrulanmış-olduğunda-sekizinci-bölüm-güzergâhına-beslenebilir) ve [§11.5](#115-ihlal-statüsü-kaydı) (*olumsuz bulgular olgularla desteklendiğinde doğrulanmış girdi kapısı*); [On Beşinci Bölüm](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (15.000) (*yeniden açılan forum gözetimi*); [On Birinci Bölüm](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (11.000).
- Şunlarla birlikte okuyun: **[CS-6.305 §5](../../corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Yeniden sınıflandırma ve yaşam döngüsü yönetişimi*) ve **[CS-9.305 §3](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Yeniden sınıflandırma gerekliliği*).
- Alt bölümler:
  - [§9.1](#91-yeniden-sertifikasyon-takvimi-ve-yeni-sistem-sertifikasyon-kaydı) (*yeniden sertifikasyon takvimi ve yeni Sistem Sertifikasyon Kaydı*);
  - [§9.2](#92-yeniden-açma-tetikleyicileri) (*yeniden açma tetikleyicileri*);
  - [§9.3](#93-geçici-ve-tam-belgelendirme) (*geçici ve tam sertifikasyon*; şunları içerir:
  - [§9.3.1 İki statü](#931-iki-statü),
  - [§9.3.2 Başarısızlık ve alt kademeye geçiş](#932-başarısızlık-ve-statü-düşürme),
  - [§9.3.3 Uyumsuzluğun nedeni](#933-uyumsuzluğun-nedeni),
  - [§9.3.4 Kademe süreleri](#934-kademe-süreleri),
  - [§9.3.5 A Sınıfı bağımlılığı](#935-a-sınıfına-güvenerek-kullanım) ve
  - [§9.3.6 İddia değil, doğrulama](#936-iddia-değil-doğrulama));
  - [§9.4](#94-kaçınmama) (*kaçınma yasağı*).

</details>


*Yalın dille: hiçbir sonuç sonsuza dek sürmez. Sistem çalışırken adı belirtilmiş sorumlular gerçek sonuçları ve güvenceleri izler, olaylara ve itirazlara yanıt verir ve Sistem Sertifikasyon Kaydındaki koşulları yerine getirir. Sertifikalı sistem, sınıfına göre belirlenen takvimde yeniden sertifikalandırılır ve her aralığın ortasında denetlenir. Önemli olgular değiştiğinde veya güvenilir bir itiraz gerektirdiğinde inceleme yeniden açılır. Kusurlar koruma, düzeltme ve bağımsız doğrulamayı gerektirir. Her inceleme geçişi, önceki kayda bağlı yeni bir Sistem Sertifikasyon Kaydıyla başlar; yeni kayıt eski kaydı veya ona yönelik itirazları silmez. Eski bir onay, güncel Hak Tabanı uyumunun yerine geçemez.*
**Doğrulama.** On Beşinci Bölüm, mevcut bir sistemin forum incelemesine *süregelen uyum doğrulaması* adını verir. Bu bölümde doğrulama ayrı bir süreç değil, zaten işletimde olan bir sistem için sertifikasyon geçişidir: yeniden sertifikasyon veya yeniden açılmış ya da yeni bir inceleme. Diğer sertifikasyon geçişleri gibi [B Kısmı §6 Forum Sürecinden](core_09.005_system_alignment_certification_record_process.md#6-forum-süreci) geçer ve [B Kısmı §7 Sertifikasyon Sonuçları](core_09.005_system_alignment_certification_record_process.md#7-sertifikasyon-sonuçları) uyarınca bir sonuçla biter.
**İzleme ve yanıt.** İşletmeciler ve gözetmenler [§8.1 Asgari kayıt içeriği](#81-asgari-kayıt-içerikleri) uyarınca Sistem Sertifikasyon Kaydındaki işletim planını yerine getirmelidir. Adı belirtilmiş sorumlular:

- izleme kanıtlarını korumak;
- önemli olayları ve göstergeleri araştırmak;
- itirazları atanmış makama yönlendirmek; ve
- gerekli geçici korumayı ve düzeltici çalışmayı yürütmek.

Aşağıdakilerden herhangi biri uyumu önemli ölçüde sorgulatıyorsa, bu bölüm uyarınca forumun zamanında incelemesi gerekir; bir sonraki planlı yeniden sertifikasyona kadar beklenemez:

- bir olay;
- yerine getirilmemiş bir sertifikasyon koşulu;
- [Bölüm B §7.3 Giderime Hazırlık: Düzeltme İsteği ve Kapasitesi](core_09.005_system_alignment_certification_record_process.md#73-giderime-hazırlık-düzeltme-isteği-ve-kapasitesi) kapsamındaki kaçırılmış kanıtlama adımı;
- hazırlığa ilişkin yanlış kanıt; veya
- güvenilir bir itiraz.

Sertifikasyon koşullarının düzeltilmesi, yerine getirilmesi ve kaldırılması [Bölüm B §7 Sertifikasyon sonuçları](core_09.005_system_alignment_certification_record_process.md#7-sertifikasyon-sonuçları) içindeki bağımsız doğrulama gereklerine tabidir.

<a id="91-recertification-schedule-and-the-new-system-certification-record"></a>
#### 9.1 Yeniden sertifikasyon takvimi ve yeni Sistem Sertifikasyon Kaydı
*Yalın dille: sertifikasyon süresiz değildir. Sistem, sınıfına göre belirlenen takvimde yeniden sertifikasyona girer ve her aralığın ortasında denetlenir. Her sertifikasyon geçişi, önceki kayda bağlı yeni bir Sistem Sertifikasyon Kaydı açar.*
Bir **Sistem Sertifikasyon Kaydı**, sistem sınıfı için [On Beşinci Bölüm §6 Zamanında çözüm, önemlilik katmanları ve geciktirmeme disiplini](../../core_15.000_forum.md#review-cadence) (*İnceleme sıklığı*) uyarınca belirlenen aralıkta yeniden sertifikalandırılmalı ve bu aralığın ortasında denetlenmelidir.
**Her sertifikasyon geçişi için yeni kayıt.** Sonraki her sertifikasyon geçişi (yeniden sertifikasyon, yeniden açılmış inceleme veya yeni inceleme) yeni bir Sistem Sertifikasyon Kaydı açar. Yeni Sistem Sertifikasyon Kaydı:
- izlediği tamamlanmış Sistem Sertifikasyon Kaydına bağlantı verir ve o zamandan beri neyin değiştiğini belirtir ([§8.1.1 Sistem kimliği, kapsam ve önceki Sistem Sertifikasyon Kaydı](#811-sistem-kimliği-kapsam-ve-önceki-sistem-sertifikasyon-kaydı)); ve
Tamamlanmış Sistem Sertifikasyon Kaydı olduğu gibi kalır ([§8 Sistem Sertifikasyon Kaydı](#8-sistem-belgelendirme-kaydı)). Kapsadığı dönem için kayıt olmayı sürdürür ve [B Kısmı §6.3 İtiraz edilebilirlik zinciri](core_09.005_system_alignment_certification_record_process.md#63-itiraz-edilebilirlik-zinciri) uyarınca itiraza açık kalır. Sertifikasyon durumu, sorunsuz yeniden sertifikasyon sayısı ve izleme göstergeleri bağlantı üzerinden taşınır. Bunlar yeni Sistem Sertifikasyon Kaydında [§9.3 Geçici ve tam sertifikasyon](#93-geçici-ve-tam-belgelendirme) uyarınca doğrulanır.

<a id="92-reopening-triggers"></a>

#### 9.2 Yeniden açma tetikleyicileri

Bir **Sistem belgelendirme kaydı** **kapsama-sınırlı** ve **zamana-sınırlı**dır. Aşağıdakilerden herhangi biri maddi olduğunda inceleme On Beşinci Bölüm ve içerilmiş sistem uygulama ödevleri altında yeniden açılır:

- **Genel tetikleyiciler:**
  - sistemde, kullanımında ya da işletim bağlamında maddi değişim;
  - gizlenmiş davranış;
  - bağımlılık büyümesi;
  - bağımlılığın büyümesi; sisteme artan dayanmayı ve ortak temellerden artan çekişi, ayrıca ../../core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable içinde benimseyenin belirlediği eşiği aşan yoğunlaşmayı kapsar (kademe artışı eşiği beklemez; Bölüm A §2.2);
  - Orantılı Sistemler Arası Destek uyarınca, sistemin ortak temellere geri akışlarında önemli düşüş;
  - yeni risk;
  - olay tarihi;
  - etkilenen taraf kanıtı;
  - [§14](#10-sertifikasyona-itiraz) altında inandırıcı itiraz;
  - ekolojik itiraz;
  - **[CS-3 §3.5](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** altında sistem-sınıfı yanlış hizalanması ya da gecikmiş yeniden değerlendirme;
  - veri-türü ya da işleme yanlış hizalanması, **[CS-2 §5.2](../../corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** altında gecikmiş ya da atlanmış periyodik veri-türü yeniden değerlendirmesi;
  - sınıflama yanlış hizalanması;
  - [Kapsam belgesi](../../core_05.040_band_continuity.md) değişikliği, kapsam belgesi–davranış uyumsuzluğu, belgelenmiş kapsamın maddi olarak dışında işlem, ya da gecikmiş periyodik kapsam belgesi incelemesi;
  - Sistemi portföyünde tutan bir Kurumun yönetişim ihlali (yönetişimin başarısız olduğuna karar verilmesi, yönetişimle ilgili bir ret veya iptal gerekçesi ya da başka bir Sistemin yanlış hizalanmasının nedenini Kuruma bağlayan bulgu); yalnızca önemliyse yeniden açar — [Bölüm On §9.6](../../core_10.000_institutional_alignment_certification.md#96-reopening-the-institutions-systems) uyarınca;
- **Belgelendirme kaydına yansıyan alan yanlış hizalanması**, şunlar dahil:
  - [§3.1](core_07_a_system_alignment_certification_evaluation.md#31-sistemik-kapsam-ve-risk-etkenleri) altında maddi risk-değerlendirme ya da risk-açıklama kusuru ya da yanlış hizalanması;
  - [§5](core_07_a_system_alignment_certification_evaluation.md#51-ekolojik-ayak-izi-değerlendirmesi) altında maddi ayak izi yanlış temsili ya da yanlış hizalanması;
  - [§7](core_07_a_system_alignment_certification_evaluation.md#54-ayrımcılık-yapmama-değerlendirmesi) altında maddi ayrımcılık-örüntüsü yanlış hizalanması ya da vekil kaçınma;
  - [§8](core_07_a_system_alignment_certification_evaluation.md#55-erişilebilirlik-değerlendirmesi) altında maddi erişilebilirlik yanlış hizalanması ya da yalnızca-kâğıt uyarlama;
  - [§9](core_07_a_system_alignment_certification_evaluation.md#52-eğitim-kapasitesi-ve-öğrenme-sistemi-bütünlüğü-değerlendirmesi) altında maddi değerlendirme-opasitesi, kimlik kapılama ya da dayatılmış-eskiyiş yanlış hizalanması;
  - [§10](core_07_a_system_alignment_certification_evaluation.md#56-güvenilirlik-ve-sisteme-dayanma-bütünlüğü-değerlendirmesi) altında maddi sahte güven, sapkın teşvik ya da onarım-bütünlüğü yanlış hizalanması;
  - karşılık gelen maddilik tetikleyicisi uygulandığında diğer A Kısmı değerlendirme yanlış hizalanması — [§2](core_07_a_system_alignment_certification_evaluation.md#2-sistem-sınıfı-değerlendirmesi), [§4](core_07_a_system_alignment_certification_evaluation.md#34-veri-türleri-ve-işleme-değerlendirmesi) ve [§6](core_07_a_system_alignment_certification_evaluation.md#53-orantılı-sistemler-arası-destek-değerlendirmesi) dahil.

**Yeniden açmanın nedeni.** Yanlış hizalanma, bağımlılık büyümesi ya da inandırıcı itiraz üzerine yeniden açma, paylaşılan sistemlerin hayatta kalma esaslarının, eğitim erişiminin, yetkinlik-inşa adlandırılmış yollarının, güvenilir bel bağlamanın ya da güvenliğin kalıcı tedarikini kapıladığı yerde [İki Anayasal Amaç](core_00_preamble.md#two-constitutional-aims) altında **Süreklilik** amacını korur. Eski belgelendirme güncel Hak Tabanı uyumunun yerine geçmemelidir.

<a id="93-provisional-and-full-certification"></a>
#### 9.3 Geçici ve tam belgelendirme

*Sade anlatımla: Bir sistem güveni aşamalı olarak kazanır. Yeni sistemler ve değerlendirmede başarısız olan sistemler daha sıkı denetim altında başlar ve sık sık yeniden kontrol edilir. Yalnızca şu anda uyumsuzluğu ve yaklaşan uyumsuzluk belirtisi bulunmayan sistem daha uzun aralıklı tam belgelendirmeye geçer. Başarısız değerlendirme sistemi yeniden sıkı denetime döndürür.*

<a id="931-the-two-statuses"></a>
##### 9.3.1 İki statü

Belgelendirme iki statüden birindedir. Her statünün kendi aralığı, [§8.1 Asgari kayıt içeriği](#81-asgari-kayıt-içerikleri) uyarınca Sistem Belgelendirme Kaydında belirtilir:

- **[Geçici belgelendirme](../../core_05.040_band_continuity.md#provisional-certification)** sistemin ilk belgelendirme statüsüdür (yeni devreye alınan sistemler dâhil); başarısız yeniden belgelendirme, yeniden açılan inceleme veya uyumsuzluk bulan yeni inceleme sonrasında belgelendirilen sistem de bu statüdedir. Geçici aralık, aynı sistem sınıfındaki tam belgelendirme aralığından kısadır. Güven sınırları kayıtta belirtilir.
- **[Tam belgelendirme](../../core_05.040_band_continuity.md#full-certification)** yalnızca geçici statüdeki sistemin yeniden belgelendirilmesinde ve aşağıdaki üç koşulun tamamı sağlandığında kazanılır:
  1. benimsenen belgenin gerektirdiği sayıda, art arda temiz geçici yeniden belgelendirme tamamlanmış olmalı: en az bir, üst sistem sınıflarında daha fazla;
  2. güncel uyumsuzluk bulunmamalı: kayıtta açık uyumsuzluk, giderilmemiş kusur, gecikmiş kontrol veya başarısız regresyon testi olmamalı; ve
  3. izleme göstergelerinin hiçbiri yaklaşan uyumsuzluğa işaret etmemeli: kayıttaki tetikleyiciler ve eğilim ölçütleri eşik aşımı veya eşiğe yönelen eğilim göstermemeli.

Tam belgelendirme, sistem sınıfına göre belirlenmiş aralıkla sürer. Süreye bağlıdır; kalıcı onay değildir. Yeniden belgelendirme, 2. ve 3. koşulları karşılıyorsa **temiz** sayılır.

<details>
<summary><strong>Okuyucu rehberi (işletimsel değildir): belgelendirme statüsü</strong></summary>

> Bu tablo §9.3'ü özetler. Metinle çelişirse metin geçerlidir.
>
> | | Geçici | Tam |
> |---|---|---|
> | **Kim taşır** | İlk belgelendirme (yeni sistem dâhil) veya başarısız yeniden belgelendirme/uyumsuzluk bulan inceleme sonrası sistem | Geçici statüdeyken yeniden belgelendirmede bu statüyü kazanan sistem |
> | **Nasıl kazanılır** | Belgelendirme sonucu ile verilir | Gerekli sayıda temiz yeniden belgelendirme; güncel veya yaklaşan uyumsuzluk yok |
> | **Aralık** | Aynı sınıfın tam aralığından kısa | Sistem sınıfına göre; yine süreli |
> | **Yeniden belgelendirme başarısızsa** | B Bölümü §7 uygulanır; sonraki belgelendirme geçici olur ve temiz sayım sıfırlanır | Aynı sonuç |
> | **Yaklaşan uyumsuzluk göstergesi varsa** | Geçici kalır; sayım ilerlemez | Geçici statüye düşer |
>
</details>

<a id="932-failure-and-step-down"></a>
##### 9.3.2 Başarısızlık ve statü düşürme

Yeniden belgelendirme, yeniden açılmış inceleme veya yeni incelemenin bulgusu sistemin statüsünü belirler:

- Güncel uyumsuzluk bulan yeniden belgelendirme **başarısızdır**. [B Bölümü §7 Belgelendirme sonuçları](core_09.005_system_alignment_certification_record_process.md#7-sertifikasyon-sonuçları) sonuçları uygulanır. Sonraki kontrolden ne kadar temiz çıkarsa çıksın, sistemin kazanabileceği bir sonraki belgelendirme geçici olur; temiz yeniden belgelendirme sayısı sıfırdan başlar.
- Güncel uyumsuzluk yokken yaklaşan uyumsuzluk göstergesi varsa yeniden belgelendirme başarısız değildir, ancak temiz de değildir. Geçici statüdeki sistem geçici kalır ve sayımı ilerlemez; tam statüdeki sistem geçiciye düşer.
- [§9 Yeniden belgelendirme ve incelemenin yeniden açılması](#9-yeniden-sertifikasyon-ve-yeniden-açma) uyarınca açılan inceleme uyumsuzluk bulursa başarısız yeniden belgelendirme ile aynı sonuç doğar.
- Belgesi bulunan sistem hakkında yapılan yeni incelemenin güncel uyumsuzluk bulması da aynı sonucu doğurur. Sistemin belgelendirme statüsü yoksa [B Bölümü §7.4 Reddetme ve iptal](core_09.005_system_alignment_certification_record_process.md#74-ret-ve-iptal) kuralları uygulanır.

<a id="933-cause-of-misalignment"></a>
##### 9.3.3 Uyumsuzluğun nedeni

Değerlendirme, yeniden belgelendirme, yeniden açılan inceleme veya yeni inceleme uyumsuzluk bulduğunda Sistem Belgelendirme Kaydı nedeni şöyle belirtir:

- **tasarım kaynaklı:** sistem veya süreç, amaçlandığı gibi çalıştırıldığında bile uyumsuz sonuç üretecek şekilde kurulmuştur;
- **işletim kaynaklı:** tasarım görünüşte sağlamdır, ancak sistemin çalıştırılma, beslenme veya bakım biçimi sonuçları uyumsuz yapar; ya da
- **henüz belirlenmedi:** forum nedeni bulana dek tasarım ve işletime ilişkin giderimler açık kalır.

Neden tespiti şu sınırlar içinde işler:

- Sistem uyumsuz sonuç üretmeye devam ediyorsa, tasarımı kâğıt üzerinde sağlam görünse bile uyumsuzdur; sağlam görünen tasarım savunma değildir.
- Uyumsuz sonuç üretecek bir tasarım, sonuç ortaya çıkmadan önce de uyumsuzluktur.
- Neden tespiti aranacak giderimi ve yeniden açılan incelemenin kapsamını belirler; sistemin uyumsuz olup olmadığına karar vermez.

Uyumsuzluk tasarımdan kaynaklanıyorsa:

- yeniden tasarım uygulanıp doğrulanana kadar temiz yeniden belgelendirme sayısı sıfır kalır;
- nedeni bulan forum veya [B Bölümü §6.2 Gözetim sırası](core_09.005_system_alignment_certification_record_process.md#62-gözetim-sırası) uyarınca sıradaki görevlendirilen forum, yeniden tasarımı [eşleşen kabul hedef süresi](../../core_05.040_band_continuity.md#tier-window) içinde doğrular; bunu ilk geçici yeniden belgelendirmede de yapabilir;
- yeniden tasarım doğrulanmadan yapılan **bileşen değerlendirmesi** (B Bölümü §6.1'in tanımladığı belgelendirme geçişinin bir bileşene ait kısmı), ne kadar temiz olursa olsun temiz toplamına eklenmez; ve
- sistemin işletilme biçimindeki değişiklik bu adımı karşılamaz.

Bunlar yukarıdaki statü düşürme maddelerine eklenir, onların yerine geçmez. İşletici veya etkilenen herhangi bir hissedebilen varlık neden tespitinin incelenmesini isteyebilir; neden değişirse bu kurallar uygulanmaz.

<a id="934-tier-windows"></a>
##### 9.3.4 Kademe süreleri

İlk değerlendirme, yeniden belgelendirme, yeniden açılan inceleme veya yeni inceleme uyumsuzluk bulduğunda:

- konu [On Beşinci Bölüm §6 Zamanında çözüm, önemlilik kademeleri ve gecikmeyi önleme disiplini](../../core_15.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) uyarınca sınıflandırılır;
- varsayılan olarak sistemin sınıfına karşılık gelen kademeye yerleştirilir (örneğin uyumsuz A Sınıfı sistem, varsayılan olarak Kademe A'dır);
- kabul, kanıtı koruma, geçici koruma ve karar bu kademenin süre ve üst sınırlarına uyar; ve
- gecikme, söz konusu bölümün gerektirdiği şekilde incelenir.

<a id="935-class-a-reliance"></a>
##### 9.3.5 A Sınıfına güvenerek kullanım

Geçici belgelendirme tam belgelendirmeden daha kısa aralıklıdır; bu nedenle yeniden belgelendirme daha erken gelir ([§9.3.1 İki statü](#931-iki-statü)) ve güvenerek kullanma sınırları kayıtta belirtilir ([§8.1 Asgari kayıt içeriği](#81-asgari-kayıt-içerikleri)). Kesinti şöyle ele alınır:

- Geçici belgelendirme, kesinti ikameler gelmeden önce temel yaşam gereksinimlerini kesecekse, tek başına sistemi kesintiye uğratmayı gerektirmez;
- bu durum, B Bölümü §7 kapsamındaki geçici koruma ve belgelendirme koşullarıyla ele alınır;
- tasarım kaynaklı uyumsuzluk bulgusu sonrasında sayımın durdurulması sırasında da aynı kural geçerlidir: sayımın durması, hissedebilen varlıkların bağımlı olduğu sistemi tek başına kesintiye uğratmaz; ve
- durdurma sürdüğü müddetçe forum geçici korumayı, güvenerek kullanmaya ilişkin belgelendirme koşullarını ve bağımlılara yapılacak bildirimi belirtir.

<a id="936-verification-not-assertion"></a>
##### 9.3.6 İddia değil, doğrulama

Sistemin statüsü, temiz yeniden belgelendirme sayısı ve izleme göstergeleri doğrulanmalı; doğrulama bağımsız incelemeye açık olmalıdır. Sistemin kendi beyanı yeterli değildir:

- Göstergeler, uyumsuzluğun ortaya çıkamayacağı şekilde seçilemez veya ayarlanamaz.
- Yeniden tasarım da başkalarının denetleyebileceği kanıtlarla doğrulanır.
- Tam belgelendirme incelemeyi yeniden açma gerekçelerini ortadan kaldırmaz. [§9 Yeniden belgelendirme ve incelemenin yeniden açılması](#9-yeniden-sertifikasyon-ve-yeniden-açma) bölümündeki tüm tetikleyiciler geçerlidir.
- Kaçınma [§9.4 Kaçınmama](#94-kaçınmama) uyarınca ele alınır.

<a id="94-non-evasion"></a>

#### 9.4 Kaçınmama

**Kaçınma yasağı.** Bu bölümün yükümlülüklerinden kaçınma Üçüncü Bölüm tarafından yönetilir — bu bölüm o disiplini yeniden belirtmez:

- [Üçüncü Bölüm §1 — Tanım bütünlüğü ve kaçınma karşıtı kısıtlar](core_03_definition_integrity.md#1-tanım-bütünlüğü-ve-kaçınma-karşıtı-kısıtlar);
- [Üçüncü Bölüm §2 — Gözlemlenebilir sistem davranışından uyumsuzluk](core_03_definition_integrity.md#2-gözlemlenebilir-sistem-davranışından-uyumsuzluk);
- [§2.1 Yaygın kaçınma örüntüleri](core_03_definition_integrity.md#21-yaygın-kaçınma-örüntüleri) altında kapsam-ve-sınır kaçınması dahil.

*Kapanış notu:* Bu B Kısmı sürecindeki hiçbir tek adım kendi başına yeni ya da radikal değildir — kayıtlar, açıklama, inceleme, itiraz, forum rolleri, yeniden açma ve güzergâh girdileri tanıdık yönetişim araçlarıdır. Farklı olan, [Anayasal Dörtlü](core_00_preamble.md#constitutional-tetrad) altında onları birlikte işleten **tutarlılık**, **gözetim** ve **hesap verebilirliktir**: aynı disiplin sistem sınıfları ve forum aileleri boyunca uygulanır, iş görünür ve yeniden kurulabilir kalır, ve belgelendirme yanlış, eski ya da kaçınmacı olduğunda aktörler yanıt vermeye devam eder.

<a id="10-challenging-a-certification"></a>

### 10. Sertifikasyona itiraz

<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Ön bağlantılar:
  - [Bölüm B §6.3 İtiraz edilebilirlik zinciri](core_09.005_system_alignment_certification_record_process.md#63-itiraz-edilebilirlik-zinciri) (*itiraz yollarının işleyiş sırası*);
  - [Bölüm B §7](core_09.005_system_alignment_certification_record_process.md#7-sertifikasyon-sonuçları) (*itiraz edilebilecek sonuç*);
  - [§8](#8-sistem-belgelendirme-kaydı) (*itiraz yollarını belirten Sistem Sertifikasyon Kaydı*);
  - [Anayasal Dörtlü](../../core_00.000_preamble.md#constitutional-tetrad);
  - [Madde XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Zamanında çözüm ve gecikme karşıtı taban*).
- Sonraki bağlantılar: [§9](#9-yeniden-sertifikasyon-ve-yeniden-açma) (*güvenilir itiraz incelemeyi yeniden açar*); [On Beşinci Bölüm](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (15.000) (*itiraz edilen nokta için forum yolları*).
- Alt bölümler:
  - [§10.1](#101-yol-ne-zaman-açılır) (*yol ne zaman açılır*); and
  - [§10.2](#102-itiraz-yolları) (*itiraz yolları*).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Tanımlar · Değerlendirme · Uyum</span></strong></summary>

- [itiraz edilebilirlik](../../core_05.035_band_accountability.md#contestability) · [O](../../core_05.035_band_accountability.md#contestability) · [M](../../core_05.035_band_accountability.md#contestability-a) · [A](../../core_05.035_band_accountability.md#contestability-a) · [C](../../core_05.035_band_accountability.md#contestability-c)

</details>


Sistem Sertifikasyon Kaydı, sentientler yanlış olduğunda karşı çıkabiliyorsa işe yarar. İtiraz gerçek olmalıdır: incelemeyi yeniden açabilmeli, güvenerek kullanmayı durdurabilmeli ve uyuşmazlık konusu üzerinde yetkili foruma ulaşabilmelidir. Hiçbir şeyi değiştirmeyen bir şikâyet kutusu yeterli değildir.

Bu bölüm, [§9 Yeniden sertifikasyon ve yeniden açma](#9-yeniden-sertifikasyon-ve-yeniden-açma) ile birlikte, Faz VI (İşletim) alt evresi VIa’nın parçasıdır. Etkilenen tarafların Sistem Sertifikasyon Kaydına nasıl itiraz edeceğini açıklar. Yayımlanan kayıt itiraz yolu sonuç yayımlandığında açılır ([§10.1 Yol ne zaman açılır](#101-yol-ne-zaman-açılır)).

[Anayasal Dörtlü](../../core_00.000_preamble.md#constitutional-tetrad) kapsamında [itiraz edilebilirlik](../../core_05.035_band_accountability.md#contestability) hesap verebilirliği uygular ve katılımı açık tutar. [Madde XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) itiraz süreleri zamanındalığı uygular.

Etkilenen tarafların gerçek itiraz yolları olmalıdır. Kayıt §10.2 yollarını belirtmeli; içerik, kapsam, sınıflandırma varsayımları, kanıta dayanma, gözetim bütünlüğü, sonuç ve devam eden güveni itiraza elverişli kılmalıdır. Mekanizmalar törensel değil, işlevsel ve erişilebilir olmalıdır. İtiraz incelemeyi açabilmeli, önemli hata veya bütünlük riski inandırıcı biçimde gösterilince güvenerek kullanmayı durdurabilmeli/sınırlayabilmeli ve hukuki yetkisi olan forum ailesine yönlendirebilmelidir. Yükümlülükler sistem sınıfı ve maddi etkiye göre ölçeklenir; maddi etki varken sisteme deneysel, iç, kişisel, yalıtılmış veya yalnızca teknik denmesiyle ortadan kalkmaz.

<a id="101-when-the-path-opens"></a>

#### 10.1 Yol ne zaman açılır

*Basitçe: Birinden sertifikasyona dayanması istenmeden önce itiraz yolu açık olmalıdır. Henüz çalışmayan bir sistemde ilk sonuç yayımlandığında açılır. Zaten çalışan bir sistemde ise zaten açıktır.*

Yol ne zaman açılır ve ne kadar süre açık kalır:

- Henüz çalışmayan bir sistem için yayımlanmış kayıt itiraz yolu, sonuç ne olursa olsun, ilk sertifikasyon sonucu yayımlandığında açılır. Böylece [Part B §7.1 Go-Live Gate](core_09.005_system_alignment_certification_record_process.md#71-canlıya-geçiş-kapısı) uyarınca sistem devreye girmeden önce itiraz edilebilir ve dayanma askıya alınabilir.
- Zaten çalışan bir sistemin paydaşları vardır. Bu nedenle yolu zaten açıktır ya da sistem kaydı açıldığında açılır. Bu, [Article XXVIII-A](../../core_06.020_rights_part_e.md#xxviii-a-existing-instantiations-adoption-transition-window) (*Aşamalı Benimseme ve Haklar Tabanının Sürekliliği*) geçiş penceresindeki sistemi ve sonraki sertifikasyonu kapsar.
- **Paydaşlar**, sistemden esaslı biçimde etkilenen veya sisteme esaslı biçimde dayanan sentientlerdir; bunları işletmeci değil değerlendirme belirler.
- Henüz çalışmayan sistemin yolu açılana kadar Sistem Sertifikasyon Kaydı sistemi adlandırır ([Part B §6.2 Supervisory sequence](core_09.005_system_alignment_certification_record_process.md#62-gözetim-sırası)). [§10.2 Contestability paths](#102-itiraz-yolları) içindeki bileşen, lider-bütünlüğü ve yükseltme yolları inceleme boyunca kullanılabilir.
- Sistem paydaşlara sahip olduğu sürece yol açık kalır. Sertifikasyondan sonra paydaşlar ortaya çıkarsa [§9 Recertification and Reopening](#9-yeniden-sertifikasyon-ve-yeniden-açma) uyarınca inceleme yeniden açılır.
- Paydaşları olan bir sistem için Sistem Sertifikasyon Kaydına itiraz edecek açık yol yoksa, sistemin uyumlu olduğu iddiası dayanaksızdır.

<a id="102-contestability-paths"></a>

#### 10.2 İtiraz yolları

*Basitçe: Sistem Sertifikasyon Kaydı, itirazın nereye yapılacağını söylemelidir. Önce olağan ilk adım, sonra itiraz edilen bulguda yetkili forum, forum liderinin kendisi sorgulanıyorsa yedek yol ve yükseltme gelir. Beklemek zarar verecekse itiraz eden doğrudan foruma gidebilir.*

Etkilenen herkesin uyuşmazlığı nereye götüreceğini bilmesi için Sistem Sertifikasyon Kaydı aşağıdaki dört itiraz yolunu belirtmelidir. Bunlar Chapter Fifteen'daki [Dispute sequencing](../../core_15.000_forum.md#dispute-sequencing) kuralını Sistem Sertifikasyon Kayıtlarına uygular. Yeni bir forum değil, forumlara giden yollardır; yetkili forumu yine Chapter Fifteen belirler. Sıralama [Part B §6.3 Contestability chain](core_09.005_system_alignment_certification_record_process.md#63-itiraz-edilebilirlik-zinciri) içindedir.

- **Yayımlanmış kayıt itiraz yolu** — kayıt hakkındaki olağan uyuşmazlık için normal ilk adım. Kayıt, contest seat'i ([§6.1.1 Four seats in a certification](core_09.005_system_alignment_certification_record_process.md#611-bir-sertifikasyondaki-dört-koltuk)) belirtir:
  - itirazı kimin aldığı;
  - nasıl sunulacağı; ve
  - [Article XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Zamanında Çözüm ve Gecikme Karşıtı Taban*) sürelerinin teslim alındığında başladığı.

  İşletmecinin iç incelemesi, satıcı tasdiki veya teknik onay bu yol değildir.
- **Bileşen forumu yolu** — kayıttaki tek bir bulguya itiraz içindir; bulguda yetkili Chapter Fifteen forum ailesine gider.
- **Lider-bütünlüğü yolu** — lider forumun sürecini yürütmesine; örneğin ele geçirilme, gizli bilgi, kendi çalışmasını inceleme veya sertifikasyonu erken bitmiş sayma durumlarına itiraz içindir. Lider forumun kendi kendisini yargılamaması için yedek forumla Integrity routing üzerinden işler.
- **Yükseltme yolu** — uyuşmazlığın Chapter Fifteen uyarınca başka veya daha üst foruma taşınmasıdır. Devir, başka foruma karar için soru gönderme, yedek yönlendirme veya forum aileleri arasında yükseltme buna dahildir. Başlıca çıkarlar başka yerdeyse, anayasal geçerlilik sorgulanıyorsa, yapısal düzeltme gerekiyorsa, iki forum ailesi çıkmaza girdiyse veya forum kendisini yargılayacaksa uygulanır.

Gecikme hakları, kanıtları, bağımsızlığı veya pratik iyileştirmeyi esaslı biçimde tehlikeye atabilecekse forum yoluna doğrudan erişim sürer. Yayımlanmış kayıt itiraz yolunun tamamlanmamış kullanımı forum yollarını engellememeli veya [Article XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) sürelerini tüketmemelidir.

<a id="11-relationship-to-standing"></a>

### 11. Güzergâhla ilişki

<details>
<summary><strong>İz</strong></summary>

- Önceki dayanaklar:
  - [Part B §6](core_09.005_system_alignment_certification_record_process.md#6-forum-süreci) through
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-sertifikasyon-sonuçları) (*forum süreci, Sistem Sertifikasyon Kaydı ve sonuçlar*);
  - [Constitutional Tetrad](../../core_00.000_preamble.md#constitutional-tetrad);
  - [Two Constitutional Aims](../../core_00.000_preamble.md#two-constitutional-aims);
  - [Verified Inputs for Standing](../../core_05.035_band_accountability.md#verified-inputs-for-standing).
- Sonraki dayanaklar: [On Birinci Bölüm](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (*güzergâh kayıtları ve doğrulanmış-girdi kapısı*); [On Üçüncü Bölüm](../../core_13.000_standing_integration.md#chapter-thirteen-standing-effects-and-integration) (*güzergâh etkileri ve bütünleştirme*).
- Birlikte okuyun: **Article III-A** (*sertifikasyonun teslimatı koşulladığı yerde yaşamsal ihtiyaçlara erişim*).
- Alt bölümler:
  - [§11.1](#111-belgelendirmenin-sağlayabileceği--iki-anayasal-amaç-altında-ve-yalnızca-aşağıdaki-sekizinci-bölüm-doğrulanmış-girdi-kapısı-üzerinden) (*Sistem Sertifikasyon Kaydının güzergâha aktarabileceği*);
  - [§11.2](#112-sonuç-ne-olursa-olsun-sistem-sistem-sertifikasyon-kaydı-üzerinden-güzergâha-girdi-sağlar-geçici-veya-tam-sertifikasyon-koşullu-ya-da-koşulsuz-koşullu-veya-ertelenmiş-sertifikasyon-ret-geri-çekme-süre-sonu-veya-başka-bir-sonuç-buna-ilk-sertifikasyon-ve-hiç-sertifikasyon-almamış-bir-sistem-de-dahildir-sertifikasyon-sürecindeki-bulgular-ilk-ve-sonraki-her-geçişte-aynı-koşullarla-güzergâha-girdi-sağlar-geri-çekme-süre-sonu-veya-sertifikasyonun-başka-biçimde-kaybı-sertifikasyon-süresinde-ortaya-çıkan-doğrulanmış-olguları-dışlamaz-tüm-girdiler-aşağıdaki-doğrulanmış-girdi-kapısına-tabidir) (*her sertifikasyon sonucu*);
  - [§11.3](#113-doğrulanmış-girdi-kapısı-bir-belgelendirme-kaydı-yalnızca-sınırlı-izlenebilir-itiraz-edilebilir-ve-şunlar-altında-doğrulanmış-olduğunda-sekizinci-bölüm-güzergâhına-beslenebilir) (*doğrulanmış-girdi kapısı*);
  - [§11.4](#114-katkı-statüsü-kaydı) (*katkı güzergâh kaydı*); ve
  - [§11.5](#115-ihlal-statüsü-kaydı) (*ihlal güzergâh kaydı*).

</details>


*Yalın dille: belgelendirme güzergâha beslenebilir, ama güzergâh değildir. İyi ya da kötü bir belgelendirme kaydı Sekizinci Bölüme doğrulanmış olgular sağlayabilir — yalnızca sıkı bir kapı üzerinden — ve güzergâh kayıtlarını ve etkilerini yalnızca Sekizinci ve Dokuzuncu Bölümler kararlaştırır.*

<a id="111-what-a-system-certification-record-can-pass-on-to-standing"></a>

#### 11.1 **Belgelendirmenin sağlayabileceği** — [İki Anayasal Amaç](core_00_preamble.md#two-constitutional-aims) altında, ve yalnızca aşağıdaki Sekizinci Bölüm doğrulanmış-girdi kapısı üzerinden:

- Hak Tabanı-uyumlu hizalamayı doğrulayan kayıtlar doğrulanmış **Gelişim**-yanı girdi sağlayabilir;
- Yanlış sınıflamayı, gizlenmiş kusurları ya da tabanı yenen işlemi belgeleyen kayıtlar doğrulanmış **Hesap verebilirlik**-yanı girdi sağlayabilir.

<a id="112-every-certification-outcome"></a>

#### 11.2 Sonuç ne olursa olsun, sistem Sistem Sertifikasyon Kaydı üzerinden güzergâha girdi sağlar: geçici veya tam sertifikasyon (koşullu ya da koşulsuz), koşullu veya ertelenmiş sertifikasyon, ret, geri çekme, süre sonu veya başka bir sonuç. Buna ilk sertifikasyon ve hiç sertifikasyon almamış bir sistem de dahildir. Sertifikasyon sürecindeki bulgular ilk ve sonraki her geçişte aynı koşullarla güzergâha girdi sağlar. Geri çekme, süre sonu veya sertifikasyonun başka biçimde kaybı, sertifikasyon süresinde ortaya çıkan doğrulanmış olguları dışlamaz. Tüm girdiler aşağıdaki doğrulanmış-girdi kapısına tabidir.

Sistemin henüz uyumlu olmadığı bulgusu tek başına ihlal değildir. Sertifikasyon geçişi sorunları bulup düzeltmek içindir. İşletmeci tutarlı ve dürüst çaba gösteriyor, ihmal etmiyorsa ihlal bulgusu olası değildir. Güzergâh girdisi, olumsuz sınıflamayı ve belirli aktöre atfı destekleyen olgular gerektirir ([§11.5 İhlal güzergâh kaydı](#115-ihlal-statüsü-kaydı)); işletmecinin sorunu düzeltmek istediği ancak yapamadığı yönündeki hazırlık bulgusu bu olguları sağlamaz ([Bölüm B §7.5 Ret ve iptalin etkileri](core_09.005_system_alignment_certification_record_process.md#75-reddin-ve-geri-almanın-sonuçları)). Bunların hiçbiri ihmali, gizlemeyi veya yanlış kanıtı kapsamaz.

<a id="113-verified-input-gate"></a>

#### 11.3 **Doğrulanmış-girdi kapısı.** Bir belgelendirme kaydı yalnızca sınırlı, izlenebilir, itiraz edilebilir ve şunlar altında doğrulanmış olduğunda Sekizinci Bölüm güzergâhına beslenebilir:

- [§2](core_07_a_system_alignment_certification_evaluation.md#2-sistem-sınıfı-değerlendirmesi) (*sistem sınıfı*);
- [§4](core_07_a_system_alignment_certification_evaluation.md#34-veri-türleri-ve-işleme-değerlendirmesi) (*veri türleri ve işleme*);
- [§5](core_07_a_system_alignment_certification_evaluation.md#51-ekolojik-ayak-izi-değerlendirmesi) maddi olduğunda;
- [§6](core_07_a_system_alignment_certification_evaluation.md#53-orantılı-sistemler-arası-destek-değerlendirmesi) **Madde IV** (*Kaynak tahsisi, bağımlılıklar ve ekosistem finansmanı*) maddilik tetikleyicisi uygulandığında;
- [§7](core_07_a_system_alignment_certification_evaluation.md#54-ayrımcılık-yapmama-değerlendirmesi) **Madde V-B** (*Ayrımcılık yasağı*) maddilik tetikleyicisi uygulandığında;
- [§8](core_07_a_system_alignment_certification_evaluation.md#55-erişilebilirlik-değerlendirmesi) **Madde V-G** (*Erişilebilirlik*) maddilik tetikleyicisi uygulandığında;
- [§9](core_07_a_system_alignment_certification_evaluation.md#52-eğitim-kapasitesi-ve-öğrenme-sistemi-bütünlüğü-değerlendirmesi) **Madde VI** (*Algılayan-merkezli eğitim hakkı*) maddilik tetikleyicisi uygulandığında;
- [§10](core_07_a_system_alignment_certification_evaluation.md#56-güvenilirlik-ve-sisteme-dayanma-bütünlüğü-değerlendirmesi) **Madde XIII** (*Sağlam ve güvenilir sistemlere hak*) maddilik tetikleyicisi uygulandığında;
- [§12](#82-sistem-sertifikasyon-kaydının-şeffaflığı-ve-denetlenebilirliği) ve [§14](#10-sertifikasyona-itiraz);
- İkinci Bölümden Dördüncü Bölüme, ve uygulanan On Birinci Bölüm süreci.

<a id="114-contribution-standing-record"></a>

#### 11.4 Katkı statüsü kaydı

Olumlu sertifikasyon, doğrulama, yeniden sertifikasyon, iyileştirmenin tamamlanması veya bir sertifikasyon koşulunun yerine getirilmesi ya da kaldırılması, aşağıdakileri gösterdiğinde **katkı statüsü kaydı** için doğrulanmış girdi sağlayabilir:

- anayasal fayda;
- yetkin gözetim;
- güvenli yetki devrine hazırlık;
- sistem optimizasyonu;
- özen; veya
- anayasal uyum.

<a id="115-violation-standing-record"></a>

#### 11.5 İhlal statüsü kaydı

Olgular olumsuz sınıflandırmayı ve eylemi gerçekleştiren kişiye özgü atfı destekliyorsa, Sistem Sertifikasyon Kaydındaki şu unsurlar **ihlal statüsü kaydı** için doğrulanmış girdi sağlayabilir:

- sertifikasyonun geri alınması;
- gizlenmiş yanlış sınıflandırma;
- başarısız yeniden sertifikasyon;
- gerektiği halde yeniden sertifikasyonda başarısız olan veya yapılmayan regresyon testi;
- hileli sertifikasyon kanıtı;
- sertifikasyon koşulunun esaslı ihlali;
- sertifikalı kapsam dışında doğrulanmış işletim;
- sistem sınıfına uygun olmayan altyapı kırılganlığı; ve
- gerekli bir Bölüm A değerlendirmesinde bulunan esaslı kusur; buna şunlar dahildir:
  - [§3.4 Data Types and Handling Evaluation](core_09.000_system_alignment_certification_evaluation.md#34-veri-türleri-ve-işleme-değerlendirmesi) kapsamındaki veri işleme kusuru;
  - sistemik risk kapsam dahilindeyken [§3.2.2 Defects and Misalignment](core_09.000_system_alignment_certification_evaluation.md#322-kusurlar-ve-uyumsuzluk) kapsamındaki risk değerlendirme veya risk açıklama kusuru;
  - açıklama gerektiğinde [§5.1 Ecological Footprint Evaluation](core_09.000_system_alignment_certification_evaluation.md#51-ekolojik-ayak-izi-değerlendirmesi) kapsamındaki ekolojik ayak izinin yanlış sunulması;
  - [§5.4 Nondiscrimination Evaluation](core_09.000_system_alignment_certification_evaluation.md#54-ayrımcılık-yapmama-değerlendirmesi) kapsamındaki ayrımcılık yapmama veya vekil ayrımcılığı kusuru;
  - [§5.5 Accessibility Evaluation](core_09.000_system_alignment_certification_evaluation.md#55-erişilebilirlik-değerlendirmesi) kapsamındaki erişilebilirlik veya anlamlı katılım kusuru;
  - [§5.2 Educational Capability and Learning-System Integrity Evaluation](core_09.000_system_alignment_certification_evaluation.md#52-eğitim-kapasitesi-ve-öğrenme-sistemi-bütünlüğü-değerlendirmesi) kapsamındaki eğitim kapasitesi, değerlendirme opaklığı, kimlik bilgisi kapı bekçiliği veya dayatılmış eskime kusuru; veya
  - [§5.6 Trustworthiness and System-Reliance Integrity Evaluation](core_09.000_system_alignment_certification_evaluation.md#56-güvenilirlik-ve-sisteme-güvenme-bütünlüğü-değerlendirmesi) kapsamındaki güvenilirlik, sahte güven, ters teşvik, erişilemeyen itiraz veya kurtarma bütünlüğü kusuru.
