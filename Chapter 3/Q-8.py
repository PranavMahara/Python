# Write a Python function to reverses a string if it's length is a multiple of 4

a = input("Enter the string --> ")
n = len(a)

if(n%4==0):
    print(a[::-1])

