import random
import os
from art import logo, vs
from game_data import data
from colorama import Fore, Style, init

# Initialize colorama for Windows
init(autoreset=True)

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
    return (a_followers > b_followers and guess == "a") or (b_followers > a_followers and guess == "b")

def clear():
    """Clear the console screen for both Windows and Mac/Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    clear()
    print(Fore.CYAN + logo)
    print(Fore.YELLOW + "🎮 Welcome to Higher-Lower Pro Edition!")
    print(Fore.MAGENTA + "Choose Difficulty: Easy (10 Rounds) or Hard (Unlimited)")
    difficulty = input(Fore.CYAN + "Type 'easy' or 'hard': ").lower()

    score = 0
    best_score = 0
    game_should_continue = True
    rounds = 0
    max_rounds = 10 if difficulty == "easy" else float('inf')

    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue and rounds < max_rounds:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(Fore.CYAN + f"\nCompare A: {format_data(account_a)}")
        print(Fore.YELLOW + vs)
        print(Fore.CYAN + f"Against B: {format_data(account_b)}")

        guess = input(Fore.WHITE + "Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(Fore.CYAN + logo)

        if is_correct:
            score += 1
            best_score = max(best_score, score)
            print(Fore.GREEN + f"✅ Correct! Current score: {score}")
        else:
            print(Fore.RED + f"❌ Wrong! Final score: {score}")
            print(Fore.YELLOW + f"🏆 Highest Score: {best_score}")
            game_should_continue = False

        rounds += 1

    if rounds >= max_rounds and game_should_continue:
        print(Fore.YELLOW + f"\n🎯 Max rounds reached! Final score: {score}")
        print(Fore.YELLOW + f"🏆 Highest Score: {best_score}")

# Start the game
game()
