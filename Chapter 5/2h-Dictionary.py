# Write a program to store the name of the players against each of a 20-20 cricket team. 
# The program should print the name of the players given the team name


T1 = {}
T2 = {}
print ("Team 1 --> ")
for i in range (1,12):
    print ("Enter player's number", i)
    T1[i] = input ()
    
print ("Team 2 --> ")

for j in range (1, 12):
    print ("Enter player's number", j)
    T2[j] = input ()
    
print("Team 1")
print(T1)
print ("Team 2")
print (T2)