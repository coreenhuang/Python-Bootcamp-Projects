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

my_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if my_choice == "0":
  print(rock)
elif my_choice == "1":
  print(paper)
elif my_choice == "2":
  print(scissors)

# Randomize number corresponding to selection for computer

computer_choice = random.randint(0,2)

print("Computer chose:")

