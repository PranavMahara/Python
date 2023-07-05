# Write a program to reverse a given number.

print("ARJUN MALHOTRA (21BBS0110)")
a = int(input("Enter the number --> "))
reversed_num = 0

while a != 0:
    digit = a % 10
    reversed_num = reversed_num * 10 + digit
    a //= 10

print(reversed_num)