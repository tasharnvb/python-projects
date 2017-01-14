# Tipper
#
# Pg 47, Challenge No. 3
#
# Write a Tipper program where the user enters a restaurant bill total.
# The program should then display two amounts: a 15% and a 20% tip.

print(
    """
                                    Tipper
    """
)

bill = input("Enter the bill total\n\n")
bill = int(bill)

tip15 = bill * 0.15

tip20 = bill * 0.20

print("\nWith a 15% tip, the total is", bill + tip15)
print("\nAnd with a 20% tip the total is", bill + tip20)

input("\nPress enter to exit")
