
# Prints the message "Type something: ", pauses the program,
# and stores the user-typed text into our variable, ret
ret = input("Type something: ")

print( "You typed:", ret )
print()


number = input("Give me a number to square: ")

# We have to cast our input from console to type: int in order to use our mathematical operations
number = int(number)

print( number**2 )

'''
Assigning a variable to a function-call is taking the function's
returned value. This is a topic we'll be getting into a lot more later.
'''