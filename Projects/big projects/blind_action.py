# ASCII art logo for the auction program
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program")

# Dictionary to store all bids in the format: {"name": bid_amount}
bids = {}

# Function to find the highest bidder
def find_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Main loop for bidding
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?")

    # Input validation for bid amount
    while True:
        try:
            price = int(input("What is your bid? $"))
            if price <= 0:
                print("Bid amount must be greater than 0. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
        
    