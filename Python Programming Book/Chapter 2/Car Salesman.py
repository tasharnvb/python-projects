# Pg 47 in the python book, Challenge No. 4

print(
"""
                                Car Salesman
"""
)

base = input("Enter the base price of the car\n\n")
base = int(base)

tax = base * 0.10
carlicense = base * 0.20
dealerprep = int(50)
delivery = int(75)

# Just some code to test that it worked correctly
#
# print("\nTax =", tax)
# print("License =", carlicense)
# print("Dealer Prep =", dealerprep)
# print("Destinatinon Charge =", delivery)

print("\nThe actual price of the car is", base + tax +
      carlicense + dealerprep + delivery)

input("\nPress enter to exit")
