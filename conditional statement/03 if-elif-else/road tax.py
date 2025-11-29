cp=int(input("enter bike price: "))
tax=0
if(cp>100000):
    tax=15/100*cp
elif(cp>50000 and cp <= 100000 ):
    tax=10/100*cp
else:
    tax=5/100*cp
print("tax to be paid",tax)