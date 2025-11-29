# EXPLICIT TYPECASTING :- conversion done via programmerr
string="13"
number=12
string_num = int(string)
sum = string_num + number
print("the sum of both number =",sum)
# IMPLICIT TYPCASTING :- conversion done via python interpreter itself
a=12
print(type(a))
b=12.22
print(type(b))
c=a+b
print(c)
print(type(c))