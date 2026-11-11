a=int(input("Enter a number: "))
k=0
while a!=1:
    if a%2==0:
        a=a//2
    else:
        a=3*a+1 
    k+=1
    print(a)
print("Total steps:",k)