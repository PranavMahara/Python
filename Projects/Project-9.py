# Write a Python program to create the multiplication table of a number.

n = int(input("Enter the number --> "))

for i in range (10):
    print(n, "*", (i+1), "=", n*(i+1))