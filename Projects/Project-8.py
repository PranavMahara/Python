# Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.

sum = 0
n = 1
count = 1

while(n!=0):
    n = int(input(""))
    sum = sum + n
    count = count + 1

print("The sum is",sum)
print("The average is",sum/count)