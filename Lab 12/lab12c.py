# Lab12 - Example Answer (Documented)
# Braedyn Lettinga

class Vector(object):

    # The Vector() object will have two attributes
    # associated with itself, an x and a y value
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y

    # To test if two vectors are equal, we can check
    # if both have the same x and y values
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    # `a` here can either be a Vector() or an int/float,
    # which is why I gave it an ambiguous name. If it's
    # an int/float, we'll scale the vector components
    # and return a new vector.

    # If `a` is another Vector() instance, we calculate
    # the dot product instead, which returns a discrete value
    def __mul__(self, a):
        if type(a) == float or type(a) == int:
            X = self.x * a
            Y = self.y * a
            return Vector(X, Y)

        else:
            dot = self.x * a.x + self.y * a.y
            return dot 
    
    # __rmul__() is the inverse of __mul__(), where for
    # __mul__() you would have some class C: C * 2, 
    # __rmul__() operates when you do the reverse,
    # so something along the lines of 2 * C. 

    # We can simply call __mul__() from __rmul__() since
    # it's the same operation, but just in a different order
    def __rmul__(self, a):
        return self.__mul__(a)

    # To add vectors, it's done component-wise. We're assuming
    # that `other` here is going to be another Vector() instance
    def __add__(self, other):
        X = self.x + other.x
        Y = self.y + other.y 
        return Vector(X, Y)

    # Subtraction is essentially the same
    def __sub__(self, other):
        X = self.x - other.x
        Y = self.y - other.y 
        return Vector(X, Y)

    # The magnitude is a derivation of the pythagorean theorem,
    # where you take the x and y components squared, sum them and
    # raise to the (1/2) power (or take the square of the result)
    def magnitude(self):
        return ( self.x**2 + self.y**2 )**(1/2)

    # Creating a unit vector is done by dividing the components by
    # its own magnitude. Importantly, we're storing this in another
    # variable. 
    # If we were to instead say:
    # self.x /= self.magnitude()
    # self.y /= self.magnitude()
    # The x component of the vector would be changed to coincide with
    # the magnitude that the vector had AT THAT TIME. When we run
    # `self.y /= self.magnitude()` after, it would be recalculating
    # the magnitude with the ALREADY CHANGED x component, since
    # it's changing ITSELF. 
    def unit(self):
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag

    # I'm using the angled bracket notation here since it looks cool
    def __str__(self):
        return "<{}, {}>".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()


v1 = Vector(1, 2)    # Testing instantiation and __str__()
print(v1)

print(v1.magnitude())    # .magnitude()

v1.unit()    # .unit()
print(v1)
print(v1.magnitude())

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print( v1 + v2 )    # .__add__()
print( v2 - v1 )    # .__sub__()

print( v1 * 2 )    # .__mul__()
print( v1 * v2 )    # .__mul__()

print( 2 * v1 )    # .__rmul__()

print( v1 == v2 )    # .__eq__()