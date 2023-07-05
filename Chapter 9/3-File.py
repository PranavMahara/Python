f = open("another.txt", "r")
# f.write("Hello this is alien WORLD")
# f.seek(5)
# print(f.tell())
# print(f.read())
# print(f.tell())


print(f.read())
print()
print("Filename is ", f.name)
print("Filemode is ", f.mode)
print("File-encoding is ", f.encoding)
print("File-closed is ", f.closed)
print("File-Readable is ", f.readable())
print("File-Writable is ", f.writable())
print("File number is ", f.fileno())
f.close()

# To Rename a file
# import os
# os.rename(“test.txt”, “test1.txt”)

# To remove a file(DELETE)
# import os
# os.remove(“test.txt”)
