import random
import os
from art import logo, vs
from game_data import data

def get_random_account():
    """Get a random account from the game data."""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description, and country."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """
    Check if the user's guess is correct.
    Returns True if guess is right, False otherwise.
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def clear():
    """Clear the console screen for both Windows and Mac/Linux (works in VS Code)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    """Main game logic for Higher or Lower."""
    print(logo)
    score = 0
    best_score = 0  # ✅ Added highest score tracker
    game_should_continue = True

    # Get two random accounts
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        # Make account B become account A for the next round
        account_a = account_b
        account_b = get_random_account()

        # Ensure A and B are different
        while account_a == account_b:
            account_b = get_random_account()

        # Display the comparison
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Get user's guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Get follower counts
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if user is correct
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear screen and show logo again
        clear()
        print(logo)

        # Give feedback
        if is_correct:
            score += 1
            if score > best_score:  # ✅ Update highest score
                best_score = score
            print(f"✅ You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"❌ Sorry, that's wrong. Final score: {score}")
            print(f"🏆 Highest score in this session: {best_score}")  # ✅ Show highest score

# Start the game
game()
