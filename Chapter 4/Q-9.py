# Write a Python program to convert a tuple to a dictionary.

tupp = ((2, "arjun"), (3, "malhotra"))

d = dict()

for x, y in tupp:
    d[x] = y

print(d)