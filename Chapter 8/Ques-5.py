# Write a Python program to reverse a string.

def reverse(s):
    a = len(s)
    for i in range (a):
        print(s[a-i-1], end = "")

s = input("Enter the string --> ")

reverse(s)