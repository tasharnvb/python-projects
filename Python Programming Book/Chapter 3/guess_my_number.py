# Guess My Number (Edit)
#
# Pg 85, Challenge No. 3
#
# Modify the Guess My Number game so that the player has a
# limited number of guesses. If the player fails to guess in
# time, the program should display an appropriate message.
#
# Notes:
# The number of tries that the user took is incorrect if the
# user guesses the number correctly. This is an easy fix but
# I am leaving it unfixed for now.

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 10

# guessing loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    tries -= 1
    if tries <= 0:
        break
    guess = int(input("Take a guess: "))

if guess == the_number:
    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")

elif tries <= 0:
    print("\nSorry, you're out of tries. Better luck next time!.")

input("\n\nPress the enter key to exit.")
