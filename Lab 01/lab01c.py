# Lab01 - Example Answer (Documented)
# Braedyn Lettinga

import math    # math module import to use math.sqrt()

'''Taking an A, B, and C coefficient through input().
Note that you can nest functions inside one another like this.'''

A = float( input( "\nEnter the coefficient A: " ) )
B = float( input( "\nEnter the coefficient B: " ) )
C = float( input( "\nEnter the coefficient C: " ) )

'''The '\n' character indicates a new-line. So this
print() statement displays "The coefficients of the
equation:" on a separate line, with an empty newline after.'''

print( "\nThe coefficients of the equation:\n" )
print( "  Coefficient A = ", A )
print( "  Coefficient B = ", B )
print( "  Coefficient C = ", C )

# The quadratic formula (in pseudocode): (-b +/- sqrt(b^2 - 4ac))/(2a)
root1 = (-B + math.sqrt((B**2) - 4 * A * C))/(2 * A)
root2 = (-B - math.sqrt((B**2) - 4 * A * C))/(2 * A)

# Another way of doing it without the math module would be raising to 1/2 power, since x^(1/2) = sqrt(x)
# (-B + (B**2 - 4*A*C)**(1/2) ) / (2*A)
# (-B - (B**2 - 4*A*C)**(1/2) ) / (2*A)

'''A general rule of thumb is to always round your numbers
at the end of calculations. This is a common problem in a lot
CSE projects. Keep your numbers un-rounded until you display it.'''

print( "\nThe roots of the equation:\n" )
print( "  Root #1 = ", round(root1, 3) ) 
print( "  Root #2 = ", round(root2, 3) )
