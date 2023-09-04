from random import randint

logo = """
   ______                        __  __            _   __                __              __
  / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____/ /
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/ / 
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /  /_/  
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/  (_)   
                                                                                           
"""

#Function to evaluate guess with target answer
def evaluate_guess(guess, target, turns):
   """Compare guessed number with target number. Returns remaining number of lives."""
   if guess == target:
      print(f"You win! The answer is {target}.")
   elif guess > target:
      print(f"Your guess is too high.")
      return turns - 1
   else:
      print(f"Your guess is too low.")
      return turns - 1

#Function to return number of lives depending on difficulty selection
def select_difficulty():
   """Return number of lives depending on difficulty level."""
   difficulty = input("Choose a diffculty. Type 'easy' or 'hard': ")
   if difficulty == "easy":
      return 10
   else:
      return 5

def game_on():

   #Select target number
   target_number = randint(1,100)

   #Print logo and welcome text
   print(logo)
   print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is {target_number}")

   #Obtain number of lives based on difficulty selected
   available_lives = select_difficulty()

   guess_input = 0

   while guess_input != target_number:

      print(f"You have {available_lives} attempts remaining to guess the number.")

      #User to input a guess
      guess_input = int(input("Please make a guess: "))

      #Evaluate guess with target answer, reduce 1 life if incorrect
      available_lives = evaluate_guess(guess_input, target_number, available_lives)

      #End game if no more lives available
      if available_lives == 0:
         print("You have no more attempts left. You lose.")
         return
      elif guess_input != target_number:
         print("Please guess another number.")

game_on()
