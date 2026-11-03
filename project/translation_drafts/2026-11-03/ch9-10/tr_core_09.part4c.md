#### 5.6 Güvenilirlik ve Sisteme Güvenme Bütünlüğü Değerlendirmesi

<details>
<summary><strong><span style="color: #2563eb;">İz</span></strong></summary>

- Üst kaynaklar:
  - [Kısım C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*kayıt içeriği*);
  - [§2](#2-system-class-evaluation) (*sistem sınıfı değerlendirmesi*); Gözetim ölçüm ailesi (*Gerçek ve epistemik bütünlük; anayasal ölçüm olarak Güvenilirlik ve Güven Aşınması ve Yanıltıcı Güven*); **Madde XIII** (*Güvenilir ve İtimat Edilebilir Sistem Hakkı*);
  - [Güvenilirlik](core_05.040_band_continuity.md#trustworthiness),
  - [Güven](core_05.040_band_continuity.md#trust),
  - [Güven Aşınması ve Yanıltıcı Güven](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance),
  - [İtiraz Edilebilirlik](core_05.035_band_accountability.md#contestability),
  - [Telafi ve Giderim](core_05.035_band_accountability.md#redress-and-remediation),
  - [Teşvik Uyumu](core_05.045_band_integrative.md#incentive-alignment),
  - [Geri Döndürülebilirlik](core_05.040_band_continuity.md#reversibility),
  - [Esaslılık](core_05.050_band_oversight.md#materiality),
  - [Bağımlılık](core_05.040_band_continuity.md#dependency) ve
  - [Risk](core_05.040_band_continuity.md#risk) (Beşinci Bölüm).
- Üst kaynaklar: İlkeler: Birinci Bölüm
  - [§3.1.5 Mevcut Kapasite ve Önleyici Yardım](core_01.000_values_principles.md#315-present-capability-and-proactive-help) (*algılayanların mevcut durumuna uygun işleyen itiraz ve inceleme yolları; yanıltıcı güvenin, sisteme güvenen algılayanlara göre değerlendirilmesi; yanıt vermeyen kişilere ulaşan hayatta kalma açısından kritik uyarılar*),
  - [§4 Güvenlik](core_01.000_values_principles.md#4-safety-harm-constraint),
  - [§6 Güven](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity),
  - [§10 Dayanıklılık ve Kendi Kendini Onaran Tasarım](core_01.000_values_principles.md#10-resilience-and-self-healing-design) ve
  - [§11.4 Kaynak ve Bağımlılık Yoğunlaşması](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*kaçınılamayan güven; §5.6.2'deki üst düzeye geçiş*).
- Alt kaynaklar:
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*Sistem sınıfına göre güvenilirliğin örnek uygulaması*);
  - [Kısım C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*kayıt bütünlüğü*);
  - [Kısım C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*doğrulanmış girdi kapısı*);
  - [Kısım B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*yanlış güven uyumsuzluğu, ters teşvik uyumsuzluğu ve kurtarma bütünlüğü uyumsuzluğu*).
- Şunlarla birlikte okuyun: **Madde XIII-A** (*Güvenilirlik ve İtimat Edilebilirlik Taban Çizgisi*), **Madde XIII-B** (*Telafi ve Giderim Hakkı*) ve **Madde XVI** (*Denetim, Şeffaflık ve Bağımsız Doğrulama*) — itiraz ve denetim hakları yine orada ele alınır; yüksek özerkliğe sahip sistemlerin yönetişim veya doğrulama yollarına esaslı biçimde aracılık ettiği durumlarda **Madde XIII-E** (*Yüksek Özerkliğe Sahip Sistemler ve Araç Aracılı Süreç Bütünlüğü*); sisteme güvenmeye devam edilmesinin hayatta kalmak için temel gereksinimlere erişimi etkileyeceği durumlarda **Madde III-A** (*Hayatta Kalma*); sistem beden, sağlık veya güvenliği etkileyebilecek ürün veya hizmetler sağladığında, listelediğinde, önerdiğinde ya da bunlar hakkında tavsiyede bulunduğunda **Madde III-F** (*Güvenli Ürünler ve Sağlık Bilgileri*); sağlık ve güvenlik bilgilerinin ona dayanan her algılayan tarafından kullanılabilir olması gerektiğinde **Madde VI-D** (*Erişilebilirlik*); [Birinci Bölüm §6 Güven](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) (1.000 §6) ve [Birinci Bölüm §5 Gerçek](core_01.000_values_principles.md#5-truth-epistemic-integrity-constraint) (1.000 §5).
- İşleyiş terimleri: ürün ve hizmetlerin sağlık ve güvenlik bilgileri, puanlamalar, sıralamalar ve ücretli tanıtım için [CJS-5.120 §10](corpus_joint_structure/cjs_05.120_participation_operations.md#product-and-service-health-and-safety-information) (*Katılım: açıklama yeterliliği ve gözlemlenebilirlik terimleri*); zarar raporları ve düzeltici bildirimler için [CJS-5.125 §15](corpus_joint_structure/cjs_05.125_accountability_operations.md#harm-reports-and-corrective-notices) (*Hesap verebilirlik: yapısal inceleme, düzeltme aciliyeti ve açıklama terimleri*).
- Alt bölümler:
  - [§5.6.1](#561-evaluation-requirement) (*değerlendirme gerekliliği*);
  - [§5.6.2](#562-system-class-scaling-and-escalation) (*sistem sınıfına göre ölçeklendirme ve yükseltme*);
  - [§5.6.3](#563-defects-and-misalignment) (*kusurlar ve uyumsuzluk*);
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*Sistem sınıfına göre güvenilirliğin örnek uygulaması*).

</details>

<br>

*Yalın dille: bir sistem algılayanların onun söylediklerine ve yaptıklarına güvenip güvenemeyeceğini — bu güven boşa çıktığında itiraz edip edemeyeceklerini de — esaslı biçimde etkilediğinde sertifikasyon, sisteme güvenmenin gerçekten gerekçeli, dürüstçe açıklanmış ve onarılabilir olup olmadığını denetlemelidir. Güvenilirlik ölçütleri ve sınama dizisi tasarımları başka belgelerde yer alır; sertifikasyon, tetikleyici geçerli olduğunda güvenilirliğin, yanlış güven riskinin ve itiraz yollarının gerçekten değerlendirilip değerlendirilmediğini denetler. Örnekler: [CS-9.320 §11 Sistem sınıfına göre güvenilirliğin örnek uygulaması](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class).*

Bu bölüm, önemli bir sistemin algılayanların ondan ne beklediğini şekillendirdiği durumlarda uygulanır: sistemin ne yaptığı, sınırlarının nerede olduğu, neyin ters gidebileceği, sisteme nasıl itiraz edileceği ve sorunların nasıl giderileceği. Bu etki aşağıdakiler yoluyla ortaya çıkabilir:

- sistemin ne kadar güvenilir olduğuna ilişkin iddialar;
- neyi açıklayıp neyi açıklamadığı;
- gerçekte nasıl çalıştığı;
- içine yerleştirilmiş teşvikler;
- arızalardan nasıl kurtulduğu; veya
- algılayanların ona bağımlı hâle geldiği benzer yollar.

Esaslılık tetikleyicisi geçerliyse sistem uyumu sertifikasyonu, **güvenilirliği ve sisteme güvenme bütünlüğünü** aşağıdakiler uyarınca değerlendirmelidir:

- **Madde XIII** (*Güvenilir ve İtimat Edilebilir Sistem Hakkı*);
- [Güvenilirlik](core_05.040_band_continuity.md#trustworthiness); ve
- [Güven Aşınması ve Yanıltıcı Güven](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance).

<a id="561-evaluation-requirement"></a>
##### 5.6.1 Değerlendirme Gerekliliği

Sertifikasyon süreci, algılayanların **Madde XIII-A** (*Güvenilirlik ve İtimat Edilebilirlik Taban Çizgisi*) uyarınca sisteme [güvenmek](core_05.040_band_continuity.md#trust) için iyi bir nedeni olup olmadığını ve sisteme doğru biçimde dayanıp dayanamayacağını denetlemelidir.

Değerlendirme ayrıca şunları sınamalıdır:

- algılayanların sisteme gerçekten itiraz edip edemediği, bir kararı inceletebilip inceletemediği ve bir sorunu çözdürebilip çözdüremediği — yalnızca kâğıt üzerinde değil. Bunun, kolayca yanıt veremeyen veya uzun bir süreci tamamlayamayanlar dâhil, algılayanların mevcut durumuna uygun biçimde işlemesi gerekir ([Birinci Bölüm §3.1.5 Mevcut Kapasite ve Önleyici Yardım](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **Madde XIII-A** (*Güvenilirlik ve İtimat Edilebilirlik Taban Çizgisi*) ve **Madde XIII-B** (*Telafi ve Giderim Hakkı*));
- hak ettiğinden daha fazla güvene veya dayanmaya algılayanların yanıltılıp yanıltılamayacağı; bu, sistemin kazanmadığı bir güven yoluyla ya da açıklamadığı sınırlar yoluyla olabilir. Bu, ortalama bir algılayana göre değil sistemi gerçekten kullanan algılayanlara göre değerlendirilir (**Madde XIII-C** (*Yanlış Güven ve Yanıltıcı Güven Yasağı*));
- sistemin sağlık veya güvenliği etkileyebilecek ürün ve hizmetler hakkında verdiği bilgilerin doğru, işlem yapmaya yetecek ölçüde eksiksiz ve ona ihtiyaç duyan algılayanın bulup anlayabilmesi için kolay olup olmadığı. Buna güvenlik uyarıları, sağlık iddiaları, besin değerleri, içerikler ve alerjen bilgileri dahildir. “Güvenli” diye okunabilecek bir boşluk bırakmak yerine bilinmeyen veya sınanmamış durumların açıkça belirtilmesi de buna dahildir (**Madde III-F** (*Güvenli Ürünler ve Sağlık Bilgileri*); sistem katmanındaki bağlantılar olarak **Madde XIII-A** (*Güvenilirlik ve İtimat Edilebilirlik Taban Çizgisi*) ile **Madde XIII-C** (*Yanlış Güven ve Yanıltıcı Güven Yasağı*));
- güvenlik ve sağlık bilgilerinin farklı duyusal, bilişsel ve dil ihtiyaçları olan algılayanlarca kullanılabilmesi ve karar verdikleri sırada onlara ulaşması; küçük yazılara gömülmemesi veya yalnızca tek biçimde sunulmaması (**Madde III-F** (*Güvenli Ürünler ve Sağlık Bilgileri*); **Madde VI-D** (*Erişilebilirlik*); [Birinci Bölüm §3.1.5 Mevcut Kapasite ve Önleyici Yardım](core_01.000_values_principles.md#315-present-capability-and-proactive-help));
- bu bilgi yanlış çıktığında veya ürünün güvenli olmadığı anlaşıldığında ona dayanmış olan herkese zararın aciliyetine uygun bildirim penceresi içinde (NU-1 ile NU-3) haber verilmesi ve bulundukları yerde onlara ulaşılması; güvensiz ürünün veya yanlış bilginin de bu aciliyete ilişkin sınırlama ve düzeltme pencereleri içinde (CU-1 ile CU-4) bulunduğu her yerde sınırlandırılıp düzeltilmesi ([Birinci Bölüm §3.1.5 Mevcut Kapasite ve Önleyici Yardım](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **Madde XIII-B** (*Telafi ve Giderim Hakkı*));
- sistemin içine yerleştirilmiş ödüllerin aldatmayı veya kestirmeden gitmeyi destekleyip desteklemediği (**Madde XIII-D** (*Teşvik Uyumu Kısıtı*)); ve
- önemli olduğu yerlerde sistemin arızaları gizlemeden veya kimsenin haklarını sessizce elinden almadan dürüstçe toparlanıp toparlanamadığı (**Madde XIII-F** (*Dayanıklılık ve Kendi Kendini Onarma Taban Çizgisi*)).

Sınama [Esaslılık](core_05.050_band_oversight.md#materiality), [Bağımlılık](core_05.040_band_continuity.md#dependency) ve [Risk](core_05.040_band_continuity.md#risk) ölçütlerine göre ölçeklendirilir.

Değerlendirme, zaman, ölçek ve bağımlılık boyunca işlevsel etkiyi yansıtmalıdır; aşağıdakileri değil:

- itibar, büyüklük veya pazarlama;
- görünürdeki güvence etiketleri;
- güvenilirlik rozetlerinin veya sağlayıcı puanlarının kimin görevlendirileceğini ya da ne satın alınacağını gerçekten belirlediği durumlarda, güvenilirlik hakkında göstermelik bir paragraf;
- açıklanan niyet; veya
- yalnızca geçmiş performans.

<a id="562-system-class-scaling-and-escalation"></a>
##### 5.6.2 Sistem Sınıfına Göre Ölçeklendirme ve Yükseltme

İncelemenin derinliği sistemin sınıfına bağlıdır. Esaslılık tetikleyicisi geçerli olduğunda:

- Bir sistemin ölçümleri, uyarıları veya kurtarma iddiaları haneleri ya da işletmecileri hayatta kalmak için temel gereksinimler (algılayanların yaşamak için ihtiyaç duyduğu şeyler) konusunda yanıltabiliyorsa kayıt, sistemin güvenilir olduğuna ilişkin bir iddiayı değil, güçlü kanıtları göstermelidir; çünkü bağımlılık, sistemin gerçekte nasıl davrandığıyla kazanılmalıdır ([Birinci Bölüm §6 Güven](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)). Kanıt şunları göstermelidir:
  - algılayanların sisteme güvenebildiğini;
  - algılayanlara yanlış bir güvence verilmeyeceğini;
  - [Birinci Bölüm §3.1.5 Mevcut Kapasite ve Önleyici Yardım](core_01.000_values_principles.md#315-present-capability-and-proactive-help) uyarınca hayatta kalma açısından kritik uyarı ve tavsiyelerin, yanıt vermediklerinde takip yapılması dâhil, bunları kabul ettiğini bildirmeyen algılayanlara ulaştığını; ve
  - [Birinci Bölüm §10 Dayanıklılık ve Kendi Kendini Onaran Tasarım](core_01.000_values_principles.md#10-resilience-and-self-healing-design) uyarınca sistemin arızalardan dürüstçe kurtulduğunu.
- Bir sistemin çalışma süresi, eşleştirme veya acil durum geçersiz kılma (“acil erişim”) iddiaları, algılayanların klinik bakım veya acil hizmet alıp alamayacağını kontrol ediyorsa ( [Birinci Bölüm §4 Güvenlik](core_01.000_values_principles.md#4-safety-harm-constraint) kapsamındaki bir risk), kayıt sistemin kritikliğine uygun ayrıntıyla şunları göstermelidir:
  - algılayanların bu iddialara nasıl itiraz edebileceğini; ve
  - algılayanların bu iddialara güvenerek yanıltılıp yanıltılamayacağını.
- Koordinasyon hayatta kalmak için vazgeçilmez olduğunda sertifikasyon incelemeyi yükseltmeli ve [§2.2 Sistem sınıfı her değerlendirmeyi nasıl ölçeklendirir](#22-how-system-class-scales-every-evaluation) uyarınca sistemin sınıfını yeniden değerlendirmelidir. Yanıltıcı güven, algılayanların hayatta kalmak için ihtiyaç duyduğu koordinasyonu kesintiye uğratabilecekse sistemin **A Sınıfına** yükseltilmesi gerekebilir. Algılayanların gerçekçi biçimde onsuz yapamayacağı güven, [Birinci Bölüm §11.4 Kaynak ve Bağımlılık Yoğunlaşması](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) ilkesinin adlandırdığı bağımlılıktır.

<a id="563-defects-and-misalignment"></a>
##### 5.6.3 Kusurlar ve Uyumsuzluk

[§5](#5-rights-floor-and-domain-evaluations) (*Hak Tabanı ve Alan Değerlendirmeleri*) kapsamındaki kusurlar, **Madde XIII** (*Güvenilir ve İtimat Edilebilir Sistem Hakkı*) uyarınca incelenmesi gereken esaslı sınırlar, riskler veya arıza geçmişi dâhil, bu değerlendirme için de geçerlidir. Ayrıca aşağıdakilerin her biri sertifikasyon kusuru sayılmalıdır:

- değerlendirilebilir bir [Güvenilirlik](core_05.040_band_continuity.md#trustworthiness) çözümlemesi olmaksızın itibarı, onayı, ölçeği veya işletmecinin öz bildirimini yeterli saymak;
- **Madde III-F** (*Güvenli Ürünler ve Sağlık Bilgileri*) uyarınca bilinmeyen veya sınanmamış olduğunu açıkça belirtmek yerine uyarının olmamasını ya da boş bir alanı ürün veya hizmetin güvenli olduğunu gösteriyor saymak; ve
- **Madde XIII** (*Güvenilir ve İtimat Edilebilir Sistem Hakkı*) kapsamındaki güvenilirlik ve **Madde XIII-A** (*Güvenilirlik ve İtimat Edilebilirlik Taban Çizgisi*) kapsamındaki itiraz disiplinlerini karşılamadan açıklamayı, itiraz edilebilirliği veya telafiyi boşa çıkarmak için verimlilik, yenilik veya güvenlik çerçevelerini kullanmak.

Belgelenmiş yanlış güven, ters teşvikler, erişilemeyen itiraz yolları ve arızayı gizleyen kurtarma uygulamaları [Birinci Bölüm §6 Güven ve Güvenilirlik](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) uyarınca sayılır.

<br>

*Forum süreci ve sonuçlarına devam edin:* [Dokuzuncu Bölüm, Kısım B — Forum Süreci ve Sonuçları](core_09.005_system_alignment_certification_record_process.md#chapter-nine-part-b-system-alignment-certification--forum-process-and-outcomes) ([§6 Forum Süreci](core_09.005_system_alignment_certification_record_process.md#6-forum-process) ve [§7 Sertifikasyon Sonuçları](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)). *Ardından kayda, yeniden sertifikasyona ve ehliyet bağlantısına geçin:* [Dokuzuncu Bölüm, Kısım C — Kayıt, Yeniden Sertifikasyon ve Ehliyet](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-system-alignment-certification--record-recertification-and-standing) ([§8 Sistem Sertifikasyon Kaydı](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) ile [§11 Ehliyetle İlişki](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing) arası).

*Her değerlendirme alanına ilişkin örnekler:* [CS-9.320 Sistem uyumu sertifikasyonu örnekleri](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-system-alignment-certification-illustrations).
