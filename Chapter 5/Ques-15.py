# Replace Last value of tuple in a list
print("Arjun Malhotra, 21BBS0110")

a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

for i in a:
    b = list(i)
    b[len(b) - 1] = 100
    x = tuple(b)
    a[a.index(i)] = x

print(a)