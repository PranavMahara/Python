# Write a Python program to count the elements in a list until an element is a tuple.

num = [10, 20, 30, (10,20), 40]
count = 0

for i in num:
    if(isinstance(i, tuple)):
        break

    else:
        count += 1

print(count)
