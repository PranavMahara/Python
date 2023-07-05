# Write a Python function that checks whether a passed string is palindrome or not.

s = input("Enter the string --> ")
p = int(len(s)/2)
q = int(len(s))
count = 0
for i in range (p):
    if(s[i] == s[q-i-1]):
        count = count+1

if(count==0):
    print("The string is palindrome")

else:
    print("The string is not a palindrome")
