# Compute the sum of all the elements stored inside a list of tuples

print("Arjun Malhotra, 21BBS0110")
a = ((1, 2), (2, 3), (3, 4))

b = ()
sum = 0
for i in a:
    for j in i:
        sum = sum + j
    b = b + (sum, )
    sum = 0

print(b)
