n=int(input("no. of electric unit"))
amt=0
if(n<=100):
    amt=0
elif(n>100 and n<=200):
    amt=(n-100)*5
elif(n>200):
    amt=500+(n-200)*10
print("amount to pay:",amt)