'''
CSE231 - Introduction to Programming I
Lab 1
Example Solution

Author: Braedyn Lettinga
'''

import math

# taking an A, B, and C coefficient through input(),
# note that you can nest functions inside one another like this!

A = float(input('\nEnter the coefficient A: '))
B = float(input('\nEnter the coefficient B: '))
C = float(input('\nEnter the coefficient C: '))

print('\nThe coefficients of the equation:\n')
print('  Coefficient A = ', A)
print('  Coefficient B = ', B)
print('  Coefficient C = ', C)

# the quadratic formula is (-b +/- sqrt(b^2 - 4ac)) / (2a),
# we simply need to translate this into Python syntax
root1 = (-B + math.sqrt((B**2) - 4*A*C)) / (2*A)
root2 = (-B - math.sqrt((B**2) - 4*A*C)) / (2*A)

print('\nThe roots of the equation:\n')
print('  Root #1 = ', round(root1, 3))
print('  Root #2 = ', round(root2, 3))