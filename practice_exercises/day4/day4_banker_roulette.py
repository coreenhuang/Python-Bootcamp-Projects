import random

# Split string 

names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")

# Count number of names

number_of_names = len(names)

# Generate random index number from 0 to number of names minus 1

random_index = random.randint(0, number_of_names - 1)

payer = names[random_index]

print(f"{payer} is going to buy the meal today!")