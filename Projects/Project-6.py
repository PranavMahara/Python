# Write a Python program to check a triangle is equilateral, isosceles or scalene.

x, y, z = input("Enter three sides: ").split()

if(x==y and y==z and z==x):
    print("The triangle is equilateral")

elif(x!=y and y!=z and z!=x):
    print("The triangle is scalene")

else:
    print("The triangle is isoceles")

    