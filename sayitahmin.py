import random as r
rastgelesayi = r.randint(1,100)
print("-- SAYI TAHMİN OYUNU --")
print("\n1 ile 100 arasında bir sayı belirlendi.")
while True:
    tahmin = int(input("\nSayıyı Tahmin Edin: "))
    if tahmin == rastgelesayi:
        print("\n******************")
        print("* Doğru Bildiniz *")
        print("******************")
        print("Doğru Sayı : ", rastgelesayi)
        print("******************")
        print("""Görüş ve Öneriler için :
Instagram : @kemalasliyuksek
Twitter : @kemalasliyuksek
Email : kemalaslyksk53@gmail.com""")
    elif tahmin < rastgelesayi:
        print("\n---------------------------")
        print("-- Daha Büyük Sayı Girin --")
        print("---------------------------")
    elif tahmin > rastgelesayi:
        print("\n---------------------------")
        print("-- Daha Küçük Sayı Girin --")
        print("---------------------------")
    elif tahmin > 100:
        print("\nGirdiğiniz sayı 100'den küçük olmalıdır!")
    elif tahmin < 0:
        print("\nGirdiğiniz sayı 0'dan büyük olmalıdır!")
    else:
        print("\nLütfen 1 ile 100 arasında bir sayı giriniz.")
