# Write a Python program to generate random even integers in a specific numerical range.

import random

for x in range(6):
    print(random.randrange(10, 100, 2), end=' ')
