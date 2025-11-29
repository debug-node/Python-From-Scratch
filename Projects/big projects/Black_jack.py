import random

# =======================
# Blackjack Game - Steps:
# 1. Show the game logo.
# 2. Deal two random cards to both user and computer.
# 3. Calculate scores for both.
# 4. Check for immediate win (Blackjack) or loss.
# 5. Allow user to take more cards ('hit') or stop ('stand').
# 6. Computer draws cards until score is 17 or more.
# 7. Compare both scores and declare the winner.
# 8. Ask user if they want to play again.
# =======================

# Blackjack Rules:
# - Cards 2–10 = face value, J/Q/K = 10, Ace = 11 or 1.
# - Player and dealer start with 2 cards.
# - If initial hand = Ace + 10 (or face card), it's a Blackjack (automatic win).
# - Player can "hit" (take more cards) or "stand" (stop).
# - If total > 21, player busts (loses).
# - Dealer must hit until score >= 17.
# =======================

# ASCII art logo for the game
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards) # Randomly choose one card
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Check for a Blackjack (Ace + 10) with only two cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Return 0 as a special case for Blackjack
    

    # Adjust Ace value from 11 to 1 if total score exceeds 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)      # Return the sum of the cards

def compare(user_score, computer_score):
    """Compare user and computer scores to determine the result"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over.You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_games():
    """Main function to play the Blackjack game"""
    print(logo)  # Display the game logo
    user_cards = []  # List to store user's cards
    computer_cards = []  # List to store computer's cards
    is_game_over = False  # Flag to check if the game is over

    # Step 1: Deal two cards to both user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    # Step 2: User's turn to choose cards
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Show user's cards and computer's first card
        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f"  Computer's first cards: {computer_cards[0]}")

        # Step 3: Check for game-ending conditions (Blackjack or bust)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())  # Deal another card
            else:
                is_game_over = True

    # Step 4: Computer's turn - keep drawing cards until score >= 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Step 5: Show final results
    print(f"  Your final hand: {user_cards}, final score: {user_score}")
    print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Step 6: Keep asking if user wants to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_games()