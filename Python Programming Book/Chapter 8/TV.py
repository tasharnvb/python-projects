# Television
# A virtual television

# Pg 246, Challenge No. 2
# Simulate a television by creating it as an object.
# The user should be able to enter a channel number and raise/lower the volume.

class Television(object):
    """A virtual television"""
    channels = [1, 2, 3, 4, 5]
    def __init__(self, channel = 1, volume = 5):
        self.__channel = channel
        self.__volume = volume

    def __str__(self):
        """Displays current object information"""
        info = "Television Object\n"
        info += "Current channel: " + str(self.__channel) + "\n"
        info += "Current volume: " + str(self.__volume) + "\n"
        return info

    def change_channel(self, new_channel):
        if int(new_channel) in self.channels:
            self.__channel = new_channel
            print("The tv is now on channel", new_channel)
        else:
            print("The channel you have chosen does not exist. Please try another.")

    def raise_volume(self):
        if self.__volume < 10:
            self.__volume += 1
            print("The volume is now", self.__volume)
        else:
            print("The volume is already at its maximum.")

    def lower_volume(self):
        if self.__volume > 0:
            self.__volume -= 1
            print("The volume is now", self.__volume)
        else:
            print("The volume is already at its minimum.")

def main():
    tv = Television()
    choice = None
    while choice != "0":
        print \
        ("""
        Television

        0 - Turn off TV
        1 - Change the channel
        2 - Raise the volume
        3 - Lower the volume
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Turning off.")

        # change the tv's channel
        elif choice == "1":
            new_channel = input("What channel do you want to change it to? ")
            tv.change_channel(new_channel)

        # raise the volume
        elif choice == "2":
            tv.raise_volume()

        # lower the volume
        elif choice == "3":
            tv.lower_volume()

        # display object attribute information
        # elif choice == "92":
        #     print(tv)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the enter key to exit.")
