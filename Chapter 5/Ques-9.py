# Write a Python program to sum all the items in a dictionary

a = {
    'a' : 1, 
    'b' : 2,
    'c' : 3
}

print(sum(a.values()))
# print(sum(a.keys()))  # Nahi chalega

b = {
    1 : 'a', 
    2 : 'b',
    3 : 'c'
}

print(sum(b.keys()))