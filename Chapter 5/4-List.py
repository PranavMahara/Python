list = [1, 2, 3, 4, 5, 6]
dict = {x:x**x for x in list if (x%2==0)}
print(dict)