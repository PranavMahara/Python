# N1 : 2345
# N2 : 4986
# Result --> 2*4 + 3*9 + 4*8 + 5*6

n1 = int(input("Enter N1 --> "))
n2 = int(input("Enter N2 --> "))

N1 = n1
N2 = n2
num = 0

while(n1!=0 and n2!=0):
    n1 = int(n1/10) 
    n2 = int(n2/10)
    num = num + 1
    
sum = 0

if(n1==0 and n2==0):
    print("Length of string is equal")
    for i in range (num):
        sum = sum + (N1%10)*(N2%10)
        N1 = int(N1/10)
        N2 = int(N2/10)

else:
    print("Length of string is not equal")

print("The sum is ", sum)


