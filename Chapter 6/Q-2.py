# Marks of 3 subject, each must have 33 percent to pass and total percent should be greater than 40

sub1 = int(input("Enter subject 1 marks --> "))
sub2 = int(input("Enter subject 2 marks --> "))
sub3 = int(input("Enter subject 2 marks --> "))

if(sub1<33 or sub2<33 or sub3<<33):
    print("You are fail")

elif((sub1+sub2+sub3)/3<40):
    print("You are fail")

else:
    print("Pass")
