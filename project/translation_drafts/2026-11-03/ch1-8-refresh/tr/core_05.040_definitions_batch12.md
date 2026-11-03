# Chapter Five definition batch 12 — Clean Recertification (tr)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Clean Recertification; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### Temiz Yeniden Sertifikasyon

<details>
<summary><strong>İzleme</strong></summary>

- Kanonik sahip: Dokuzuncu Bölüm C Kısmı §9.3.1 İki statü. Yeniden sertifikasyon, geçici ve tam sertifikasyonla okuyun. Küme bileşeni yok.

</details>

*Basitçe: mevcut uyumsuzluk bulunmayan ve izleme göstergesinin yaklaşan uyumsuzluğa işaret etmediği yeniden sertifikasyon temizdir. Tam sertifikasyona yalnız temiz yeniden sertifikasyonlar sayılır.*

- **What it is**
  - **In scope / out of scope / dependencies:** Kapsam: mevcut uyumsuzluk veya yaklaşan uyumsuzluk göstergesi bulmayan yeniden sertifikasyon. Art arda gereken temiz geçici yeniden sertifikasyon sayısı Tam Sertifikasyonun bir girdisidir. Kapsam dışı: mevcut uyumsuzluk bulup sayacı sıfırlayan başarısız yeniden sertifikasyon; mevcut uyumsuzluk bulmayıp yaklaşan uyumsuzluk göstergesi bulan yeniden sertifikasyon (başarısız değildir, temiz de değildir). Yeniden, geçici ve tam sertifikasyona bağlı. Sayı ve gerekler Dokuzuncu Bölüm C §9.3.1’de; bu madde Beşinci Bölüm anlamıdır.
<a id="clean-recertification-a"></a>
- **How to measure and assess**
  - Süreklilik ölçümüyle değerlendirin: sayacı yalnız temiz yeniden sertifikasyon ilerletiyor mu; başarısız yeniden sertifikasyon sıfırlıyor mu.
<a id="clean-recertification-c"></a>
- **What must hold**
  - **Primary failure:** Başlıca başarısızlık: açık uyumsuzluk, kusur, gecikmiş kontrol veya başarısız regresyon testi varken temiz saymak; yaklaşan uyumsuzluk göstergesine rağmen sayacı ilerletmek.
