# Write a Python program to calculate the sum of the digits in an integer.

n = int(input("Enter the number --> "))

sum = 0
while(n!=0):
    sum = sum + int(n%10)
    n = n/10

print(sum)