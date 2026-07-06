class BankaHesabi:
    def __init__(self, isim, bakiye=0):
        self.isim = isim
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar <= 0:
            raise ValueError("Yatırılacak miktar pozitif olmalı!")
        self.bakiye += miktar
        print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")

    def para_cek(self, miktar):
        if miktar <= 0:
            raise ValueError("Çekilecek miktar pozitif olmalı!")
        if miktar > self.bakiye:
            raise ValueError(f"Yetersiz bakiye! Mevcut bakiye: {self.bakiye} TL")
        self.bakiye -= miktar
        print(f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL")

    def __str__(self):
        return f"Hesap Sahibi: {self.isim} | Bakiye: {self.bakiye} TL"


if __name__ == "__main__":
    hesap1 = BankaHesabi("Ahmet", 1000)
    hesap2 = BankaHesabi("Ayşe", 500)

    hesap1.para_yatir(250)
    hesap1.para_cek(100)

    hesap2.para_yatir(1000)

    try:
        hesap2.para_cek(5000)  
    except ValueError as e:
        print(f"Hata: {e}")

    print()
    print(hesap1)
    print(hesap2)