# Write a Python program to remove the characters which have odd index values of a given string.

s = input("Enter the string --> ")
print(s[1::2])


print("-----------------")
# OTHER WAY
def odd(str):
    result = "" 
    for i in range (len(str)):
        if (i % 2 == 0):
            result = result + str[i]
        
    return result

print(odd("abcdef"))
