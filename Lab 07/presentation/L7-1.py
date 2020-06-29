# The id() function gives you the object's memory location.
# The `is` keyword checks to see if two objects have the 
# same location in memory. 

# Here, we're using ints. Ints are IMMUTABLE.

x = 10

y = x

print( "Address of x:", id(x), "x =", x )
print( "Address of y:", id(y), "y =", y )
print( "x is y:", x is y )

y += 1

print( "\nAddress of x:", id(x), "x =", x )
print( "Address of y:", id(y), "y =", y )
print( "x is y:", x is y )

##########################################################

# Here, we're using lists. Lists are MUTABLE.

x = [1, 2, 3, 4]

y = x

print( "\nAddress of x:", id(x), "x =", x )
print( "Address of y:", id(y), "y =", y )
print( "x is y:", x is y )

y.append(5)

print( "\nAddress of x:", id(x), "x =", x )
print( "Address of y:", id(y), "y =", y )
print( "x is y:", x is y )