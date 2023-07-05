# Write a program to print the following number pattern using a loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

print("ARJUN MALHOTRA (21BBS0110)")
rows = int(input("Enter the rows --> "))

for i in range (rows+1):
    for j in range (i):
        print("*", end = " ")
    print()

for i in range(rows):
    for j in range(rows-i-1):
        print("*", end = " ")
    print()
