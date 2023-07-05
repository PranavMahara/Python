f = open("sample.txt", "r") # By default the mode is r in case you dont mention the mode
# data = f.read() # data ki jagah kuch  bhi likh sakte ho
data = f.read(15) # Reads the first 5 characters from the file
print(data)
f.close()