# A	super	market	plan	to	conduct	a	surprise	cum	lucky	winner	contest	in	a	different
# way.	 They	 decide	 to	 give	 a	 prize	 for	 two	 customers	 with	maximum	 number	 of
# items	in	common	in	their	shopping	list.	Write	a	program	to	identify	common	items
# from	the	shopping	list	of	two	customers.	Prepare	the	common	items	list	as	read
# only

n = int(input("Enter n --> "))

l = [[0 for j in range(n)] for i in range(n)]
for i in range(0, n):
    stt = input("Items purchased by customer "+ str(i+1) + " --> ")
    s = set(stt.split())
    l[i] = s
maxl = 0
Customer1 = 0
Customer2 = 0

for i in range(0, n):
    print(l[i])

for i in range(0, n-1):
    for j in range(i+1, n):
        k = l[i] & l[j]
        if(len(k) > maxl):
            Customer1 = i
            Customer2 = j
            max1 = len(k)
print(Customer1)
print(Customer2)
print(tuple(l[Customer1] & l[Customer2]))
