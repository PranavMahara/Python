file = open("s.txt", "w")

fruits = ["Apple\n", "Orange\n", "Grapes\n", "Watermelon"]
file.writelines(fruits)
file.close()

file = open("s.txt", "a")
file.write("\nGuava")
file.close()
