# ============================================================
# dosya_islemleri.py - CSV Okuma / Yazma
# Proje: Kişisel Finans ve Harcama Takip Sistemi
# Öğrenci: Senanur Özcan | 24111005 | Yazılım Geliştirme
# ============================================================

import csv                   # CSV okuma/yazma için standart kütüphane
import os                    # Dosya varlığı kontrolü için
from finans_modeli import Islem   # Islem nesnesi oluşturmak için

# CSV dosyasındaki sütun başlıkları (sıra önemli)
CSV_BASLIKLAR = ["id", "tutar", "tarih", "aciklama", "tip"]


def csv_kaydet(dosya_adi: str, gelirler: list, giderler: list) -> None:
    """
    Tüm gelir ve gider verilerini belirtilen CSV dosyasına kaydeder.

    Args:
        dosya_adi (str): Kaydedilecek CSV dosyasının adı (ör: 'veriler.csv')
        gelirler (list): Gelir işlemlerinin listesi
        giderler (list): Gider işlemlerinin listesi
    """
    try:
        # Gelir ve gider listelerini tek bir listede birleştir
        tum_islemler = gelirler + giderler

        # Tarihe göre kronolojik sırala (CSV daha okunabilir olur)
        tum_islemler.sort(key=lambda x: x.tarih)

        # Dosyayı yaz modunda aç; newline='' satır sonu sorunlarını önler
        # utf-8-sig: Excel'in Türkçe karakterleri doğru göstermesi için BOM ekler
        with open(dosya_adi, mode="w", newline="", encoding="utf-8-sig") as dosya:
            writer = csv.DictWriter(dosya, fieldnames=CSV_BASLIKLAR)

            # İlk satır olarak başlıkları yaz (id, tutar, tarih, ...)
            writer.writeheader()

            # Her işlemi sözlüğe çevirip CSV satırı olarak yaz
            for islem in tum_islemler:
                writer.writerow(islem.to_dict())

        print(f"✅ Veriler başarıyla kaydedildi → '{dosya_adi}' ({len(tum_islemler)} kayıt)")

    except PermissionError:
        # Dosya başka bir program tarafından açıksa (örn: Excel) bu hata oluşur
        print(f"❌ Hata: '{dosya_adi}' dosyasına yazma izni yok.")
    except Exception as hata:
        # Diğer beklenmedik hatalar (disk dolu, geçersiz yol vb.)
        print(f"❌ CSV kaydetme hatası: {hata}")


def csv_oku(dosya_adi: str) -> tuple:
    """
    CSV dosyasındaki verileri okuyarak gelir ve gider listelerini oluşturur.

    Args:
        dosya_adi (str): Okunacak CSV dosyasının adı

    Returns:
        tuple: (gelirler listesi, giderler listesi)
    """
    # Boş listelerle başla; dosya okunamazsa bunlar döndürülür
    gelirler = []
    giderler = []

    # Dosya mevcut değilse uyar ve boş listelerle devam et
    if not os.path.exists(dosya_adi):
        print(f"⚠️ '{dosya_adi}' dosyası bulunamadı. Boş listelerle başlanıyor.")
        return gelirler, giderler

    try:
        # Dosyayı oku modunda aç (utf-8-sig ile BOM karakterini otomatik atlar)
        with open(dosya_adi, mode="r", encoding="utf-8-sig") as dosya:
            reader = csv.DictReader(dosya)  # Her satırı sözlük olarak oku

            for satir in reader:
                # Sözlükten Islem nesnesi oluştur (from_dict tip dönüşümlerini halleder)
                islem = Islem.from_dict(satir)

                # Tip alanına göre doğru listeye ekle
                if islem.tip == "gelir":
                    gelirler.append(islem)
                elif islem.tip == "gider":
                    giderler.append(islem)

        print(f"✅ Veriler yüklendi → '{dosya_adi}' "
              f"({len(gelirler)} gelir, {len(giderler)} gider)")

    except csv.Error as hata:
        # Bozuk veya hatalı formatlı CSV dosyası
        print(f"❌ CSV okuma hatası: {hata}")
    except Exception as hata:
        # Kodlama hatası, eksik sütun vb. beklenmedik durumlar
        print(f"❌ Beklenmeyen hata: {hata}")

    # Her durumda (hata olsa bile) listeleri döndür
    return gelirler, giderler
