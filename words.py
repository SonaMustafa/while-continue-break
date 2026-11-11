coxluq=[]
enUzunSoz=""
saitSayi=0
saitler="AIOUEƏİÖÜaıoueəiöü"
while True:
    soz=input("söz daxil edin: ")
    if soz.lower()=="stop":
        break

    reqem=False
    for i in soz:
        if i.isdigit():
            reqem=True
            break
    if reqem==True:
        print("Rəqəm qəbul edilmir")

    if soz in coxluq:
        print("Bu söz artıq daxil edilib")
        continue
    coxluq.append(soz)
    if len(soz)>len(enUzunSoz):
        enUzunSoz=soz

    if soz and soz[0] in saitler:
        saitSayi+=1

print("Daxil edilmiş sözlər: ", coxluq)
print("Ən uzun söz: ", enUzunSoz)
print("Saitlə başlayan sözlərin sayı: ", saitSayi)