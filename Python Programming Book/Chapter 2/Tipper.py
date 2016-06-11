# Pg 47 in the python book, Challenge No. 3

print(
"""
                                    Tipper
"""
)

bill = input("Enter the bill total\n\n")
bill = int(bill)

pertip15 = bill * 0.15

pertip20 = bill * 0.20

print("\nWith a 15% tip, the total is", bill + pertip15)
print("\nAnd with a 20% tip the total is", bill + pertip20)

input("\nPress enter to exit")
