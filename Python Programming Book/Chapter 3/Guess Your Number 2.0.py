# Pg 85, Challenge No. 4
# I'm too lazy to do the first part (Writing the pseudocode for this)

import random

print("\t\tGuess Your Number")
print("\nThink of a number between 1 and 100. "
      "Once you have, press enter.")
input("\nNOTE: I am case sensitive. ")

old_guess = 0
lower_limit = 1
upper_limit = 100

comp_guess = random.randint(lower_limit,upper_limit)

print("\n\nMy guess is...", comp_guess)
your_number = input("\nIs that your number? (Type yes or no) ")

if your_number == "yes":
    print("\nWell that's the end of the game then")

elif your_number == "no":

    while your_number != "yes":
        
        old_guess = comp_guess
        
        h_or_l = input("\nHigher or Lower? (Type h or l) ")
        
        if h_or_l == "h":
            
            if old_guess == upper_limit:
                print("\nI said think of a number BETWEEN 1 "
                      "AND 100!!! Play the game properly next time")
                break
            
            lower_limit = old_guess
            
        elif h_or_l == "l":
            
            if old_guess == lower_limit:
                print("\nI said think of a number BETWEEN 1 "
                      "AND 100!!! Play the game properly next time")
                break
            
            upper_limit = old_guess
            
        else:
            print("\nAnswer the question CORRECTLY next time.")
            
        comp_guess = random.randint(lower_limit,upper_limit)

        while comp_guess == old_guess:
            comp_guess = random.randint(lower_limit,upper_limit)
            
        print("\nMy guess is...", comp_guess)
        your_number = input("\nIs that your number? (Type yes or no) ")
    
        if your_number == "yes":
            print("\nWell that's the end of the game then.")
            break
    
        elif your_number == "no":
            
            if upper_limit-lower_limit == 1:
                print("\nEither", comp_guess, "is your number, or you "
                      "lied while answering an earlier question.")
                break
            
            else:
                continue
            continue
    
        else:
            print("\nAnswer the question CORRECTLY next time.")

else:
    print("\nI'm not going to play if you can't follow simple "
          "instructions.")


input("\n\nPress the enter key to exit.")

# My improved version of this. Specifically, I changed it to implement a
# higher or lower feature to make it so the game always has an ending
