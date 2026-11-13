> Yapay zekâ destekli çeviri taslağı — dil: Türkçe; kaynak: commit 9c2c8c10c871d91157bcd27b9f56ad6a1cec90d3; durum: incelenmemiş; kısmi kapsam: On Birinci Bölüm, yalnızca §4. Bu, bölümün tam çevirisi değildir.

### 4. Doğrulama ve kayıt gereklilikleri

<details>
<summary><strong><span style="color: #2563eb;">İzleme</span></strong></summary>

- Önce gelenler: [§2](#2-question-1--what-happened) (*Soru 1 kayıtları ve olay türü rehberi*); [İkinci ila Dördüncü Bölümler](core_02.000_definition_structure.md) (*kayıt, doğrulama ve tanımların sonuçlara kadar izlenebilirliği*).
- Sonra gelenler:
  - [§4.1](#41-minimum-record-contents) (*asgari içerik*);
  - [§4.2](#42-related-standing-record-cross-references) (*çapraz referanslar*);
  - [§5](#5-record-custody-and-opening-authority) (*kaydın muhafazası ve açma yetkisi*);
  - [§6](#6-handling-a-standing-record) (*bir güzergâh kaydının işlenmesi*);
  - [On İkinci Bölüm §1](core_12.000_standing_measurement.md#1-question-2--how-good-or-bad-was-it) (*Soru 2*).
- Birlikte okuyun: [CF-15.415 §8 Kısıtlı bilgi yetkisi](corpus_forum/cf_15.415_routing_operations_transfer_certification_representative_treatment.md#cf-15415-8-restricted-information-authority) (*[§4.1](#41-minimum-record-contents) uyarınca belirtilen bir açıklama sınırı hakkındaki uyuşmazlıkta ilk başvurulacak yer*).

</details>

<br>

*Yalın dille: Bu bölüm, her güzergâh kaydında nelerin bulunması gerektiğini, bağlantılı güzergâh kayıtlarının birbirine nasıl atıfta bulunduğunu ve kayıtların nasıl sürümlendiğini belirtir. Bir güzergâh kaydını kimin açıp muhafaza edebileceği ve kayda nasıl itiraz edilebileceği ya da kaydın nasıl düzeltilebileceği [§5 Kayıt muhafazası ve açma yetkisi](#5-record-custody-and-opening-authority) bölümündedir. Soru 2 ölçümleri ancak doğrulanmış olgusal dayanak kaydedildikten sonra eklenebilir.*

Gerekli kanıt ve kayıt ayrıntıları, maddi paya ve sistemin sınıfına göre artırılabilir. Bu ölçeklendirme, kapsamdaki hiçbir algılayanı, kurumu veya sistemi güzergâh sürecinin dışında bırakmaz.

<a id="41-minimum-record-contents"></a>

#### 4.1 Asgari kayıt içeriği

Bir güzergâh kaydı aşağıdaki alanları taşır; son iki alt bölüm her eksen için ek alanlar getirir. Bir güzergâh kaydına hangi bilgilerin girebileceğini belirleyen doğrulanmış girdi geçidi [§2.5 Doğrulanmış girdi geçidi](#25-verified-input-gate) bölümünde açıklanır. Soru 1 olgularını Soru 2 ölçümünden ayrı tutan kural [§2.6 Aşama sınırı](#26-stage-boundary) bölümünde açıklanır.

<a id="411-fields-every-standing-record-must-carry"></a>

##### 4.1.1 Her güzergâh kaydında bulunması gereken alanlar

Her güzergâh kaydı en azından şunları içermelidir:

- güzergâh kaydının türü — **katkı güzergâh kaydı** veya **ihlal güzergâh kaydı**;
- kimin veya neyin değerlendirildiği ve değerlendirmenin kapsamı; buna ilgili sistem sınırları, rol sınırları, etkilenen topluluklar ve bağımlılık ilişkileri dahildir;
- hangi davranışın veya bulgunun değerlendirildiği; buna güzergâh kaydının dayandığı eylemler, ihmaller, görevler, etkiler, sınırlandırılmış olay, kapsamdaki örüntü, katkı kaydı veya ihlal bulgusu dahildir;
- kayıt dönemi ve mevcut inceleme durumu — örneğin geçici, belirtilen bir amaç için nihai, itiraz altında, yürürlükten kalkmış veya planlı yeniden değerlendirme zamanı gelmiş;
- **§4.2** uyarınca çapraz referans verilen ilgili güzergâh kayıtları;
- güzergâh kaydını İkinci ila Dördüncü Bölümler uyarınca kanıtlanabilir, incelenebilir ve itiraz edilebilir kılan resmî kayıtlar, tanıklar, ölçümler, denetimler, forum kararları veya diğer doğrulama materyalleri;
- olgusal dayanağı doğrulayan ve kayda girişe izin veren **kayıt açma yetkisi** ile kaydı girip muhafaza eden ayrı **kayıt emanetçisi**; her ikisi de **§5** uyarınca adlandırılmalıdır;
- güzergâh kaydına nasıl itiraz edileceği; buna şunlar dahildir:
  - kaydı hangi forumun veya yetkilinin inceleyeceği;
  - varsa açıklama sınırları; ve
  - aşağıdakilere ilişkin koşullar:
    - düzeltme;
    - eski hâline getirme;
    - sona erme; veya
    - planlı inceleme;
- ölçüm gerçekleştiğinde aşağıda gerekli görülen, eksene özgü Soru 2 ölçüm alanları.

<a id="412-inspectable-attributable-action"></a>

##### 4.1.2 İncelenebilir ve atfedilebilir eylem

Atfedilebilir eylem kanıtı güzergâh kaydıyla şu şekilde ilişkilidir:

- Kritik Sistem Yönetimi veya maddi operasyonel yetki kullanan personel/ajanlar için yeniden oluşturulabilir atfedilebilir eylem kanıtı, karma ekipler için varsayılan kayıt sözleşmesi olarak **[CS-16.305 §10 incelenebilir ve atfedilebilir eylem](corpus_systems/cs_16.305_critical_system_stewardship.md#cs-16305-103-inspectable-attributable-action)** içinde belirtilir.
- Bu kanıt, bu güzergâh kaydına girdi sağlayabilir.
- Bu güzergâh kaydının yerini almaz.
- Bir güzergâh kaydı, bir yapay zekâ modelinin ağırlıklarını (modelin içindeki sayıları) veya özel akıl yürütmesini içermez. Tek istisna, kimin veya neyin sorumlu olduğunu gösterecek başka hiçbir şey kalmadığı durumdur.
- Bir konu, bir kişinin mahremiyetiyle veya bir sistemin korunan iç durumuyla ilgili diye güzergâh ölçümünün dışında kalmaz. Güzergâh konusuyla ilgili olduğunda yine ölçülür.

<a id="413-no-privacy-or-opacity-exemption"></a>

##### 4.1.3 Mahremiyet veya kapalılık istisnası yoktur

Mahremiyet, gizlilik veya bir sistemin iç işleyişinin kapalılığı, bir konuyu güzergâh ölçümünden muaf tutmaz. Bunlar doğrulanmış kayıt gerekliliğiyle çatıştığında, çatışma [Birinci Bölüm §13.1 Temel ödünleşim ilkeleri](core_01.005_interaction_interpretation.md#131-core-tradeoff-principles) ve oradaki karar kaydı disiplini uyarınca çözülür; bağımsız incelemecinin erişimi korunur.

<a id="414-additional-fields-for-contribution-standing-records"></a>

##### 4.1.4 Katkı güzergâh kayıtları için ek alanlar

**Katkı güzergâh kayıtları** ayrıca şunları belirtmelidir:

- Soru 2 katkı ölçümü; buna şunlar dahildir:
  - birincil bant;
  - atandığında `s` yuvası (bkz. [On İkinci Bölüm §4 Yuva dilbilgisi ve ortak ölçekleme](core_12.000_standing_measurement.md#4-slot-grammar-and-shared-scaling));
  - kanıt dayanağı;
  - maddilik gerekçesi; ve
  - şeffaf desteği göstermek için kullanılan, kabul edilmiş LEQU veya benzer kalibrasyon;
- katkı paylaşılıyorsa, aşağıdakilerin dikkate alınması da dahil olmak üzere kredinin nasıl dağıtıldığı:
  - zaman;
  - çaba;
  - koordinasyon;
  - bakım;
  - nedensel katkı; ve
  - daha az görünür destek çalışmaları;
- burada kaydedildiği biçimiyle, On Üçüncü Bölüm kapsamındaki daha sonraki herhangi bir güzergâh etkisinin dayanması gereken katkı ölçümü.

<a id="415-additional-fields-for-violation-standing-records"></a>

##### 4.1.5 İhlal güzergâh kayıtları için ek alanlar

**İhlal güzergâh kayıtları** ayrıca şunları belirtmelidir:

- Soru 2 ihlal ölçümü; buna şunlar dahildir:
  - bulgu yetkilisi veya kayıt dayanağı;
  - LEQU etkisi;
  - atandığında `s` yuvası (bkz. [On İkinci Bölüm §4 Yuva dilbilgisi ve ortak ölçekleme](core_12.000_standing_measurement.md#4-slot-grammar-and-shared-scaling));
  - uygulanabildiğinde süreç / yanıt niteliği; ve
  - On Dördüncü Bölüm kapsamındaki varsa belirleme durumu;
- bir ihlale ilişkin sorumluluğu birden fazla aktör paylaşıyor veya bölüşüyorsa, belirli bir aktör aleyhine kaydedilen olumsuz güzergâha ilişkin doğrulanmış gerekçeler; bunlara şunlar dahildir:
  - nedensel rol;
  - görev;
  - yetki;
  - kontrol;
  - öngörülebilirlik;
  - menfaat;
  - gizleme; veya
  - uygulanabilir önleme kapasitesi;
- ihlal bulgusu, forumda açıklama yapılmamasını veya çekilme sürecindeki kasıtlı bir aksaklığı içeriyorsa (ölçüm disiplini için **§8.2.2**'yi (*Bir zararın meydana gelme biçimi nasıl kaydedilir*) okuyun):
  - açıklama yapılmaması veya aksaklığa ilişkin doğrulanmış dayanak;
  - yerine getirilmemiş açıklama veya çekilme görevi;
  - tespit edildiği durumlarda aktörün bilgisi, pervasızlığı veya kastı; ve
  - davranışın maddi olarak aşağıdakileri etkileyip etkilemediği:
    - heyetin hukuka uygunluğu;
    - bağımsızlık;
    - çekilmeye itiraz;
    - kanıtların bütünlüğü;
    - telafi zamanlaması;
    - yedek yönlendirme; veya
    - uygulamadaki itiraz edilebilirlik;
- burada kaydedildiği biçimiyle, On Üçüncü Bölüm kapsamındaki daha sonraki herhangi bir güzergâh etkisinin dayanması gereken ihlal ölçümü.

<a id="42-related-standing-record-cross-references"></a>

#### 4.2 İlgili güzergâh kayıtlarına çapraz referans

Bir katkı güzergâh kaydı ile ihlal güzergâh kaydı aynı özneyle ilgiliyse, zaman bakımından örtüşüyorsa veya aynı olay, örüntü ya da kararla ilgiliyse, her biri diğerine işaret etmelidir.

Her çapraz referans en azından şunları belirtmelidir:

- ilgili güzergâh kaydı ve bunun katkı kaydı mı yoksa ihlal kaydı mı olduğu;
- iki güzergâh kaydının neden bağlantılı olduğu; buna **§2.4** uyarınca bir ihlal bulgusunun iddia edilen bir katkıyı çürüttüğü, düzelttiği veya sınırladığı durumlar da dahildir;
- iki güzergâh kaydının ortak yönü: özne, olay, örüntü veya karar; ve
- kayıtların kapsadığı zaman dönemlerinin veya konuların nasıl örtüştüğü.

Çapraz referanslar:

- denetlenebilir ve itiraza açık kalmalıdır;
- ayrı ölçümün yerini almamalıdır;
- birleşik bir puan oluşturmamalıdır; ve
- gerçekte aynı konuları veya zaman dönemlerini kapsamıyorlarsa, iki güzergâh kaydının bunları kapsadığı izlenimini yaratmamalıdır.

<a id="43-collective-and-actor-specific-records"></a>

#### 4.3 Kolektif ve aktöre özgü kayıtlar

Birkaç algılayan veya tüzel kişi aynı menfaati ya da ihlali paylaştığında sistem, hem kolektif bir güzergâh kaydı hem de aktörlere özgü ayrı kayıtlar tutabilir. Şu kurallar geçerlidir:

- Katkı ve ihlal bulguları **§2.1** uyarınca ayrı güzergâh kayıtlarında kalmalıdır.
- Paylaşılan katkı için takdir, her algılayanın fiilen sunduğu katkıya göre verilmelidir; şunlar dikkate alınır:
  - rol;
  - zaman;
  - çaba;
  - risk;
  - beceri;
  - koordinasyon;
  - bakım; ve
  - nedensel etki.
- Çok sayıda algılayan yardım etmiş ve bireysel paylar açıkça ayrılamıyorsa, geniş dağıtım tercih edilir.
- Paylaşılan ihlallerde kusur yalnızca grup üyeliğine dayanarak yüklenmemelidir.
- Aktöre özgü olumsuz güzergâh için aşağıdakilerle doğrulanmış bağlantı gerekir:
  - nedensel rol;
  - görev;
  - yetki;
  - kontrol;
  - öngörülebilirlik;
  - menfaat;
  - gizleme; veya
  - uygulanabilir önleme kapasitesi.

<a id="44-versioning"></a>

#### 4.4 Sürümleme

Aşağıdakilerden herhangi biri değiştiğinde güzergâh kayıtlarına sürüm verilmelidir:

- önemli olgular;
- bulgular;
- inceleme sonuçları;
- giderim durumu;
- katkı kanıtları;
- uygulama kalibrasyonu; veya
- anayasal kurallar.

Daha sonraki bir sürüm:

- güzergâh kaydını ileriye dönük güncelleyebilir;
- yanlış olduğu durumlarda geriye dönük düzeltebilir;
- tamamlanmış bir karar bağlamı için süresini sona erdirebilir; veya
- yeni bir karar bağlamı için önceki sürümün yerini alabilir.

Daha sonraki sürüm, önceki denetim izini korumalı ve neyin değiştiğini, değişikliği kimin yaptığını, **§5** kapsamındaki hangi kayıt açma veya muhafaza yetkisine dayanıldığını, hangi doğrulama materyallerinin kullanıldığını ve kimin talebi üzerine değişiklik yapıldığını açıklamalıdır.

<a id="45-implementation-tools"></a>

#### 4.5 Uygulama araçları

Ekipler, güzergâh kayıtları için aşağıdakiler dahil pratik araçlar geliştirebilir:

- veri alanları;
- etiketler;
- eşikler;
- formlar;
- panolar;
- inceleme adımları; ve
- **§13** kapsamında yinelenen görevler için yayımlanmış **standart katkı ölçütleri**.

Bu araçlar, **§4.1** kapsamındaki alanları ayrı ayrı görünür ve itiraza açık tutmalıdır. Bu alanları tek, opak bir puanın veya gizli bir etiketin içine gömmemelidir.
