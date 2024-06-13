n=int(input())
if n%400 == 0 :
    print(1)
elif n%4 == 0 and n%100 !=0 :
    print(1)
elif n%100 == 0 and n%400 !=0 :
    print(0)
else :
    print(0)