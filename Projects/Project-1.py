# Write a Python program that accepts a string and calculate the number of digits and letters.

s = input("Enter the string --> ")
dig = 0
let = 0
for i in range (len(s)):
    if((s[i]>='A' and s[i]<='Z') or (s[i]>='a' and s[i]<='z')):
        let = let + 1
    
    else:
        dig = dig + 1

print("The number of digits are ", str(dig), "and the number of letters are ", str(let))


# Other Way
# s = input("Enter the string --> ")
# dig = 0
# let = 0
# for i in s:
#     if(i.isdigit()):
#         dig = dig + 1
    
#     else:
#         let = let + 1

# print("The number of digits are ", str(dig), "and the number of letters are ", str(let))
