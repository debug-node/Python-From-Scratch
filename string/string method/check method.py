# endswith() :- check string ends with that value
a = "aditya kumar $$"
print(a.endswith("$"))

a = "aditya kumar"
print(a.endswith("a",4,8)) # also check by given index no.

# find() :- check occurance of given value if { yes = returns index no. / no = -1 }
a = "he is a good boy"
print(a.find("a"))
print(a.find("n"))

# index() :- just like find() but when value absent then returns value error
a = "he is a good boy"
print(a.index("is"))
# a = "he is a good boy"
# print(a.index("was"))

# isalnum() :- returns true { A-Z,a-z.0-9 } exist
a = "welcometojungle"
print(a.isalnum())
a = "welcome to jungle"
print(a.isalnum())

# isalpha() :- checks only alphabets
a = "welcome"
print(a.isalpha())
a = "welcome 4"
print(a.isalpha())

# islower() :- checks lower case
a = "aditya"
print(a.islower())
a = "Aditya"
print(a.islower())

# isprintable() :- checks string are printable
a = "he is a good boy"
print(a.isprintable())
a = "aditya\n"
print(a.isprintable())

# isspace() :- check white spaces
a = "    "
print(a.isspace())
a = "adityakumar"
print(a.isspace())

# istitle() :- check first character of each words of string is upper case 
a = "World Health Organisation"
print(a.istitle())
a = "World health organisation"
print(a.istitle())

# isupper() :- checks upper case 
a = "ADITYA"
print(a.isupper())
a = "aditya"
print(a.isupper())

# startswith() :- checks the given string start with that value
a = "he is a good boy"
print(a.startswith("he"))
a = "he is a good boy"
print(a.startswith("is"))
