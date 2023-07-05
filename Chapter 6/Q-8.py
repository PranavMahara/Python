# Write a Python program to get the Fibonacci series between 0 to 50.

x, y = 0, 1

n = int(input("Enter the number of terms --> "))

for i in range (n):
    print(y, end = " ")
    x, y = y, x+y