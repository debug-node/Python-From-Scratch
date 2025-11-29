km=int(input("enter kilometer : "))
amt=0
if(km<=10):
    amt=km*11
elif(km>10 and km<=100):
    amt=110+(km-10)*10
else:
    amt=1010+(km-100)*9
print("total bill",amt)