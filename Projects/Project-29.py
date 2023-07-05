#  Write a Python program to print alphabet pattern 'T'.

n = int(input("Enter the rows(odd only) --> "))

print("* "*(n))

for i in range (n):
    print(" "*(int(n)), "*")