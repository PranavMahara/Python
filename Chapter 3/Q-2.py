letter = ''' Dear <|NAME|>, 
Greetings from THE coding house. I am happy to tell you about your selection
You are selected!
Thanks and Regards
Date : <|DATE|>
'''

name = input("Enter your name --> ")
date = input("Enter Date --> ")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
