# Write a Python function to check whether a number falls in a given range.

def check(a, b, c):
    if((a>=b and a<=c) or (a<=b and a>=c)):
        print("YES")

    else:
        print("NO")

a = int(input("Enter the number: "))
print("Enter the range --> ", end = "")
b, c = int(input()), int(input()) 

check(a, b, c)