import random
import os

# Function to clear screen using escape sequences
def clear_screen():
    # Works on most terminals
    print("\033[H\033[J", end="")

stages = ['''\033[31m
  +---+
  |   |
      |
      |
      |
      |
=========\033[0m''', '''\033[31m
  +---+
  |   |
  O   |
      |
      |
      |
=========\033[0m''', '''\033[31m
  +---+
  |   |
  O   |
  |   |
      |
      |
=========\033[0m''', '''\033[31m
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========\033[0m''', '''\033[31m
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========\033[0m''', '''\033[31m
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========\033[0m''', '''\033[31m
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\033[0m''']

end_of_game = False
word_list = ["lion", "camel", "monkey"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6 
display = ["_"] * word_length
guessed_letters = []

print("\033[1;34m🎮 Welcome to Hangman!\033[0m\n")

while not end_of_game:
    clear_screen()
    print(stages[6 - lives])
    print(f"\nWord: \033[1m{' '.join(display)}\033[0m")
    print(f"\033[36mGuessed letters: {', '.join(guessed_letters)}\033[0m\n")

    guess = input("🔤 Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("\033[33m⚠️ Please enter a single alphabetic letter.\033[0m")
        input("Press Enter to continue...")
        continue

    if guess in guessed_letters:
        print(f"\033[33mYou've already guessed '{guess}'.\033[0m")
        input("Press Enter to continue...")
        continue
    else:
        guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"\033[31mYou guessed '{guess}', that's not in the word. You lose a life.\033[0m")
        lives -= 1
        input("Press Enter to continue...")
        if lives == 0:
            clear_screen()
            print(stages[6])
            print(f"\n\033[1;31m💀 You Lose! The word was '\033[4m{chosen_word}\033[0;31m'.\033[0m")
            end_of_game = True

    if "_" not in display:
        clear_screen()
        print(stages[6 - lives])
        print(f"\n\033[1;32m🎉 You Win! The word was '\033[4m{chosen_word}\033[0;32m'.\033[0m")
        print(f"Final Word: \033[1m{' '.join(display)}\033[0m")
        end_of_game = True
