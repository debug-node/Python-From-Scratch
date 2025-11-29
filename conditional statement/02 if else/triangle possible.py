s1=int(input("enter side : "))
s2=int(input("enter side : "))
s3=int(input("enter side : "))
if((s1+s2 >s3) and (s1+s3>s2) and (s2+s3>s1)):
    print("triangle is possible")
else:
    print("triangle is not possible")