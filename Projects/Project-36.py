# Write a Python program to swap two variables.

x = int(input("Input first number: "))
y = int(input("Input second number: "))

print("The number before swapping --> ", x, "and", y)

temp = x
x = y
y = temp

print("The number before swapping --> ", x, "and", y)