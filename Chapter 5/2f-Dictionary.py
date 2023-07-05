student = { "name":"aaa", 
            "regno":"345"
        }

mark = {   "m1":100, 
            "m2":89, 
            "m3":90
        }
student.update(mark)
print(student)
student.dict(mark)
print(student)
student1 = {**student, **mark}
print(student1)
# student2 = student.copy()
# print(student2)
# student3 = {"name":"aaa", "class":"III", "marks":mark}
# print(student3["marks"]["m2"])

# for i in student3:
#     print(student3[i])
#     if(i=="marks"):
#         for j in mark:
#             print(mark[j])