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

my_choice = random.randint(0,2)

computer_choice = random.randint(0,2)

print(my_choice)
print(computer_choice)
