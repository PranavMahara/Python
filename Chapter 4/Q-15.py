# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

def new_string(str):
    for i in range(len(str)):
        if(str[i]=='I' and str[i+1]=="s"):
            flag = 1
        
    if(flag==1):
            return str

    else:
        return ("Is" + str)

print(new_string("Array"))
print(new_string("EmIspty"))