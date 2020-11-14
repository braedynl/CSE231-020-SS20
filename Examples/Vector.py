'''
PROBLEM
-------

Create a class called "Vector" that simulates a two-dimensional, 
euclidean vector. 

https://en.wikipedia.org/wiki/Euclidean_vector

The class should have two attributes, 'x' and 'y', that is the x 
and y component of the vector instance, respectively. 

The class should have the following method functions:

__init__(self, x:float=0, y:float=0) -> None

    The constructor can take a pre-set x and y component
    through its parameters, and should set those as the
    attributes appropriately. These arguments default to
    0, the "zero vector". Ints and floats are allowed 
    (type-hinting a float implies compatability with int
    in most circumstances).

__str__(self) -> str

    Represents the vector as a string. The two components
    should be comma-separated and encapsulated by angled brackets.
    For example, Vector(1, 2) would be represented as '<1.00, 2.00>'.
    Component values should be rounded to the second decimal
    place, but kept un-rounded when handling other manipulations.
    This method allows compatability for str() and print().

__repr__(self) -> str

    Should be identical to __str__. Allows compatability with
    the repr() function.

add(self, other:Vector) -> Vector

    Returns the summation of two vectors, which is another vector.
    Vector addition is done component by component. Example:
    Let v1 = <1, 3> and v2 = <1, 3>. Then v1 + v2 = <2, 6>.

sub(self, other:Vector) -> Vector

    Returns the vector instance minus the passed-in vector. Like
    vector addition, vector subtraction is done component by
    component. Example:
    Let v1 = <1, 3> and v2 = <1, 3>. Then v1 - v2 = <0, 0>.

mul(self, a:float) -> Vector

    Multiplies the vector by a scalar value, and returns a new
    vector. The scalar value gets multiplied against each component
    individually. Example:
    Let v1 = <1, 3>. Then v1 * 2 = <2, 6>.

div(self, a:float) -> Vector

    Divides the vector by a scalar value, and returns a new vector.
    The scalar value gets divided through each component individually.
    Example:
    Let v1 = <2, 6>. Then v1 / 2 = <1, 3>.

dot(self, other:Vector) -> float

    Takes the dot product between two vectors. The dot product is
    the multiplicity of the two components between each vector, 
    summed together. Example:
    Let v1 = <1, 3> and v2 = <2, 5>. Then v1 dot v2 = 1*2 + 3*5 = 17

mag(self) -> float

    Returns the magnitude of the vector. The magnitude can be found
    by using the euclidean distance formula. Example:
    Let v1 = <0, 3>. Then mag(v) = sqrt(0^2 + 3^2) = sqrt(3^2) = 3

unit(self) -> Vector

    Returns the unit vector form of the vector as a new instance.
    The unit vector form can be calculated as the vector divided by
    its own magnitude. Example:
    Let v1 = <0, 3>. Then...
        unit(v1) = <0 / sqrt(0^2 + 3^2), 3 / sqrt(0^2 + 3^2)>
                 = <0 / sqrt(3^2), 3 / sqrt(3^2)>
                 = <0 / 3, 3 / 3>
                 = <0, 1>


EXAMPLE FUNCTIONALITY
---------------------

v = Vector()
print(v)  # <0.00, 0.00>

v1 = Vector(1, 3)
v2 = Vector(1, 3)

print(v1.x)  # 1
print(v1.y)  # 3

v3 = v1.add(v2)
print(v3)  # <2.00, 6.00>

v3 = v1.sub(v2)
print(v3)  # <0.00, 0.00>

v3 = v1.mul(2)
print(v3)  # <2.00, 6.00>

v3 = v1.div(3)
print(v3)  # <0.33, 1.00>

v1_dot_v2 = v1.dot(v2)  # 1*1 + 3*3 = 10
print(v1_dot_v2)  # 10

# mag(v1) = sqrt(1^2 + 3^2) = 3.1622776601683795
print(v1.mag())  # 3.1622776601683795
print(v2.mag())  # 3.1622776601683795

v = Vector(0, 3)

unit_v = v.unit()
print(unit_v)  # <0.00, 1.00>
'''

from __future__ import annotations
from math import sqrt

class Vector():

    def __init__(self, x:float=0, y:float=0):
        # 'x' and 'y' refer to the parameters being passed into the constructor.
        # 'self.x' and 'self.y' are data members, so they can be named similarly
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '<{:.2f}, {:.2f}>'.format(self.x, self.y)
    
    __repr__ = __str__  # you can make two methods identical by doing this

    def add(self, other:Vector) -> Vector:
        new_x = self.x + other.x     # 'other' is just another Vector instance! we can access
        new_y = self.y + other.y     # all of its info to do these mathematical operations
        return Vector(new_x, new_y)
    
    def sub(self, other:Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def mul(self, a:float) -> Vector:
        new_x = self.x * a           # if we assume the incoming argument is of a different type, 
        new_y = self.y * a           # then we of course need to adjust our method's behavior
        return Vector(new_x, new_y)

    def div(self, a:float) -> Vector:
        new_x = self.x / a
        new_y = self.y / a
        return Vector(new_x, new_y)

    def dot(self, other:Vector) -> float:
        # the dot product does NOT return a new vector, it's a numeric
        # value. (in mathematics, this value is used as a sort of guage
        # for how perpendicular one vector is to another)
        return (self.x * other.x) + (self.y * other.y)
    
    def mag(self) -> float:
        # similar deal down here. (the magnitude represents the length of the
        # vector, it uses the euclidean distance formula since the vector could
        # be pointing in a direction other than along the axes)
        return sqrt(self.x**2 + self.y**2)
    
    def unit(self) -> Vector:
        m = self.mag()               # we can call our own methods inside other methods!
        new_x = self.x / m           # reuse what you've written as much as possible!
        new_y = self.y / m
        return Vector(new_x, new_y)


v = Vector()
print(v)  # <0.00, 0.00>

v1 = Vector(1, 3)
v2 = Vector(1, 3)

print(v1.x)  # 1
print(v1.y)  # 3

v3 = v1.add(v2)
print(v3)  # <2.00, 6.00>

v3 = v1.sub(v2)
print(v3)  # <0.00, 0.00>

v3 = v1.mul(2)
print(v3)  # <2.00, 6.00>

v3 = v1.div(3)
print(v3)  # <0.33, 1.00>

v1_dot_v2 = v1.dot(v2)  # 1*1 + 3*3 = 10
print(v1_dot_v2)  # 10

# mag(v1) = sqrt(1^2 + 3^2) = 3.1622776601683795
print(v1.mag())  # 3.1622776601683795
print(v2.mag())  # 3.1622776601683795

v = Vector(0, 3)

unit_v = v.unit()
print(unit_v)  # <0.00, 1.00>


'''
Example Application Problem (just for fun)

Eva and John are simultaneously pushing a crate on a frictionless floor. 
Eva pushes the crate directly southward with a force of 300 N, while John 
is pushing the crate directly eastward with a force of 400 N.

1. What is the resultant force?
2. What direction is the crate being pushed in?

Rudimentary diagram (let 'C' represent the crate):

               John; 400 N
            C -------------->
            |
            |
 Eva; 300 N |
            |
            |
            v
'''

# with no changes to our reference frame (assuming up/down
# is along the y-axis and left/right is along the x-axis),
# we can represent, and find the answers to these questions
# as follows:

# Eva pushes down the negative y-axis at 300 N, no x component
eva = Vector(0, -300)

# John pushes to the right, along the x-axis at 400 N, no y component
john = Vector(400, 0)

res = eva.add(john)  # we add their force vectors together

print(res)  # <400.00, -300.00>

# the resultant force vector has a positive x component,
# and a negative y component. if we think about where that is
# on the xy-plane, that'd put us in the 4th quadrant, meaning
# that we're ultimately pushing the crate to the south-east

'''
               John; 400 N
            C -------------->
            | \
            |   \
 Eva; 300 N |     \  resultant force
            |       \
            |         \
            v           \
'''

# we can then find the total force being exerted through the
# magnitude of the resultant vector

# sqrt(400^2 + (-300)^2) = sqrt(160000 + 90000) = sqrt(250000) = 500
print(res.mag())  # 500.00

# John and Eva are pushing the crate to the south-east at 500 N!
'''
               John; 400 N
            C -------------->
            | \
            |   \
 Eva; 300 N |     \  resultant force; 500 N
            |       \
            |         \
            v           \
'''
