from art import *
from data import data
from random import randint

# print(data[0]['name'])
# print(data[0]['follower_count'])
# print(data[0]['description'])
# print(data[0]['country'])

#Function to generate a random index number
def generate_random_index():
    return randint(0, len(data) - 1)

#Generate random indexes for option A and B
index_a = generate_random_index()
index_b = generate_random_index()

#Regenerate index for B if it is the same as A
while index_a == index_b:
    index_b = generate_random_index()

#Generate options from data dictionary
option_a = data[index_a]
option_b = data[index_b]

print(logo)
print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
print(vs)
print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")
