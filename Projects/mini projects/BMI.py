weight = int(input("Enter a weight in KG \n"))
height = float(input("Enter a height in meter float \n"))
bmi = weight / (height * height)
# bmi_as_int = int(bmi)
# print(bmi_as_int)
print(bmi)
if bmi < 18.5:
    print(f"your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"your BMI is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"your BMI is {bmi}, you are obese.")
else:
    print(f"your BMI is {bmi}, your are clinically obese")