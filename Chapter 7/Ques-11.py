# Matrix Addition and Matrix Multiplication

print("Arjun Malhotra, 21BBS0110")

X = []
Y = []

for i in range(3):
    A = []
    for j in range(3):
        element = int(input("Enter element --> "))
        A.append(element)        
    X.append(A)

for i in range(3):
    B = []
    for i in range(3):
        element = int(input("Enter element --> "))
        B.append(element)        
    Y.append(B)


result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
print("------------------------------")
result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)