# Write a Python program to convert a given tuple of positive integers into an integer.

n = int(input("Enter the number of elements in the tuple --> "))
L = ()
for i in range (n):
    num = int(input("Enter element --> "))
    L = L + (num, )

new = ""
for i in L:
    new = new + str(i)

print(new)