a=int(input("eded daxil edin: (1-100)"))
eded=22
k=1
while a!=eded:
    if a<eded:
        print("Daha boyuk eded daxil edin!")
    else:
        print("Daha kicik eded daxil edin!")
    a=int(input("eded daxil edin: (1-100)"))
    k+=1
print("Tebrikler! " + str(k) + " cehd ile dogru ededi tapdiniz!")
