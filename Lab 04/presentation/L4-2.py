# x = 10
#
# def increment():
#   x += 1
# 
# ^^ Non-working code

x = 10

def increment(number):  
    number += 1
    return number

# If we want to change a global variable,
# we have to do it like this
x = increment(x)