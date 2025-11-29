m=float(input("enter marks :"))
if(m>=300 and m<=500):
    print("first division")
elif(m<300 and m>=240):
    print("second division")
elif(m<240 and m>=170):
    print("third division")
elif(m<170 and m>=120):
    print("pass")
else:
    print("fail")