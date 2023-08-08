# First -- Is it  easy or hard
# Pick a number between 1 - 100
import random

number = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# print(number)
# Prints my attempts with easy = 10 and hard = 5

choice = input("Do you want this to be easy or hard?\n")

if choice == "easy":
    guesses = 10

if choice =="hard":
    guesses = 5

# def too_high():


# Asks for input for my Guess
# game_on = True
while guesses > 0:
    choice_on_number = int(input("Make a guess?\n"))

    if choice_on_number == number:
        print("You guessed it!!")
        guesses = 0
    elif choice_on_number < number:
        print("Too low!")
        guesses -= 1
        if guesses != 0:
            print(f"You have {guesses} attempts remaining to guess the number")
        else:
            print("You've run out of guesses, you lose.")
    elif choice_on_number > number:
        print("Too High")
        guesses -= 1
        if guesses != 0:
            print(f"You have {guesses} attempts remaining to guess the number")
        else:
            print("You've run out of guesses, you lose.")

# If correct, it will say you got it and print the number. If it isn't it'll show me if that is lower or higher.