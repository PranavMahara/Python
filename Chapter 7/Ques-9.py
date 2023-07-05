# sum of all elements in a list

print("Arjun Malhotra, 21BBS0110")

a = []
n = int(input("Enter the how many numbers --> "))

for i in range (n):
    num = int(input("Enter the number --> "))
    a.append(num)
    
sum = 0

for i in a:
    sum = sum + i

print(sum)