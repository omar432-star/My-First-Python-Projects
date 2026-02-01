import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
      _______
 ---'    ____)____
            ______)
            _______)
          _______)
 ---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_photos = [rock , paper , scissors]

user_input =int(input("What do you choose ? Type 0 Rock, Type 1 Paper and 2 for Scissors.\n"))

if user_input < 0 or user_input > 2:
    print("Invalid number . You lose")
else:
    if user_input == 0:
        print(game_photos[0])
    elif user_input == 1:
        print(game_photos[1])
    else :
        print(game_photos[2])
    computer_choice = random.randint(0,2)
    print("Computer choice :\n")
    if computer_choice == 0:
        print(game_photos[0])
    elif computer_choice == 1:
        print(game_photos[1])
    else:
        print(game_photos[2])

    if user_input == 0 and computer_choice == 2:
        print("You win!")
    elif user_input == 2 and computer_choice == 0:
        print("You lose!")
    elif user_input == 1 and computer_choice == 0:
        print("You win!")
    elif user_input == 0 and computer_choice == 1:
        print("You lose!")
    elif user_input == 1 and computer_choice == 2:
        print("You lose!")
    elif user_input == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("Thats a draw.")
