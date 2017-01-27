# Guess the Word
#
# Pg 120, Challenge No. 4
#
# Create a game where the computer picks a random word and the
# player has to guess that word. The computer tells the player
# how many letters are in the word. Then the player gets five
# chances to ask if a letter is in the word. The computer can
# only respond with a "yes" or "no". Then, the player must
# guess the word.

import random

print("\t\tGuess the Word")
#print("Try to guess the word i'm thinking of")
print("\nI'll tell you how many letters are in the word, then you'll"
      "\nhave 5 chances to ask whether a letter is in the word. After"
      "\nthat, you will have to try and guess the word.")

input("\nWhen you're ready to start playing, press enter.")

# Setting up values

# The tuple (array) of words that the program will choose from.
# (The variable name is capitalised to show that it shouldn't change)
WORDS = ("escape", "cookie", "python", "pokemon", "bioshock", "number", "array", "evangelion")
# The random word that the program has chosen
choice = random.choice(WORDS)
# The length of the random word
length = len(choice)
# Used to keep track of how many letters the user has asked about
question_number = 1

# The game part of the game
print("\n\nThere are", length, "letters in the word.")

while question_number < 6:
    letter = ""
    while not letter:   # To force the user to pick a letter
        letter = input("\n" + str(question_number) + ". Type a letter to see if it is in the word: ")
    if letter.lower() in choice:    # Just in case the user types in a capital letter
        print("Yes.")
    else:
        print("No.")
    question_number += 1

guess = ""
while not guess:
    guess = input("\nWhat do you think the word is?\n") # Asking for the users guess

if guess.lower() == choice:   # Ignore the case
    print("\nYou guessed correctly! Well done!")
else:
    print("\nI'm afraid that your guess was incorrect. The actual word "
          "was", choice, "\nBetter luck next time!")

input("\n\nPress the enter key to close the program.")
