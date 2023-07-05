from array import *
a = array('i', [1, 2, 3, 4])  # i is for signed int, u can see rest in png file Arrays-In-Python

for i in a:
    print(i, end = " ")

print("\n------------------")

a.append(69)  # Adding element to the end
b = len(a)
for i in range (b):   # Other way of printing elements
    print(a[i], end = " ")

