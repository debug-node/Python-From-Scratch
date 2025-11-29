import random

Rock = (r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = (r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = (r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game_images = [Rock, Paper, Scissors]

user_choice = int(input("what do you choose? Type 0 for Rock , Type 1 for papper and Type 2 for scissors\n"))
if user_choice >=3 or user_choice <0:
    print("You type an invalid number, you lose!")
else:
    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("🎉 You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("💀 You lose!")
    elif computer_choice > user_choice:
        print("💀 You lose!")
    elif user_choice > computer_choice:
        print("🎉 You win!")
    elif computer_choice == user_choice:
        print("😐 It's a draw.")