n=(input("enter digit : "))
l=len(n)
m=int(n)%100//10
if l!=3:
    print("enter three digit n")
else:
    print("middle digit is :",m)