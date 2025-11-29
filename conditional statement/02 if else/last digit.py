n=int(input("enter a number :"))
ld=n%10
print("last digit of number :",ld)
if(ld%3==0):
    print("last digit is divisible by 3")
else:
    print("not divisible by 3")