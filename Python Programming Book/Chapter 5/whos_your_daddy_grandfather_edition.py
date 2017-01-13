# Pg 155, Challenge No. 3 (With 2 extra options)
#
# Who's Your Daddy? (Grandfather Edition)
#
# A program that allows users to find
# out someone's father (and grandfather) by entering the son's name

# Setting up a dictionary to hold the father(grandfather)/son pairs
# Note: It is in the format son:[father, grandfather]
pairs = {"World":["Hello", "Greetings"],
         "Alsanna":["Manus", "Dark Lord"],
         "Gwyndolin":["Gwyn", "Unknown"],
         "Humanity":["Dark", "Manus"],
         "Sorcery":["Seath", "Unknown"]
         }

choice = None

while choice != "0":
    print("""
    Who's Your Daddy? (Grandfather Edition)

    0 - Exit program
    1 - Find father (Using son's name)
    2 - Add father/son pair
    3 - Change father (For a specified son)
    4 - Delete father/son pair
    5 - View all names that can be entered
    6 - Find grandfather (Using grandson's name)
    7 - Change grandfather (For a specified grandson)
    """)

    choice = input("Choice: ")
    print()

    # Exit
    if choice == "0":
        print("Thank you for using the Who's Your Daddy program")
    # Return father based on given name
    elif choice == "1":
        son = input("What is the name of the son that you want to view the father of? ")
        # Check if the son exists in the dictionary
        if son in pairs:
            print("The father of", son, "is", pairs[son][0])
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
            pairs[son][0] = father
            print(son, "has been updated")
        else:
            print("The son", son, "does not exist! Please try again with another name.")        
    # Delete (father/grandfather)/son pair
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
    # Return grandfather based on given name
    elif choice == "6":
        son = input("What is the name of the son that you want to view the grandfather of? ")
        # Check if the son exists in the dictionary
        if son in pairs:
            print("The grandfather of", son, "is", pairs[son][1])
        else:
            print(son, "does not exist! Please try again with another name.")
   # Change grandfather (For specified grandson)
    elif choice == "7":
        son = input("What is the name of the son that you want to change the grandfather of? ")
        if son in pairs:
            grandfather = input("What is the name of the new grandfather? ")
            pairs[son][1] = grandfather
            print(son, "has been updated")
        else:
            print("The son", son, "does not exist! Please try again with another name.")        
    else:
        print(choice, "is not a valid choice! Please try again")
        

input("\n\nPress the enter key to close the program.")
        
