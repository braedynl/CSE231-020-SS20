def hello_none():   # No parameters
    print("Hello!")

def hello_single(name):    # Single parameter
    print("Hello " + name + "!")

def hello_multi(name1, name2, name3):   # Multiple parameters
    print("Hello " + name1 + ", " + name2 + " and " + name3 + "!")

hello_none()
hello_single("Bob")
hello_multi("Bob", "Steve", "Mark")

def get_roots(a, b, c):
    root1 = (-b + (b**2 - 4*a*c)**(1/2) ) / (2*a)
    root2 = (-b - (b**2 - 4*a*c)**(1/2) ) / (2*a)
    
    return root1, root2    # Multiple returns requires a ','
    
# Let's take for example x^2+5x+6
# in factored form, we have (x+3)(x+2)
# so we should expect our results to be x = -3, -2

# We can't have our computer factor (at least not
# easily), so let's use the quadratic formula

ret1, ret2 = get_roots(1, 5, 6)

print(ret1, ret2)