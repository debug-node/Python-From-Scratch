a=int(input("first no."))
b=int(input("second no."))
c=int(input("third no."))
if((a>b and a<c) or (a<b and a>c)):
    print("middle =",a)
elif((b>a and b<c) or (b<a and b>c)):
    print("middle =",b)
else:
    print("middle =",c)