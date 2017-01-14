# Useless Trivia (Edit)
#
# My attempt at making the useless trivia program

notice = "After entering your answers to the questions, press the enter key to continue"

print(notice.upper())

name = input("\nHi. What's your name? ")

age = input("\nHow old are you? ")
age = int(age)

# age = int(age) - this turns the string into an integer so
# that python recognises it as an integer

weight = input("\nOkay, this is my last question for you. "
               "How many pounds do you weigh? ")
weight = int(weight)

# Same with this^

print("""\n--------------------------------------------------------------------------""")

print("\nIf poet ee cummings were to email you he would address you as", name.lower())

print("\nBut if ee was mad at you, he'd call you", name.upper())

# ee cummings was an american poet who didn't use uppercase letters

called = name * 5

print("\nIf a small child was trying to get your attention, your name "
      "would become:")
print(called)

seconds = age * 365 * 24 * 60 * 60

# seconds - 365 days a year, 24 hours a day,
#           60 minutes an hour, 60 seconds a minute

print("\nYou are over", seconds, "seconds old.")

moon_weight = weight / 6

sun_weight = weight * 27.1

# The moon only has 1/6th of the gravitational pull of earth
# The suns gravitational pull is 27.1 times earths

print("\nDid you know that on the moon you would weigh", moon_weight, "pounds")

print("\nAnd on the sun you would weigh", sun_weight, "pounds.")
print("But you should just take my word on that.")


input("\n\nPress enter to exit")
