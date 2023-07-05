# Write a python program to create a tupple with numbers and print all elements 
# Add an element "hello" to the tuple

print("Arjun Malhotra, 21BBS0110")

n = int(input("Enter the number of elements in the tuple --> "))
a = ()
for i in range (n):
    ele = int(input("Enter element --> "))
    a = a + (ele, )

print(a)

# other way!
# for i in a:
#     print(i, end = " ")

a = a + ("hello", )
print(a)