# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

a = set(["White", "Black", "Red"])
b = set(["Red", "Green"])

print(a.difference(b))
print(b.difference(a))