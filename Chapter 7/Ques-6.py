rows = int(input("Enter the number --> "))

for i in range(3): 
    print(" " * (rows-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (rows-i-1))