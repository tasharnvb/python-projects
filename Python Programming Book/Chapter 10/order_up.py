# Pg 319, Challenge No. 3
# Create a GUI program called Order Up!, that presents the user with
# a simple restarant menu, which lists items and prices.
# Let the user select different items and then show the user the total bill

from tkinter import *

class Application(Frame):
    """Restaurant application"""
    def __init__(self, master):
        """Initialize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create labels, entru, button and text wudgets."""

# main
root = Tk()
root.title("Restaurant")
# root.geometry("300x150")

app = Application(root)

root.mainloop()
