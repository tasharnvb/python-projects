# Pg 155, Challenge No. 2 (With 2 extra options)
#
# Character Creator
#
# A character creator for an RPG

import random

# Setting up variables
CHARACTER = {"Strength":0,
             "Health":0,
             "Wisdom":0,
             "Dexterity":0
            }

choice = None
pointPool = 30

while choice != "0":
    print("""
    Character Creator

    0 - Exit character creator
    1 - Add points to an attribute
    2 - Remove points from an attribute (And add them back to the point pool)
    3 - Remove points from all attributes (And add them back to the point pool)
    4 - Randomly assign points from the point pool to characters
    
    Your character:

    Strength - """, CHARACTER["Strength"], """
    Health - """, CHARACTER["Health"], """
    Wisdom - """, CHARACTER["Wisdom"], """
    Dexterity - """, CHARACTER["Dexterity"], """

    Point Pool - """, pointPool, """
    """)

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Thank you for using the character creator")
    # Add points to an attribute
    elif choice == "1":
        if pointPool != 0:
            attribute = input("What attribute do you want to add points to? ")
            # Check that the attribute exists
            if attribute in CHARACTER:
                addPoints = int(input("How many points do you want to add? "))
                
                # Check that the number of points being added does not exceed
                # the number of points in the pool
                newPool = pointPool - addPoints
                while newPool < 0:
                    print(addPoints, "is more than the number of points in "
                          + "the pool. Please choose a lower number.")
                    addPoints = int(input("How many points do you want to add? "))
                    newPool = pointPool - addPoints

                # Calculate the new number of points for the attribute
                newAttPoints = CHARACTER[attribute] + addPoints
                CHARACTER[attribute] = newAttPoints

                # Update the point pool to reflect the change
                pointPool = newPool
            
                print("\n", addPoints, "points added to", attribute)
            else:
                print("The attribute", attribute, "doesn't exist. Please try again.")
        else:
            print("You don't have any points left!")
    # Remove points from an attribute
    elif choice == "2":
        if pointPool != 30:
            attribute = input("What attribute do you want to remove points from? ")
            # Check that the attribute exists
            if attribute in CHARACTER:
            
                remPoints = int(input("How many points do you want to remove? "))
                # Check that the number of points being removed does not exceed
                # the number of points in the atttribute
                newAttPoints = CHARACTER[attribute] - remPoints
                while newAttPoints < 0:
                    print(remPoints, "is more than the number of points in "
                          + "the attribute. Please choose a lower number.")
                    remPoints = int(input("How many points do you want to remove? "))
                    newAttPoints = CHARACTER[attribute] - remPoints

                # Calculate the new number of points for the point pool
                newPool = pointPool + remPoints
                pointPool = newPool

                # Update the attribute to reflect the change
                CHARACTER[attribute] = newAttPoints
            
                print("\n", remPoints, "points removed from", attribute)
            else:
                print("The attribute", attribute, "doesn't exist. Please try again.")
        else:
            print("You haven't added any points to the attributes yet!")
    # Remove all points from the attributes (AKA reset the character)
    elif choice == "3":
        if pointPool != 30:
            for attribute in CHARACTER:
                CHARACTER[attribute] = 0
                pointPool = 30
            print("Attributes emptied, point pool refilled")
        else:
            print("The attributes are already empty!")
    # Randomly assign the remaining points from the point pool to attributes
    elif choice == "4":
        if pointPool != 0:
            while pointPool != 0:
                # You can't use random.choice with dictionaries, so this
                # temporary list is to store the name of the attributes
                temp = []
                for att in CHARACTER:
                    temp.append(att)
                # Choose a random attribute and a random number of points from
                # the available amount of points
                randAtt = random.choice(temp)
                randPoint = random.randint(0, pointPool)
                # Update attribute points and point pool
                newAttPoints = CHARACTER[randAtt] + randPoint
                CHARACTER[randAtt] = newAttPoints
                newPool = pointPool - randPoint
                pointPool = newPool
            print("Remaining points have been randomly allocated.")
        else:
            print("You have no points left!")
    else:
        print(choice, "is not a valid choice! Please try again")
        

input("\n\nPress the enter key to close the program.")
