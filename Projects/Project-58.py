# Wind - chill INDEX

v = float(input("Enter v --> "))
t = float(input("Enter t --> "))

k = 13.12 + 0.6215*t - 11.37*(v**0.16) + 0.3965*(v**0.16)
print(k)