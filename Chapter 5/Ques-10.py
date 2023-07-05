# Write a Python program to multiply all the items in a dictionary.

a = {
    'a' : 13, 
    'b' : 22,
    'c' : 31
}

result = 1

for i in a:
    result = result*a[i]

print(result)