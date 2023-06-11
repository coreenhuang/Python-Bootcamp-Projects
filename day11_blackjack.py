logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

import random

card_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if start_game == 'y':
    print(logo)

    #First round
    user_cards = []

    first_card = random.choice(card_options)
    second_card = random.choice(card_options)
    user_cards.append(first_card)
    user_cards.append(second_card)

    user_total = first_card + second_card

    computer_cards = []
    computer_card = random.choice(card_options)
    computer_cards.append(computer_card)

    print(f"Your cards: {user_cards}, current score: {user_total}")
    print(f"Computer's first card: {computer_card}")

    hit_or_stand = input("Would you like to hit or stand? Please type 'hit' or 'stand'.")

    def add_card(who):
        additional_card = random.choice(card_options)




    #insert recursion here to continue hitting 
    if hit_or_stand == 'hit':
        additional_card = random.choice(card_options)
        print(additional_card)

        user_total += additional_card
        print(user_total)
    elif hit_or_stand == 'stand':
        computer_second_card = random.choice(card_options)
        print(computer_second_card)

        computer_total = computer_card + computer_second_card
        print(computer_total)


else:
    exit()