# Guess My Number (Function Edit)
#
# Pg 188, Challenge No. 2
#
# Modify the Guess My Number chapter project from Chapter 3 by
# reusing the function ask_number().
#
# Note:
# This is an edit of the existing guess my number game from chapter 3.
# I did not write the ask_number function, it was taken from the
# tic-tac-toe game that was used as an example in this chapter.

import random

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

print("\tWelcome to 'Guess My Number (Edit)'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = ask_number("Take a guess: ", 1, 100)
tries = 10

# guessing loop
while guess != the_number:
    tries -= 1
    if tries <= 0:
        break
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = ask_number("Take a guess: ", 1, 100)

if guess == the_number:
    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")

elif tries <= 0:
    print("\nSorry, you're out of tries. Better luck next time!.")

input("\n\nPress the enter key to exit.")
