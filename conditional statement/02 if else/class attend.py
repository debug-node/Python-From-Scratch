wd=int(input("toal number of working days: "))
ab=int(input("total number of days absent: "))
print("total number of days present:",wd-ab)
per=(wd-ab)/wd*100
print("percentage of class attend =",per)
if(per>=75):
    print("you can sit in exam")
else:
    print("you can't sit in exam")