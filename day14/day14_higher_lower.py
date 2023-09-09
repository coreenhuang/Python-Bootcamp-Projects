from art import *
from data import data
from random import randint

#Function to generate a random index number
def generate_random_index():
    return randint(0, len(data) - 1)

#Function to compare number of followers
def compare_followers(option_1, option_2):
    """Returns whoever has more followers, A or B"""
    if option_1['follower_count'] > option_2['follower_count']:
        return 'A'
    else:
        return 'B'

#Generate random indexes for option A and B
index_a = generate_random_index()
index_b = generate_random_index()

#Regenerate index for B if it is the same as A
while index_a == index_b:
    index_b = generate_random_index()

#Generate options from data dictionary
option_a = data[index_a]
option_b = data[index_b]

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
        print("correct")
        score += 1
        option_a = option_b
        option_b = data[generate_random_index()]
        while index_a == index_b:
            index_b = generate_random_index()
    else:
        print("not correct")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        play_game = False

    print(option_a['follower_count'])
    print(option_b['follower_count'])

    print(compare_followers(option_a, option_b))

