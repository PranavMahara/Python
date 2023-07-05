# Set --> Unordered, Heterogenous, Immutable, No duplicate

a = {1, 2, 3, 4, 9, 6}
print(type(a))
print(a)

b = {} # This creates an empty dictionary and not an empty set
print(type(b))

k = {1, 9, 6}
print(a.issuperset(k))
print(a.issubset(k))
print(a.isdisjoint(k))

print(3 in a)
print(95 in a)
c = set() # This is empty set
# q = set(1, 2, 3) # this is also a set

# c.add(4, 5) wrong
c.add(5)
c.add(5)
# c.add({4 : 5})
# c.add([6, 7, 8]) # Lists and dictionary can not be added
c.add((6, 7, 8)) # Tupples can be added
print(c)

# # print(len(c)) --> prints length of this set
# # We can remove element with the help of c.remove(5)
# c.pop() # removes any random element from the set
# print(c)

# # c.clear() empties the set c

d = {18, "18"}
print(d)
d.update((18, 68))
print(d)