# Critter Caretaker (Edit)
# A virtual pet to care for

# Pg 246, Challenge No. 3
# Create a back door in the Critter Caretaker program that
# shows the exact values of the object's attributes

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        """Displays current object information"""
        rep = "Critter Object\n"
        rep += "name: " + self.name + "\n"
        rep += "hunger: " + str(self.hunger) + "\n"
        rep += "boredom: " + str(self.boredom) + "\n"
        return rep

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
        phrase = "How much food do you want to feed your critter?: "
    elif choice == "3":
        phrase = "How much time do you want to spend playing with your critter?: "
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

def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()
        
        # feed your critter
        elif choice == "2":
            amount(choice)
            crit.eat()
         
        # play with your critter
        elif choice == "3":
            amount(choice)
            crit.play()

        # display object attribute information
        elif choice == "92":
            print(crit)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
