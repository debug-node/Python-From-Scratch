import time
t = time.strftime('%H:%M:%S')
print(t)
h = int(time.strftime('%H'))
##h = int(input("enter hour : "))
print(h)
if(h>=00 and h<=12):
    print("good morning sir")
elif(h>12 and h<=16):
    print("good afternoon sir")
elif(h>16 and h<=18):
    print("good evening sir")
else:
    print("good night sir")