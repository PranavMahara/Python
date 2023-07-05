# Copy a Dictioanry

dict1 = {'Jessa': 70, 'Emma': 55}
# Copy dictionary using copy() method
dict2 = dict1.copy()
# printing the new dictionary
print(dict2)
# output {'Jessa': 70, 'Emma': 55}
# Copy dictionary using dict() constructor
dict3 = dict(dict1)
print(dict3)
# output {'Jessa': 70, 'Emma': 55}
# Copy dictionary using the output of items() methods
dict4 = dict(dict1.items())
print(dict4)
# output {'Jessa': 70, 'Emma': 55}

# Copy Using Assignment Operator
dict1 = {'Jessa': 70, 'Emma': 55}
# Copy dictionary using assignment = operator
dict2 = dict1
# modify dict2
dict2.update({'Jessa': 90})
print(dict2)
# Output {'Jessa': 90, 'Emma': 55}
print(dict1)
# Output {'Jessa': 90, 'Emma': 55}