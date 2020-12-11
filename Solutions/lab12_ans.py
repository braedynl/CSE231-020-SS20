'''
CSE231 - Introduction to Programming I
Lab 12
Example Solution

Author: Braedyn Lettinga
'''

from __future__ import annotations  # allows self-referencing type-hints
from typing import Union  # used to represent a set of allowed types
from math import sqrt

class Vector:

    def __init__(self, x:float=0, y:float=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '<{}, {}>'.format(self.x, self.y)

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self, other:Vector) -> Vector:  # overload for: Vector + Vector
        new_x = self.x + other.x
        new_y = self.y + other.y 
        return Vector(new_x, new_y)

    def __sub__(self, other:Vector) -> Vector:  # overload for: Vector - Vector
        new_x = self.x - other.x
        new_y = self.y - other.y 
        return Vector(new_x, new_y)

    # can be invoked with a scalar value (float) OR another Vector instance.
    # Vector * int -> Vector
    # OR
    # Vector * Vector -> float
    def __mul__(self, other:Union[float, Vector]) -> Union[float, Vector]:

        # checks if `other` param is an int/float
        # if true, scalar multiply
        if isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)

        # otherwise, `other` must be a Vector instance.
        # we take the dot product in this circumstance
        else:
            return self.x * other.x + self.y * other.y

    # invoked in cases of:
    # int * Vector
    # since int's __mul__() method doesn't support user-defined classes
    def __rmul__(self, other:Union[float, Vector]) -> Union[float, Vector]:
        return self.__mul__(other)

    def __eq__(self, other:Vector) -> bool:  # overload for: Vector == Vector
        return self.x == other.x and self.y == other.y

    def magnitude(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    # notice how we're changing the data attributes without returning back to
    # the caller. we're making an in-place method here!
    def unit(self) -> None:
        mag = self.magnitude()  # take our own magnitude
        if mag == 0:
            raise ValueError('Cannot convert zero vector to a unit vector')
        self.x /= mag   # ... and divide through the components
        self.y /= mag


v1 = Vector(1, 2)
print(v1)
print(v1.magnitude())

v1.unit()  # we made this an in-place method, remember!
print(v1)
print(v1.magnitude())

v2 = Vector(3, 4)

print(v1 + v2)   # invokes __add__()  ... mapping: v1.__add__(v2)
print(v2 - v1)   # invokes __sub__()  ... mapping: v2.__sub__(v1)
print(v1 * 2)    # invokes __mul__()  ... mapping: v1.__mul__(2)
print(2 * v1)    # invokes __rmul__() ... mapping: v1.__rmul__(2)
print(v1 * v2)   # invokes __mul__()  ... mapping: v1.__mul__(v2)
print(v1 == v2)  # invokes __eq__()   ... mapping: v1.__eq__(v2)