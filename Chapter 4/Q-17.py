s = 'aaa', 10, 30, 40, '***', ['first', 'ssecond', 'third']
print(s[:-3:-1])
print(s[-1:-3:-1])
# print(s[-3:1:-1])
s2 = [i*2 for i in s[5]]
print(s2, type(s2), type(s), s)
