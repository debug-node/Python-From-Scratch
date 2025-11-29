# ----------------- Coffee Machine Simulator -----------------
# This script simulates a coffee machine that serves espresso, latte, and cappuccino.
# Features:
#   ✔ Tracks resources (water, milk, coffee)
#   ✔ Processes coin payments with error handling
#   ✔ Reports current machine status
#   ✔ Stops gracefully on 'off'
#   ✔ Handles drinks that don’t use all ingredients (e.g., espresso has no milk)
# ------------------------------------------------------------

MENU = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Track total money earned from successful transactions
profit = 0.0

# Available resources in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Check if the machine has enough resources to make a drink.
    Returns True if yes, False if not."""
    for item in order_ingredients:
        if item not in resources:
            print(f"❌ Sorry, this machine doesn’t have {item}.")
            return False
        if order_ingredients[item] > resources[item]:
            print(f"❌ Sorry, not enough {item}. (Need {order_ingredients[item]}, available {resources[item]})")
            return False
    return True


def process_coins():
    """Ask user to insert coins. Handles invalid input safely.
    Returns total money inserted in dollars."""
    print("💰 Please insert coins:")

    def safe_int_input(prompt):
        try:
            return int(input(prompt))
        except ValueError:
            print("  (Invalid input → counted as 0)")
            return 0

    total = safe_int_input("How many quarters? ($0.25): ") * 0.25
    total += safe_int_input("How many dimes? ($0.10): ") * 0.10
    total += safe_int_input("How many nickels? ($0.05): ") * 0.05
    total += safe_int_input("How many pennies? ($0.01): ") * 0.01
    return round(total, 2)


def is_transaction_successful(money_received, drink_cost):
    """Check if the payment covers the cost of the drink.
    If yes → return True and update profit.
    If no → return False and refund money."""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"💵 Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("❌ Sorry, that’s not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct ingredients from resources and serve the coffee."""
    for item in order_ingredients:
        # ✅ Safe deduction (only subtract ingredients actually required)
        resources[item] -= order_ingredients[item]

    print(f"✅ Here is your {drink_name} ☕. Enjoy!")
    print("--- Machine Status ---")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")   # get() prevents crash if milk not present
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")
    print("----------------------")


# ----------------- Main Loop -----------------
is_on = True
while is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower().strip()

    if choice == "off":
        is_on = False
        print("🔌 Machine turned off. Goodbye!")

    elif choice == "report":
        print("--- Report ---")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources.get('milk', 0)}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit:.2f}")
        print("--------------")

    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("⚠️ Invalid choice. Options: espresso, latte, cappuccino, report, off.")
