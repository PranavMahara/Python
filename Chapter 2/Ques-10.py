# Write a program to find the largest among three numbersusing nested if.

print("ARJUN MALHOTRA 21BBS0110")
a = int(input("Enter the first number --> "))  
b = int(input("Enter the second number --> "))
c = int(input("Enter the third number --> "))

if (a >= b):
    if (a >= c):
        print(a, " is largest number")
    else:
        print(c, " is largest number")

else: 
    if (b >= c):
        print(b, " is largest number")
    else:
        print(c, " is largest number")
  
