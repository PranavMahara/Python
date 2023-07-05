# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

d = {}

n = int(input("Enter n: "))

for i in range (n):
    new = (i+1)*(i+1)
    d[i] = new

print(d)