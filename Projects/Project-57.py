# Write a Python program to convert a float to ratio.

from fractions import Fraction
value = float(input("Enter the number --> "))
print(Fraction(value).limit_denominator())