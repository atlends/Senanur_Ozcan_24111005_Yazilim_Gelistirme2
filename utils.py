# ============================================================
# utils.py - Yardımcı Fonksiyonlar
# Proje: Kişisel Finans ve Harcama Takip Sistemi
# Öğrenci: Senanur Özcan | 24111005 | Yazılım Geliştirme
# ============================================================

import re                        # Düzenli ifadeler (regex) için
from datetime import datetime    # Tarih doğrulama için


def yeni_id_olustur(liste: list) -> int:
    """
    Verilen listedeki en büyük ID'yi bulup bir artırarak yeni benzersiz ID üretir.

    Args:
        liste (list): Islem nesnelerinden oluşan liste

    Returns:
        int: Yeni benzersiz ID
    """
    # Liste boşsa ilk ID olarak 1'den başla
    if not liste:
        return 1

    # Listedeki tüm ID'lerin en büyüğünü bul, üstüne 1 ekle
    return max(islem.id for islem in liste) + 1


def tarih_kontrol(tarih: str) -> bool:
    """
    Girilen tarihin doğru formatta (YYYY-MM-DD) olup olmadığını kontrol eder.

    Args:
        tarih (str): Kontrol edilecek tarih string'i

    Returns:
        bool: Geçerli ise True, değil ise False
    """
    # Önce regex ile format kontrolü: 4 rakam - 2 rakam - 2 rakam
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, tarih):
        return False  # Format uyuşmuyorsa direkt False dön

    try:
        # Regex geçse de geçersiz tarih olabilir (örn: 2026-13-45)
        # strptime ile gerçek tarih geçerliliğini doğrula
        datetime.strptime(tarih, "%Y-%m-%d")
        return True
    except ValueError:
        # Geçersiz tarih değeriyse (ay > 12 vb.) False dön
        return False


def sayi_kontrol(deger: str) -> bool:
    """
    Kullanıcıdan alınan değerin sayıya (float) dönüştürülebilir olup olmadığını kontrol eder.

    Args:
        deger (str): Kontrol edilecek değer

    Returns:
        bool: Dönüştürülebilir ise True, değil ise False
    """
    try:
        # float() çevrim başarılıysa geçerli bir sayıdır
        float(deger)
        return True
    except (ValueError, TypeError):
        # Harf, boş değer veya None gibi durumlar için False dön
        return False


def menu_goster() -> None:
    """
    Programın ana menüsünü ekrana yazdırır.
    """
    # Görsel ayraç çizgisi
    print("\n" + "=" * 45)
    print("   💰 KİŞİSEL FİNANS TAKİP SİSTEMİ 💰")
    print("=" * 45)

    # Kullanıcıya sunulan 7 menü seçeneği
    print("  1. Gelir Ekle")
    print("  2. Gider Ekle")
    print("  3. İşlemleri Listele")
    print("  4. Analiz Yap")
    print("  5. Grafik Göster")
    print("  6. CSV Kaydet")
    print("  7. Çıkış")

    print("=" * 45)
    # Kullanıcı girişini aynı satırda beklet
    print("Seçiminizi yapın (1-7): ", end="")
