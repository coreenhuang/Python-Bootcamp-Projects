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

############### Blackjack Project #####################

#Difficulty Normal : Use all Hints below to complete the project.
#Difficulty Hard : Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard : Only use Hints 1 & 2 to complete the project.
#Difficulty Expert : Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random

play_game = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

while play_game is True:

    user_cards = []
    computer_cards = []

    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    print(user_cards)
    print(computer_cards)

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

    def calculate_score(deck):
        score = sum(deck)

        if score == 21:
            return 0
        
        if 11 in deck and score > 21:
            index = deck.index(11)
            deck[index] = 1

        return score

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

    def calculate_decks():
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            play_game = False

    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

        draw_card = input("Would you like to draw another card? Type 'y' or 'n'.\n")

        if draw_card == 'y':
            user_cards.append(deal_card())

            print(user_cards)
            print(sum(user_cards))
        elif draw_card == 'n':
            play_game = False

    calculate_decks()

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

