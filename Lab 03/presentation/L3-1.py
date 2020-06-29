hello_str = "Hello World"

# .lower() returns a copy, original variable is not modified
hello_str.lower()
print(hello_str)    # Prints "Hello World"

# hello_str has now been modified since we re-assigned
hello_str = hello_str.lower()
print(hello_str)    # Prints "hello world"


my_str = "This is my cool string"

# Gives the index of the first character within the
# substring search, no matter the search type
print( my_str.find("is") )
print( my_str.rfind("is") )

# .replace() returns a copy like .lower()/.upper()
my_str.replace("cool", "rad")    # So my_str is not affected
print(my_str)

my_str = my_str.replace("cool", "rad")
print(my_str)    # Prints "This is my rad string"