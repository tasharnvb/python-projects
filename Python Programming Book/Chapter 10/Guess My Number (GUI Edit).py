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

        # setup the values that will be used in the game
        self.the_number = random.randint(1, 100)
        self.remaining_tries = 10

        self.create_widgets()

    def create_widgets(self):
        """Create labels, entru, button and text wudgets"""
        # create welcome label
        Label(self, text = "Welcome to Guess My Number!").grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create instruction label
        Label(self, text = "I'm thinking of a number between (and including) 1 and 100. Try to guess it in as few attempts as possible.").grid(row = 1, column = 0, columnspan = 2, sticky = W)

        # create label and text entry for the user's guess
        Label(self, text = "Enter you guess:").grid(row = 2, column = 0, sticky = W)
        self.ent_user_guess = Entry()
        self.ent_user_guess.grid(row = 2, column = 1, sticky = W)

        # create button to allow to user to submit their guess
        Button(self, text = "Submit guess", command = self.submit_guess()).grid(row = 2, column = 2)

        # create text area for the output/result of the guess
        self.txt_output = Text(self, width = 35, height = 5, wrap = WORD)
        self.txt_output.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def submit_guess(self):
        """Check whether the user's guess was correct, higher or lower"""
        user_guess = self.ent_user_guess.get()
        # convert to integer for the comparison
        user_guess = int(user_guess)

        response = "Your guess: " + str(user_guess)
        response += "\n"

        if user_guess == self.the_number:
            response = "You guessed it!\nAnd it only took you " + str(self.remaining_tries) + "tries"
        elif user_guess > self.the_number:
            response += "Lower..."
        elif user_guess < self.the_number:
            response += "Higher..."
        else:
            response += "Something's not right here..."

        self.remaining_tries -= 1
        if self.remaining_tries <= 0:
            response += "\n\nSorry, you're out of tries. Better luck next time!."

        self.txt_output.delete(0.0, END)
        self.txt_output.insert(0.0, response)
