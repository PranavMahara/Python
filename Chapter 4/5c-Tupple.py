tuple1 = ("aaa")
print(type(tuple1))

tuple2 = (56)
print(type(tuple2))

tuple3 = ("aaa", 56)
print(type(tuple3))

tuple4 = ()
print(type(tuple4))

print(len(tuple3))


t = ((1, 2, 3), (4, 5, 6))
for i in t:
    for j in i:
        print(j, end = " ")
    print()