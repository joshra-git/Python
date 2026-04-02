import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards = [11, 11]

def deal_card():
    return random.choice(cards)

def calculate_score():
    current_score = sum(user_cards)
    if current_score == 21:
        print(f"Your cards {user_cards}, current score: {current_score}")
    elif current_score > 21:
        if 11 in user_cards:
            print(user_cards)
    else:
        print(f"Your cards {user_cards}, current score: {current_score}")
        print(f"Computer's first card: {computer_cards[0]}")

def final_score():
    print(f"Your score was {sum(user_cards)} -- Your cards were: {user_cards}")
    print(f"Computer score was {sum(computer_cards)} -- Computers cards were: {computer_cards}")

def deal_user_cards():
    if computer_cards != 0:
        computer_cards.append(deal_card())
        computer_cards.append(deal_card())
    user_cards.append(deal_card())
    if 11 in user_cards:
        if len(user_cards) > 2:
            cards.remove(11)
            cards.append(1)
            user_cards.append(deal_card())
        else:
            cards.remove(11)
            cards.append(1)
            user_cards.append(deal_card())
    else:
        user_cards.append(deal_card())

    # calculate_score()

user_cards = []
computer_cards = []
deal_user_cards()
calculate_score()


# game_on = True
## I don't think this quite works yet. 
# while game_on:

game_on = True
while game_on == True:
    if sum(user_cards) < 21:
        on_game = input("Would you like to get another card? Y or N:  ")
        if on_game == 'Y' or on_game == 'y':
            if sum(user_cards) < 21:
                new_card = random.choice(cards)
                user_cards.append(new_card)
                calculate_score()
            elif sum(user_cards) == 21:
                calculate_score()
                print("BLACKJACK SON!")
                game_on = False
                break
            else:
                print(f"Your currently stuck and your cards are {user_cards} and the computer has {computer_cards}")
        elif on_game == 'N' or on_game == 'n':
            if sum(computer_cards) < 17 and sum(computer_cards) != sum(user_cards):
                if sum(computer_cards) > sum(user_cards):
                    calculate_score()
                    print(f"Computer's second card: {computer_cards[1]}")
                    print("Computer Wins")
                    break
                elif sum(computer_cards) <= sum(user_cards):
                    computer_cards.append(deal_card())
                    if sum(computer_cards) < 21:
                        if sum(computer_cards) == sum(user_cards):
                            print("It was a draw")
                            final_score()                        
                        else:
                            final_score()
                            print("You won!")
                        break
                    elif sum(computer_cards) > sum(user_cards) and sum(computer_cards) > sum(user_cards):
                        final_score()
                        print(f"Computer wins with {sum(computer_cards)} but come back to this to fix it")
                        break
                    elif sum(computer_cards) == sum(user_cards):
                        final_score()
                        print("Draw")
                        break
                    else:
                        print(f"ONE Your currently stuck and your cards are {user_cards} and the computer has {computer_cards}")
                else:
                    print(f"FOUR Your currently stuck and your cards are {user_cards} and the computer has {computer_cards} THIS SHOULD BE FIXED")
            elif sum(computer_cards) < sum(user_cards):
                    calculate_score()
                    print(f"Computer's second card: {computer_cards}")
                    print("You Win!")
                    break
            elif sum(computer_cards) > sum(user_cards):
                final_score()
                print(f"Computer Wins with a score of {sum(computer_cards)} and {computer_cards}")
                break
            else:
                print(f"TWO - Your currently stuck and your cards are {user_cards} and the computer has {computer_cards}")
                break
        else:
            print(f"THREE Your currently stuck and your cards are {user_cards} and the computer has {computer_cards}")
    elif sum(user_cards) == 21:
        print("BLACKJACK SON!")
        print(f"Computer's cards were:{computer_cards}")
        break
    else:
        final_score()
        print(f"Your lost")
        break