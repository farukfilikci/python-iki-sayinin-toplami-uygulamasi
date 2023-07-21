def toplama():
    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        toplam = sayi1 + sayi2
        print("Sonuç: {:.2f}".format(toplam))
    except ValueError:
        print("Hatalı giriş yaptınız. Lütfen sayıları düzgün bir şekilde girin.")

if __name__ == "__main__":
    toplama()
