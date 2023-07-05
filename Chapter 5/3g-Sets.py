# FrozenSet
# A frozenset is an immutable set. Frozen Set is thus an unordered collection of immutable 
# unique items.
# We can create a frozenset using the frozenset() function, which takes a single iterable 
# object as a parameter

rainbow = ('violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red')
# create a frozenset
f_set = frozenset(rainbow)
print(f_set)
# output frozenset({'green', 'yellow', 'indigo', 'red', 'blue', 'violet', 'orange'})

# When to use frozenset ?
# • When you want to create an immutable set that doesn’t allow adding or 
# removing items from a set.
# • When you want to create a read-only set
# Now if we try to drop or add any item then it will throw an error as a frozen set 
# is immutable

rainbow = ('violet', 'indigo', 'blue')
f_set = frozenset(rainbow)
# Add to frozenset
f_set.add(f_set)
# output AttributeError: 'frozenset' object has no attribute 'add'

# All the mathematical operations performed in a set is possible with the frozenset. We can 
# use union(), intersection(), difference(), and symmetric_difference() on a frozenset as 
# well.
# But we can’t use the intersection_update(), difference_update(), 
# and symmetric_difference_update() on frozenset as it is immutable.

colorset1 = frozenset(('violet', 'indigo', 'blue', 'green'))
colorset2 = frozenset(('blue', 'green', 'red'))
# Mathametical operations with a frozen set
# union
print('The colors of the rainbow are:', colorset1.union(colorset2))
# output frozenset({'red', 'green', 'blue', 'violet', 'indigo'})
# intersection
print('The common colors are:', colorset1.intersection(colorset2))
# output frozenset({'green', 'blue'})
# difference
print('The unique colors in first set are:', colorset1.difference(colorset2))
# output frozenset({'violet', 'indigo'})
print('The unique colors in second set are:', colorset2.difference(colorset1))
# output frozenset({'red'})
# symmetric difference
print('The unique colors second set are:',
colorset1.symmetric_difference(colorset2))
# output frozenset({'indigo', 'red', 'violet'})