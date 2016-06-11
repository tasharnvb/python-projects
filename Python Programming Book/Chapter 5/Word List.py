# Pg 155, Challenge No. 1
#
# Word List
#
# A program that prints a list of words in a random order.
# (All of the words should be printed and none should repeat)

import random

# Setting up a constant list to hold the words
WORDS = ["Python", "Java", "SQL", "C#", "Bash", "HTML", "PHP", "JavaScript"]

# Select a random word, display it and then remove it from the list
for i in range(len(WORDS)):
    currWord = random.choice(WORDS)
    print(currWord)
    WORDS.remove(currWord)

# An alternate version where the word is not removed after it is displayed
#
# Set up another list to hold the displayed words
#displayed = []
#
#for i in range(len(WORDS)):
#    currWord = random.choice(WORDS)
#    while currWord in displayed:
#        currWord = random.choice(WORDS)
#    displayed.append(currWord)
#    print(currWord)



input("\n\nPress the enter key to close the program.")
