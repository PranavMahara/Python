# Spam comment is 
# "make a lot of money"
# "make money"
# "buy now"
# "subsribe this"
# "click this"

# Write a program to detec these spams

text = input("Enter the text --> ")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam is True):  # or simply if(spam)
    print("This text is spam")

else:
    print("this text is not spam")