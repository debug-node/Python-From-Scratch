# upper() :- converts into upper case
a = "aditya kumar"
print(a.upper())

# lower() :- converts into lower case
a = "ADITYA KUMAR"
print(a.lower())

# strip() :- removes white spaces before/after
a = " aditya kumar "
print(a.strip())

# rstrip() :- removes any trailing character
a = "hello baby #$"
print(a.rstrip("#$"))

# replace() :- replaces all occurences of a string with another string
a = "silver spoon"
print(a.replace("sp","m"))

# split() :- seprate string to list
a = "silver spoon"
print(a.split(" "))

# capitalize() :- turns first character = upper case / rest all = lower case
blog = "introduction to python"
print(blog.capitalize())

# center() :- aligns string to the center
b = "welcome to the jungle"
print(b.center(51,"."))
print(len(b))

# count() :- check no of times the given value occur
str = "abrakadabra"
print(str.count("a"))

# title() :- capitalizes each letter of word within a string
a = "he is a good boy"
print(a.title())

# swapcase() :-  converts upper case - lower case / lower case - upper case 
a = "He Is a Good Boy"
print(a.swapcase())