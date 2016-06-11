# Pg 155, Challenge No. 3 (With an extra option)
#
# Who's Your Daddy?
#
# A program that allows users to find
# out someone's father by entering the son's name

# Setting up a dictionary to hold the father/son pairs
# Note: It is in the format son:father
pairs = {"World":"Hello",
         "Alsanna":"Manus",
         "Gwyndolin":"Gwyn",
         "Humanity":"Dark",
         "Sorcery":"Seath"
         }

choice = None

while choice != "0":
    print("""
    Who's Your Daddy?

    0 - Exit program
    1 - Find father (Using son's name)
    2 - Add father/son pair
    3 - Change father (For a specified son)
    4 - Delete father/son pair
    5 - View all names that can be entered
    """)

    choice = input("Choice: ")
    print()

    # Exit
    if choice == "0":
        print("Thank you for using the Who's Your Daddy program")
    # Search dictionary for father/son pair
    elif choice == "1":
        son = input("What is the name of the son that you want to view the father of? ")
        # Check if the son exists in the dictionary
        if son in pairs:
            print("The father of", son, "is", pairs[son])
        else:
            print(son, "does not exist! Please try again with another name.")
    # Add new father/son pair
    elif choice == "2":
        son = input("What is the name of the son for this new pair? ")
        if son not in pairs:
            father = input("What is the name of the father for this pair? ")
            pairs[son] = father
            print(son, "has been added")
        else:
            print("The son", son, "already exists! If you want to change the father's name for this son, then try replacing instead of adding.")
    # Change father (For specified son)
    elif choice == "3":
        son = input("What is the name of the son that you want to change the father of? ")
        if son in pairs:
            father = input("What is the name of the new father? ")
            pairs[son] = father
            print(son, "has been updated")
        else:
            print("The son", son, "does not exist! Please try again with another name.")        
    # Delete father/son pair
    elif choice == "4":
        son = input("What is the name of the son of the pair that you want to delete? ")
        if son in pairs:
            del pairs[son]
            print(son, "has been deleted")
        else:
            print("The son", son, "does not exist! Please try again with another name.")
    # View all keys in dictionary
    elif choice == "5":
        print("Here is a list of the names that are currently available:\n")
        for key in pairs:
            print(key)
    else:
        print(choice, "is not a valid choice! Please try again")
        

input("\n\nPress the enter key to close the program.")
        
