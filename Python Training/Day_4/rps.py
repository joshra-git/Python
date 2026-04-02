import random
rock = "🪨"

paper = "📃"

scissors = "✂️"

#Write your code below this line 👇

# import random
# list=[rock],[paper],[scissors]
# user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
# player = int(player)
# computer = random.randint(0,2)
game_images=[rock],[paper],[scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_choice >= 3 or user_choice < 0:
    print("You choice of numbers is floored")
else:
    print("You chose:")
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose: \n")
    print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print ("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's a draw")


# if computer == choice_paper:
#     if player == choice_scissors:
#         print(f"You picked\n")
#         print(f"{scissors}\n")
#         print("Computer Chose\n")
#         print(f"{paper}\n")
#         print("You Win!")
#     elif player == choice_rock:
#         print(f"You picked\n")
#         print(f"{rock}\n")
#         print("Computer Chose\n")
#         print(f"{paper}\n")
#         print("You Lose!")
#     elif player == choice_paper:
#         print(f"You picked\n")
#         print(f"{paper}\n")
#         print("Computer Chose\n")
#         print(f"{paper}\n")
#         print("You Draw!")
# elif computer == choice_rock:
#     if player == choice_scissors:
#         print(f"You picked\n")
#         print(f"{scissors}\n")
#         print("Computer Chose\n")
#         print(f"{rock}\n")
#         print("You Lose!")
#     elif player == choice_rock:
#         print(f"You picked\n")
#         print(f"{rock}\n")
#         print("Computer Chose\n")
#         print(f"{rock}\n")
#         print("You Draw!")
#     elif player == choice_paper:
#         print(f"You picked\n")
#         print(f"{paper}\n")
#         print("Computer Chose\n")
#         print(f"{rock}\n")
#         print("You Win!")
# elif computer == choice_scissors:
#     if player == choice_scissors:
#         print(f"You picked\n")
#         print(f"{scissors}\n")
#         print("Computer Chose\n")
#         print(f"{scissors}\n")
#         print("You Draw!")
#     elif player == choice_rock:
#         print(f"You picked\n")
#         print(f"{rock}\n")
#         print("Computer Chose\n")
#         print(f"{scissors}\n")
#         print("You Win!")
#     elif player == choice_paper:
#         print(f"You picked\n")
#         print(f"{paper}\n")
#         print("Computer Chose\n")
#         print(f"{scissors}\n")
#         print("You Lose!") 