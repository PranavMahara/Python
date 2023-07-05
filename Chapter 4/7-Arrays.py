from array import *
p = array('i', [1, 2, 3, 4, 3, 4, 6])

q = list(p)
print(q)

print(p.buffer_info())
print(p.itemsize)

e = array('i', [1.1, 2.4, 45.5])
print(e.itemsize)
