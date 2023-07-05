# Python Program to add, subtract, multiply and division of complex number
# Write a Python program to get the length and the angle of a complex number.

comp = complex(2, 5)
com = complex(1, 3)

print("Addition of two complex numbers : ",comp+com)
print("Subtraction of two complex numbers : ",comp-com)
print("Multiplication of two complex numbers : ",comp*com)
print("Division of two complex numbers : ",comp/com)

import cmath
#length of a complex number. 
print("Length of a complex number: ", abs(comp))
# gets angle. return in radians, between  [-π, π]
print("Complex number Angle: ",cmath.phase(0+1j) )