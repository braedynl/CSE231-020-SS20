
my_int = 1    # type: int, no quotes

my_float = 3.5    # type: float, no quotes, always has a decimal point

# Ints and floats can be negative, and have a lot of operations that
# work with them exactly as you would expect. We'll get to those in 
# a second here.

my_string = "Hello, world!"    # type: string, has quotes, can be double or single

# We also showed you some default Python functions. We'll be getting
# to how functions work at a later date, but for now, all you need
# to know is that the print() function can take any type as a 
# parameter and display it in the console.

print( my_int )
print( my_float )
print( my_string )

# There's also a type() function in the default Python library.
# type() takes any kind of object as a parameter and deciphers 
# the of that object.

print( type(my_int) )    # The variable my_int holds the value: 1, and has type: int
print( type(my_float) )    # likewise with the float and string
print( type(my_string) )

# Bools

# Boolean variables are something we'll be talking about a bit later,
# but for right now, just know that they hold one of two states: True or False.

bool_true = True    # Declared with title-casing
bool_false = False