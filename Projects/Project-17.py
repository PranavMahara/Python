# Write a Python program to find the missing number in a given array of numbers between 10 and 20.
# Original array: 10 11 12 13 14 16 17 18 19 20
# Missing number in the said array (10-20): 15

from array import *
a = array('i', [])
sum = 0

for i in range (10):
    print("Enter element ", str(i+1), end = " --> ")
    num = int(input(" "))
    a.append(num)
    sum = sum + num

print("The missing number is ", 165-sum)  # 165 as 10+11+12+...20 is 165