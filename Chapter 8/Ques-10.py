# Write a Python program to print the even numbers from a given list.

def even(lst):
    new_lst = []
    for i in range (len(lst)):
        if(lst[i]%2==0):
            new_lst.append(lst[i])
        
    return new_lst

lst = []
n = int(input("Enter the number of elements in the list --> "))

for i in range (n):
    elemen = int(input("Enter element " + str(i+1) + " --> "))
    lst.append(elemen)

print(even(lst))