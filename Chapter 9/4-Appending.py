f = open("another.txt", "a")
f.write("9877023350")

f.close()
f = open("another.txt", "r")
print(f.read())
f.close()
