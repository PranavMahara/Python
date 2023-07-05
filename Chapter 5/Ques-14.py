# Average value of numbers in given tuple of tuples
print("Arjun Malhotra, 21BBS0110")

a = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
b = []

for i in a:
    total = 0
    for j in i:
        total += j

    avg = total/(len(i))
    b.append(avg)

print(b)