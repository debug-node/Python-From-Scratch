unt=int(input("no. of electric unit"))
amt=0
if(unt<=100):
    amt=0
elif(unt>100 and unt<=300):
    amt=(unt-100)*2
else:
    amt=400+(unt-300)*5
print("amount to pay:",amt)