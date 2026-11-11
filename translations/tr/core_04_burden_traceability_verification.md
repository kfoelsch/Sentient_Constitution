<a id="chapter-four-burden-of-proof-traceability-and-verification"></a>
# DÖRDÜNCÜ BÖLÜM: KANIT YÜKÜ, İZLENEBİLİRLİK VE DOĞRULAMA

<details>
<summary><strong><span style="color: #2563eb;">Corpus konumu (işlemsel değil): dosya yapısı ve okuma kuralları</span></strong></summary>

> Bu dosya, [İngilizce Dördüncü Bölüm](../../core_04.000_burden_traceability_verification.md)ün bir **okur-dili pilotudur**. Algılayanlar Anayasasının bağlayıcı bir parçası **değildir**. İkinci bir anayasa **değildir**. Bir gönderim baskısı **değildir**. `SC-Corpus-2026.08.09`a **sabitlenmiştir**. Bu çeviri ile İngilizce asıl görünür biçimde ayrışırsa, numaralı [`core_04_burden_traceability_verification.md`](../../core_04.000_burden_traceability_verification.md) kazanır. Okuma sırası ve baskı üstverisi [README.md](../../README.md)de tutulur. Yöntem ve sözlük: [translations/tr/README.md](README.md).
>
> **Önceki (bu dil):** [core_03_definition_integrity.md](core_03_definition_integrity.md)
>
> **Sonraki (bu dilde):** [core_05__definitions_home.md](core_05__definitions_home.md)
> **Okuma yayı:** §1 yük tahsisi → §2 iz haritası → §3 gözlemlenebilirlik → §4 güvenlik sınırları → §5 kanıt standardı → §6 belgelendirme katmanı sınırı (işlemsel değil)
> **Sonraki etkiler:** [Dokuzuncu Bölüm — Sistem Uyum Sertifikasyonu](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification); [On Birinci Bölüm — Durum Kayıtları](core_11_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Okur rehberi (işlemsel değil): Dördüncü Bölümün nerede yaşadığı ve burada neyin kaldığı</span></strong></summary>

> Nerede yaşar (gezinme):
> - **Dörtlü haritası:** Yük tahsisi, kanıt, izlenebilirlik, gözlemlenebilirlik ve doğrulama, [Önsöz](core_00_preamble.md#önsöz--temel-gerekler)de kurulan [Anayasal Dörtlü](core_00_preamble.md#constitutional-tetrad) **gözetim** ve **hesap verebilirlik** bacaklarını işlemsel kılar; maddi olarak gerektiğinde **katılım**, **3** ve **4**. kesitler altında pratik gözlemlenebilirlik ve bağımsız itiraz yoluyla. Gerekler [maddi pay](core_00_preamble.md#material-stake) ile ölçeklenir.
> - **Anayasal sorumluluk sahibi:** yükün dağıtımı, uyum kanıtı, tanım izlenebilirliği, gözlemlenebilirlik ve güvenlik kısıtlarına bağlı doğrulama. On Birinci Bölüm, bu bölümle birlikte okunan durum kaydı ve doğrulanmış girdi disiplininin sahibidir.
> - **Uygulama sahibi:** belirlenmiş uygulama dosyalarındaki dağıtım, veri-işleme ve güvence mekaniği bu kurallarla tutarlı kalmalıdır ve corpus zaten daha sıkı-kural mantığı sağladığında daha sıkı olabilir.
> - **Yer değiştirmeyi önleme kuralı:** Bu bölüm yalnızca yükü, izi, gözlemlenebilirliği, güvenlik sınırlarını ve kanıtı düzenler. Beşinci Bölüm tanımlarını, **On İkinci Bölüm** katkı veya durum ölçümünü ya da On Dördüncü Bölüm anayasa karşıtı kötü davranış ölçütlerini yeniden ifade etmez. Doğrulanmış uyumsuzluğun duruma yönlendirilmesini [Üçüncü Bölüm §3 — Uyumsuzluk Bulgusu Profilleri](core_03_definition_integrity.md#3-non-compliance-finding-profiles) ve [On Birinci Bölüm — Durum Kayıtları](core_11_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) düzenler. **Bölüm 6**, İkinci ila Dördüncü Bölümlerin [Dokuzuncu Bölüm — Sistem Uyum Sertifikasyonundan](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification) nasıl ayrıldığını belirtir.

</details>

<br>

Dördüncü Bölüm, **yük tahsisi, uyum kanıtı, tanım izlenebilirliği, gözlemlenebilirlik ve güvenlik-kısıtlı doğrulama**nın anayasal sahibidir.

*Yalın dille: kuralları izlediğinizi söylüyorsanız, bunu kanıtlamak zorundasınız — ve anayasanın tanımladığından algılayanların gerçekten gözlemleyebileceğine giden açık, denetlenebilir bir yol göstermek zorundasınız.*

<a id="1-exclusive-enforcement-and-burden-allocation"></a>
### 1. Münhasır yaptırım ve yük tahsisi

*Yalın dille: uyum iddia ediyorsanız, kanıtlarsınız — tek bir beş-adımlı denetimle. Herhangi bir adımı kaçırın, iddia düşer.*

- **İddia edenin yükü:** Uyumu gösterme yükü, onu iddia eden sistemin ya da aktörün üzerindedir.
- **Münhasır yaptırım yolu:** Bu bölümün başka yerlerinde anılan tüm değerlendirme standartları münhasıran bu bölümün **1** ile **5**. kesitleri aracılığıyla yaptırılır.
- **Bütünleşik zincir:** **1** ile **5**. kesitler tek bir doğrulama zincirini işler; herhangi bir kesitteki başarısızlık bütünü düşürür.

Sırayla okuyun. Her adım bir öncekinin üzerine kurulur; hiçbirini atlamayın.

| Adım | Yalın iş | Kesit |
| --- | --- | --- |
| **1 — Kim kanıtlar** | Yük, uyum iddiasında bulunana aittir | [§1 Münhasır Yaptırım ve Yük Dağılımı](#1-exclusive-enforcement-and-burden-allocation) |
| **2 — Haritayı göster** | Tanımlardan gözlemlenebilir davranışa yapılandırılmış iz | [§2 Tanım İzlenebilirliği Gereği](#2-definition-traceability-requirement) |
| **3 — Denetlenebilir kıl** | Sistemler, haritanın yalnızca teoride değil uygulamada da doğrulanmasına yetecek kadarını açığa çıkarmalıdır | [§3 İzlenebilirliğin Gözlemlenebilirliği Gereği](#3-observability-of-traceability-requirement) |
| **4 — Güvenlik sınırları** | Gerçek güvenlik sınırlarına izin verilir; bahane olarak engellemelere verilmez | [§4 Güvenlik Kısıtlı Gözlemlenebilirlik ve Doğrulama Kuralı](#4-security-constrained-observability-and-verification-rule) |
| **5 — Ne sayılır** | Kanıt gerçek, eksiksiz, bağımsız ve süreklilik taşıyan nitelikte olmalıdır | [§5 Uyum Kanıtı Standardı](#5-compliance-evidence-standard) |

**Sade dile erişim.** [Birinci Bölüm §5.2 — Sade Dilde Erişilebilirlik (Katılım ve Emanet Sorumluluğu Görevi)](core_01_a_values_principles.md#52-plain-language-accessibility-participation-and-stewardship-duty), sentient'ların haklarını kullanmak, kararlara itiraz etmek veya uyumu doğrulamak için kullandığı yönetişim, yargılama ve işletim materyallerine uygulanır. Sade dil, İkinci ila Dördüncü Bölümlerin gerekliliklerini **değiştirmez veya azaltmaz**. Sade dil sürümü buradaki tanım ya da doğrulama kurallarıyla çelişirse o kurallar geçerlidir. [İtiraz edilebilirlik](../../core_05.035_band_accountability.md#contestability) veya [Madde XVI: Denetim, Şeffaflık ve Bağımsız Doğrulama](core_06_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification) erişimini engellemek için jargon, katmanlı karmaşıklık veya kapalılık kullanılması, bu bölüm ve **Birinci Bölüm §5.2 Sade Dilde Erişilebilirlik (Katılım ve Emanet Sorumluluğu Görevi)** kapsamında uyumsuzluktur.

<a id="2-definition-traceability-requirement"></a>
### 2. Tanım izlenebilirliği gereği
<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Yukarı: [Dördüncü Bölüm, kesit 1 — Münhasır yaptırım ve yük tahsisi](#1-münhasır-yaptırım-ve-yük-tahsisi); [İkinci Bölüm, §1 — Amaç ve rol](core_02_definition_structure.md#1-amaç-ve-rol); [İkinci Bölüm, §2 Tanım bütünlüğü gereği](core_02_definition_structure.md#2-tanım-bütünlüğü-gereği); [Üçüncü Bölüm, kesit 1 — Tanım bütünlüğü ve kaçınma karşıtı kısıtlar](core_03_definition_integrity.md#1-tanım-bütünlüğü-ve-kaçınma-karşıtı-kısıtlar); [Üçüncü Bölüm, kesit 2 — Gözlemlenebilir sistem davranışından uyumsuzluk](core_03_definition_integrity.md#2-gözlemlenebilir-sistem-davranışından-uyumsuzluk) — maddi tanım ve uyumsuzluk kuralları; **§3** yalnızca iz-haritası gereğini belirtir ve o kuralları yeniden belirtmez.
- Aşağı: [Dördüncü Bölüm, kesit 3 — İzlenebilirliğin gözlemlenebilirliği gereği](#3-izlenebilirliğin-gözlemlenebilirliği-gereği); [Dördüncü Bölüm, kesit 4 — Güvenlik-kısıtlı gözlemlenebilirlik ve doğrulama kuralı](#4-güvenlik-kısıtlı-gözlemlenebilirlik-ve-doğrulama-kuralı); [Dördüncü Bölüm, kesit 5 — Uyum kanıtı standardı](#5-uyum-kanıtı-standardı).

</details>

<br>

*Yalın dille: her tanımın parçalarından — O, M, A ve C — sistemin gerçekten yaptığına giden denetlenebilir bir harita gösterin, **3** ile **5**. kesitler kimsenin bunu doğrulayıp doğrulayamayacağına ve kanıtın durup durmadığına hükmetmeden önce.*

Bu kesit bir **yapılandırılmış iz haritası** ister. Sistem davranışına maddi olarak uygulanan her tanım için — maddi olarak gereken her **Beşinci Bölüm** tanımı dahil — harita her parçayı **gözlemlenebilir** davranışa ve gerçek-dünya etkilerine bağlamalıdır:

- **nedir (O)** — terimin ne hakkında olduğu
- **Nasıl ölçülür (M)** — her katmanda hangi ölçütün uygulandığı
- **nasıl yargılanır (A)** — terimin nasıl değerlendirilmesi gerektiği
- **neyin geçerli kalması gerekir (C)** — pratikte neyin doğru olması gerektiği

İz haritası ayrıca:
- sistem güncellemeleri, sürüm değişiklikleri ve dağıtım bağlamları boyunca **sürdürülmüş** olmalıdır; zaman boyunca izlemeyi sürdürmemek uyumsuzluktur
- İkinci ve Üçüncü Bölümlerin istediği işletim ve değerlendirme koşulları altında **doğrulanmış** olmalıdır
- gözlemlenebilir ve bağımsız denetlenebilir terimlerle belirtilmiş olmalıdır — **3** ile **5**. kesitlerin, sistemin güvenlik sınırları altında doğrulamaya yeterince açık olup olmadığına ve kanıtın yeterli olup olmadığına karar verirken uyguladığı standart
- çift yönlü, öyle ki:
  - her tanım bileşeni (O/M/A/C) gözlemlenebilir sistem davranışına ve etkilere eşlenir, maddi olarak ilgili yerde doğrudan, dolaylı, gecikmeli ve toplanmış etkiler dahil
  - maddi olarak ilgili tüm sistem davranışları tam ve temsilî olarak eşlenmelidir, maddi olarak ilgili davranışların ya da koşulların dışarıda bırakılması olmadan

Maddi olarak gereken herhangi bir **Beşinci Bölüm** tanımını çağırmamak ya da doğru uygulamamak, ilişkili değerlendirmeyi, kanıtı ve uyum belirlemesini bütünüyle geçersiz kılar. Kısmi, seçici ya da temsilî olmayan izleme uyumsuzluktur.

<a id="3-observability-of-traceability-requirement"></a>
### 3. İzlenebilirliğin gözlemlenebilirliği gereği
<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Üst kaynak: İlkeler: [Dördüncü Bölüm, bölüm 3 — İzlenebilirliğin Gözlemlenebilirliği Gereği](#3-observability-of-traceability-requirement); [Birinci Bölüm, bölüm 6.2 — Epistemik Açıklama Kısıtları](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints) (1.005).
- Alt kaynak: [Dördüncü Bölüm, bölüm 5 — Uyum Kanıtı Standardı](#5-compliance-evidence-standard); **[CS-6.305](../../corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Bilgi türleri ve işleme*) ve [CS-6.310 — Veri sınıflandırmaları](../../corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** ve **[CS-6.340](../../corpus_systems/cs_06.340_system_requirements.md#cs-6340-system-requirements)** (*Sistem gereklilikleri*) — kullanıcıya dönük yetenek yüzeyleri, kimlik bilgileri ve bilgi türlerinin işlenmesi.
- Birlikte oku: [Beşinci Bölüm kümelenmiş tanımları (Öngörülebilirlik özeni)](../../core_05.050_band_oversight.md#foreseeability) — makul öngörülebilir koşullar altında pratikte ulaşılabilir olmayan kuramsal doğrulanabilirlik uyumsuzluktur.
- Birlikte oku: [Beşinci Bölüm kümelenmiş tanımları (Öngörülebilirlik özeni)](../../core_05.050_band_oversight.md#foreseeability) — tasarım-kaynaklı opaklık, en iyi durum işletimine değil, makul öngörülebilir koşullara karşı değerlendirilmelidir.

</details>

<strong><span style="color: #2563eb;">Tanım:</span></strong> [Öngörülebilirlik](../../core_05.050_band_oversight.md#foreseeability) · [O](../../core_05.050_band_oversight.md#foreseeability) · [M](../../core_05.050_band_oversight.md#foreseeability-diligence-a) · [A](../../core_05.050_band_oversight.md#foreseeability-diligence-a) · [C](../../core_05.050_band_oversight.md#foreseeability-diligence-c)

*Yalın dille: 2. kesit bir iz haritası ister — bu kesit, yetkilendirilmiş ya da etkilenen tarafların haritayı pratikte, yalnızca kuramda değil, denetleyebilmesi için sistemin kendinden yeterince açmasını ister. Opak mimari, dış bağımlılıklar ve kara kutu bileşenler muafiyet almaz.*

2. kesit bir iz haritası ister; bu kesit, o haritanın pratikte denetlenmesi için sistemin kendinden yeterince açmasını ister.

**Sistemler şunları yapmalıdır:**
- **2. kesiti** tam karşılamak için bileşenlere, veriye ve etkileşimlere yeterli **gözlemlenebilirlik, enstrümantasyon ve erişim** sağlamak — uygun biçimde yetkilendirilmiş ya da etkilenen taraflar için, orantılı yöntemler, kaynaklar ve erişim koşullarıyla
- uyumsuzluğu saptama, itiraz etme ve yanıt verme yeteneğini koruyan süreler içinde erişim sağlamak
- bilgiyi doğrulama için tam ve kullanılabilir olacak biçimde yapılandırmak — parçalama, toplama ya da gürültü yoluyla örtülmemiş
- bu bölümün değerlendirme koşulları altında maddi olarak ilgili herhangi bir O/M/A/C parçasını gözlemleyememek, ölçememek ya da doğrulayamamayı **uyumsuz** saymak
- sistem tasarımı, mimari opaklık, dış bağımlılıklar ya da üçüncü-taraf bileşenlerden gelen sınırlamaları, değişiklik, kısıt ya da dışlama yoluyla ele alınacak **tasarım başarısızlıkları** saymak
- tam izleme başarılamadığında etkilenen tanım parçalarını ve herhangi bir bağımlı uyum iddiasını **uyumsuz** saymak

*Sade ifadeyle: Bölüm 2 bir iz haritası ister — bu bölüm ise yetkili veya etkilenen tarafların haritayı uygulamada, yalnızca teoride değil, denetleyebilmesi için sistemin kendisinin yeterli bölümünü açığa çıkarmasını ister. Kapalı mimari, dış bağımlılıklar ve kara kutu bileşenler mazur görülmez.*
- bu gereğin **makul öngörülebilir** koşullar altında karşılanmasını engelleyen bileşenlere ya da bağımlılıklara bel bağlamak
- tasarım sınırlamalarını, mimari opaklığı, dış bağımlılıkları ya da üçüncü-taraf bileşenleri bu gereğin muafiyetleri saymak
- bağımsız doğrulamayı maddi olarak bozan maliyet, karmaşıklık, gecikme, erişim kısıtları ya da bilgisel koşullar dayatmak
- pratik doğrulama makul öngörülebilir koşullar altında ulaşılabilir değilken **kuramsal** doğrulanabilirliğe bel bağlamak
- sıkı gerekli olanın ötesinde, uyum iddia eden sisteme ya da aktöre bağımlılık istemek

Doğrulama teknik olarak mümkün ama pratikte ulaşılabilir değilse, uyum iddialarını **uyumsuz** sayın.

<a id="4-security-constrained-observability-and-verification-rule"></a>
### 4. Güvenlik-kısıtlı gözlemlenebilirlik ve doğrulama kuralı
<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Yukarı: İlkeler: [Dördüncü Bölüm, kesit 3 — İzlenebilirliğin gözlemlenebilirliği gereği](#3-izlenebilirliğin-gözlemlenebilirliği-gereği); [Birinci Bölüm, kesit 8.2 — Epistemik açıklama kısıtları](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints).
- Aşağı: [Dördüncü Bölüm, kesit 5 — Uyum kanıtı standardı](#5-uyum-kanıtı-standardı); [corpus_systems.md](../../corpus_systems.md), **CS-2 — Bilgi türleri ve işleme**, ve **CS-5** — işlemsel kriptografi, kimlik bilgileri ve bilgi-türü işleme.
- Birlikte oku: [Beşinci Bölüm kümelenmiş tanımları (Öngörülebilirlik özeni)](../../core_05.050_band_oversight.md#foreseeability) — makul öngörülebilir koşullar altında doğrulamayı öngörülebilir biçimde engelleyen tasarım seçimleri, belirtilmiş güvenlik gerekçesinden bağımsız olarak uyumsuzluktur; [Beşinci Bölüm Doğruluk (Anayasal kısıt)](../../core_05.050_band_oversight.md#truth-constitutional-constraint) ve [Beşinci Bölüm Güvenlik (Kısıt)](../../core_05.040_band_continuity.md#safety-constitutional-constraint) — kriptografik ve bilgi-türü işleme **2**, **3** ya da **5**. kesitlerin yerine geçmemelidir; ortam-ayrımı kısıtlarının maddi olduğu yerde **Articles VII-A**, **VII-B**, **XVI-A** ve **XVII-A**.

</details>

<strong><span style="color: #2563eb;">Tanım:</span></strong> [Öngörülebilirlik](../../core_05.050_band_oversight.md#foreseeability) · [O](../../core_05.050_band_oversight.md#foreseeability) · [M](../../core_05.050_band_oversight.md#foreseeability-diligence-a) · [A](../../core_05.050_band_oversight.md#foreseeability-diligence-a) · [C](../../core_05.050_band_oversight.md#foreseeability-diligence-c)

*Yalın dille: güvenlik, açıklamanın ya da denetimin nasıl, ne zaman ve kime olacağını daraltabilir — izleme, doğrulama ve bağımsız denetim ödevini silemez.*

3. kesit gözlemlenebilirlik ister. **Güvenlik, kötüye-kullanım önleme ve karşıt risk** açıklama, denetim ya da doğrulama üzerinde orantılı sınırları haklı kılabilir. O sınırlar **2** ve **3**. kesitlerdeki ödevleri **kaldırmaz**.

**Sistemler şunları yapmalıdır:**
- sömürü, dolanma ya da sistemik zarar dahil öngörülebilir riski hâlâ karşılayan **en az kısıtlayıcı** sınırı uygulamak, sistem etkisi, bağımlılık ve riske orantılı yöntemler kullanarak
- ulaşılabilir **azami** bağımsız denetim, doğrulama ve itiraz haklarını korumak
- herhangi bir sınırın **maddi olarak gerekli**, **orantılı**, **dar kapsamlı**, **denetlenebilir** ve **bahaneli olmayan** olmasını sağlamak; gerekçesi ve kapsamı **bağımsız doğrulanabilir** olmalıdır; yapılabilir olduğunda **zaman-sınırlı** olmalıdır
- **bağımsız geçerleme**yi uyum iddia eden sistemden ya da aktörden bağımsız tutmak

**Sistemler şunları yapmamalıdır:**
- maddi olarak ilgili uyum kanıtını yaratmaktan, sürdürmekten ya da bağımsız geçerlemeden kaçınmak için güvenlik, gizlilik ya da kötüye-kullanım riskine başvurmak
- makul öngörülebilir koşullar altında gözlemlenebilirliği, izlenebilirliği, doğrulanabilirliği ya da denetlenebilirliği öngörülebilir biçimde engelleyecek biçimde tasarlanmış ya da yapılandırılmış olmak

Bir sınır anlamlı bağımsız geçerlemeyi engellediğinde, ilişkili uyum iddiaları aşağıdakilerin tümü doğru olmadıkça **uyumsuzdur**:
- daha güvenli bir geçerleme yolu makul biçimde ulaşılabilir değildir
- o belirleme bağımsız gerekçelendirilmiş ve denetlenebilirdir
- kalan yöntem uyum belirlemesi için yeterli epistemik bütünlüğü korur

Kriptografi ve bilgi türlerinin işlenmesi Anayasa ile **[CS-6.305](../../corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Bilgi türleri ve işleme*) ve [CS-6.310 — Veri sınıflandırmaları](../../corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** ile uyumlu olmalı; önemli olduğu durumlarda bu bölüm kapsamında tam uyum doğrulamasına yine de izin vermelidir. Kriptografi ve bilgi türlerinin işlenmesi [Doğruluk (Anayasal Kısıt)](core_05_band_oversight.md#truth-constitutional-constraint) veya [Güvenlik (Anayasal Kısıt)](../../core_05.040_band_continuity.md#safety-constitutional-constraint) yerine ya da **2**, **3** veya **5. bölümlerdeki** yükümlülüklerin yerine geçemez.

<a id="5-compliance-evidence-standard"></a>
### 5. Uyum kanıtı standardı
<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Yukarı: [Dördüncü Bölüm, 1 ile 4. kesitler](#1-münhasır-yaptırım-ve-yük-tahsisi); [İkinci Bölüm, §1 — Amaç ve rol](core_02_definition_structure.md#1-amaç-ve-rol); [İkinci Bölüm, §2 Tanım bütünlüğü gereği](core_02_definition_structure.md#2-tanım-bütünlüğü-gereği); [İkinci Bölüm, §3 Tanım yığını boyunca tutarlılık](core_02_definition_structure.md#3-tanım-yığını-boyunca-tutarlılık); [Üçüncü Bölüm, kesit 1 — Tanım bütünlüğü ve kaçınma karşıtı kısıtlar](core_03_definition_integrity.md#1-tanım-bütünlüğü-ve-kaçınma-karşıtı-kısıtlar); [Üçüncü Bölüm, kesit 2 — Gözlemlenebilir sistem davranışından uyumsuzluk](core_03_definition_integrity.md#2-gözlemlenebilir-sistem-davranışından-uyumsuzluk); [Üçüncü Bölüm, §2.6 Belirsizlik bütünlüğü ve sömürmeme kısıtı](core_03_definition_integrity.md#26-belirsizlik-bütünlüğü-ve-sömürmeme-kısıtı) — maddi tanım ve uyumsuzluk kuralları; **§4** yalnızca kanıt-katmanı gereklerini belirtir ve o kuralları yeniden belirtmez.
- Alt kaynak: [On Birinci Bölüm — Durum Kayıtları](core_11_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (11.000).
- [Birinci Bölüm, §13 — Anayasal Çatışma Çözüm Süreci](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process) (1.005 §13);

</details>

<br>

*Yalın dille: kanıt gerçek olmalıdır — iz haritasına bağlı, gerçek koşullar altında denetlenmiş, mümkün olduğunda bağımsız, tam ve zaman boyunca süregelen. Seçmece anlık kesitler, yalnızca-vekil tasdikler ve kendine yarayan kanıt sayılmaz.*

**2** ile **4**. kesitler iz, gözlemlenebilirlik ve güvenlik sınırlarını koyar; bu kesit, **1. kesit** altındaki yükü karşılamak için kanıtın ne göstermesi gerektiğini belirtir. Standart [maddi pay](core_00_preamble.md#material-stake) ile ölçeklenir — sistem etkisi, bağımlılık ve risk.

**Kanıt şunları yapmalıdır:**
- gereken değerlendirme kapsamı ve koşulları altında **İkinci ve Üçüncü Bölümler**le uyumu göstermek, **2. kesit** altında uyumlu iz artefaktları ve **3. kesit** altında gözlemlenebilirlik dahil
- gerçek sistem davranışını, işletimini ve etkisini temsil eden koşullar altında üretilmiş ve değerlendirilmiş olmak
- **gözlemlenebilir**, **doğrulanabilir**, gereken kapsama görece **tam**, zaman boyunca **süregelen** ve sistem etkisi, bağımlılık ve riske orantılı titizlikte **yeterli** olmak ki bağımsız denetime ve karşıt sınamaya dayansın
- makul biçimde ulaşılabilir olduğunda **bağımsız geçerleme** kullanmak; yokluğu orantılılık kısıtları altında gerekçelendirilmelidir
- kanıt üretimi, açıklama ve doğrulama üzerindeki **4. kesit** kısıtlarına uymak, uygulandığında kriptografik ve bilgi-türü işleme dahil
- Aynı değerlendirmede anayasal değerler veya kısıtlar çatıştığında [Birinci Bölüm, §13 — Anayasal Çatışma Çözüm Süreci](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process) ile tutarlı kalın
- uyum, sınıflama ya da yönetişim için maddi **empirik**, **öngörücü** ya da **nedensel** iddialarda, orantılı olduğunda **bilimsel bütünlük** yansıtmak — denenebilir ya da incelenebilir yöntemler, belgelenmiş varsayımlar ve sınırlamalar, kararları ilgilendirdikleri yerde boş sonuçların ya da başarısız yinelemelerin bastırılmaması ve sonuçların yeni kanıtta revize edilebilir olması

**Aşağıdakiler 1. kesit altındaki kanıt yükünü karşılamaz:**
- [İkinci Bölüm, §2.1 Çekirdek bütünlük koşulları](core_02_definition_structure.md#21-çekirdek-bütünlük-koşulları) altında gereken herhangi bir tanımı ya da bileşeni karşılamamak, ya da [Üçüncü Bölüm, kesit 2 — Gözlemlenebilir sistem davranışından uyumsuzluk](core_03_definition_integrity.md#2-gözlemlenebilir-sistem-davranışından-uyumsuzluk) altında uyumsuzluk — bu bölüm altında tüm bağımlı uyum iddialarını geçersiz kılar
- bu bölüm altında var olan ya da gereken yerde gereken kanıtı sağlamamak
- sistemin uyum gösterimi sayıldığında [Üçüncü Bölüm, kesit 2](core_03_definition_integrity.md#2-gözlemlenebilir-sistem-davranışından-uyumsuzluk) altında uyumsuz olacak yalnızca-vekil, öz-tasdikli, kısmi ya da seçici kapsamlı kanıt
- yukarıdaki **Kanıt şunları yapmalıdır** gereklerini karşılamaya yetersiz kanıt

Belirsizlik, maddi olarak ilgili tanım bileşenleri için kesin uyum gösterimini engellediğinde, [Üçüncü Bölüm, §2.6 Belirsizlik bütünlüğü ve sömürmeme kısıtı](core_03_definition_integrity.md#26-belirsizlik-bütünlüğü-ve-sömürmeme-kısıtı)nı uygulayın. Kanıt yükü karşılanmadığında, varsayılan **uyumsuz** durumdur.

<a id="6-relationship-to-system-alignment-certification"></a>
### 6. Sistem hizalama belgelendirmesiyle ilişki
<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Alt kaynak: [Dokuzuncu Bölüm — Sistem Uyum Sertifikasyonu](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification) (9.000); [On Birinci Bölüm — Durum Kayıtları](core_11_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (11.000).
- Şununla birlikte okuyun: [Dokuzuncu Bölüm §7 — Sertifikasyon Sonuçları](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) — İkinci ila Dördüncü Bölümler kapsamındaki doğrulanmış uyumsuzluk, önceki sertifikasyondan bağımsız olarak sertifikasyonu yeniden açabilir veya geçersiz kılabilir.
- Birlikte oku: [Dokuzuncu Bölüm §7 — Belgelendirme sonuçları](../../core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) — İkinci Bölümden Dördüncü Bölüme doğrulanmış uyumsuzluk, önceki belgelendirmeden bağımsız olarak belgelendirmeyi yeniden açabilir ya da boşa çıkarabilir.

</details>

<br>

*Yalın dille: İkinci Bölümden Dördüncü Bölüme her uyum iddiasının karşılaması gereken kuralları koyar — tanımların ne anlama geldiğini, davranışın onları ne zaman kırdığını ve kanıtın nasıl gösterilmesi gerektiğini. Dokuzuncu Bölüm, bir sistemin biçimsel hizalama belgelendirmesine ihtiyaç duyduğunda o kuralları kullanan ayrı, forum-gözetimli bir belgelendirme sürecidir. Güncel bir belgelendirme, İkinci Bölümden Dördüncü Bölümü atlatan bir serbest geçiş değildir.*

Bu kesit **işlemsel değildir**. Yalnızca bir **katman sınırı** belirtir.

**İkinci, Üçüncü ve Dördüncü Bölümler** kalıcı tanım ve doğrulama alttaşını sağlar:
- **[İkinci Bölüm](core_02_definition_structure.md#ikinci-bölüm-tanim-yapisi-ve-bileşen-gerekleri)** — tanımların nasıl kurulduğu ve içten tutarlı tutulduğu (O/M/A/C)
- **[Üçüncü Bölüm](core_03_definition_integrity.md#üçüncü-bölüm-tanim-bütünlüğü-kaçinma-ve-uyumsuzluk)** — tanımların gerçek davranışa nasıl uygulandığı, uyumsuzluk ve kaçınma dahil
- **[Dördüncü Bölüm](core_04_burden_traceability_verification.md#dördüncü-bölüm-kanit-yükü-izlenebilirlik-ve-doğrulama)** (**1** ile **5**. kesitler) — kanıt yükü, iz haritaları, gözlemlenebilirlik, güvenlik sınırları ve kanıt standartları

Bunlar uyumun değerlendirildiği her yerde uygulanır — belgelendirme olsun ya da olmasın.

**[Dokuzuncu Bölüm — Sistem Uyum Sertifikasyonu](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification)** ilgili olduğu ölçüde forum gözetimindeki **sertifikasyon sürecini** sağlar: tüm sistem değerlendirme alanları, Sistem ve Kurum Sertifikasyon Kaydı görevleri, sertifikasyon sonuçları, sertifikasyon aralığı, itiraz edilebilirlik zinciri ve On Birinci Bölüme doğrulanmış girdi köprüsü. İkinci ila Dördüncü Bölümleri **uygular**; onları **yeniden ifade etmez**.

Okurlar şunları saymamalıdır:
- İkinci ila Dördüncü Bölümler kapsamındaki devam eden uyumun yerine bir **Sistem veya Kurum Sertifikasyon Kaydını** kullanmak
- **Dokuzuncu Bölüm** belgelendirmesini, koşullu belgelendirmesini ya da yeniden belgelendirmesini bu bölümdeki kanıtlama, iz ya da kanıt standartlarını düşüren şey olarak
- **İkinci Bölümden Dördüncü Bölümü** bir sistemin daha önce belgelendirilmiş olması nedeniyle isteğe bağlı olarak — o bölümler altında doğrulanmış uyumsuzluk, Dokuzuncu Bölüm altında belgelendirmeyi yeniden açabilir ya da boşa çıkarabilir

---

**Önceki dosya (bu dil):** [core_03_definition_integrity.md](core_03_definition_integrity.md)

**Sonraki dosya (bu dilde):** [core_05__definitions_home.md](core_05__definitions_home.md)

**Bağlayıcı asıl:** [core_04_burden_traceability_verification.md](../../core_04.000_burden_traceability_verification.md)
