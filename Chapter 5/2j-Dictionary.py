person = {'name': 'Jessa',
          'country': 'USA',
          'telephone': 1178,
          'weight': 50,
          'height': 6
          }

deleted_item = person.popitem()
print(deleted_item)

deleted_item = person.pop('telephone')
print(deleted_item)

del person['weight']
# display updated dictionary
print(person)

# Checking if key exists
key_name = 'country'
if key_name in person.keys():
    print("country name is", person[key_name])
else:
    print("Key not found")

val_name = 'USA'
