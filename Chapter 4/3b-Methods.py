a = [1, 2, 3.4, "Arjun"]

# a.sort()
# print(a) # Sort nahi hoga because of "Arjun", obvio how can you sort!

a.reverse()
print(a)

a.append("Hello")
print(a)

a.pop(2)
print(a)

a.remove("Arjun")
print(a)

a.insert(2, "lolol")

from random import shuffle
shuffle(a)
print(a)



l = [1, 2, 3, 4, 5, 6]
l.index(3, 3, 6)

l1 = [6, 7, 8]
l3 = l + l1

l.extend(l1)
print(l)

# append and extend diff?
# with append we can only add one element to the ened but with the help of extend we can
# add one or more than one elements to the end..