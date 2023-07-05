#  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

a = int(input("Enter first number --> "))
b = int(input("Enter second number --> "))

if(((a+b) == 5) or ((a-b) == 5) or ((b-a) == 5)):
    print("TRUE")

else:
    print("FALSE")