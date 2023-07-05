myDict = {
    "Fast": "In a Quick Manner",
    "Arjun": "A Coder",
    "Marks": [1, 2, 5], 
    "AnotherDict": {'Arjunn':'Player'} # Another dictionary in a dictionary
}

print(myDict["Fast"]) # ' ' bhi kar sakte ho  " " aese bhi kar sakte ho
print(myDict['Arjun'])
print(myDict['Marks'])
print(myDict['AnotherDict']['Arjunn'])

myDict['Marks'] = [45, 60]   # Change ho jaega