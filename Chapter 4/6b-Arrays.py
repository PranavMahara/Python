from array import *
p = array('i', [1, 2, 3, 4, 3, 4, 6])

p.reverse()
print(p)

b = len(p)
print("The elements of the array are --> ", end = " ")
for i in range (b):  
    print(p[i], end = " ")