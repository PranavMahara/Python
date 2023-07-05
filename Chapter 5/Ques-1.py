# Dictionary with english to hindi

Dict = {
    "Pankha" : "FAN", 
    "Dabba" : "Box",
    "Bro" : "BHAI",
}

print("Options are ", Dict.keys())
a = input("Enter the word --> ")
print("The meaning is", Dict.get(a))