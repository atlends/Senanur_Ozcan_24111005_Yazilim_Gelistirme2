# ============================================================
# gorsellestirme.py - Veri Görselleştirme (Matplotlib & Seaborn)
# Proje: Kişisel Finans ve Harcama Takip Sistemi
# Öğrenci: Senanur Özcan | 24111005 | Yazılım Geliştirme
# ============================================================

import matplotlib.pyplot as plt   # Grafik çizim kütüphanesi
import matplotlib                 # Genel matplotlib ayarları için
import seaborn as sns             # Gelişmiş görselleştirme teması
import pandas as pd               # DataFrame tipi için

# Türkçe eksi işaretinin bozulmasını önle (örn: -500 yerine ? göstermez)
matplotlib.rcParams["axes.unicode_minus"] = False

# Varsayılan grafik boyutunu belirle (genişlik x yükseklik, inç)
plt.rcParams["figure.figsize"] = (10, 6)

# Seaborn temasını ayarla: ızgara çizgili, pastel renkler
sns.set_theme(style="whitegrid", palette="pastel")


def aylik_grafik(df: pd.DataFrame) -> None:
    """
    Aylık gelir ve giderleri karşılaştıran çizgi grafiği oluşturur.

    Args:
        df (pd.DataFrame): Ay sütunu içeren işlem DataFrame'i
    """
    # Grafik çizmek için veri gerekli
    if df.empty:
        print("⚠️ Grafik için yeterli veri yok.")
        return

    # Aya ve tipe göre grupla; sütunlara taşı (gelir | gider)
    aylik = df.groupby(["ay", "tip"])["tutar"].sum().unstack(fill_value=0)

    # Bazı aylarda hiç gelir veya gider olmayabilir; eksik sütunları 0 ile ekle
    if "gelir" not in aylik.columns:
        aylik["gelir"] = 0
    if "gider" not in aylik.columns:
        aylik["gider"] = 0

    # Grafik alanı oluştur
    fig, ax = plt.subplots(figsize=(10, 5))

    # Gelir çizgisi: yeşil, daire işaretli
    aylik["gelir"].plot(ax=ax, marker="o", color="green", label="Gelir", linewidth=2)

    # Gider çizgisi: kırmızı, kare işaretli
    aylik["gider"].plot(ax=ax, marker="s", color="red", label="Gider", linewidth=2)

    # Grafik başlık ve eksen etiketleri
    ax.set_title("Aylık Gelir & Gider Karşılaştırması", fontsize=14, fontweight="bold")
    ax.set_xlabel("Ay")
    ax.set_ylabel("Tutar (TL)")

    ax.legend()                      # Açıklama kutusunu göster
    ax.tick_params(axis="x", rotation=45)  # X eksenini 45° döndür (okunabilirlik)

    plt.tight_layout()               # Kenar boşluklarını otomatik ayarla
    plt.savefig("aylik_grafik.png", dpi=150)  # Dosyaya kaydet (yüksek çözünürlük)
    plt.show()
    print("✅ Aylık grafik oluşturuldu → 'aylik_grafik.png'")


def gelir_gider_bar(df: pd.DataFrame) -> None:
    """
    Toplam gelir ve gider değerlerini karşılaştıran sütun (bar) grafiği oluşturur.

    Args:
        df (pd.DataFrame): İşlemleri içeren DataFrame
    """
    if df.empty:
        print("⚠️ Grafik için yeterli veri yok.")
        return

    # Tipe göre grupla ve toplamları al
    toplam = df.groupby("tip")["tutar"].sum().reset_index()

    # Her çubuk için renk belirle: gelir=yeşil, gider=kırmızı
    renkler = ["#2ecc71" if t == "gelir" else "#e74c3c" for t in toplam["tip"]]

    fig, ax = plt.subplots(figsize=(7, 5))

    # Sütun grafiği çiz (capitalize: ilk harfi büyük yap)
    bars = ax.bar(toplam["tip"].str.capitalize(), toplam["tutar"],
                  color=renkler, edgecolor="white", linewidth=1.2)

    # Her çubuğun tepesine değeri yazdır
    for bar in bars:
        yukseklik = bar.get_height()   # Çubuğun yüksekliği = tutarı
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,  # Yatay: çubuğun ortası
            yukseklik + 50,                         # Dikey: çubuğun biraz üstü
            f"{yukseklik:,.0f} TL",                 # Binlik ayraçlı format
            ha="center", va="bottom", fontsize=11
        )

    ax.set_title("Toplam Gelir & Gider", fontsize=14, fontweight="bold")
    ax.set_ylabel("Tutar (TL)")
    ax.set_xlabel("İşlem Tipi")

    plt.tight_layout()
    plt.savefig("gelir_gider_bar.png", dpi=150)  # PNG olarak kaydet
    plt.show()
    print("✅ Bar grafiği oluşturuldu → 'gelir_gider_bar.png'")


def pasta_grafik(df: pd.DataFrame) -> None:
    """
    Gelir ve gider oranlarını gösteren pasta (pie) grafiği oluşturur.

    Args:
        df (pd.DataFrame): İşlemleri içeren DataFrame
    """
    if df.empty:
        print("⚠️ Grafik için yeterli veri yok.")
        return

    # Tipe göre toplamları hesapla (Series: indeks=tip, değer=tutar)
    toplam = df.groupby("tip")["tutar"].sum()

    # En az 1 kategori olması gerekir
    if len(toplam) < 1:
        print("⚠️ Pasta grafiği için yeterli veri yok.")
        return

    # Sıraya uygun renk listesi oluştur
    renkler = []
    for tip in toplam.index:
        renkler.append("#2ecc71" if tip == "gelir" else "#e74c3c")

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.pie(
        toplam.values,                                      # Dilim değerleri
        labels=[t.capitalize() for t in toplam.index],     # Etiketler
        autopct="%1.1f%%",                                  # Yüzde göster (1 ondalık)
        colors=renkler,
        startangle=140,                                     # Başlangıç açısı
        wedgeprops={"edgecolor": "white", "linewidth": 2}, # Dilimler arası çizgi
    )

    ax.set_title("Gelir / Gider Dağılımı", fontsize=14, fontweight="bold")

    plt.tight_layout()
    plt.savefig("pasta_grafik.png", dpi=150)  # PNG olarak kaydet
    plt.show()
    print("✅ Pasta grafiği oluşturuldu → 'pasta_grafik.png'")
