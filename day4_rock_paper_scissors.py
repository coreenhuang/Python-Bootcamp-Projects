import random

# Rock, Paper, and Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# User selects one option

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if my_choice == 0:
  print(rock)
elif my_choice == 1:
  print(paper)
elif my_choice == 2:
  print(scissors)
else:
  print("Please try again with a valid option.")
  quit()

# Randomize number corresponding to selection for computer

print("Computer chose:")

computer_choice = random.randint(0,2)

if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)

# Compare selections to see who wins

if my_choice == computer_choice:
  print("It's a draw!")
elif my_choice == 0:
  if computer_choice == 1:
    print("You lose.")
  elif computer_choice == 2:
    print("Congratulations! You win!")
elif my_choice == 1:
  if computer_choice == 2:
    print("You lose.")
  elif computer_choice == 0:
    print("Congratulations! You win!")
elif my_choice == 2:
  if computer_choice == 0:
    print("You lose.")
  elif computer_choice == 1:
    print("Congratulations! You win!")