# Write a Python function to check whether a number is perfect or not.

n = int(input("Enter the number --> "))
sum = 0
count = 0
for i in range(1, n):
    if(n%i==0):
        sum = sum + i
        count = count + 1
    
if(n==sum):
    print("The number is perfect")

else:
    print("The number is not perfect")

