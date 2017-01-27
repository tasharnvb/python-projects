# Word List
#
# Pg 155, Challenge No. 1
#
# Create a program that prints a list of words in a random order.
# The program should print all of the words and not repeat any.

import random

# Setting up a constant list to hold the words
WORDS = ["Python", "Java", "SQL", "C#", "Bash", "HTML", "PHP", "JavaScript"]

# Select a random word, display it and then remove it from the list
for i in range(len(WORDS)):
    curr_word = random.choice(WORDS)
    print(curr_word)
    WORDS.remove(curr_word)

# An alternate version where the word is not removed after it is displayed
#
# Set up another list to hold the displayed words
# displayed = []
#
# for i in range(len(WORDS)):
#     curr_word = random.choice(WORDS)
#     while curr_word in displayed:
#         curr_word = random.choice(WORDS)
#     displayed.append(curr_word)
#     print(curr_word)



input("\n\nPress the enter key to close the program.")
