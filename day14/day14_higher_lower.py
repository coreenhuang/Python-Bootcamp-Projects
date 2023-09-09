from art import *
from data import data
from random import randint

# print(logo)
# print(vs)

# print(randint(0,len(data) - 1))

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

print(option_a)
print(option_b)