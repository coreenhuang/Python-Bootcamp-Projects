import random

logo = """
   ______                        __  __            _   __                __              __
  / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____/ /
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/ / 
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /  /_/  
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/  (_)   
                                                                                           
"""

#Select target number
target_number = random.randint(1,100)

#Print welcome text
print(logo)
print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is {target_number}")

#Allocate number of lives based on difficulty selection
difficulty_selection = input("Choose a diffculty. Type 'easy' or 'hard': ")

if difficulty_selection == 'easy':
    number_of_lives = 10
elif difficulty_selection == 'hard':
    number_of_lives = 5
else:
    print("Invalid input. Please try again.")

#Commence guessing
number_guess = input(f"You have {number_of_lives} attempts remaining to guess the number.\nMake a guess: ")