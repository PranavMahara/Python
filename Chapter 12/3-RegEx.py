import re

pattern = "[\w]{4}"
test_string = 'Look, Look at the brown foxes!They jump over the lazy dogs'

result = re.finditer(pattern, test_string)
for i in result:
    print(i) 