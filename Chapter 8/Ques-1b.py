# Find max of 3 num using functions

def max(num1, num2, num3):
    if(num1>num2 and num1>num3):
        return num1
    
    elif(num2>num1 and num2>num3):
        return num2
    
    else:
        return num3

a = int(input("Enter first number --> "))
b = int(input("Enter second number --> "))
c = int(input("Enter third number --> "))

print("The maximum is", max(a, b, c))