# Write a program to program to print the total no of the digits in a given number.

print("ARJUN MALHOTRA (21BBS0110)")
a = int(input("Enter the number --> "))

count = 0

while(a!=0):
    a//=10
    count = count + 1

print("The number of digits in count -->", count)