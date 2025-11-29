print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N").upper()
extra_cheese = input("Do you want extra cheese? Y or N").upper()
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid pizza size selected.")
    exit()

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
elif add_pepperoni != "N":
    print("Invalid input for pepperoni option.")
    exit()     

if extra_cheese == "Y":
    bill += 1
elif extra_cheese != "N":
    print("Invalid input for extra cheese option.")
    exit()

print("\nThank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is : ${bill}")

