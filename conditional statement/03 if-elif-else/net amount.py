mp=int(input("market price of product: "))
d=0
if(mp>10000):
    d=20/100*mp
elif(mp>7000 and mp<=10000):
    d=15/100*mp
elif(mp<=7000):
    d=10/100*mp
print("net price :",mp-d)