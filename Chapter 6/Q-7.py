# Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

rows = int(input("Enter the number of rows --> "))

for i in range (rows):
    print("*"*(i+1))

for i in range (rows-1):
    print("*"*(rows-i-1))

