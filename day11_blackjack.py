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
    first_card = random.choice(card_options)
    second_card = random.choice(card_options)
    user_total = first_card + second_card

    computer_card = random.choice(card_options)

    print(f"    Your cards: [{first_card}, {second_card}], current score: {user_total}")
    print(f"    Computer's first card: {computer_card}")

    input("Would you like to hit or stand?")
else:
    exit()