# Find max of 3 num using functions

def maximum(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    
    else:
        if(num2>num3):
            return num2
        else:
            return num3


m = maximum(3, 5, 6)
print("The max value is", m)
         