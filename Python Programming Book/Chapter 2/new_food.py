# New Food
#
# Pg 47, Challenge No. 2
#
# Write a program that allows a user to enter his or her
# two favourite foods. The program should then print out
# the name of a new food by joining the original food
# names together.

food1 = input("Enter the name of your first favourite food\n\n")
food2 = input("\nEnter the name of your second favourite food\n\n")

print("\n\nSo, have you tried combining them to make " + food1
      + " " + food2 + "?")

print("\nOr you could try " + food2 + " " + food1 + "."
      " That could be good.")

input("\n\nPress enter to exit")
