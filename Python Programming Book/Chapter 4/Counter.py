# Pg 120, Challenge No. 1

print("\t\t\tCounter")

start = int(input("\nEnter the number you would like to start at: "))

end =  int(input("\nEnter the number you would like to end at: "))

count = int(input("\nEnter the amount by which to count: "))
print("\n")
for i in range(start, end, count):
    print(i)

input("\n\nPress enter to exit")
