# Kişisel Finans ve Harcama Takip Sistemi

**Öğrenci:** Senanur Özcan  
**Öğrenci No:** 24111005  
**Bölüm:** Yazılım Geliştirme  
**Ders:** BGY210 - Python Programlama II  
**Öğretim Elemanı:** Dr.Öğr.Üyesi Tohid YOUSEFİ  

---

## Proje Açıklaması

Bu uygulama; kullanıcıların gelir ve giderlerini kaydedebildiği, listeleyebildiği, finansal analizler yapabildiği ve verilerini grafiklerle görselleştirebildiği modüler bir kişisel finans takip sistemidir.

## Özellikler

- Gelir ve gider ekleme (tarih, tutar, açıklama)
- Tüm işlemleri listeleme ve net bakiyeyi görme
- Aylık bazda finansal analiz (Pandas)
- NumPy ile istatistiksel hesaplamalar
- Çizgi, sütun ve pasta grafikleri (Matplotlib & Seaborn)
- CSV formatında veri saklama ve yükleme
- Konsol menüsü ile kolay kullanım

## Proje Yapısı

```
Senanur_Özcan_24111005_Yazılım_Geliştirme/
├── main.ipynb            # Ana Jupyter Notebook
├── finans_modeli.py      # Islem sınıfı (OOP)
├── islem_yonetimi.py     # Gelir/gider işlemleri
├── dosya_islemleri.py    # CSV okuma/yazma
├── analiz.py             # Pandas & NumPy analizleri
├── gorsellestirme.py     # Grafikler
└── utils.py              # Yardımcı fonksiyonlar
```

## Kurulum ve Çalıştırma

```bash
pip install pandas numpy matplotlib seaborn
jupyter notebook main.ipynb
```

## Kullanılan Kütüphaneler

- `pandas` - DataFrame ve veri analizi
- `numpy` - İstatistiksel hesaplamalar
- `matplotlib` - Grafik oluşturma
- `seaborn` - Gelişmiş görselleştirme
- `csv` - Dosya okuma/yazma (standart kütüphane)

## Veri Yapıları

```python
gelirler = []   # Islem nesnelerinin listesi (tip='gelir')
giderler = []   # Islem nesnelerinin listesi (tip='gider')
```

Her eleman `Islem` sınıfının bir örneğidir:

```python
class Islem:
    id: int
    tutar: float
    tarih: str  # YYYY-MM-DD
    aciklama: str
    tip: str    # 'gelir' veya 'gider'
```

## Menü

```
1. Gelir Ekle
2. Gider Ekle
3. İşlemleri Listele
4. Analiz Yap
5. Grafik Göster
6. CSV Kaydet
7. Çıkış
```

## GitHub

> GitHub repo linki buraya eklenecek: `https://github.com/...`
