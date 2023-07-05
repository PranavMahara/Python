# Read the marks of three subjects and credits of the respective course and compute the following
# (i)compute the grades for each course (ii)display CGPA.

Marks = list()
Credits = list()
Grades = [None, None, None]
GradeList = {'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'F': 0}

for i in range(3):
    mark = int(input("Enter marks for course {0}: ".format(i+1)))
    Marks.append(mark)
    credit = int(input("Enter credits for course {0}: ".format(i+1)))
    Credits.append(credit)

for i in range(3):
    m = Marks[i]
    if (100>=m>=90):
        Grades[i] = 'S'
    elif (90>m>=80):
        Grades[i] = 'A'
    elif (80>m>=70):
        Grades[i] = 'B'
    elif (70>m>=60):
        Grades[i] = 'C'
    elif (60>m>=50):
        Grades[i] = 'D'
    else:
        Grades[i] = 'F'
        
    print("Grade for course {0}: {1}".format(i+1, Grades[i]))


tots = 0
tc = 0

for i in range(3):
    tots += int(GradeList[Grades[i]])*Credits[i]
    tc += Credits[i]
    cgpa = tots/tc

print("CGPA -->  ", cgpa)