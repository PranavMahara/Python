# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

x1 = int(input("Enter x1 --> "))
x2 = int(input("Enter x2 --> "))
y1 = int(input("Enter y1 --> "))
y2 = int(input("Enter y2 --> "))

t = pow(pow(x2-x1, 2) + pow(y2-y1, 2), 1/2)
print(t)