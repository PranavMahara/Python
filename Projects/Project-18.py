# Write a Python program to print the numbers of a specified list after removing even numbers from it.

L = []
n = int(input("Enter the number of elements in the list --> "))

for i in range (n):
    num = int(input("Enter element --> "))
    if(num%2!=0):
        L.append(num)

print(L)