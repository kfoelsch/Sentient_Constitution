### 4. İlgili Olduğu Durumlarda Değerlendirmeler

<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Üst kaynaklar: [§3](#3-whole-system-certification-evaluation) (*her zaman uygulanabilir alt aşama dâhil, tüm sistem değerlendirmesi*); [§2](#2-system-class-evaluation) (*sistem sınıfı değerlendirmesi*); [Birinci Bölüm §12 Sistemik Değerlendirme Gerekliliği](core_01.000_values_principles.md#12-systemic-evaluation-requirement) (1.000 §12).
- Alt kaynaklar:
  - [§4.1](#41-privacy-informational-joint-invocation) (*mahremiyet odakları*);
  - [§4.2](#42-voluntary-discontinuation-major-self-modification-and-exit-rights) (*çıkış hakları*);
  - [§4.3](#43-assembly-collective-organization-and-institutional-formation) (*toplanma ve muhalefet*);
  - [Kısım C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*kayıt içeriği*).
- Birlikte okuyun: [§5 Hak Tabanı ve Alan Değerlendirmeleri](#5-rights-floor-and-domain-evaluations) (*tetiklendiğinde uygulanan alt aşama*).

</details>

<br>

*Yalın dille: üç denetim yalnızca sistem gerçekten bu konulara dokunduğunda uygulanır: özel bilgilerin uygun biçimde korunup korunmadığı, algılayanların kapana kısılmadan ayrılıp ayrılamadığı ve grupların hâlâ örgütlenip muhalefet edebilip edemediği. Sistem bunlardan birine dokunuyorsa sertifikasyon bunu incelemelidir.*

Bu bölüm, II. Aşamanın (Değerlendir) IIb alt aşamasıdır. Yalnızca bir alt bölümün kendi tetikleyicisi karşılandığında uygulanan tüm sistem değerlendirmelerini bir araya getirir.

<a id="41-privacy-informational-joint-invocation"></a>
#### 4.1 Mahremiyetin (Bilgisel) Birlikte Uygulanması

<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Birlikte okuyun: Beşinci Bölüm [**Tan.C3** (*Mahremiyet (Bilgisel)* — eş düzeyli küme başı)](core_05.040_band_continuity.md#defc3-privacy-informational--peer-level-cluster-head) ve anlamın sahibi olan küme başının ana kaynağı [Mahremiyet (Bilgisel)](core_05.040_band_continuity.md#privacy-informational).

</details>

<br>

*Yalın dille: Altıncı Bölüm mahremiyet korumalarını tek bir düzenli köşede değil, çeşitli maddelere yayar. Bir sertifikasyon incelemesi bu korumalardan birden fazlasına dokunuyorsa incelemeyi yapanlar gerçekten uygulanabilir olanların her birini denetlemelidir. En kolay kutucuğu işaretleyip işi bitmiş saymak yeterli değildir.*

Bir sertifikasyon konusu Altıncı Bölümdeki birden fazla mahremiyet odağını esaslı biçimde ilgilendiriyorsa sertifikasyon bu odakların her birini ele almalıdır. Konuyu yalnızca tek bir odak kapsamında kapatmak yeterli değildir.

**Uygulanacak ilkeler.** Bunlar, odakların birlikte nasıl okunacağını belirler:

- *Birlikte değerlendirme.* Konu, başka bir odaktan kaçınılmasına olanak verecek biçimde tek bir odağa yönlendirilemez ([§15.1.1 Bölümlere Ayırmayı Önleme İlkesi](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle)).
- *Başka kaynaktan okuyarak gevşetme yok.* Her küme üyesinin yerel olarak belirtilen standardı kendi kapsamı içinde belirleyicidir; başka bir üyeden daha gevşek bir standart aktararak gevşetilemez ([§15.1.1 Bölümlere Ayırmayı Önleme İlkesi](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle)).
- *Tür asgarileri korunur.* Bu etken, kapsam içindeki verilere uygulanan hiçbir **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Bilgi türleri ve işlenmesi*) ve [CS-6.310](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** (*Veri sınıflandırmaları*) türünün işlenmesini daraltmaz. Uygulanabilir her türün erişim düzeni ve [CS-6.310 Kısım B §9](corpus_systems/cs_06.310_data_classifications.md#cs-6310-9-data-classifications) (*Veri sınıflandırmaları*) kapsamındaki işleme yükümlülükleri, o türün adlandırdığı [mahremiyet ana kaynakları](corpus_systems/cs_06.310_data_classifications.md#privacy-link) ile birlikte bütünüyle uygulanır.
- *En koruyucu tür belirleyicidir.* Aynı veriye birden fazla tür uyduğunda [CS-6.305 Kısım A §2](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-2-determination-of-classification) (*Sınıflandırmanın belirlenmesi*) uyarınca uygulanabilir en koruyucu işleme yöntemi belirleyicidir; bir türün işleme gereklerini karşılamak diğer türün gereklerini yerine getirmez.

**Küme odakları.** Dağıtık mahremiyet kapsamı, eriştiği veri türleriyle birlikte aşağıdakilerde yer alır:

- **Madde VII-A** (*Bedenin Öz Sahipliği*) — sağlık, biyometrik ve taşıyıcıya bağlı kayıtlar için [**Tür I**](corpus_systems/cs_06.310_data_classifications.md#95-type-i-identity-and-attribution-data);
- **Madde VII-B** (*Zihnin Öz Sahipliği*) — yeniden yapılandırılmaları veya çıkarım yoluyla belirlenmeleri dâhil iç durumlar için [**Tür N**](corpus_systems/cs_06.310_data_classifications.md#96-type-n-neurocognitive-and-internal-data);
- **Madde IX** (*Benzerlik, Deneyimsel Veri ve Yayın Hakları*):
  - [Madde IX-A](core_06.005_rights_part_b.md#article-ix-a-self-ownership-of-likeness-and-reputation) (*Benzerlik ve İtibarın Öz Sahipliği*) kapsamındaki benzerlik ve ses için **Tür I**;
  - [**Tür H**](corpus_systems/cs_06.310_data_classifications.md#94-type-h-historical-relational-transactional-and-participation-data), [Madde IX-B](core_06.005_rights_part_b.md#article-ix-b-experiential-and-derived-data-rights) (*Deneyimsel ve Türetilmiş Veri Hakları*) kapsamındaki deneyimsel ve etkileşimden türetilen veriler için; ve
  - [**Tür Y**](corpus_systems/cs_06.310_data_classifications.md#98-type-y-yours), [Madde IX-D](core_06.005_rights_part_b.md#article-ix-d-creative-work-training-data-use-and-anti-displacement) (*Yaratıcı Eser, Eğitim Verisi Kullanımı ve Yerinden Etmeyi Önleme*) kapsamındaki yaratıcıya ait eserler içindir; bu maddenin korumaları [**Tür W**](corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published), [**Tür U**](corpus_systems/cs_06.310_data_classifications.md#911-type-u-use-licensed) ve [**Tür T**](corpus_systems/cs_06.310_data_classifications.md#912-type-t-transferred) için de geçerliliğini korur ve yaratıcının [saklı hakları](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights) ile birlikte uygulanır;
- **Madde X-A** (*Eyleme Geçme Yetisi ve Manipülasyondan Özgürlük*) — yeniden yapılandırılmaları veya çıkarım yoluyla belirlenmeleri dâhil iç durumlar için [**Tür N**](corpus_systems/cs_06.310_data_classifications.md#96-type-n-neurocognitive-and-internal-data); ve
- **Madde XIV-A** (*Güvenlik, İstihbarat ve Gizli Gücün Sınırları*) — kısıtlı güvenlik ve soruşturma malzemeleri için [**Tür S**](corpus_systems/cs_06.310_data_classifications.md#97-type-s-safety-security-and-restricted-investigation-data); kısıtlama sona erdiğinde bu türün **H**, **I** veya **N** bileşenleri korumasını sürdürür.

**Sertifikasyonun göstermesi gerekenler:**

- *Katılıma olanak sağlama.* [Mahremiyet (Bilgisel)](core_05.040_band_continuity.md#privacy-informational), esaslı [Katılıma](core_05.025_apex_participation_leg.md#participation-constitutional) olanak sağlar. Sertifikasyon; söz hakkını, müzakereyi, örgütlenmeyi ve itirazı destekleyen mahremiyet korumalarının bölümlere ayırma, başka kaynaktan okuma veya ifşa baskısı yoluyla etkisiz kılınmadığını doğrulamalıdır.
- *Açık ve denetime erişilebilir türler.* Asgari güvenceler her iki yönde de geçerlidir:
  - **Tür E**, **Tür G** veya **Tür O** kapsamındaki malzemede bulunan kişisel, ilişkisel ya da iç durumlara ilişkin içerik, **H**, **I** veya **N** işleme gereklerini korur;
  - bir mahremiyet odağı tek başına, **Tür O** veya **Tür E** verisinin kendi kurallarının izin verdiği dar kapsamlı alıkoymaların ötesinde saklanmasını haklı çıkarmaz; ve
  - bir kişinin mahremiyetini korumak ile kamuoyunun hakkı olan bilgiyi yayımlamak gerçekten çatıştığında hiçbir taraf kendiliğinden üstün gelmez: çatışma, [CS-6.305 §7](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems) (*A/B/C Sınıfı sistemler için Tür O taban çizgisi*) uyarınca açıkça ve kayıt üzerinde karara bağlanır.
- *Veri türlerine ilişkin kanıt.* Sertifikasyon, ulaştığı her mahremiyet odağı için [Sistem Veri Türleri Kaydını](core_05.040_band_continuity.md#system-data-types-record), [§3.4 Veri Türleri ve İşleme Değerlendirmesi](#34-data-types-and-handling-evaluation) uyarınca doğrulanmış biçimde, kanıt olarak kullanmalıdır: kapsam içindeki türler ile bunların amacı, alıcıları, dayanağı ve türetilmiş verileri. Bir mahremiyet odağı, bu kaydın göstermediği bir işleme dayanarak kapatılamaz.

<a id="42-voluntary-discontinuation-major-self-modification-and-exit-rights"></a>
#### 4.2 Gönüllü Olarak Sonlandırma, Esaslı Öz Değişiklik ve Çıkış Hakları

[Birinci Bölüm §7.4 Gönüllü Olarak Sonlandırma, Esaslı Öz Değişiklik ve Çıkış Hakları](core_01.000_values_principles.md#74-voluntary-discontinuation-and-exit-rights) bir sertifikasyon konusu bakımından uygulanıyorsa sertifikasyon iddiası geçerlilik kazanmadan önce gönüllülüğü, rızayı, zorlamayı önlemeyi, bağımlılık baskısını, bilgilendirmeyi ve geri döndürülebilirliği sınamalıdır. Yalnızca biçimsel onay yeterli değildir.

<a id="43-assembly-collective-organization-and-institutional-formation"></a>
#### 4.3 Toplanma, Kolektif Örgütlenme ve Kurumsal Oluşum

[Birinci Bölüm §7.2 Toplanma, Kolektif Örgütlenme ve Kurumsal Oluşum](core_01.000_values_principles.md#72-assembly-collective-organization-and-institutional-formation) bir sertifikasyon konusu bakımından uygulanıyorsa sertifikasyon, konuyu [Bölümlere Ayırmayı Önleme İlkesi](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle) uyarınca birlikte sınamalıdır. Konuyu yalnızca tek bir çerçeve üzerinden yönlendirerek toplanma veya kolektif örgütlenme korumasını etkisiz kılıyorsa değerlendirme tamamlanmış değildir.

<a id="431-dissent-and-peaceful-protest"></a>