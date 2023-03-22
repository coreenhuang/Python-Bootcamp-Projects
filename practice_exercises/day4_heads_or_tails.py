import random

# Generate 0 or 1 using random module

number = random.randint(0,1)

# Print "Tails" if number is 0 and "Heads" if number is 1

if number == 0:
    print("Tails")
elif number == 1:
    print("Heads")