#String Slicing
name = "Arjun"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4]) 
# print(name[5]) error aaega
# A=0, R=1, J=2, U=3, N=4

# name[3] = "d" yeh nahi hoga,  Does not Workn It will not change

print(name[0:3]) #We will see 0,1,2 we will see and 3 is not included
print(name[1:4]) 
print(name[:3]) # Automatically 0 se start kardega
print(name[1:]) # Automatically end tak ho jaega in terminal

#Negative Indices
print(name[:-4]) # A=-5,R=-4,J=-3,U=-2,N=-1
print(name[-4:-1]) # A=-5,R=-4,J=-3,U=-2,N=-1
print(name[-1:-4]) # A=-5,R=-4,J=-3,U=-2,N=-1