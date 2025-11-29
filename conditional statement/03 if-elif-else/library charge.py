nd=int(input("enter number of days : "))
amt=0
if(nd<=5):
    amt=nd*2
elif(nd>=6 and nd<=10):
    amt=nd*3
elif(nd>=11 and nd<=15):
    amt=nd*4
else:
    amt=nd*5
print("total charge",amt)