# Write a Python program to print alphabet pattern 'O'.
#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 

n = int(input("Enter the rows --> "))

print(" "*2, end = "")
print("*"*(3))

for i in range (n):
    print("*", " "*3, "*")

print(" "*2, end = "")
print("*"*(3))
    