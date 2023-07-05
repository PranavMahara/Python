myDict = {
    "Fast": "In a Quick Manner",
    "Arjun": "A Coder",
    "Marks": [1, 2, 5], 
    "AnotherDict": {'Arjunn':'Player'},
    1 : 2
}

print(myDict.get("Arjun")) # Prints value associated with key "Arjun"
print(myDict["Arjun"]) # Prints value associated with key "Arjun"

# The Difference between .get and []
print(myDict.get("Arjun2")) # --> Returns None as Arjun2 is not present in the dictionary
# print(myDict["Arjun2"]) # --> Throws an error as Arjun2 is not present in the dictionary

# Making Dictionary with the help of dict() constructor

person = dict([("name", "Mark"), ("country", "USA"), ("telephone", 1178)])
print(person)