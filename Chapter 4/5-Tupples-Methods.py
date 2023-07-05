t = (1, 3, 2, 4, 5, 6)

print(t.count(1)) # --> Shows the count of 1
print(t.index(5)) # --> Shows the index where value 5 is.
print(t[1:3])
index = t.index(1)
print(index)

print(len(t))
print(tuple(reversed(t)))

print("----------------------------")
p = tuple("HELLO WORLD")
print(p[1:7])
print(p[1:7:2])
print(t[::-1])
print(t[:])

q = (1, 2, 3, "a", [4, 5, 6])
print(q[-1][-1])
print(q[4][0])