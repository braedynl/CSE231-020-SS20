from Vector import Vector
from math import acos

'''
This example is associated with a video I did on classes:
https://www.youtube.com/watch?v=gEd5WZ4LwuQ
(best if watched at higher speed!)

With your vector class, develop two functions:

dot_product(a, b)    # Calculates the dot product of two Vector()s, a and b
vector_angle(a, b)    # Calculates the angle between two Vector()s, a and b
'''

def dot_product(a:Vector, b:Vector):
    return a.i*b.i + a.j*b.j

def vector_angle(a:Vector, b:Vector):
    return acos( dot_product(a, b) / (a.magnitude() * b.magnitude()) )
    
    
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print( dot_product(v1, v2) )
print( vector_angle(v1, v2) )
