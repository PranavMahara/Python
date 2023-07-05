# Display course titlebased on course code.If the user enters CSE1007then display Java Programming , 
# If the user enters CBS1011then display  programmingin python and for any other input display “Invalid input”.

print("ARJUN MALHOTRA 21BBS0110")
grades = input("Enter the Course Code --> ")  

if(grades == "CSE1007"):
    print("Java Programming")

elif(grades == "CBS1011"):
    print("Programming in Python")

else:
    print("Invalid Input")
