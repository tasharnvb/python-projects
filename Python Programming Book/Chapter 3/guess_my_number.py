# Pg 85, Challenge No. 3
# This is an edit of the existing guess my number game.
# I changed the original game to give the user a limited
# number of guesses.

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
