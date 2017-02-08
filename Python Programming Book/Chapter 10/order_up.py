# Order Up!
#
# Pg 319, Challenge No. 3
#
# Create a GUI program called Order Up!, that presents the user
# with a simple restarant menu, which lists items and prices.
# Let the user select different items and then show the user
# the total bill.

import tkinter as tk

class Application(tk.Frame):
    """Order Up! restaurant application"""
    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()

        # a dictionary that contains the items and prices for the restaurant
        self.menu = {"Pizza" : {"price" : 7.00, "selected" : False},
                     "Whole Chicken" : {"price" : 8.50, "selected" : False},
                     "Steak" : {"price" : 11.00, "selected" : False}}
        self.bill = []

        self.create_widgets()

    def create_widgets(self):
        """Create labels, entry, button and text widgets."""
        # create welcome label
        tk.Label(self, text="Welcome to Order Up!").grid(row=0, column=0, columnspan=2, sticky=tk.W)

        # create instruction label
        tk.Label(self, text="Choose the item(s) that you would like "
                            "from the menu").grid(row=1, column=0, columnspan=2, sticky=tk.W)

        # create menu
        tk.Label(self, text="Menu:").grid(row=2, column=0, sticky=tk.W)
        col_num = 0
        for item in self.menu:
            self.menu[item]["selected"] = tk.BooleanVar()
            tk.Checkbutton(self, text=item, variable=self.menu[item]["selected"],
                           command=self.update_bill).grid(row=3, column=col_num, sticky=tk.W)
            col_num += 1

        # create button to allow to user to pay for their meal
        tk.Button(self, text="Complete order", command=self.pay).grid(row=4, column=0)

        # create text area for the bill
        self.txt_output = tk.Text(self, width=35, height=10, wrap=tk.WORD)
        self.txt_output.grid(row=5, column=0, columnspan=2, sticky=tk.W)

    def update_bill(self):
        """Update the user's bill."""
        for item in self.menu:
            if self.menu[item]["selected"].get() is True:
                if item not in self.bill:
                    self.bill.append(item)
            elif self.menu[item]["selected"].get() is False:
                if item in self.bill:
                    self.bill.remove(item)

        total = self.calculate_total()
        self.display_bill(total)

    def calculate_total(self):
        """Calculate the total of the user's bill"""
        total = 0
        for item in self.bill:
            total += self.menu[item]["price"]

        return total

    def display_bill(self, total):
        """Display the user's bill including the total"""
        response = ""
        for item in self.bill:
            response += item + " - " + str(self.menu[item]["price"]) + "\n"

        response += "\nTotal: " + str(total)

        self.txt_output.delete(0.0, tk.END)
        self.txt_output.insert(0.0, response)

    def pay(self):
        """do nothing (would allow for a payment system to be implemented in the future)."""
        pass

# main
root = tk.Tk()
root.title("Order Up!")
# root.geometry("300x150")

app = Application(root)

root.mainloop()
