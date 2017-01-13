# Pg 319, Challenge No. 2
# Write a version of the Guess My Number game (from chapter 3) using a GUI

import random
from tkinter import *

class Application(Frame):
    """GUI version of the Guess My Number game"""
    def __init__(self, master):
        """Initialize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create labels, entru, button and text wudgets"""
        # create welcome label
        Label(self, text = "Welcome to Guess My Number!").grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create instruction label
        Label(self, text = "I'm thinking of a number between 1 and 100. Try to guess it in as few attempts as possible.").grid(row = 1, column = 0, columnspan = 2, sticky = W)

        # create label and text entry for the user's guess
        Label(self, text = "Enter you guess:").grid(row = 2, column = 0, sticky = W)
        self.ent_user_guess = Entry()
        self.ent_user_guess.grid(row = 2, column = 1, sticky = W)

        # create button to allow to user to submit their guess
        Button(self, text = "Submit guess", command = self.submit_guess()).grid(row = 2, column = 2)

        # create text area for the output/result of the guess
        self.txt_output = Text()
        self.txt_output.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def submit_guess(self):
        """Check whether the user's guess was correct, higher or lower"""
        user_guess = self.ent_user_guess.get()
        # convert to integer for the comparison
        user_guess = int(user_guess)

        response = "Your guess: " + str(user_guess)
        response += "\n"

        if user_guess == self.the_number:
            response = "You guessed it!\nAnd it only took you " + str(self.tries) + "tries"
        elif user_guess > self.the_number:
            response += "Lower..."
        elif user_guess < self.the_number:
            response += "Higher..."
        else:
            response += "Something's not right here..."

        self.remaining_tries -= 1
        if remaining_tries <= 0:
            response += "\n\nSorry, you're out of tries. Better luck next time!."

# print("\tWelcome to 'Guess My Number'!") # Label 1
# print("\nI'm thinking of a number between 1 and 100.") # Label 2
# print("Try to guess it in as few attempts as possible.\n")
#
# # set the initial values
# the_number = random.randint(1, 100)
# guess = int(input("Take a guess: ")) # Label 3 + Text entru 1
# tries = 10
#
# # guessing loop
# while guess != the_number:
#     if guess > the_number:
#         print("Lower...") # Text area 1
#     else:
#         print("Higher...") # Text area 1
#     tries -= 1
#     if tries <= 0:
#         break
#     guess = int(input("Take a guess: "))
#
# if guess == the_number:
# 	print("You guessed it!  The number was", the_number)
# 	print("And it only took you", tries, "tries!\n")
#
# elif tries <= 0:
# 	print("\nSorry, you're out of tries. Better luck next time!.")
#
# input("\n\nPress the enter key to exit.") # Uneeded?
