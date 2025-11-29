import random 

stages = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

end_of_game = False
word_list = ["lion", "camel", "monkey"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6 

# print(f'pssst, the solution is {chosen_word}. ')

display = []
for _ in range(word_length):
    display += "_"

guessed_letters = []  # NEW: to track already guessed letters

print("🎮 Welcome to Hangman! \n")

while not end_of_game:
    print(stages[6 - lives])
    print(f"{' '.join(display)}")
    print(f"Guessed letters: {', '.join(guessed_letters)}\n")

    guess = input("Guess a letter: ").lower()

    # if guess in display:
    #     print(f"You've already guessed {guess}")
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'.")
        input("Press Enter to continue...")
        continue
    else:
        guessed_letters.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter {guess}")
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"\033[31mYou guessed '{guess}', that's not in the word. You lose a life.\033[0m")

        lives -= 1
        input("Press Enter to continue...")
        if lives == 0:
           
            print(stages[6])
            print(f"\n\033[1;31m💀 You Lose! The word was '\033[4m{chosen_word}\033[0;31m'.\033[0m")
            end_of_game = True
    
    if "_" not in display:
        
        print(stages[6 - lives])
        print(f"{' '.join(display)}")
        print(f"\033[1;32m🎉 You Win! The word was '\033[4m{chosen_word}\033[0;32m'.\033[0m")

        end_of_game = True