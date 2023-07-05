# Write a Python program to calculate the sum of a list of numbers using recursion
# CHECK
def sum(M):
    if len(M) == 1:
        return M[0]
    else:
        return M[0] + M[1:]

n = int(input("Enter num --> "))
L = []

for i in range (n):
    num = int(input("Enter the number --> "))
    L.append(num)

print("The sum is ", sum(L))