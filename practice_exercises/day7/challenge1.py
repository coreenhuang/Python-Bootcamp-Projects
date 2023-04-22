# Picking a random word and checking answers
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

word_split = list(chosen_word)

# print(word_split)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

number_of_letters = len(word_split)

# print(number_of_letters)

for letter in word_split:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")