# Backwards
#
# Pg 120, Challenge No. 2
#
# Create a program that gets a message from the user
# and prints it out backwards.

print("\t\tBackwards")

word = input("\n\nType in the word you want to see backwards ")

# The first letter of the word is at index 0,
# index -1 is the last letter of the word
position = -1
backwards = ""

for i in range(len(word)):
    backwards += word[position]
    position -= 1

# An alternate way to do this with a while loop
# position = len(word) - 1
#
# while position >= 0:
#     backwards += word[position]
#     position -= 1

print("\nYour word backwards is: " + backwards)

input("\n\nPress enter to exit")
