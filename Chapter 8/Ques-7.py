# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def func(abc, a, b):
    for i in range (len(abc)):
        if(abc[i]==' '):
            continue

        if(abc[i]>='A' and abc[i]<='Z'):
            a = a + 1
        
        else:
            b = b + 1
    print("The number of upper case are --> ", a)
    print("The number of lower case are --> ", b)

abc = input("Enter the string --> ")

a = 0
b = 0
func(abc, a, b)