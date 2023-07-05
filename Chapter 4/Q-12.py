# Write a Python program to flatten a shallow list.

a = [[1, 2], [1, 3, 5], [3, 4, 7]]
b = []

for i in a:
    for j in range (len(i)):
        b.append(i[j])

print(b)