a = {
    9 : 13, 
    2 : 22,
    5 : 31
}

result = 1
res = 1

for i in a:
    res = res*i
    result = result*a[i]

print("ITEMS MULTIPLY --> ", result)
print("KEYS MULTIPLY --> ", res)