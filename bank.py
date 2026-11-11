balans=500
while True:
    print("1. Balansı göstər")
    print("2. Pul yatır")
    print("3. Pul çıxar")
    print("4. Çıxış")

    secim=input("Seçiminizi edin (1-4): ")
    if secim=="1":
        print("Cari balans: ", balans, "AZN")
    elif secim=="2":
        mebleg=(float(input("Yatırmaq istədiyiniz məbləği daxil edin: ")))
        if mebleg<=0:
            print("Yanlış məbləğ")
        else:
            balans+=mebleg
        print("Uğurlu əməliyyat! Yeni balans:", balans, "AZN")
    elif secim=="3":
        mebleg=float(input("Çıxarmaq istədiyiniz məbləği daxil edin: "))
        if mebleg<=0:
            print("Yanlış məbləğ")
        elif mebleg>balans:
            print("Balansınızda kifayət qədər vəsait yoxdur.")
        else:
            balans-=mebleg
            print("Uğurlu əməliyyat! Qalan balans: ", balans, "AZN")
    elif secim=="4":
        print("Proqram bitdi. Son balans: ", balans, "AZN")
        break
    else:
        print("Belə seçim mövcud deyil")