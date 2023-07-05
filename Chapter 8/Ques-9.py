# Write a Python function that takes a number as a parameter and check the number is prime or not.

def prime(b):
    count = 0
    for i in range (b+1):
        if(b%(i+1)==0):
            count = count + 1
        
    if(count==2):
        return "YES"
        
    else:
        return "NO"

a = int(input("Enter the number --> "))
p = prime(a)
print(p)