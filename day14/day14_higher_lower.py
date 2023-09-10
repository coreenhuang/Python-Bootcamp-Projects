from art import *
from data import data
from random import choice
import os

#Function to compare number of followers
def compare_followers(option_1, option_2):
    """Returns whoever has more followers, A or B"""
    if option_1['follower_count'] > option_2['follower_count']:
        return 'A'
    else:
        return 'B'

#Generate options from data dictionary
option_a = choice(data)
option_b = choice(data)

#Regenerate option for B if equal to A
while option_a == option_b:
    option_b = choice(data)

#Introduce score and play game variables
score = 0
play_game = True

while play_game:
    #Start Game - Display art and options for user to choose
    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}.")

    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    #Compare number of followers between both options
    if guess == compare_followers(option_a, option_b):
        #If correct, score + 1, option A becomes B, new option B
        score += 1
        option_a = option_b
        option_b = choice(data)
        while option_a == option_b:
            option_b = choice(data)
        os.system('clear')
    else:
        #End game if not correct and display score
        os.system('clear')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        play_game = False
