# Critter Farmer
# A virtual farm to care for

# Pg 246, Challenge No. 4
# Create a Critter Farm program by instantiating several
# Critter objects and keeping track of them through a list.
# Each menu option should allow the user to perform an
# action for all of the critters. Also give all of the critters
# random starting hungerand boredom levels.

import random

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        """Displays current object information"""
        info = "Critter Object\n"
        info += "name: " + self.name + "\n"
        info += "hunger: " + str(self.hunger) + "\n"
        info += "boredom: " + str(self.boredom) + "\n"
        return info

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def amount(choice):
    if choice == "2":
        phrase = "How much food do you want to feed your critters?: "
    elif choice == "3":
        phrase = "How much time do you want to spend playing with your critters?: "
    else:
        phrase = "Something went wrong here..."
    number = ""
    # Code adapted from here: http://stackoverflow.com/a/8114405
    while True:
        # This gives an infinite loop
        try:
            number = int(input(phrase))
        except ValueError as e:
            # The user did not enter a number
            print("Only numbers are accepted! Please try again.\n")
        else:
            break
    return number

def rng():
    """Returns a random number between 0 and 10 (including 0 and 10)"""
    return int(random.randrange(11))

def main():
    # The farm is empty at first
    farm = []

    crit1_name = input("What do you want to name your first critter?: ")
    crit1 = Critter(crit1_name, rng(), rng())

    crit2_name = input("What do you want to name your second critter?: ")
    crit2 = Critter(crit2_name, rng(), rng())

    crit3_name = input("What do you want to name your third critter?: ")
    crit3 = Critter(crit3_name, rng(), rng())

    farm.append(crit1)
    farm.append(crit2)
    farm.append(crit3)

    choice = []
    while choice != "0":
        print \
        ("""
        Critter Farmer

        0 - Quit
        1 - Listen to your critters
        2 - Feed all of your critters
        3 - Play with all of your critters
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critters
        elif choice == "1":
            for critter in farm:
                critter.talk()

        # feed your critters
        elif choice == "2":
            food_amount = amount(choice)
            for critter in farm:
                critter.eat(food_amount)

        # play with your critters
        elif choice == "3":
            play_length = amount(choice)
            for critter in farm:
                critter.play(play_length)

        # display object attribute information
        elif choice == "92":
            for critter in farm:
                print(critter)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the enter key to exit.")
