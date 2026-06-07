# ============================================================
# analiz.py - Pandas & NumPy Analizleri
# Proje: Kişisel Finans ve Harcama Takip Sistemi
# Öğrenci: Senanur Özcan | 24111005 | Yazılım Geliştirme
# ============================================================

import pandas as pd    # Veri analizi ve DataFrame işlemleri için
import numpy as np     # İstatistiksel hesaplamalar için


def verileri_dataframe_yap(gelirler: list, giderler: list) -> pd.DataFrame:
    """
    Gelir ve gider listelerini birleştirerek pandas DataFrame yapısına dönüştürür.

    Args:
        gelirler (list): Gelir Islem nesnelerinin listesi
        giderler (list): Gider Islem nesnelerinin listesi

    Returns:
        pd.DataFrame: Tüm işlemleri içeren DataFrame
    """
    # Gelir ve gider listelerini tek bir listede birleştir
    tum_islemler = gelirler + giderler

    # Veri yoksa boş DataFrame döndür
    if not tum_islemler:
        print("⚠️ Veri yok. Önce işlem ekleyiniz.")
        return pd.DataFrame()

    # Her Islem nesnesini sözlüğe çevirip DataFrame oluştur
    veri = [islem.to_dict() for islem in tum_islemler]
    df = pd.DataFrame(veri)

    # Sütun tiplerini düzenle: CSV'den gelen string değerleri doğru tipe çevir
    df["tutar"] = pd.to_numeric(df["tutar"])           # Sayısal tip
    df["tarih"] = pd.to_datetime(df["tarih"])          # Tarih tipi (datetime)

    # Aylık gruplama için yardımcı sütun ekle (örn: "2026-04")
    df["ay"] = df["tarih"].dt.to_period("M").astype(str)

    return df


def toplam_gelir_gider(df: pd.DataFrame) -> dict:
    """
    DataFrame üzerinden toplam gelir ve toplam gider değerlerini hesaplar.

    Args:
        df (pd.DataFrame): İşlemleri içeren DataFrame

    Returns:
        dict: {'toplam_gelir': float, 'toplam_gider': float, 'net': float}
    """
    # Boş DataFrame kontrolü
    if df.empty:
        return {"toplam_gelir": 0.0, "toplam_gider": 0.0, "net": 0.0}

    # Sadece 'gelir' tipindeki satırların tutar sütununu topla
    toplam_gelir = df[df["tip"] == "gelir"]["tutar"].sum()

    # Sadece 'gider' tipindeki satırların tutar sütununu topla
    toplam_gider = df[df["tip"] == "gider"]["tutar"].sum()

    # Net bakiye: gelir eksi gider
    net = toplam_gelir - toplam_gider

    # Sonuçları 2 ondalık basamağa yuvarla ve sözlüğe ekle
    sonuclar = {
        "toplam_gelir": round(toplam_gelir, 2),
        "toplam_gider": round(toplam_gider, 2),
        "net": round(net, 2),
    }

    # Ekrana özet raporu yazdır
    print("\n📊 FİNANSAL ÖZET:")
    print(f"  Toplam Gelir : {toplam_gelir:>12.2f} TL")
    print(f"  Toplam Gider : {toplam_gider:>12.2f} TL")

    # Net pozitifse kâr, negatifse zarar etiketi göster
    durum = "✅ Kâr" if net >= 0 else "⚠️ Zarar"
    print(f"  Net Bakiye   : {net:>12.2f} TL  {durum}")

    return sonuclar


def aylik_analiz(df: pd.DataFrame) -> pd.DataFrame:
    """
    Verileri tarihe göre gruplayarak aylık bazda özet analiz oluşturur.

    Args:
        df (pd.DataFrame): İşlemleri içeren DataFrame

    Returns:
        pd.DataFrame: Aylık gelir, gider ve net değerleri içeren tablo
    """
    # Boş DataFrame kontrolü
    if df.empty:
        return pd.DataFrame()

    # Ay ve işlem tipine göre grupla, tutarları topla
    # unstack: 'tip' sütununu sütunlara taşır (gelir | gider)
    # fill_value=0: eksik kombinasyonlara 0 yaz (örn: o ayda gider yoksa)
    aylik = df.groupby(["ay", "tip"])["tutar"].sum().unstack(fill_value=0)

    # Sadece gelir veya sadece gider varsa eksik sütunu 0 ile ekle
    if "gelir" not in aylik.columns:
        aylik["gelir"] = 0
    if "gider" not in aylik.columns:
        aylik["gider"] = 0

    # Net sütunu: o ayki gelir - gider
    aylik["net"] = aylik["gelir"] - aylik["gider"]

    # İndeksi (ay) normal sütuna çevir ve sütun adlarını Türkçe yap
    aylik = aylik.reset_index()
    aylik.columns = ["Ay", "Gelir (TL)", "Gider (TL)", "Net (TL)"]

    # Tabloyu ekrana yazdır (indeks olmadan)
    print("\n📅 AYLIK ANALİZ:")
    print(aylik.to_string(index=False))

    return aylik


def numpy_istatistik(df: pd.DataFrame) -> dict:
    """
    NumPy kullanarak veri üzerinde ortalama, minimum, maksimum ve
    standart sapma hesaplar.

    Args:
        df (pd.DataFrame): İşlemleri içeren DataFrame

    Returns:
        dict: İstatistiksel sonuçlar
    """
    # Boş DataFrame kontrolü
    if df.empty:
        return {}

    # Tüm tutarları NumPy dizisine çevir (numpy fonksiyonları için gerekli)
    tutarlar = df["tutar"].values

    # Gelir ve gider tutarlarını ayrı ayrı al
    gelir_tutarlar = df[df["tip"] == "gelir"]["tutar"].values
    gider_tutarlar = df[df["tip"] == "gider"]["tutar"].values

    # NumPy fonksiyonlarıyla istatistikleri hesapla
    sonuclar = {
        "genel_ortalama": round(np.mean(tutarlar), 2),   # Tüm işlemlerin ortalaması
        "genel_min": round(np.min(tutarlar), 2),          # En düşük tutar
        "genel_max": round(np.max(tutarlar), 2),          # En yüksek tutar
        "genel_std": round(np.std(tutarlar), 2),          # Standart sapma (dağılım)
        # Gelir/gider ortalaması: liste boşsa sıfır döndür
        "gelir_ortalama": round(np.mean(gelir_tutarlar), 2) if len(gelir_tutarlar) > 0 else 0,
        "gider_ortalama": round(np.mean(gider_tutarlar), 2) if len(gider_tutarlar) > 0 else 0,
    }

    # Sonuçları ekrana yazdır
    print("\n📈 NUMPY İSTATİSTİKLERİ:")
    print(f"  Genel Ortalama  : {sonuclar['genel_ortalama']:>10.2f} TL")
    print(f"  Minimum Tutar   : {sonuclar['genel_min']:>10.2f} TL")
    print(f"  Maksimum Tutar  : {sonuclar['genel_max']:>10.2f} TL")
    print(f"  Standart Sapma  : {sonuclar['genel_std']:>10.2f} TL")
    print(f"  Gelir Ort.      : {sonuclar['gelir_ortalama']:>10.2f} TL")
    print(f"  Gider Ort.      : {sonuclar['gider_ortalama']:>10.2f} TL")

    return sonuclar
