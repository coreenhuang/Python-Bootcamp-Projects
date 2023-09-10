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

def format_option_data(option):
    """Returns a string with name, description, and country"""
    name = option["name"]
    description = option["description"]
    country = option["country"]
    return f"{name}, a {description}, from {country}"

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

    print(f"Compare A: {format_option_data(option_a)}.")
    print(vs)
    print(f"Against B: {format_option_data(option_b)}.")

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
