y=int(input("time period of service: "))
s=int(input("enter salary: "))
if(y>10):
    b=10/100*s
elif(y>=6 and y<=10):
    b=8/100*s
elif(y<6):
    b=5/100*s
print("net bonus amount :",b)