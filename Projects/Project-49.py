# Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.

n = int(input("Enter the number of elements in the list --> "))
L = []
for i in range (n):
    num = int(input("Enter element --> "))
    L.append(num)

y = L.count(19)
z = L.count(5)

if(y==2 and z>=3):
    print("TRUE")

else:
    print("FALSE")