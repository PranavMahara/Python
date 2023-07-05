# Write a Python program to get the number of occurrences of a specified element in an array.

from array import *
a = array('i', [])

n = int(input("Enter the number of elements in the array --> "))
k = int(input("Enter the element --> "))
count = 0

for i in range (n):
    print("Enter element ", str(i+1), end = " --> ")
    num = int(input(" "))
    a.append(num)
    if(num==k):
        count = count + 1

print("The number of occurences are ", count)
print(a)