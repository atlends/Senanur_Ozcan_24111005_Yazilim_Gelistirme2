# Kişisel Finans ve Harcama Takip Sistemi

| Alan | Bilgi |
|------|-------|
| **Öğrenci** | Senanur Özcan |
| **Öğrenci No** | 24111005 |
| **Bölüm** | Yazılım Geliştirme |
| **Ders** | BGY210 - Python Programlama II |
| **Öğretim Elemanı** | Dr.Öğr.Üyesi Tohid YOUSEFİ |
| **Dönem** | Bahar 2026 |
| **GitHub** | https://github.com/atlends/Senanur_Ozcan_24111005_Yazilim_Gelistirme2 |

---

## Proje Açıklaması

Bu proje; kullanıcıların gelir ve giderlerini kaydedebildiği, listeleyebildiği, finansal analizler yapabildiği ve verilerini grafiklerle görselleştirebildiği **modüler, nesne tabanlı ve veri odaklı** bir kişisel finans takip sistemidir.

Proje; temel Python yapıları, fonksiyonel programlama, OOP, dosya işlemleri (CSV), veri analizi (Pandas & NumPy), veri görselleştirme (Matplotlib & Seaborn), hata yönetimi ve konsol uygulaması konularını bir arada kullanmaktadır.

---

## Proje Yapısı (Modüler Mimari)

Proje tek dosya olarak değil, her biri ayrı sorumluluğa sahip modüller halinde yazılmıştır:

```
Senanur_Özcan_24111005_Yazılım_Geliştirme/
├── main.ipynb              # Ana Jupyter Notebook (demo + konsol menüsü)
├── finans_modeli.py        # Islem sınıfı — Nesne Tabanlı Programlama (OOP)
├── islem_yonetimi.py       # Gelir/gider ekleme, listeleme, silme işlemleri
├── dosya_islemleri.py      # CSV okuma ve yazma işlemleri
├── analiz.py               # Pandas & NumPy ile veri analizi
├── gorsellestirme.py       # Matplotlib & Seaborn grafikleri
├── utils.py                # Yardımcı fonksiyonlar (ID, tarih, sayı kontrolü)
├── finans_verileri.csv     # Uygulama çıktısı — kayıtlı veriler
├── aylik_grafik.png        # Uygulama çıktısı — aylık çizgi grafiği
├── gelir_gider_bar.png     # Uygulama çıktısı — sütun grafiği
└── pasta_grafik.png        # Uygulama çıktısı — pasta grafiği
```

---

## Nesne Tabanlı Programlama (OOP)

`finans_modeli.py` içinde tanımlanan `Islem` sınıfı, her finansal kaydı temsil eden temel veri modelidir.

```python
class Islem:
    def __init__(self, id: int, tutar: float, tarih: str, aciklama: str, tip: str):
        self.id = id            # Benzersiz kayıt numarası
        self.tutar = tutar      # İşlem tutarı (TL)
        self.tarih = tarih      # Tarih (YYYY-MM-DD formatında)
        self.aciklama = aciklama  # Açıklama metni
        self.tip = tip          # 'gelir' veya 'gider'
```

`Islem` nesneleri `gelirler` ve `giderler` listelerinde tutulur; tüm modüller bu nesneler üzerinden çalışır.

---

## Veri Yapıları

```python
gelirler = []   # Islem nesnelerinin listesi (tip='gelir')
giderler = []   # Islem nesnelerinin listesi (tip='gider')
```

Her liste elemanı bir `Islem` nesnesidir. Veriler uygulama boyunca bu listeler üzerinden yönetilir, `csv_kaydet()` ile diske yazılır, `csv_oku()` ile geri yüklenir.

---

## Zorunlu Fonksiyonlar

### utils.py — Yardımcı Fonksiyonlar

| Fonksiyon | Açıklama |
|-----------|----------|
| `yeni_id_olustur(liste)` | Verilen listedeki en büyük ID'yi bulup bir artırarak yeni benzersiz ID üretir |
| `tarih_kontrol(tarih)` | Girilen tarihin `YYYY-MM-DD` formatında olup olmadığını kontrol eder |
| `sayi_kontrol(deger)` | Kullanıcıdan alınan değerin sayıya dönüştürülebilir olup olmadığını kontrol eder |
| `menu_goster()` | Programın ana menüsünü ekrana yazdırır |

### islem_yonetimi.py — İşlem Yönetimi

| Fonksiyon | Açıklama |
|-----------|----------|
| `gelir_ekle(gelirler)` | Kullanıcıdan alınan bilgileri doğrulayarak yeni bir gelir kaydı oluşturur ve listeye ekler |
| `gider_ekle(giderler)` | Kullanıcıdan alınan bilgileri doğrulayarak yeni bir gider kaydı oluşturur ve listeye ekler |
| `islemleri_listele(gelirler, giderler)` | Tüm gelir ve gider kayıtlarını düzenli bir formatta ekrana yazdırır |
| `islem_sil(gelirler, giderler, id)` | Verilen ID'ye sahip işlemi bularak ilgili listeden siler |

### dosya_islemleri.py — Dosya İşlemleri

| Fonksiyon | Açıklama |
|-----------|----------|
| `csv_kaydet(dosya_adi, gelirler, giderler)` | Tüm gelir ve gider verilerini belirtilen CSV dosyasına kaydeder |
| `csv_oku(dosya_adi)` | CSV dosyasındaki verileri okuyarak gelir ve gider listelerini oluşturur |

### analiz.py — Veri Analizi (Pandas & NumPy)

| Fonksiyon | Açıklama |
|-----------|----------|
| `verileri_dataframe_yap(gelirler, giderler)` | Gelir ve gider listelerini birleştirerek pandas DataFrame yapısına dönüştürür |
| `toplam_gelir_gider(df)` | DataFrame üzerinden toplam gelir ve toplam gider değerlerini hesaplar |
| `aylik_analiz(df)` | Verileri tarihe göre gruplayarak aylık bazda özet analiz oluşturur |
| `numpy_istatistik(df)` | NumPy kullanarak ortalama, minimum, maksimum ve standart sapma hesaplar |

### gorsellestirme.py — Görselleştirme (Matplotlib & Seaborn)

| Fonksiyon | Açıklama |
|-----------|----------|
| `aylik_grafik(df)` | Aylık gelir ve giderleri karşılaştıran çizgi grafiği oluşturur |
| `gelir_gider_bar(df)` | Toplam gelir ve gider değerlerini karşılaştıran sütun grafiği oluşturur |
| `pasta_grafik(df)` | Gelir ve gider oranlarını gösteren pasta grafiği oluşturur |

---

## Hata Yönetimi

Proje genelinde `try-except` blokları kullanılarak kullanıcı hataları yönetilmektedir:

- **Tarih formatı kontrolü:** `tarih_kontrol()` fonksiyonu yanlış formatlarda `ValueError` yakalar
- **Sayısal giriş kontrolü:** `sayi_kontrol()` fonksiyonu sayısal olmayan girişlerde `ValueError` yakalar
- **CSV okuma/yazma:** `csv_kaydet()` ve `csv_oku()` fonksiyonlarında `FileNotFoundError` ve `Exception` blokları mevcuttur
- **Boş veri kontrolü:** Analiz ve görselleştirme fonksiyonları boş DataFrame durumunu kontrol ederek hata vermeden uyarı mesajı döndürür

---

## Konsol Menüsü

Uygulama `uygulamayi_calistir()` fonksiyonu ile başlatılır. Kullanıcı aşağıdaki menü üzerinden tüm işlemlere erişir:

```
===== KİŞİSEL FİNANS TAKİP SİSTEMİ =====
1. Gelir Ekle
2. Gider Ekle
3. İşlemleri Listele
4. Analiz Yap
5. Grafik Göster
6. CSV Kaydet
7. Çıkış
==========================================
```

---

## Kullanılan Kütüphaneler

| Kütüphane | Kullanım Amacı |
|-----------|----------------|
| `pandas` | DataFrame oluşturma, gruplama, aylık analiz |
| `numpy` | Ortalama, min, max, standart sapma hesabı |
| `matplotlib` | Çizgi, sütun ve pasta grafikleri |
| `seaborn` | Gelişmiş görselleştirme stili |
| `csv` | Standart CSV okuma/yazma (built-in) |
| `datetime` | Tarih format doğrulaması |

---

## Kurulum ve Çalıştırma

```bash
# Gerekli kütüphaneleri yükle
pip install pandas numpy matplotlib seaborn

# Jupyter Notebook ile çalıştır
jupyter notebook main.ipynb
```

Notebook açıldıktan sonra **Run All** ile tüm hücreler sırasıyla çalıştırılır. Demo verileri otomatik yüklenir, grafikler oluşturulur ve CSV dosyası kaydedilir.

---

## Proje Çıktıları

| Dosya | Açıklama |
|-------|----------|
| `finans_verileri.csv` | 13 kayıt içeren gelir/gider veri dosyası |
| `aylik_grafik.png` | Aylık gelir & gider karşılaştırma çizgi grafiği |
| `gelir_gider_bar.png` | Toplam gelir/gider sütun grafiği |
| `pasta_grafik.png` | Gider dağılımı pasta grafiği |

---

## Clean Code Prensipleri

- Tüm fonksiyonlar **docstring** ile belgelenmiştir
- Değişken ve fonksiyon isimleri Türkçe ve anlamlıdır (`gelir_ekle`, `tarih_kontrol` vb.)
- Her modül **tek sorumluluk** prensibine göre tasarlanmıştır
- Tekrar eden kod bloklarından kaçınılmış, yardımcı fonksiyonlar `utils.py`'de toplanmıştır
- Kod içi yorumlar her kritik satırda mevcuttur
