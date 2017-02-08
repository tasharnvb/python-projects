# Guess My Number (GUI Edit)
#
# Pg 319, Challenge No. 2
#
# Write a version of the Guess My Number game, the Chapter 3
# project, using a GUI.

import random
import tkinter as tk

class Application(tk.Frame):
    """GUI version of the Guess My Number game"""
    def __init__(self, master):
        """Initialize the frame"""
        super(Application, self).__init__(master)
        self.grid()

        # setup the values that will be used in the game
        self.TRIES = 10
        self.the_number = random.randint(1, 100)
        self.remaining_tries = self.TRIES

        self.create_widgets()

    def create_widgets(self):
        """Create labels, entru, button and text wudgets"""
        # create welcome label
        tk.Label(self, text="Welcome to Guess My "
                            "Number!").grid(row=0, column=0, columnspan=2, sticky=tk.W)

        # create instruction label
        tk.Label(self, text="I'm thinking of a number between (and including) 1 and 100. "
                            "Try to guess it in as few attempts as "
                            "possible.").grid(row=1, column=0, columnspan=2, sticky=tk.W)

        # create label and text entry for the user's guess
        tk.Label(self, text="Enter you guess:").grid(row=2, column=0, sticky=tk.W)
        self.ent_user_guess = tk.Entry(self)
        self.ent_user_guess.grid(row=2, column=1, sticky=tk.W)

        # create button to allow to user to submit their guess
        tk.Button(self, text="Submit guess", command=self.submit_guess).grid(row=2, column=2)

        # create text area for the output/result of the guess
        self.txt_output = tk.Text(self, width=35, height=5, wrap=tk.WORD)
        self.txt_output.grid(row=3, column=0, columnspan=2, sticky=tk.W)

    def submit_guess(self):
        """Check whether the user's guess was correct, higher or lower"""
        user_guess = self.ent_user_guess.get()
        # convert to integer for the comparison
        user_guess = int(user_guess)

        response = "Your guess: " + str(user_guess)
        response += "\n"

        if user_guess == self.the_number:
            # the brackets are needed to make the multi-line statement work
            response = ("You guessed it!\nAnd it only took you "
                        + str(self.TRIES - self.remaining_tries) +  " tries")
        elif user_guess > self.the_number:
            response += "Lower..."
            self.remaining_tries -= 1
        elif user_guess < self.the_number:
            response += "Higher..."
            self.remaining_tries -= 1
        else:
            response += "Something's not right here..."

        if self.remaining_tries <= 0:
            response += "\n\nSorry, you're out of tries. Better luck next time!."

        self.txt_output.delete(0.0, tk.END)
        self.txt_output.insert(0.0, response)

# main
root = tk.Tk()
root.title("Guess My Number")
# root.geometry("300x150")

app = Application(root)

root.mainloop()
