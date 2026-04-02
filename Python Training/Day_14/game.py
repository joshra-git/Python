from art import logo
from art import vs
from game_data import data
import random
# print(logo)
# runs two random ints against gate_data to pull two of the same
## make sure they're not the same person

def person_choice():

    person_1 = (random.choice(data))
    person_2 = (random.choice(data))
    while person_1 == person_2:
        person_2 = (random.choice(data))


    condition = True
    score = 0
    while condition:
        print(logo)
        print(f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}")
        print(vs)
        print(f"Compare B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ")

        for i in choice:      
            if i == "A" or "a":
                if person_1["follower_count"] > person_2["follower_count"]:
                    print ("You win!")
                    score += 1
                    person_1 = person_2
                    person_2 = (random.choice(data))
                    
                else:
                    print (f"Sorry, that's wrong, Final score: {score}")
                    condition = False

            elif i == "B" or "b":
                if person_2["follower_count"] > person_1["follower_count"]:
                    print ("You win!")
                    score += 1
                    person_2 = person_1
                    person_2 = (random.choice(data))
                    
                else:
                    print ("You lost")
                    print (f"Sorry, that's wrong, Final score: {score}")
                    condition = False

person_choice()