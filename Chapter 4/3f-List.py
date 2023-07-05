L = []
n = int(input("Enter the number of elements in the list --> "))

for i in range(n):
    ele = int(input("Enter the element --> "))
    L.append(ele)

for i in range(n):
    for j in range(n):
        if(L[i]<L[j]):
            temp = L[i]
            L[i] = L[j]
            L[j] = temp

print(L)