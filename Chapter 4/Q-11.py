a = ['1 ', "bottle ", 'beer'] # Make sure all have same data type
print(''.join(a))

# Other way
b = ""
for i in a:
    b = b + i

print(b)