myDict = {
    "Fast": "In a Quick Manner",
    "Arjun": "A Coder",
    "Marks": [1, 2, 5], 
    "AnotherDict": {'Arjunn':'Player'},
    1 : 2
}
print(myDict[1])
print(myDict.keys())
print(type(myDict.keys())) # you can convert this to list and tuple also --> Typecast, By default it is dict_keys

print(list(myDict.keys()))
print(list(myDict.values()))

print(myDict.values()) # Prints the keys of the dictionary
print(myDict.items()) # Prints the  (key, value) for all contents of the dictionary

print(myDict)
updateDict = {
    "ATG": "Friend",
    "MTG": "Dost",
    "Arjun": "A Boy"
}

myDict.update(updateDict) # Updates the dictionary by adding key-value pairs

myDict["Bro"]=69
print(myDict)