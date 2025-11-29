phy=float(input("enter physics number :"))
che=float(input("enter chemistry number :"))
ma=float(input("enter math number :"))
eng=float(input("enter english number :"))
hin=float(input("enter hindi number :"))
sum=phy+che+ma+eng+hin
average=sum/5.0
percentage=(sum/500.0)*100
print("total marks : ",sum)
print("average:",average)
print("percetage",percentage)
if(percentage>= 75):
    print("very good")
elif(percentage>= 60):
    print("good")
elif(percentage>=33):
    print("pass")
else:
    print("fail")