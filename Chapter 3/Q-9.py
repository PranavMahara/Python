# Write a Python program to print the following floating numbers upto 2 decimal places.

x = float(input("Enter the number --> "))
print("Number --> ", "{:.2f}".format(x))
print("Number --> "+"{:+.2f}".format(x))
print("Number --> ", "{:.0f}".format(x))