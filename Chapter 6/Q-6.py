# Write to check whether arjun/ArjUn or any other possible combination is there in string or not

s = input("Enter line --> ")
bool = True

if((s[0]=='a' or s[0]=='A') and (s[1]=='r' or s[1]=='R') and (s[2]=='j' or s[2]=='J') and (s[3]=='u' or s[3]=='U') and (s[4]=='n' or s[4]=='N')):
    bool = False

if(bool is True):
    print("WRONG")

else:
    print("RIGHT")