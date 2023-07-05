# Sum of elements in List

n = int(input("Enter the number of elements in the list --> "))
L = []
sum = 0
for i in range (n):
    num = int(input("Enter element --> "))
    L.append(num)

for i in L:
    sum += i

print(sum)


