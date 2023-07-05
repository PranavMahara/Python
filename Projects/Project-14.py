# Write a Python program to get the smallest and max number from a list.

n = int(input("Enter the number of elements in the list --> "))
L = []
for i in range (n):
    num = int(input("Enter element --> "))
    L.append(num)

min = L[0]
max = L[0]
for i in L:
    if(i<min):
        min = i
    
    if(i>max):
        max = i
    
print("The smallest element in the list is ", min)
print("The maximum element in the list is ", max)

# Or simply the best solution
# a = [1, 7, 4, 9]
# a.sort()
# print(a[0]) # --> Min
# print(a[len(a)-1]) # --> Max