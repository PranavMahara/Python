# A	marketing	company	has	branch	in	a	set	of	cities	‘S’.	The	company	sends	three	of
# their	 salesmen to	 various	 cities	 in	 set	 ‘S’.	 In	 the	 middle	 of	 the	 year,	 help	 the
# manager	 to	 find	 out	 the	 cities	 that	are	already	 visited	 by	 the	 salesmen and	 the
# cities	that	are	yet	to	be	visited.

cities = {"New Delhi", "Ropar", "Mumbai", "Hyderabad",
          "Bangalore", "Surat", "Jaipur", "Kolkata"}

salesman1 = ["Mumbai", "Jaipur", "New Delhi"]
salesman2 = ["Bangalore", "Mumbai", "Kolkata"]
salesman3 = ["Jaipur", "New Delhi", "Mumbai", "Surat"]

visited = set()

for city in salesman1:
    visited.add(city)

for city in salesman2:
    visited.add(city)

for city in salesman3:
    visited.add(city)

print("These are the visited cities:")
print(visited)
print()
print("The following cities are not visited yet:")
print(cities.difference(visited))
