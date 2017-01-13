# Pg 85, challenge no. 2

import random

print("\tCoin Flipper")

no_of_flips = 0
heads = 0
tails = 0

while no_of_flips < 100:
    number = random.randrange(2)
    if number == 0:
        heads += 1
    elif number == 1:
        tails += 1
    no_of_flips +=1

print("\n\nNo. of heads:", heads)
print("\nNo. of tails:", tails)

input("\n\nPress enter to exit")
