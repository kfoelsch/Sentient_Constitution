<!-- AI-assisted translation draft; unreviewed. Source lines 201–318; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

#### 6.1 Forum gözetimi ve bileşen rolleri

*Basitçe: bir sistemin anayasal uyuma ulaştığını onaylamak, kanıtların ve paydaşların kaygılarının bağımsız biçimde incelenmesini gerektirir. Farklı forum türleri bu çalışmanın kendilerine verilen bölümünü yürütür. Etkilenen sentientler, sonuç yayımlanmadan önce bileşen ve Integrity itiraz yollarını kullanarak kanıt ekleyebilir ve incelemeye itiraz edebilir. Teknik inceleme veya Integrity koordinasyonu dâhil hiçbir uzmanlık alanı bütün süreci tek başına yürütemez.*

Bu bölüm, sistem uyum sertifikasyonunda her forum ailesine bir **bileşen rolü** verir. Bu rol, geri çekme veya sertifikasyon vermeme ile sonuçlanan bir tur da dâhil olmak üzere sertifikasyon, doğrulama veya yeniden sertifikasyonun her turunu ve [C Kısmı §8 Sistem Sertifikasyon Kaydı](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) kapsamındaki ilgili kayıtları içerir. Bu roller [§6.2 Gözetim sırasına](#62-supervisory-sequence) katkı sağlar. Forumların tam tanımları ve yönlendirme ayrıntıları [On Üçüncü Bölümde](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction), [CF-13.405](corpus_forum/cf_14.405_forum_formation_chamber_structure.md#cf-14405-forum-formation-forum-structure-mapping-and-chamber-structure) (*Forum kurulması, forum yapısının haritalanması ve daire yapısı*) ile [CF-13.415](corpus_forum/cf_14.415_routing_operations_transfer_certification_representative_treatment.md#cf-14415-routing-operations-transfer-certification-and-representative-treatment) (*Operasyon yönlendirmesi, devir, sertifikasyon ve temsilî muamele*) içinde yer alır. Burada her aile, sertifikasyon kaydını oluşturma, gözetme veya itiraz etme konusunda yalnızca sınırlı rolünü üstlenir; hiçbir aile başka bir ailenin işini devralmaz.

<a id="611-four-seats-in-a-certification"></a>

##### 6.1.1 Bir sertifikasyondaki dört koltuk

Bu alt bölüm, Dokuzuncu Bölümün [Sekizinci Bölüm §2 Dört Koltuklu Anayasal Gerekliliği](core_08.000_functional_independence_separation_of_duties.md#2-four-seat-constitutional-requirement) nasıl uyguladığını açıklar. [Sekizinci Bölüm §9 Sonraki Süreçlerle İlişki](core_08.000_functional_independence_separation_of_duties.md#9-relationship-to-later-processes), sonraki her sürecin dört koltuğun tümünü nasıl tahsis ettiğini ve kullandığını belirtmesini gerektirir; bu alt bölüm sertifikasyon için gereken açıklamadır. Sertifikasyon bir [Maddi Bağlayıcılığı Olan İşlem](core_05.035_band_accountability.md#materially-binding-act) olduğundan, her turda Sekizinci Bölümün tanımladığı dört koltuk, o bölümde verilen adlarla bulunur. Bu alt bölüm yeni bir koltuk eklemez ve Sekizinci Bölümün hiçbir kuralını gevşetmez. Bu bölümdeki başka kurallar daha katı olabilir, hiçbir zaman daha gevşek olamaz.

Sertifikasyon işlemi için koltuklar şöyle tahsis edilir:

- **[Başlatan Koltuk](core_05.035_band_accountability.md#initiating-seat):** Sertifikasyon isteyen sistem operatörü, emanetçisi, satıcısı veya başka bir teklif sahibi. Başvuru yapar, sistemi işletir veya uyum iddiasında bulunur.
- **[Doğrulama veya Yetkilendirme Koltuğu](core_05.035_band_accountability.md#verify-or-authorize-seat):** Kanıtları ve yetkiyi geçerli standarda göre denetleyen ve yetkisi dâhilinde bulgusunu açıklayan forum ya da sınırları belirlenmiş bileşen makamı.
- **[Kayıt Koltuğu](core_05.035_band_accountability.md#record-seat):** Koordineli Sistem Sertifikasyon Kaydını açan, kayda geçiren, değiştiren, koruyan ve yayımlayan ofis. Bu kayıt, sertifikasyon işleminin İşlem Kaydıdır (bkz. [C Kısmı §8.1 Asgari kayıt içeriği](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)).
- **[İtiraz Koltuğu](core_05.035_band_accountability.md#contest-seat):** Yayımlanmış kayda itiraz yolu ve itiraz edilen işlem için yetkili inceleme ya da yedek forum (bkz. [C Kısmı §9.1.1 İtiraz edilebilirlik yolları](core_09.010_system_alignment_certification_record_recertification.md#911-contestability-paths)).

**Koltukların yerleşimi:**

- Sistemin [Tüzük Rol Haritası](core_05.040_band_continuity.md#charter-role-map), sertifikasyonun başlatan, kayıt ve itiraz koltuklarının yerini belirler. Her biri için uygun ofisleri, şu anda koltuğu tutmaya yetkili emanetçileri ve yedeği listeler.
- Haritada adı geçen kayıt ve itiraz koltukları, operatörün ve teklif sahibinin [Maddi Kontrol Hattı](core_05.035_band_accountability.md#material-control-line) dışında yer alır.
- Harita doğrulama veya yetkilendirme koltuğunu yerleştirmez. Baş forum ve bileşen makamları [§6.2 Gözetim sırası](#62-supervisory-sequence) ve On Üçüncü Bölüm uyarınca atanır; böylece operatör kendi doğrulama makamını seçemez.
- Sistem Sertifikasyon Kaydı, her tur için yürürlükteki Tüzük Rol Haritası sürümünü belirtir (bkz. [C Kısmı §8.1 Asgari kayıt içeriği](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)).
- Haritada yeri belirlenmemiş bir koltuk, kayda geçirilip düzeltilmesi gereken bir Sistem Tüzüğü kusurudur; tur [Sekizinci Bölüm §5 Yayımlanmış Yerleşim, Boşluk ve Yedekleme](core_08.000_functional_independence_separation_of_duties.md#5-published-placement-vacancy-and-substitution) uyarınca ilerler.

**Operatörün dışında.** Sertifikasyonda doğrulama veya yetkilendirme koltuğunu tutan herkes, operatörün ve teklif sahibinin [Maddi Kontrol Hattının](core_05.035_band_accountability.md#material-control-line) dışında olmalı ve sonucu belirleyecek herhangi bir çıkarı bulunmamalıdır. Özellikle:

- Operatör, emanetçi, satıcı veya başka bir teklif sahibi, kendisini denetleyen forumu ya da bileşen makamını seçemez, atayamaz, kontrol ettiği bir kanal üzerinden finanse edemez veya görevden alamaz.
- Onun için çalışan, onun mülkiyetinde olan ya da ona hesap veren hiç kimse kendi sertifikasyonu için bu koltuğu tutamaz.
- Bu koşulu karşılayamayan bir sentient o turdan çekilmelidir (On Üçüncü Bölüm uyarınca çekilme).
- Bu koşula aykırı bir yerleşim, Tüzük Rol Haritasında ne yazarsa yazsın geçersizdir ([Sekizinci Bölüm §3 Bağımsızlık, Çıkar Çatışması ve Kontrol Hatları](core_08.000_functional_independence_separation_of_duties.md#3-independence-conflict-and-control-lines)).

Bir forum ailesi farklı işlemlerde farklı koltukları tutabilir. Ancak aynı işlemde, [Sekizinci Bölüm §2 Dört Koltuklu Anayasal Gerekliliğin](core_08.000_functional_independence_separation_of_duties.md#2-four-seat-constitutional-requirement) yasakladığı koltukları aile adını kullanarak birleştiremez.

**Baş forum ve kayıt sahibi:**

- Sonuç için doğrulama veya yetkilendirme koltuğunu baş forum tutar; bileşen bulgusu veren her forum veya makam da o bulgu için bu koltuğu tutar.
- Baş forum sıralamayı yönetir, ancak aynı işlemde kayıt koltuğunu tutmaz.
- Tüzük Rol Haritasında adı geçen kayıt sahibi, kaydı açar, değiştirir, korur ve yayımlar. Karar veren forumların belirlediği hususları kayda geçirir ve kendisi karar vermez.
- On Üçüncü Bölümdeki “koordineli tek kayıt” yükümlülüğü, baş forumun kaydı koordine etme görevidir; kaydı elinde tutma görevi değildir.

<a id="612-technical-forums"></a>

##### 6.1.2 Teknik Forumlar

**Teknik işlev:**

- Hukuka uygun yetki alanları içinde teknik şartnameleri, ölçüm yöntemlerini, test protokollerini, uzman kanıt standartlarını, belirsizliği azaltma yöntemlerini ve teknik yeterlilik bulgularını sürdürmek ve uygulamak;
- Sertifikasyon kaydı için **bileşen bulguları** sağlamak. Bunlar, [§2 Sistem Sınıfı Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) ve [§3.4 Veri Türleri ve İşleme Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#34-data-types-and-handling-evaluation) kapsamındaki sistem sınıfına göre ölçeklendirilmiş güvence ve veri işleme altyapısı bulgularını içerir;
- [On Üçüncü Bölüm §4.2 Teknik Forum Alanlarının](core_14.000_forum.md#42-technical-forum-domains) izin verdiği üzere, baş forumun sertifikasyon kaydı için kendilerine yönelttiği teknik soruları yanıtlamak;
- Sistem, bedeni, sağlığı veya güvenliği etkileyebilecek ürün ya da hizmetleri sağlıyor, listeliyor, öneriyor veya bunlar hakkında tavsiyede bulunuyorsa sağlık ve güvenlik bilgileri konusunda bileşen bulguları sağlamak. [§5.6 Güvenilirlik ve Sisteme Dayanma Bütünlüğü Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#56-trustworthiness-and-system-reliance-integrity-evaluation) bunu **Madde III-F** (*Güvenli Ürünler ve Sağlık Bilgileri*) kapsamında sınar. Teknik bulgu; uyarıların, sağlık iddialarının, besin bilgilerinin, içeriklerin ve alerjen bilgilerinin doğru, kanıtlarla destekli ve güncel olup olmadığını; bilinmeyen veya sınanmamış hususların açıkça belirtilip belirtilmediğini inceler; ve
- [Sentience Durumu Kararı](core_05.055_band_participation.md#sentience-status-adjudication) bileşen rolünü yürütmek (gösterge değerlendirmesi, uzman kanıtı ve sınırlandırılmış belirsizlik):
  - Sertifikasyon, haklar, statü veya koruma amaçları için kimin **sentient** sayıldığını önemli ölçüde etkiliyorsa bu rol [Madde VI-B](core_06.005_rights_part_b.md#article-vi-b-sentience-status-adjudication-floor) (*Sentience Durumu Kararı Tabanı*) uyarınca uygulanır.
  - [On Üçüncü Bölüm §4.2 Teknik Forum Alanları](core_14.000_forum.md#42-technical-forum-domains) ve [On Üçüncü Bölüm §5 Yükseltme ve sertifikasyon](core_14.000_forum.md#5-escalation-and-certification) (*sentience durumu kararı* kancası) kapsamında varsayılan baş forum Teknik Forumlardır.
  - On Üçüncü Bölüm gerektirdiğinde konu, bu kanca uyarınca Integrity, Kurumsal veya Anayasal özel yollara yönlendirilir.

<a id="613-integrity-forums"></a>

##### 6.1.3 Integrity Forumları

**Varsayılan baş koordinasyon:**

- On Üçüncü Bölüm başka bir birincil menfaat belirlemedikçe, resmî anayasal sistem uyumu sertifikasyonuna ve süregelen uyum doğrulamasına liderlik etmek;
- Teknik Forum standartlarını önemli ölçüde uygulanabilir oldukları yerlerde kullanmak; ve
- [§6.2 Gözetim sırasının](#62-supervisory-sequence) gerektirdiği üzere, diğer forum ailelerine ait bileşen sorularını yönlendirmek, onaylamak veya [bekletmek](core_05.035_band_accountability.md#stay) (duraklatmak).

<a id="614-environment-forums"></a>

##### 6.1.4 Çevre Forumları

**Ekoloji önemli olduğunda çevresel uyum:**

- Önemli ekolojik maruziyet, çevresel önkoşullara bağımlılık, yaşam döngüsü yükü, iyileştirme görevi veya makul biçimde öngörülebilir ekolojik risk varsa çevresel uyum bileşen rolünü üstlenmek; ve
- Atfedilebilir çevresel yüklerin önemli olduğu durumlarda [§5.1 Ekolojik Ayak İzi Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#51-ecological-footprint-evaluation) uyarınca [Ekolojik Ayak İzinin](core_05.040_band_continuity.md#ecological-footprint) atfını, açıklanmasını ve karşılaştırılmasını dâhil etmek.

<a id="615-sentient-forums"></a>

##### 6.1.5 Sentient Forumları

Bir sistem, bir topluluğun kendini yönetme biçimini önemli ölçüde etkilediğinde Sentient Forumları:

- Sistem kararlarının topluluğun yayımlanmış süreçlerini izleyip izlemediği, etkilenen üyelerin görüş bildirmesine ve itiraz etmesine izin verip vermediği ve uygulanabilir A Kısmı testlerini karşılayıp karşılamadığı konusunda **topluluk yönetimi bulguları** sağlar ([§4.3 Meclis, Kolektif Örgütlenme ve Kurum Oluşumu](core_09.000_system_alignment_certification_evaluation.md#43-assembly-collective-organization-and-institutional-formation), [§5.3 Orantılı Sistemler Arası Destek Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#53-proportionate-cross-system-support-evaluation) ve [§5.4 Ayrımcılık Yapmama Değerlendirmesi](core_09.000_system_alignment_certification_evaluation.md#54-nondiscrimination-evaluation)). Sistem kimin tarafından işletilirse işletilsin; üyeliği, dışlamayı, moderasyonu, ortak topluluk süreçlerine erişimi, katılımcı girdileri ve ortak kaynakların kullanımını kapsar ([On Üçüncü Bölüm §4.1 Sentient Forumları](core_14.000_forum.md#41-sentient-forums) bu konuları açıklar);
- Dışlama, ortak topluluk süreçlerine erişim veya ortak kaynak kullanımı gibi topluluk düzeyindeki menfaatler için Haklar Tabanı bileşenini üstlenir. Daha geniş Haklar Tabanı soruları [§6.1.6 Kurumsal Forumların](#616-institutional-forums) yetkisindedir. Hiçbir aile bu bileşeni üstlenmiyorsa Integrity lideri, diğer bileşen bulgularını kullanarak Haklar Tabanını uygular;
- Haklar Tabanı bulguları çelişirse, o turda son sözü söyleme yetkisi Kurumsal Forumda olduğundan ona uyar. Her iki bulgu da [§6.2 Gözetim sırası](#62-supervisory-sequence) uyarınca kayıtta kalır; çelişki [§6.3 İtiraz edilebilirlik zinciri](#63-contestability-chain) uyarınca itiraza açık olur;
- Yalnızca topluluk yönetimi bulgusuyla sınırlı itirazları dinler ([§6.3 İtiraz edilebilirlik zinciri](#63-contestability-chain) kapsamındaki bileşen forumu yolu) ve inceleme sırasında etkilenen üyelerden topluluk düzeyindeki kanıt ve kaygıları alır; bu, [§6.2 Gözetim sırası](#62-supervisory-sequence) uyarınca atanmış forumların katılım görevinin bir parçasıdır; ve
- Bir tur topluluk üyelerine zarar verildiğini saptadıktan sonra sentientler arasındaki giderim ve iyileştirmeyi ele alır ([On Üçüncü Bölüm §4.1 Sentient Forumları](core_14.000_forum.md#41-sentient-forums) uyarınca). Bu işlem turun ardından gelir ve esasa ilişkin ikinci bir inceleme hattı oluşturmaz.

<a id="616-institutional-forums"></a>

##### 6.1.6 Kurumsal Forumlar

Bir kurum söz konusu olduğunda Kurumsal Forumlar:

- Sertifikasyon sırasında bu sorular ortaya çıktığında kurumun ne yapmaya yetkili ve yükümlü olduğu, hangi gözetim kapsamına tabi bulunduğu, nasıl sınıflandırıldığı ve görevlerini yerine getirip getirmediği konusunda bileşen bulguları sağlar; ve
- Sertifikasyonun anayasal koruma altındaki tabanları koruyup korumayacağına karar verir. Bu tabanlar önemli ölçüde söz konusuysa ve şu durumlardan biri varsa bu kural uygulanır: kurum zorunlu taraftır; operatör veya emanetçi kurumsaldır; ya da kurumsal yetki veya gözetimli uyum başlıca menfaattir. Bu tabanlar [A Kısmı §5 Haklar Tabanı ve Alan Değerlendirmeleri](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) tablosundaki Altıncı Bölüm Haklar Tabanlarıdır. Tetikleyicisi oluştuğunda karar, tablodaki ilgili alan bölümüne göre değerlendirmeyi de içerir. Tabanlar şunlardır:
  - **Madde III-A** (*Hayatta Kalma*);
  - **Madde IV-A** (*Eğitime Eşit Erişim*);
  - **Madde IV** (*Sentient Merkezli Eğitim Hakkı*);
  - **Madde V** (*Kaynak Tahsisi, Bağımlılıklar ve Ekosistem Finansmanı*);
  - **Madde VI-C** (*Ayrımcılık Yapmama*);
  - **Madde VI-D** (*Erişilebilirlik*);
  - **Madde XIII** (*Güvenilir ve İtimat Edilebilir Sistem Hakkı*); ve
  - [**Güvenli Koşullarla**](core_05.040_band_continuity.md#safe-conditions) birlikte **Madde XIII-A** (*Güvenilirlik ve İtimat Edilebilirlik Tabanı*).

<a id="617-constitutional-and-other-regular-forum-families"></a>

##### 6.1.7 Anayasal ve diğer olağan forum aileleri

**Anayasal ve artık menfaatler:**

- On Üçüncü Bölümün kendilerine verdiği soruları üstlenmek: anayasa metninin geçerli olup olmadığı, ne anlama geldiği ve sınıf çapındaki bir düzeltmenin yönetimi yeniden yapılandırmasının gerekip gerekmediği; ayrıca başlıca menfaati On Üçüncü Bölümün yukarıda adı geçmeyen bir aileye verdiği diğer sorular;
- [On Üçüncü Bölüm §5 Yükseltme ve sertifikasyon](core_14.000_forum.md#5-escalation-and-certification) uyarınca baş forumun kendilerine yönelttiği anayasal soruları yanıtlamak: geçerlilik sorusu, yönetimin yeniden yapılandırılmasına ilişkin yapısal soru veya anayasal bir konuda alt kurullar arasındaki çelişki. Yanıt verilene kadar baş forum bu noktayı kesin olarak çözümlenmiş sayamaz ([§6.2 Gözetim sırası](#62-supervisory-sequence), 5. adım); ve
- Teknik uzmanlık ve Integrity koordinasyonu bu soruları devralmamalıdır.

