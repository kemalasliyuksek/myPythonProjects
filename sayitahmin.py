import random as r
rastgelesayi = r.randint(1,100)
print("-- SAYI TAHMİN OYUNU --")
print("\n1 ile 100 arasında bir sayı belirlendi.")
islem = 0
while True:
    tahmin = int(input("\nSayıyı Tahmin Edin: "))
    if tahmin == rastgelesayi:
        islem = islem + 1
        islemstr = str(islem)
        print("\nTebrikler. ", islemstr + ". tahminde doğru sayıya (", rastgelesayi, ") ulaştınız.")
        print("\nGörüş ve Öneriler için : \nInstagram : @kemalasliyuksek \nTwitter : @kemalasliyuksek \nEmail : kemalaslyksk53@gmail.com")

    elif tahmin < rastgelesayi:
        islem = islem + 1
        print("\n---------------------------")
        print("-- Daha Büyük Sayı Girin --")
        print("---------------------------")
    elif tahmin > rastgelesayi:
        print("\n---------------------------")
        print("-- Daha Küçük Sayı Girin --")
        print("---------------------------")
        islem = islem + 1
    elif tahmin > 100:
        print("\nGirdiğiniz sayı 100'den küçük olmalıdır!")
    elif tahmin < 0:
        print("\nGirdiğiniz sayı 0'dan büyük olmalıdır!")
    else:
        print("\nLütfen 1 ile 100 arasında bir sayı giriniz.")
