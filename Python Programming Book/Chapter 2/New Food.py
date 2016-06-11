# Pg 47 in the python book, Challenge No. 2

# Challenge = Write  program that allows a user to enter his or her
#             two favourite foods. The program should then print out
#             the name of a new food by joining the original food
#             names together.

Food1 = input("Enter the name of your first favourite food\n\n")
Food2 = input("\nEnter the name of your second favourite food\n\n")

print("\n\nSo, have you tried combining them to make " + Food1
      + " " + Food2 + "?")

print("\nOr you could try " + Food2 + " " + Food1 + "."
      " That could be good.")

input("\n\nPress enter to exit")
