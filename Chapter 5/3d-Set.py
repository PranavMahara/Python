book_set = {"Harry Potter", "Angels and Demons", "Atlas Shrugged"}
for book in book_set:
    print(book)

if 'Harry Potter' in book_set:
    print("Book exists in the book set")
else:
    print("Book doesn't exist in the book set")

print(len(book_set))

# Updating elements in set
book_set.add('The God of Small Things')
book_set.update(('Atlas Shrugged', 'Ulysses'))
print(book_set)