# Write a Python program to print the following integers with zeros on the left of specified width.
# Original Number:  3                                                                                           
# Formatted Number(left padding, width 2): 03                                                                   
# Original Number:  123                                                                                         
# Formatted Number(left padding, width 6): 000123 



# Check this method
# x = int(input("Enter the number --> "))
# y = str(x)
# # print(len(y))

# print("New Number is --> "+"{:0>d}".format(x))







# ------------------------------------------------------
# Other way

x = int(input("Enter the number --> "))
y = str(x)
print("New Number --> " + "0"*len(y) +  y)
