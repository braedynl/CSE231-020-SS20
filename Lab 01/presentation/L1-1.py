
my_int = 1    # int, no quotes

my_float = 3.5    # float, no quotes, always has a decimal point

# Ints and floats can be negative, and have a lot of operations that
# work with them exactly as you would expect. We'll get to those in a bit.

my_string = "Hello, world!"    # string, has quotes, can be double or single quotes

# We also showed you some default Python functions. We'll be getting
# to know how functions work at a later date, but for now, all you need
# to know is that the print() function can take any type as a 
# parameter and display it to the console.

print( my_int )
print( my_float )
print( my_string )

# There's also a type() function in the default Python library.
# It takes any kind of object as a parameter and deciphers the type

print( type(my_int) )    # The variable my_int holds the value: 1, and has type: int
print( type(my_float) )    # likewise with the float and string
print( type(my_string) )

# Bools

# Booleans are something we'll be talking much more about later.
# For right now, just know that they hold one of two states: True or False.

bool_true = True    # Declared with title-casing
bool_false = False