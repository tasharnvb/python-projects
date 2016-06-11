# Fortune Cookie
# Pg 85, challenge 1

import random

print("\t\tFortune Cookie")

print("\n\nYour fortune for today is:\n")

fortune_number = random.randrange(5)

if fortune_number == 0:
    print("A gambler not only will "
          "lose what he has, but also will "
          "lose what he doesn’t have.")

elif fortune_number == 1:
    print("Curiosity kills boredom. "
          "Nothing can kill curiosity.")

elif fortune_number == 2:
    print("Good to begin well, better to "
          "end well.")

elif fortune_number == 3:
    print("Now is the time to try something new")

elif fortune_number == 4:
    print("You will always be surrounded "
          "by true friends.")

else:
    print("No fortune available")

input("\n\nPress enter to exit")

