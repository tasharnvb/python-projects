# Guess Your Number
#
# Pg 85, Challenge No. 4
#
# Write a program where the player and the computer change
# places in the Guess My Number game. The player picks a number
# between 1 and 100 and the computer has to guess.
#
# Note:
# The first part of this challenge was actually to write the
# psuedocode code for this program, but I didn't feel like
# doing it so I just made it instead.

import random

print("\t\tGuess Your Number")
input("\nThink of a number between 1 and 100. "
      "Once you have, press enter.")

comp_guess = random.randrange(100)

print("\n\nMy guess is...", comp_guess)
your_number = input("\nIs that your number? (Type yes or no) ")

if your_number == "yes":
    print("\nWell that's the end of the game then")

elif your_number == "no":
    while your_number != "yes":
        comp_guess = random.randrange(100)
        print("\nMy guess is...", comp_guess)
        your_number = input("\nIs that your number? (Type yes or no) ")

        if your_number == "yes":
            print("\nWell that's the end of the game then.")
            break

        elif your_number == "no":
            continue

        else:
            print("\nAnswer the question CORRECTLY next time.")

else:
    print("\nI'm not going to play if you can't follow simple "
          "instructions.")


input("\n\nPress the enter key to exit.")
