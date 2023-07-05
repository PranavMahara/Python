# Rotated List

def Rotate(lis, k, n):
    if (k < 0 or k >= n):
        return 0
    

    for i in range(k):
        last = lis[n-1]
        i = n-2
        for i in range (n-2, -1, -1):
            lis[i+1] = lis[i]

        lis[0] = last
L = []

n = int(input("Enter the number of elements in the list --> "))
k = int(input("Enter the shift --> "))

for i in range(n):
    ele = int(input("Enter the element --> "))
    L.append(ele)

Rotate(L, k, n)

for i in range(n):
    print(L[i], end = " ")







    