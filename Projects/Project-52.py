#  Write a Python program to check whether the given strings are palindromes or not. Return True, False.

s = input("Enter the string --> ")
n = len(s)
count = 0

for i in range (int(n/2)):
    if(s[i]!=s[n-i-1]):
        # print(i)
        # print(s[i])
        count+=1
    

if(count==0):
    print("The string is palindrome")

else:
    print("The string is not palindrome")
