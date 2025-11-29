l =float(input("enter length: "))
b =float(input("enter breadth: "))
p=2*(l+b)
ar=l*b
print("perimeter:",p)
print("area :",ar)
if(ar>p):
    print("area is greater")
elif(ar<p):
    print("perimeter is greater")
else:
    print("both are equal")