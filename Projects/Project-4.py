# Write a Python program to convert month name to a number of days.

month = input("Enter the month --> ")

if(month == "February"):
    print("No. of days: 28/29 days")

elif(month == "April", "June", "September", "November"): # month_name in ("April", "June", "September", "November"):  <-- OTHER WAY
    print("No. of days: 30 days")

elif(month == "January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 day")