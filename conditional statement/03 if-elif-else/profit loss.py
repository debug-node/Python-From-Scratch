cp=int(input("enter cost price : "))
sp=int(input("enter selling price : "))
if(cp<sp):
    print("profit")
elif(cp>sp):
    print("loss")
else:
    print("equal")