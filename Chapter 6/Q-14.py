# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
print("ARJUN MALHOTRA (21BBS0110)")
rows = int(input("Enter the rows --> "))

for i in range (rows+1):
    for j in range (i):
        print(i, end = " ")
    print()
