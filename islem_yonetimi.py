# ============================================================
# islem_yonetimi.py - Gelir/Gider İşlemleri
# Proje: Kişisel Finans ve Harcama Takip Sistemi
# Öğrenci: Senanur Özcan | 24111005 | Yazılım Geliştirme
# ============================================================

# Kendi modüllerimizden gerekli sınıf ve fonksiyonları içe aktar
from finans_modeli import Islem
from utils import yeni_id_olustur, tarih_kontrol, sayi_kontrol


def gelir_ekle(gelirler: list) -> None:
    """
    Kullanıcıdan alınan bilgileri doğrulayarak yeni bir gelir kaydı
    oluşturur ve listeye ekler.

    Args:
        gelirler (list): Mevcut gelir listesi (güncellenir)
    """
    print("\n--- 📥 Gelir Ekle ---")
    try:
        # --- Tutar Girişi ---
        tutar_str = input("Tutar (TL): ").strip()  # Baştaki/sondaki boşlukları temizle

        # Girilen değer sayıya çevrilebilir mi?
        if not sayi_kontrol(tutar_str):
            print("❌ Hata: Geçersiz tutar. Sayısal bir değer giriniz.")
            return

        tutar = float(tutar_str)

        # Tutar pozitif olmalı; negatif veya sıfır kabul edilmez
        if tutar <= 0:
            print("❌ Hata: Tutar sıfırdan büyük olmalıdır.")
            return

        # --- Tarih Girişi ---
        tarih = input("Tarih (YYYY-MM-DD): ").strip()

        # Tarih formatı ve geçerliliğini kontrol et
        if not tarih_kontrol(tarih):
            print("❌ Hata: Geçersiz tarih formatı. Örnek: 2026-06-01")
            return

        # --- Açıklama Girişi ---
        aciklama = input("Açıklama: ").strip()

        # Boş açıklama kabul edilmez
        if not aciklama:
            print("❌ Hata: Açıklama boş bırakılamaz.")
            return

        # --- Nesne Oluşturma ve Listeye Ekleme ---
        # Mevcut listedeki en büyük ID + 1 ile yeni benzersiz ID üret
        yeni_id = yeni_id_olustur(gelirler)

        # Islem nesnesi oluştur (tip sabit olarak 'gelir')
        yeni_islem = Islem(id=yeni_id, tutar=tutar, tarih=tarih,
                           aciklama=aciklama, tip="gelir")

        # Gelirler listesine ekle
        gelirler.append(yeni_islem)
        print(f"✅ Gelir başarıyla eklendi → {yeni_islem}")

    except Exception as hata:
        # Beklenmedik hataları yakala (örn: klavye kesintisi)
        print(f"❌ Beklenmeyen hata: {hata}")


def gider_ekle(giderler: list) -> None:
    """
    Kullanıcıdan alınan bilgileri doğrulayarak yeni bir gider kaydı
    oluşturur ve listeye ekler.

    Args:
        giderler (list): Mevcut gider listesi (güncellenir)
    """
    print("\n--- 📤 Gider Ekle ---")
    try:
        # --- Tutar Girişi ---
        tutar_str = input("Tutar (TL): ").strip()

        # Sayısal değer kontrolü
        if not sayi_kontrol(tutar_str):
            print("❌ Hata: Geçersiz tutar. Sayısal bir değer giriniz.")
            return

        tutar = float(tutar_str)

        # Negatif veya sıfır gider mantıklı değil
        if tutar <= 0:
            print("❌ Hata: Tutar sıfırdan büyük olmalıdır.")
            return

        # --- Tarih Girişi ---
        tarih = input("Tarih (YYYY-MM-DD): ").strip()

        # YYYY-MM-DD formatı ve geçerli tarih kontrolü
        if not tarih_kontrol(tarih):
            print("❌ Hata: Geçersiz tarih formatı. Örnek: 2026-06-01")
            return

        # --- Açıklama Girişi ---
        aciklama = input("Açıklama: ").strip()

        # Açıklama zorunlu alan
        if not aciklama:
            print("❌ Hata: Açıklama boş bırakılamaz.")
            return

        # --- Nesne Oluşturma ve Listeye Ekleme ---
        # Gider listesindeki en yüksek ID'nin bir fazlasını al
        yeni_id = yeni_id_olustur(giderler)

        # Islem nesnesi oluştur (tip sabit olarak 'gider')
        yeni_islem = Islem(id=yeni_id, tutar=tutar, tarih=tarih,
                           aciklama=aciklama, tip="gider")

        # Giderler listesine ekle
        giderler.append(yeni_islem)
        print(f"✅ Gider başarıyla eklendi → {yeni_islem}")

    except Exception as hata:
        print(f"❌ Beklenmeyen hata: {hata}")


def islemleri_listele(gelirler: list, giderler: list) -> None:
    """
    Tüm gelir ve gider kayıtlarını düzenli bir formatta ekrana yazdırır.

    Args:
        gelirler (list): Gelir işlemlerinin listesi
        giderler (list): Gider işlemlerinin listesi
    """
    # Başlık çerçevesi
    print("\n" + "=" * 65)
    print("                 📋 TÜM İŞLEMLER")
    print("=" * 65)

    # Her iki liste de boşsa uyarı ver
    if not gelirler and not giderler:
        print("  Henüz hiç işlem kaydedilmemiş.")
        return

    # --- Gelirler Bölümü ---
    if gelirler:
        print("\n  💚 GELİRLER:")
        print("  " + "-" * 60)

        # Tarihe göre kronolojik sırala ve yazdır
        for islem in sorted(gelirler, key=lambda x: x.tarih):
            print(f"  {islem}")

        # Tüm gelir tutarlarının toplamını hesapla
        toplam_gelir = sum(i.tutar for i in gelirler)
        print(f"\n  Toplam Gelir: {toplam_gelir:>10.2f} TL")
    else:
        print("\n  💚 GELİRLER: (Kayıt yok)")

    print()

    # --- Giderler Bölümü ---
    if giderler:
        print("  ❤️  GİDERLER:")
        print("  " + "-" * 60)

        # Tarihe göre kronolojik sırala ve yazdır
        for islem in sorted(giderler, key=lambda x: x.tarih):
            print(f"  {islem}")

        # Tüm gider tutarlarının toplamını hesapla
        toplam_gider = sum(i.tutar for i in giderler)
        print(f"\n  Toplam Gider: {toplam_gider:>10.2f} TL")
    else:
        print("  ❤️  GİDERLER: (Kayıt yok)")

    # --- Net Bakiye ---
    if gelirler or giderler:
        # Net = Toplam Gelir - Toplam Gider
        net = sum(i.tutar for i in gelirler) - sum(i.tutar for i in giderler)

        # Pozitifse kâr, negatifse zarar simgesi göster
        durum = "✅" if net >= 0 else "⚠️"
        print(f"\n  {durum} NET BAKİYE: {net:>10.2f} TL")

    print("=" * 65)


def islem_sil(gelirler: list, giderler: list, islem_id: int) -> bool:
    """
    Verilen ID'ye sahip işlemi bularak ilgili listeden siler.

    Args:
        gelirler (list): Gelir listesi
        giderler (list): Gider listesi
        islem_id (int): Silinecek işlemin ID'si

    Returns:
        bool: Silme başarılı ise True, işlem bulunamadı ise False
    """
    # Önce gelirler listesinde ara
    for i, islem in enumerate(gelirler):
        if islem.id == islem_id:
            # Eşleşen işlemi listeden çıkar (pop indekse göre siler)
            silinen = gelirler.pop(i)
            print(f"✅ Gelir silindi → {silinen}")
            return True  # Başarıyla silindi

    # Gelirde bulunamadıysa giderler listesinde ara
    for i, islem in enumerate(giderler):
        if islem.id == islem_id:
            silinen = giderler.pop(i)
            print(f"✅ Gider silindi → {silinen}")
            return True  # Başarıyla silindi

    # Her iki listede de bulunamadı
    print(f"❌ ID={islem_id} ile eşleşen işlem bulunamadı.")
    return False
