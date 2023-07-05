set1 = {1, 2, 3}
# set1.remove(5)   # This will show error that 5 is not there
set1.discard(5)  # This will not show any error 
set1.pop() # Remove any random item from a set

# set1.clear() This will clear items from the set
del set1 # This will completely delete the entire set


# Iterating
# We cannot use keys so we iterate to get elements in the set
for i in set1:
    print(i)

set2 = set1.copy()   # or set2 = set(set1)    or  set2 = set1
print(set2)

# Remove() v/s Discard()
'''
The remove() method throws a keyerror if the item you want to delete is not 
present in a set
The discard() method will not throw any error if the item you want to delete is 
not present in a set
'''
# why shouldn't we go with assignment operator in set python
# When you set set2= set1, you are making them refer to the same dict object, so when you 
# modify one of them, all references associated with that object reflect the current state of the 
# object. So don’t use the assignment operator to copy the set instead use the copy() method 
# or set() constructor.