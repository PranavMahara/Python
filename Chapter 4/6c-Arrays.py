from array import *
a = array('i', [1, 2, 3, 4])

a.insert(1, 4) # Inserts value 4 at index 1 
# a.remove(3) # Removes element 3
a.pop(2) # Removes element at index 2
for i in a:
    print(i, end = " ")

