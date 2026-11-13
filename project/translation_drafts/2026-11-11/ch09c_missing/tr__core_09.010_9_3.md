<!-- Yapay zekâ destekli çeviri taslağı; incelenmedi. Güncel kaynak, Dokuzuncu Bölüm C Kısım §9.3; kaynak SHA-256 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Temel commit 247e2180509e5e029c1106878cf225067339e010; temel SHA-256 faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Yalnızca taslaktır; translations/ içine eşitlemeyin. -->

<a id="93-provisional-and-full-certification"></a>
#### 9.3 Geçici ve tam belgelendirme

*Sade anlatımla: Bir sistem güveni aşamalı olarak kazanır. Yeni sistemler ve değerlendirmede başarısız olan sistemler daha sıkı denetim altında başlar ve sık sık yeniden kontrol edilir. Yalnızca şu anda uyumsuzluğu ve yaklaşan uyumsuzluk belirtisi bulunmayan sistem daha uzun aralıklı tam belgelendirmeye geçer. Başarısız değerlendirme sistemi yeniden sıkı denetime döndürür.*

<a id="931-the-two-statuses"></a>
##### 9.3.1 İki statü

Belgelendirme iki statüden birindedir. Her statünün kendi aralığı, [§8.1 Asgari kayıt içeriği](#81-minimum-record-contents) uyarınca Sistem Belgelendirme Kaydında belirtilir:

- **[Geçici belgelendirme](core_05.040_band_continuity.md#provisional-certification)** sistemin ilk belgelendirme statüsüdür (yeni devreye alınan sistemler dâhil); başarısız yeniden belgelendirme, yeniden açılan inceleme veya uyumsuzluk bulan yeni inceleme sonrasında belgelendirilen sistem de bu statüdedir. Geçici aralık, aynı sistem sınıfındaki tam belgelendirme aralığından kısadır. Güven sınırları kayıtta belirtilir.
- **[Tam belgelendirme](core_05.040_band_continuity.md#full-certification)** yalnızca geçici statüdeki sistemin yeniden belgelendirilmesinde ve aşağıdaki üç koşulun tamamı sağlandığında kazanılır:
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

- Güncel uyumsuzluk bulan yeniden belgelendirme **başarısızdır**. [B Bölümü §7 Belgelendirme sonuçları](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) sonuçları uygulanır. Sonraki kontrolden ne kadar temiz çıkarsa çıksın, sistemin kazanabileceği bir sonraki belgelendirme geçici olur; temiz yeniden belgelendirme sayısı sıfırdan başlar.
- Güncel uyumsuzluk yokken yaklaşan uyumsuzluk göstergesi varsa yeniden belgelendirme başarısız değildir, ancak temiz de değildir. Geçici statüdeki sistem geçici kalır ve sayımı ilerlemez; tam statüdeki sistem geçiciye düşer.
- [§9 Yeniden belgelendirme ve incelemenin yeniden açılması](#9-recertification-and-reopening) uyarınca açılan inceleme uyumsuzluk bulursa başarısız yeniden belgelendirme ile aynı sonuç doğar.
- Belgesi bulunan sistem hakkında yapılan yeni incelemenin güncel uyumsuzluk bulması da aynı sonucu doğurur. Sistemin belgelendirme statüsü yoksa [B Bölümü §7.4 Reddetme ve iptal](core_09.005_system_alignment_certification_record_process.md#74-denial-and-revocation) kuralları uygulanır.

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
- nedeni bulan forum veya [B Bölümü §6.2 Gözetim sırası](core_09.005_system_alignment_certification_record_process.md#62-supervisory-sequence) uyarınca sıradaki görevlendirilen forum, yeniden tasarımı [eşleşen kabul hedef süresi](core_05.040_band_continuity.md#tier-window) içinde doğrular; bunu ilk geçici yeniden belgelendirmede de yapabilir;
- yeniden tasarım doğrulanmadan yapılan **bileşen değerlendirmesi** (B Bölümü §6.1'in tanımladığı belgelendirme geçişinin bir bileşene ait kısmı), ne kadar temiz olursa olsun temiz toplamına eklenmez; ve
- sistemin işletilme biçimindeki değişiklik bu adımı karşılamaz.

Bunlar yukarıdaki statü düşürme maddelerine eklenir, onların yerine geçmez. İşletici veya etkilenen herhangi bir hissedebilen varlık neden tespitinin incelenmesini isteyebilir; neden değişirse bu kurallar uygulanmaz.

<a id="934-tier-windows"></a>
##### 9.3.4 Kademe süreleri

İlk değerlendirme, yeniden belgelendirme, yeniden açılan inceleme veya yeni inceleme uyumsuzluk bulduğunda:

- konu [On Beşinci Bölüm §6 Zamanında çözüm, önemlilik kademeleri ve gecikmeyi önleme disiplini](core_15.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) uyarınca sınıflandırılır;
- varsayılan olarak sistemin sınıfına karşılık gelen kademeye yerleştirilir (örneğin uyumsuz A Sınıfı sistem, varsayılan olarak Kademe A'dır);
- kabul, kanıtı koruma, geçici koruma ve karar bu kademenin süre ve üst sınırlarına uyar; ve
- gecikme, söz konusu bölümün gerektirdiği şekilde incelenir.

<a id="935-class-a-reliance"></a>
##### 9.3.5 A Sınıfına güvenerek kullanım

Geçici belgelendirme tam belgelendirmeden daha kısa aralıklıdır; bu nedenle yeniden belgelendirme daha erken gelir ([§9.3.1 İki statü](#931-the-two-statuses)) ve güvenerek kullanma sınırları kayıtta belirtilir ([§8.1 Asgari kayıt içeriği](#81-minimum-record-contents)). Kesinti şöyle ele alınır:

- Geçici belgelendirme, kesinti ikameler gelmeden önce temel yaşam gereksinimlerini kesecekse, tek başına sistemi kesintiye uğratmayı gerektirmez;
- bu durum, B Bölümü §7 kapsamındaki geçici koruma ve belgelendirme koşullarıyla ele alınır;
- tasarım kaynaklı uyumsuzluk bulgusu sonrasında sayımın durdurulması sırasında da aynı kural geçerlidir: sayımın durması, hissedebilen varlıkların bağımlı olduğu sistemi tek başına kesintiye uğratmaz; ve
- durdurma sürdüğü müddetçe forum geçici korumayı, güvenerek kullanmaya ilişkin belgelendirme koşullarını ve bağımlılara yapılacak bildirimi belirtir.

<a id="936-verification-not-assertion"></a>
##### 9.3.6 İddia değil, doğrulama

Sistemin statüsü, temiz yeniden belgelendirme sayısı ve izleme göstergeleri doğrulanmalı; doğrulama bağımsız incelemeye açık olmalıdır. Sistemin kendi beyanı yeterli değildir:

- Göstergeler, uyumsuzluğun ortaya çıkamayacağı şekilde seçilemez veya ayarlanamaz.
- Yeniden tasarım da başkalarının denetleyebileceği kanıtlarla doğrulanır.
- Tam belgelendirme incelemeyi yeniden açma gerekçelerini ortadan kaldırmaz. [§9 Yeniden belgelendirme ve incelemenin yeniden açılması](#9-recertification-and-reopening) bölümündeki tüm tetikleyiciler geçerlidir.
- Kaçınma [§9.4 Kaçınmama](#94-non-evasion) uyarınca ele alınır.
