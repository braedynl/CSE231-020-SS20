from math import sqrt

'''
This example is associated with a video I did on classes:
https://www.youtube.com/watch?v=gEd5WZ4LwuQ

Create a class called Vector() that has attributes: "i" and "j".
It has a constructor with two int/float parameters, i and j. 
The default value of i should be 1, and the default for j should be 0
The str method should return a string in the format "<{i}, {j}>"
Lastly, it should have the following methods:

.scale(a)    # Will multiply the components by the scalar `a`
.magnitude()    # Will return the magnitude of the vector
'''

class Vector( object ):

    def __init__(self, i=1, j=0):
        self.i = i
        self.j = j

    def scale(self, a):
        self.i *= a 
        self.j *= a

    def magnitude(self):
        return sqrt( self.i**2 + self.j**2 )

    def __str__(self):
        return "<{}, {}>".format(self.i, self.j)


if __name__ == "__main__":
    
    v = Vector(2, 3)
    print(v)
    print(v.magnitude())

    v.scale(2)
    print(v)
    print(v.magnitude())