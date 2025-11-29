import time
t=time.strftime('%I:%M:%S:%p') # current time
print(t)
p=time.strftime('%x') # DATE
print(p)
p=time.strftime('%X') # TIME
print(p)
p=time.strftime('%z') # TIME ZONE
print(p)
p=time.strftime('%Z') # TIME ZONE NAME
print(p)
p=time.strftime('%a') # WEEK DAY NAME = MON
print(p)
p=time.strftime('%A') # FULL WEEK DAY NAME = MONDAY
print(p)
p=time.strftime('%b') # MONTH NAME = JAN
print(p)
p=time.strftime('%B') # FULL MONTH NAME = JANUARY
print(p)
p=time.strftime('%c') # DATE AND TIME FULL REPRESENTATION = Mon Sep 16 19:22:16 2024
print(p)
p=time.strftime('%d') # TODAY DATE
print(p)
p=time.strftime('%H') # 24-HR. CLOCK
print(p)
p=time.strftime('%j') # DAY OF THE YEAR [001,366].
print(p)
p=time.strftime('%m') # MONTH [01,12]
print(p)
p=time.strftime('%U') # WEEK NUMBER [00,53] :(Sunday as the first day of the week) 
print(p)
p=time.strftime('%w') # WEEK DAY SUNDAY=0
print(p)
p=time.strftime('%W') # WEEK NUMBER [00,53] : (MONDAY as the first day of the week) 
print(p)
p=time.strftime('%y') # YEAR WITHOUT CENTURY = 24
print(p)
p=time.strftime('%Y') # YEAR WITH CENTURY = 2024
print(p)

