# Sort the elements in ascending order

print("Arjun Malhotra, 21BBS0110")

a = []
n = int(input("Enter the how many numbers --> "))

for i in range (n):
    num = int(input("Enter the number --> "))
    a.append(num)

minimum = a[0]

for i in range (n):
    for j in range(i + 1, n):
        if(a[i] > a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)