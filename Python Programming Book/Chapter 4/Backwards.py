# Pg 120, Challenge No. 2

print("\t\tBackwards")

word = input("\n\nType in the word you want to see backwards ")

position = -1   # The first letter of the word is at index 0,
                     # index -1 is the last letter of the word 
backwards = ""

for i in range(len(word)):
    backwards += word[position]
    position -= 1

# An alternate way to do this with a while loop

#position = len(word) - 1   # Eg. if the word was 'test' then the length would be 4,
                                      # but when counting we start at 0 so index 3 is the end
                                      # of the word not 4
#while position >= 0:
#    backwards += word[position]
#    position -= 1

print("\nYour word backwards is: " + backwards)

input("\n\nPress enter to exit")
