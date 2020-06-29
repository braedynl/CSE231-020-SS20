
my_int = 123
my_float = 3.14

# We can tell it's a float now because of the trailing decimal
print( "my_int in float form:", float(my_int) )

# The value's trailing decimal values are stripped
print( "my_float in int form:", int(my_float) )


my_str = "hello world."
# We get a ValueError attempting to cast this particular string
# print( int(my_str) )

my_str_int = "123"    # But what if we have number values?

print()
print( int(my_str_int) )
print( float(my_str_int) )

# Booleans

print()
print( bool( 0 ) )    # int 0 is considered False
print( bool( 1 ) )    # int 1 is considered True

print()
print( bool(50) )    # In fact, any int that isn't 0 is considered True
print( bool(-50) )

print()
print( bool(0.0) )    # Likewise, a float 0.0 is False
print( bool(1.25) )   # All the same rules apply
print( bool(0.001) )

print()
print( bool("") )    # An empty string is considered False
print( bool("Hello") )    # Any string containing anything is True