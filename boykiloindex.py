print("Boy Kilo İndexi Hesaplama")
while True:
    boy = float(input("\nLütfen metre cinsinden boyunuzu giriniz (ör: 1.60) : "))
    kilo = int(input("\nLütfen kilogram cinsinden kilonuzu giriniz (ör: 45) : "))
    boykiloindexi = kilo / boy ** 2
    if boykiloindexi <= 18.5:
        print("\nDurumunuz : 'ZAYIF'",boykiloindexi)
    elif 18.5 <= boykiloindexi <= 24.9:
        print("\nDurumunuz : 'NORMAL KİLOLU'", boykiloindexi)
    elif 25 <= boykiloindexi <= 29.9:
        print("\nDurumunuz : 'FAZLA KİLOLU'", boykiloindexi)
    elif 30 <= boykiloindexi <= 34.9:
        print("\nDurumunuz : '1. DERECEDEN OBEZ'", boykiloindexi)
    elif 35 <= boykiloindexi <= 39.9:
        print("\nDurumunuz : '2. DERECEDEN OBEZ'", boykiloindexi)
    elif 40 <= boykiloindexi:
        print("\nDurumunuz : '3. DERECEDEN MORBİD OBEZ'", boykiloindexi)
    print("\n--------------------")
    print("""18.5 kg/m2’nin altında ise ZAYIF
18.5-24.9 kg/m2 arasında ise NORMAL KİLOLU
25-29.9 kg/m2 arasında ise FAZLA KİLOLU
30-34.9 kg/m2 arasında ise I.DERECEDE OBEZ
35-39.9 kg/m2 arasında ise II.DERECEDE OBEZ
40 kg/m2 üzerinde ise III.DERECEDE MORMİD OBEZ""")
    print("--------------------")
