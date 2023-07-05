# Write a Python program to print alphabet pattern 'D'.

rows = int(input("Enter the number of rows --> "))

print("*"*rows)
for i in range (rows):
    print("*", " "*(rows-3), "*")
    
print("*"*rows)