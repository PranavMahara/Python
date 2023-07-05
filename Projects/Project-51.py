# Write a Python program to check a given list of integers where the sum of the first i integers is i.

n = int(input("Enter the number of elements in the list --> "))
L = []
for i in range (n):
    num = int(input("Enter element --> "))
    L.append(num)

sum = 0
count = 0

for i in L:
    sum = sum + i
    count = count + 1

if(sum==count):
    print("TRUE")

else:
    print("FALSE")