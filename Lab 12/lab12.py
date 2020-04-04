# Lab12 - Example Answer (Undocumented)
# Braedyn Lettinga

class Vector(object):

    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __mul__(self, a):
        if type(a) == float or type(a) == int:
            X = self.x * a
            Y = self.y * a
            return Vector(X, Y)

        else:
            dot = self.x * a.x + self.y * a.y
            return dot 
    
    def __rmul__(self, a):
        return self.__mul__(a)

    def __add__(self, other):
        X = self.x + other.x
        Y = self.y + other.y 
        return Vector(X, Y)

    def __sub__(self, other):
        X = self.x - other.x
        Y = self.y - other.y 
        return Vector(X, Y)

    def magnitude(self):
        return ( self.x**2 + self.y**2 )**(1/2)

    def unit(self):
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag

    def __str__(self):
        return "<{}, {}>".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()


v1 = Vector(1, 2)
print(v1)

print(v1.magnitude())

v1.unit()

print(v1)
print(v1.magnitude())

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print( v1 + v2 )
print( v2 - v1 )

print( v1 * 2 )
print( v1 * v2 )

print( 2 * v1 )

print( v1 == v2 )