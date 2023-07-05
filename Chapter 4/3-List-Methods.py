L1 = [1, 5, 2, 8, 6]
# L1_new = L1.sort() Wont work it will return None
# print(L1_new)

# L1.sort()    --> Sorts the List
# L1.reverse()  --> Reverses the List
# L1.append(45)  --> Adds 45 at the end of the list
# L1.insert(0, 544) --> Now 544 is at index zero
# L1.pop(2) --> Remove element at index 2
# L1.pop() --> Removes the last
# L1.remove(6) --> Removes 6 from the list
# print(sum(L1))
# print(len(L1))
# L1.extend([1, 2, 3, 4])  --> Extends the List
# L1.clear()  --> Makes the List empty
print(L1)
# A list can also be copied using the slicing operator. This is the fastest way to copy a list.
P = [1, 2]
if(not P):
    print("The list is empty")

else:
    print("The list is not empty")