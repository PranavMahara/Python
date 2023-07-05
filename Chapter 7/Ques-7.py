# Write a program to print the multiplication table from 2 to n upto 10th term

print("Arjun Malhotra, 21BBS0110")

n = int(input("Enter the number --> "))

for i in range(2, n+1):
    for j in range(1, 11):
        print(i, "x", j, " = ",i*j, end = "|| ")
    print()
    