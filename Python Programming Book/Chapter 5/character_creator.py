# Character Creator
#
# Pg 155, Challenge No. 2
#
# Write a Character Creator program for a role-playing game.
# The player should be given a pool of 30 points to spend on
# four attributes: Strength, Health, Wisdom, and Dexterity.
# The player should be able to spend points from the pool on
# any attribute and should be able to take points from an
# attribute and put them back into the pool.
#
# Note:
# I added two extra options to this; The ability to remove
# all of points from the attributes and the ability to
# assign the remaining points in the pool to the
# attributes randomly.

import random

# Setting up variables
character = {"Strength":0,
             "Health":0,
             "Wisdom":0,
             "Dexterity":0
            }

choice = None
point_pool = 30

while choice != "0":
    print("""
    Character Creator

    0 - Exit character creator
    1 - Add points to an attribute
    2 - Remove points from an attribute (And add them back to the point pool)
    3 - Remove points from all attributes (And add them back to the point pool)
    4 - Randomly assign points from the point pool to characters

    Your character:

    Strength - """, character["Strength"], """
    Health - """, character["Health"], """
    Wisdom - """, character["Wisdom"], """
    Dexterity - """, character["Dexterity"], """

    Point Pool - """, point_pool, """
    """)

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Thank you for using the character creator")
    # Add points to an attribute
    elif choice == "1":
        if point_pool != 0:
            attribute = input("What attribute do you want to add points to? ")
            # Check that the attribute exists
            if attribute in character:
                add_points = int(input("How many points do you want to add? "))

                # Check that the number of points being added does not exceed
                # the number of points in the pool
                new_pool = point_pool - add_points
                while new_pool < 0:
                    print(add_points, "is more than the number of points in "
                          + "the pool. Please choose a lower number.")
                    add_points = int(input("How many points do you want to add? "))
                    new_pool = point_pool - add_points

                # Calculate the new number of points for the attribute
                new_att_points = character[attribute] + add_points
                character[attribute] = new_att_points

                # Update the point pool to reflect the change
                point_pool = new_pool

                print("\n", add_points, "points added to", attribute)
            else:
                print("The attribute", attribute, "doesn't exist. Please try again.")
        else:
            print("You don't have any points left!")
    # Remove points from an attribute
    elif choice == "2":
        if point_pool != 30:
            attribute = input("What attribute do you want to remove points from? ")
            # Check that the attribute exists
            if attribute in character:

                rem_points = int(input("How many points do you want to remove? "))
                # Check that the number of points being removed does not exceed
                # the number of points in the atttribute
                new_att_points = character[attribute] - rem_points
                while new_att_points < 0:
                    print(rem_points, "is more than the number of points in "
                          + "the attribute. Please choose a lower number.")
                    rem_points = int(input("How many points do you want to remove? "))
                    new_att_points = character[attribute] - rem_points

                # Calculate the new number of points for the point pool
                new_pool = point_pool + rem_points
                point_pool = new_pool

                # Update the attribute to reflect the change
                character[attribute] = new_att_points

                print("\n", rem_points, "points removed from", attribute)
            else:
                print("The attribute", attribute, "doesn't exist. Please try again.")
        else:
            print("You haven't added any points to the attributes yet!")
    # Remove all points from the attributes (AKA reset the character)
    elif choice == "3":
        if point_pool != 30:
            for attribute in character:
                character[attribute] = 0
            point_pool = 30
            print("Attributes emptied, point pool refilled")
        else:
            print("The attributes are already empty!")
    # Randomly assign the remaining points from the point pool to attributes
    elif choice == "4":
        if point_pool != 0:
            while point_pool != 0:
                # You can't use random.choice with dictionaries, so this
                # temporary list is to store the name of the attributes
                temp = []
                for att in character:
                    temp.append(att)
                # Choose a random attribute and a random number of points from
                # the available amount of points
                randAtt = random.choice(temp)
                randPoint = random.randint(0, point_pool)
                # Update attribute points and point pool
                new_att_points = character[randAtt] + randPoint
                character[randAtt] = new_att_points
                new_pool = point_pool - randPoint
                point_pool = new_pool
            print("Remaining points have been randomly allocated.")
        else:
            print("You have no points left!")
    else:
        print(choice, "is not a valid choice! Please try again")


input("\n\nPress the enter key to close the program.")
