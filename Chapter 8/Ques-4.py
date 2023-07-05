# Write a Python function to sum all the numbers in a list.

def sum(abc):
    sum = 0
    for i in range (len(abc)):
        sum = sum + lst[i]
    
    return sum

lst = []
n = int(input("Enter the number of elements in the list --> "))

for i in range (n):
    elemen = int(input("Enter element " + str(i+1) + " --> "))
    lst.append(elemen)

# print(lst)
print("The sum of elements in the list ", lst, " is", sum(lst))
