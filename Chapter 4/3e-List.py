# deep copy
# shallow copy

a = "HelloATG"

def func(a):
    count = 0
    for i in a:
        if(i=='l'):
            count = count + 1
    return count

print(func(a))