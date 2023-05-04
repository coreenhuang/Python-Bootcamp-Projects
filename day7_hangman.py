# Hangman Game

import random
from practice_exercises.day7.hangman_art import *
from practice_exercises.day7.hangman_words import word_list

# Choose random word from word list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Create blanks display for unknown chosen word

display = []
for _ in range(word_length):
    display += "_"

# A list of all guessed letters

guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Prompt user if they have already guessed a letter
    if guess in guessed_letters:
        print(f"You have already guessed the letter {guess}. Please guess another letter.")
    
    else:
        # Add letter to the guessed letters list
        guessed_letters.append(guess)

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]

            # If letter is in chosen word, replace blank 
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:

            print(f"Letter {guess} is not in this word. You have lost one life.")

            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        # Print hangman art with display 
        print(stages[lives])