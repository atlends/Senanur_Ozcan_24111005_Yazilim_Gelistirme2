# ============================================================
# finans_modeli.py - Sınıf (Class) Yapıları
# Proje: Kişisel Finans ve Harcama Takip Sistemi
# Öğrenci: Senanur Özcan | 24111005 | Yazılım Geliştirme
# ============================================================


class Islem:
    """
    Bir gelir veya gider işlemini temsil eden sınıf.

    Attributes:
        id (int): Benzersiz işlem kimliği
        tutar (float): İşlem tutarı (TL)
        tarih (str): İşlem tarihi (YYYY-MM-DD formatında)
        aciklama (str): İşleme ait açıklama
        tip (str): İşlem tipi - 'gelir' veya 'gider'
    """

    def __init__(self, id: int, tutar: float, tarih: str, aciklama: str, tip: str):
        """
        Islem nesnesini başlatır.

        Args:
            id (int): Benzersiz işlem ID'si
            tutar (float): İşlem tutarı
            tarih (str): YYYY-MM-DD formatında tarih
            aciklama (str): Kısa açıklama
            tip (str): 'gelir' veya 'gider'
        """
        # Her işlemin benzersiz kimlik numarası
        self.id = id

        # İşlem miktarı (Türk Lirası cinsinden)
        self.tutar = tutar

        # İşlemin gerçekleştiği tarih (YYYY-MM-DD formatı zorunlu)
        self.tarih = tarih

        # İşlemi açıklayan kısa not (örn: "Maaş", "Kira")
        self.aciklama = aciklama

        # İşlem kategorisi: yalnızca 'gelir' veya 'gider' olabilir
        self.tip = tip

    def __str__(self) -> str:
        """İşlemi okunabilir formatta döndürür."""
        # Gelir için '+', gider için '-' sembolü kullan
        tip_sembol = "+" if self.tip == "gelir" else "-"

        # Sütunları hizalayarak düzenli tablo görünümü oluştur
        return (
            f"[ID:{self.id:>4}] {self.tarih} | "
            f"{tip_sembol}{self.tutar:>10.2f} TL | "
            f"{self.tip.upper():<6} | {self.aciklama}"
        )

    def to_dict(self) -> dict:
        """İşlemi sözlük (dict) formatına dönüştürür (CSV kaydetme için kullanılır)."""
        # CSV satırına yazılabilmesi için tüm alanları anahtar-değer çiftine çevir
        return {
            "id": self.id,
            "tutar": self.tutar,
            "tarih": self.tarih,
            "aciklama": self.aciklama,
            "tip": self.tip,
        }

    @classmethod
    def from_dict(cls, veri: dict) -> "Islem":
        """
        Sözlükten Islem nesnesi oluşturur (CSV okuma için).

        Args:
            veri (dict): CSV'den okunan satır verisi

        Returns:
            Islem: Oluşturulan nesne
        """
        # CSV'den okunan değerler string geldiği için uygun tiplere dönüştür
        return cls(
            id=int(veri["id"]),          # String → int
            tutar=float(veri["tutar"]),  # String → float
            tarih=veri["tarih"],         # Tarih string olarak kalır
            aciklama=veri["aciklama"],
            tip=veri["tip"],             # 'gelir' veya 'gider'
        )
