harcamalar = []  # Harcamaları saklayacak liste

while True:
    print("-----------HARCAMA TAKİP UYGULAMASI-----------")
    print("1- Harcama eklemek için seçiniz")
    print("2- Harcamalari listelemek için seçiniz")
    print("3- Seçilen kategorinin toplam tutarini gösterilmesi için seçiniz")
    print("4- Çikiş yapiniz")


    secim = input("Seçiminizi giriniz: ")


    if secim == "1":
        kategori = input("Kategori giriniz: ")
        tutar = float(input("Tutar giriniz: "))
        tarih = input("Tarih giriniz (G/A/Y): ")

        harcamakayit = {"kategori": kategori, "tutar": tutar, "tarih": tarih} #bir sözlük oluşturuz değerler eklenir
        harcamalar.append(harcamakayit) #alınan değerler harcamalar listesine atanır
        print("Harcamalar başari ile kaydedildi!")


    elif secim == "2":
        print("-----Harcama Listesi-----")
        for element in harcamalar:
            print(f"{element['tarih']} | {element['kategori']} | {element['tutar']} TL")

    elif secim == "3":
        arananKategori = input("Kategori giriniz: ")
        toplam = 0
        for element in harcamalar:
            if element["kategori"] == arananKategori:
                toplam += element["tutar"]
        print(f"{arananKategori} kategorisinde toplam harcama: {toplam} TL")


    elif secim == "4":
        print("Programdan çikiliyor...")
        break

    else:
        print("Geçersiz seçim.")
