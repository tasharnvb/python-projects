# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

#Challenge ver. Pg 120, Challenge 3 (Add hints)

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# Create a tuple for the hints
HINTS = ("This program is coded in this language", "The word is in the title of this game",
        "The opposite of difficult", "The opposite of easy", "You are trying to give the correct _______",
        "This is a musical instument")
# Use a random number to select the word and hint
position = random.randrange(len(WORDS))
# pick one word randomly from the sequence
word = WORDS[position]
# Get the hint associated with the chosen word
hint = HINTS[position]
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
(Type hint to see a hint)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    if guess == "hint":
        print(hint)
    else:
        print("Sorry, that's not it.")
    guess = input("Your guess: ")
    
if guess == correct:
    print("That's it!  You guessed it!\n")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
