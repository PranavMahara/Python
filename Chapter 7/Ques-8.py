# Write a program to modify all elements in a list using list comprhension if number is odd find cube of those

print("Arjun Malhotra, 21BBS0110")

a = [5, 6, 7]
a = [i**3 for i in a if i%2!=0]

print(a)