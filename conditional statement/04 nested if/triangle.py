s1=int(input("enter side : "))
s2=int(input("enter side : "))
s3=int(input("enter side : "))
if(s1==s2 and s2==s3):
    print("equilateral triangle")
if((s1==s2 and s2!=s3) or (s1==s3 and s3!=s2) or (s2==s3 and s1!=s2)):
    print("isosceles triangle")
if(s1!=s2 and s2!=s3 and s1!=s3):
    print("scalene triangle")