person_details = {"name": "Jessa", "country": "USA", "telephone": 1178}
# set default value if key doesn't exists
person_details.setdefault('state', 'Texas')
# key doesn't exists and value not mentioned. default None
person_details.setdefault("zip")
# key exists and value mentioned. doesn't change value
person_details.setdefault('country', 'Canada')
# Display dictionary
for key, value in person_details.items():
    print(key, ':', value)

# As seen in the above example the value of the setdefault() method has 
# no effect on the ‘country’ as the key already exists