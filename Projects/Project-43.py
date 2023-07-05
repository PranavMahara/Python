# Write a Python program to remove an empty tuple(s) from a list of tuples.

L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L.remove(())

print(L)


# Other way
l =[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
l1=[]
for i in l:
    if(len(i))>0:
        l1.append(i)
print(l1)