a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}

c = a & b # Intersection
print(c)

d = a | b  # other way --> d = a.union(b)  # Union
print(d)

e = a.difference(b) # other way -->  e = a-b # Difference of Sets
f = a.difference(a)
g = b.difference(a)
h = b.difference(b)

print(e)
print(f)
print(g)
print(h)

i = a.symmetric_difference(b) # other way --> i = a^b # Symmetric Difference

print(i)