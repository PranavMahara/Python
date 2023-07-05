# Write a Python program to get unique values from a list.

L = [1, 2, 3, 1, 5, 8, 9, 15, 24, 24, 57]

NewSet = set(L)
L = list(NewSet)

print(L)