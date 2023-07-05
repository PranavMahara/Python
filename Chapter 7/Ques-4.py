num = int(input("Enter the number --> "))

pro = 1
for i in range(1, num+1):
    pro = pro*i

print("The Factorial of", num, "is", pro)