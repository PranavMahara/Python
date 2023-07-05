#  Write a program to maintain a telephone directory of the employees of an 
# organization. If the employee has more than one number store all the numbers. Write 
# a program to print the mobile numbers given full or part of the name of the employee. 
# Eg: Given name of the employee as ‘John’ the program must print phone numbers of 
# ‘John Paul’ and ‘Michel John’.

test = "y"

dict = {}

while test == "y":
    name = input("Enter name of the Employee : ")
    n = int(input("Total number of mobile numbers : "))
    ls = []
    for i in range(n):
            phone = int(input("Enter phone number : "))
            ls.append(phone)
    dict[name] = ls
    test = input("Do you wish to proceed (y/n) : ")

n2 = input("Enter a name : ")

for i in dict.keys():
    if n2 in i:
        for j in dict.get(i):
            print(j)