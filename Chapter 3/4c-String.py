a = "Arjun Is Great"

print(a.lower())
print(a.upper())

# Reversing strings -->
# METHOD - 1
def reverse(string):
    string = string[::-1]
    return string
  
s = "ARJUN"
  
print ("The reversed string s : ", end = "")
print(reverse(s))

# METHOD - 2
def reverse(string):
    string = "".join(reversed(string))
    return string
  
s = "ARJUN"

print ("The reversed string is : ", end = "")
print (reverse(s))

# METHOD - 3
def reverse(s):
  str = ""
  for i in s:
    # print(i)
    str = i + str  # str + i se seedha aajega
  return str
  
s = "ARJUN"

print ("The reversed string is : ",end = "")
print (reverse(s))

# METHOD - 4
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
  
s = "ARJUN"

print ("The reversed string is : ", end = "")
print (reverse(s))