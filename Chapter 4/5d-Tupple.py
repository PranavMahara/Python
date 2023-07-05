tup = (1, 2, 6, 8, 547, 99)

print(tup.index(2))
print(5 not in tup)
print(min(tup))
print(max(tup))


tupp = 1, 2, 3    # Packing
print(tupp, type(tupp))

i, j, k = tupp
print(i, j, k)

# assigns the right-hand side of values into the left-hand side. 
# In another way, it is called unpacking of a tuple of values into a variable. 
# In packing, we put values into a new tuple while in unpacking we extract those values into a single variable.