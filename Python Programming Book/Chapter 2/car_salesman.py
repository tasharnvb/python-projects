# Car Salesman
#
# Pg 47, Challenge No. 4
#
# Write a Car Salesman program where the user enters the base price
# of a car. The program should add on a bunch of extra fees such as
# tax, license, dealer prep and destination charge. Display the actual
# price of the car once all the extras are added.

print(
    """
                                Car Salesman
    """
)

base = input("Enter the base price of the car\n\n")
base = int(base)

tax = base * 0.10
car_license = base * 0.20
dealer_prep = int(50)
delivery = int(75)

# Test code
#
# print("\nTax =", tax)
# print("License =", car_license)
# print("Dealer Prep =", dealer_prep)
# print("Destination Charge =", delivery)

print("\nThe actual price of the car is", base + tax +
      car_license + dealer_prep + delivery)

input("\nPress enter to exit")
