# Pg 319, Challenge No. 3
# Create a GUI program called Order Up!, that presents the user with
# a simple restarant menu, which lists items and prices.
# Let the user select different items and then show the user the total bill

from tkinter import *

class Application(Frame):
    """Order Up! restaurant application"""
    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()

        # a dictionary that will contain the items and prices for the restaurant
        # example format -> {pizza : {"price" : 5.00, "selected" : False}}
        self.menu = {"Pizza" : {"price" : 5.00, "selected" : False}, "Jerk Chicken" : {"price" : 6.50, "selected" : False}}
        self.bill = []

        self.create_widgets()

    def create_widgets(self):
        """Create labels, entry, button and text widgets."""
        # create welcome label
        Label(self, text = "Welcome to Order Up!").grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create instruction label
        Label(self, text = "Choose the item(s) that you would like from the menu").grid(row = 1, column = 0, columnspan = 2, sticky = W)

        # create menu
        Label(self, text = "Menu:").grid(row = 2, column = 0, sticky = W)
        col_num = 0
        for item in self.menu:
            self.menu[item]["selected"] = BooleanVar()
            Checkbutton(self, text = item, variable = self.menu[item]["selected"], command = self.update_bill).grid(row = 3, column = col_num, sticky = W)
            col_num += 1

        # create button to allow to user to pay for their meal
        Button(self, text = "Complete order", command = self.pay).grid(row = 4, column = 0)

        # create text area for the bill
        self.txt_output = Text(self, width = 35, height = 10, wrap = WORD)
        self.txt_output.grid(row = 5, column = 0, columnspan = 2, sticky = W)

    def update_bill(self):
        """Update the user's bill."""
        for item in self.menu:
            if self.menu[item]["selected"]  == True:
                if item not in self.bill:
                    self.bill.append(item)

        total = self.calculate_total()
        self.display_bill(total)

    def calculate_total(self):
        pass

    def display_bill(self, total):
        pass

    def pay(self):
        """do nothing (would allow for a payment system to be implementes in the future)."""
        pass

# main
root = Tk()
root.title("Order Up!")
# root.geometry("300x150")

app = Application(root)

root.mainloop()
