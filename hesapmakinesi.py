print("---------- HESAP MAKİNESİ (deneme) ----------")
print("\nHangi İşlemi Yapmak İstiyorsunuz ? (Uygulamamız şu anda sadece iki sayı içeren işlemlerden oluşmaktadır.)")
print("\n1 - Toplama \n2 - Çıkarma \n3 - Çarpma \n4 - Bölme \n5 - Karekök Alma \n6 - Üst Alma \n7 - Mutlak Değer Alma \n8 - Tam Sayıya Yuvarlama \n9 - Logaritma Alma \n10 - Faktoriyel Hesaplama \n11 - Tarih Hesaplama")
while True:
    islem = input("\nNumara:  ")
    if islem == "1":
        print("\n-- TOPLAMA İŞLEMİ --")
        t1 = int(input("\nToplanacak 1. Sayı: "))
        t2 = int(input("\nToplanacak 2. Sayı: "))
        print("\n--------------------------------")
        print("--------------------------------")
        print("İşleminizin Sonucu =  " , t1 + t2)
        print("--------------------------------")
        print("--------------------------------")
        print("Görüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")
    elif islem == "2":
        print("\n-- ÇIKARMA İŞLEMİ --")
        c1 = int(input("\nEksilen Sayı:  "))
        c2 = int(input("\nÇıkan Sayı: "))
        print("\n--------------------------------")
        print("--------------------------------")
        print("İşleminizin Sonucu =  " , c1 - c2)
        print("--------------------------------")
        print("--------------------------------")
        print("\nGörüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")
    elif islem == "3":
        print("\n-- ÇARPMA İŞLEMİ --")
        ca1 = int(input("\nÇarpan Sayı:  "))
        ca2 = int(input("\nÇarpan Sayı:  "))
        print("\n--------------------------------")
        print("--------------------------------")
        print("İşleminizin Sonucu =  " , ca1 * ca2)
        print("--------------------------------")
        print("--------------------------------")
        print("\nGörüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")

    elif islem == "4":
        print("\n-- BÖLME İŞLEMİ --")
        b1 = float(input("\nBölünen Sayı:  "))
        b2 = float(input("\nBölen Sayı:  "))
        print("\n--------------------------------")
        print("--------------------------------")
        print("İşleminizin Sonucu =  " , b1 / b2)
        print("--------------------------------")
        print("--------------------------------")
        print("\nGörüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")

    elif islem == "5":
        import math
        print("\n-- KAREKÖK ALMA İŞLEMİ --")
        k = int(input("Kareökü Alınacak Sayı:  "))
        print("\n--------------------------------")
        print("--------------------------------")
        print("İşleminizin Sonucu =  " , math.sqrt(k))
        print("--------------------------------")
        print("--------------------------------")
        print("\nGörüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")

    elif islem == "6":
        import math
        print("\n-- ÜS ALMA İŞLEMİ --")
        us1 = int(input("Taban Sayı:  "))
        us2 = int(input("Üs:  "))
        print("\n--------------------------------")
        print("--------------------------------")
        print("İşleminizin Sonucu =  " , us1 ** us2)
        print("--------------------------------")
        print("--------------------------------")
        print("\nGörüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")

    elif islem == "7":
        print("\n-- MUTLAK DEĞER ALMA --")
        mu = int(input("\nMutlak Değeri Alınacak Sayı: "))
        print("\n--------------------------------")
        print("--------------------------------")
        print("Mutlak Değeri =  " , abs(mu))
        print("--------------------------------")
        print("--------------------------------")
        print("\nGörüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")

    elif islem == "8":
        print("\n-- TAM SAYIYA YUVARLAMA --")
        ts = float(input("\nTam Sayıya Yuvarlanacak Sayı:  "))
        print("\n--------------------------------")
        print("--------------------------------")
        print("Tam Sayı Hâli =  " , round(ts))
        print("--------------------------------")
        print("--------------------------------")
        print("\nGörüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")

    elif islem == "9":
        import math
        print("\n-- Logaritma --")
        print("\n(x = y sayısının a tabanına göre logaritması)")
        lg1 = int(input("\ny: "))
        lg2 = int(input("\na: "))
        print("\n--------------------------------")
        print("--------------------------------")
        print("Sonuç   x =  " , math.log(lg1 , lg2))
        print("--------------------------------")
        print("--------------------------------")
        print("\nGörüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")

    elif islem == "10":
        import math
        print("\n-- Faktoriyel Hesaplama --")
        fak = int(input("\nFaktoriyeli Alınacak Sayı: "))
        print("\n--------------------------------")
        print("--------------------------------")
        print("Logaritma Sonucu =  " , math.factorial(fak))
        print("--------------------------------")
        print("--------------------------------")
        print("\nGörüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")

    elif islem == "11":
        print("\n-- Tarih Hesaplama --")
        print("\nGün -> Yıl \nGün -> Ay \nGün -> Hafta \n \nHafta -> Yıl \nHafta -> Ay \nHafta -> Gün \n \nAy -> Yıl \nAy -> Hafta \nAy -> Gün \n \nYıl -> Ay \nYıl -> Hafta \nYıl -> Gün \n \n1 Ay 30 gün olarak hesaplanmaktadır. ")
        tur = input("\nNe tür bir dönüştürme yapmak istiyorsunuz? (Örn: Gün -> Yıl için 'gün yıl' yazılmalı.) :  ")
        if tur == "gün yıl":
            gnyl = int(input("\nGün:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", gnyl / 365)
        elif tur == "gün ay":
            gnay = int(input("\nGün:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", gnay / 30)
        elif tur == "gün hafta":
            gnhft = int(input("\nGün:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", gnhft / 7)
        elif tur == "hafta yıl":
            hftyl = int(input("\nHafta:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", hftyl / 52)
        elif tur == "hafta ay":
            hftay = int(input("\nHafta:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", gnhft / 4)
        elif tur == "hafta gün":
            hftgn = int(input("\nHafta:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", hftgn * 7)
        elif tur == "ay yıl":
            ayyl = int(input("\nAy:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", ayyl / 12)
        elif tur == "ay hafta":
            ayhft = int(input("\nAy:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", ayhft * 4)
        elif tur == "ay gün":
            aygn = int(input("\nAy:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", aygn * 32)
        elif tur == "yıl ay":
            ylay = int(input("\nYıl:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", ylay * 12)
        elif tur == "yıl hafta":
            ylhft = int(input("\nYıl:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", ylhft * 52)
        elif tur == "yıl gün":
            ylgn = int(input("\nYıl:  "))
            print("\n--------------------------------")
            print("Sonuç :  ", ylgn * 365)
        else:
            print("\n--------------------------------")
            print("Geçersiz Giriş...")
        print("--------------------------------")
        print("\nGörüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")
    else:
        print("\nGeçersiz giriş...")
        print("\n--------------------------------")
        print("Tekrar İşlem Yapmak İsterseniz Lütfen Uygulamamızı Yeniden Başlatınız. \n> Uygulama geliştirme aşamasındadır. <")
        print("--------------------------------")
        print("Görüş ve Önerileriniz İçin \nInstagram: @kemalasliyuksek \nTwitter: @kemalasliyuksek \nMail Adresleri: \nkemalaslyksk53@gmail.com \nkemalaslyksk53@outlook.com")
        print("--------------------------------")
