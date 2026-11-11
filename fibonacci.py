a=0
b=1
say=0
sonEded=0

while a<=1000:
    print(a)
    sonEded=a
    say+=1
    x=a+b
    a=b
    b=x
print("Sonuncu ədəd:", sonEded, "Ədədlərin sayı:", say)