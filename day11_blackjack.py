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

# start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# import random

# card_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# if start_game == 'y':
#     print(logo)

#     #new card function returns an integer
#     def add_card():
#         additional_card = random.choice(card_options)
#         return additional_card
    
#     #first round
#     user_cards = []

#     for n in range(2):
#         user_cards.append(add_card())

#     user_total = sum(user_cards)

#     computer_cards = []
#     computer_cards.append(add_card())

#     print(f"Your cards: {user_cards}, current score: {user_total}")
#     print(f"Computer's first card: {computer_cards[0]}")

#     def continue_playing():
        
#         #second round onwards
#         hit_or_stand = input("Would you like to hit or stand? Please type 'y' to hit or 'n' to stand.\n")

#         #insert recursion here to continue hitting 
#         if hit_or_stand == 'y':
#             new_card = add_card()
#             user_cards.append(new_card)
#             print(user_cards)

#             user_new_total = sum(user_cards)
#             print(user_new_total)

#             continue_playing()

#         elif hit_or_stand == 'n':
#             computer_second_card = random.choice(card_options)
#             print(computer_second_card)

#             computer_total = computer_card + computer_second_card
#             print(computer_total)

#     continue_playing()


# else:
#     exit()

#-------------------Pseudo-Code---------------------

#have a deck
#ace can be 1 or 11
#yes or no to start game ----
#if yes print logo, draw cards, 2 for user, 1 for computer
#continue? hit or stand ---
#if hit, add card to deck, print new total
#put in recursion to keep hitting
#if over 21, user loses automatically
#if stand, add card to dealer
#if total is under a certain amount ->check, then keep dealing
#if over 21, dealer loses automatically
#compare user to dealer, if tie, then draw
#whoever is higher wins
#add winner message
#add loser message

#---------------------Solution------------------------------

