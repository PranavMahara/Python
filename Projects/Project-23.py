# Write a Python script to print a dictionary where the keys are numbers between 1 and n (both included) and the values are square of keys. 

d = {}

n = int(input("Enter n: "))

for i in range (1, n+1):
    new = (i)*(i)
    d[i] = new

print(d)
