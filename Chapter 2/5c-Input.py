a, b = int(input("Enter first  --> ")), int(input("Enter second num --> "))
print(a, b)

# print(values, sep = ' ', end = '\n', file = sys.stdout, flush = False)
# This is default which runs when we call run

# print("hi", "bye", "guy", sep = "#")  # sep is seperator
# File Arguement --> it determines where value is to be stored
# Flush --> It makes sure that the output parameter reach to the output screen
# flush() forces it to “flush” the buffer, 
# meaning that it will write everything in the buffer to the terminal, 
# even if normally it would wait before doing so. 
# import time
# a = 10
# b = 20
# print(a, b, flush=True)
# time.sleep(5)