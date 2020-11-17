'''
PROBLEM
-------

Create a class called "Fraction" that performs fractional 
operations using two integer values, 'num' and 'den', that 
represent the numerator and denominator of the fraction, 
respectively.

The functions gcd() and lcm() are given to you.
- gcd() calculates the greatest common divisor of two integer values.
- lcm() calculates the least common multiple of two integer values.

The class should have the following methods:

__init__(self, num:int, den:int)

    The constructor takes a numerator and denominator
    value on instantiation. These are then passed to
    attributes, self.num and self.den

    The fraction should be reduced to its lowest indivisible form. 
    This can be achieved by finding the greatest common divisor between
    the numerator and denominator. The numerator and denominator 
    would then become themselves floor divided by the greatest common 
    divisor. Example:

        Let A = (5 / 10), then GCD(5, 10) = 5

        A = ((5 // GCD(5, 10)) / (10 // GCD(5, 10)))
          = ((5 // 5) / (10 // 5))
          = (1 / 2)

__str__(self) -> str

    Represents the fraction as a string. The format
    should be as "({} / {})". For example, if a Fraction
    instance of Fraction(num=1, den=2) is created, then
    its __str__ representation would be "(1 / 2)". This
    method allows compatability with the str() and print()
    functions.

__repr__(self) -> str

    Identical to __str__. This method allows compatability
    with the repr() function.

__neg__(self) -> Fraction

    Returns a new Fraction instance that is the negative of
    the current Fraction.

__add__(self, other:Fraction) -> Fraction

    Adds two Fraction instances and returns a new Fraction 
    instance. The denominators of two fractions must be 
    equivalent in order to add together the numerators.
    This can be done by finding the least common multiple
    between the two denominators, and scaling the numerators
    by the least common multiple, floor divided by the
    denominator. Example:

        Let A = (1 / 2), B = (1 / 4). Then LCM(2, 4) = 4

        A_scale = LCM(2, 4) // 2
                = 4 // 2
                = 2

        B_scale = LCM(2, 4) // 4
                = 4 // 4
                = 1
        
        A = ((1 * A_scale) / LCM(2, 4))
          = ((1 * 2) / 4)
          = (2 / 4)
        
        B = ((1 * B_scale) / LCM(2, 4))
          = ((1 * 1) / 4)
          = (1 / 4)

        A + B = (2 / 4) + (1 / 4) = (3 / 4)

__sub__(self, other:Fraction) -> Fraction

    Subtracts the Fraction by the other Fraction, and returns
    a new Fraction instance. Like __add__, the denominators
    of two fractions must be equivalent to subtract the
    numerators.
    Hint: Think about how you can reuse __add__ and __neg__!
    Remember that:
                    A + (-B) = A - B

__mul__(self, other:Fraction) -> Fraction

    Multiplies the Fraction by the other Fraction, and returns
    a new Fraction instance. The numerators and denominators
    can be multiplied directly.

__truediv__(self, other:Fraction) -> Fraction

    Divides the Fraction by the other Fraction, and returns
    a new Fraction instance. If 'A' and 'B' are fractions,
    (A / B) is equivalent to A * reciprocal(B).
    Hint: Think about how you can reuse __mul__ and reciprocal()!
    (see the reciprocal() method description below)

reciprocal(self) -> Fraction

    Returns a new Fraction that is the reciprocal of this Fraction.
    The reciprocal of a fraction is the denominator divided by the
    numerator. Example:

    Let A = (1 / 2), then reciprocal(A) = (2 / 1)

evaluate(self) -> float

    Divides the numerator by the denominator, and returns the resulting
    value.

is_improper(self) -> bool

    Returns True if the fraction is improper, else False. A fraction is
    improper if the numerator is greater than or equal to the denominator.


EXAMPLE FUNCTIONALITY
---------------------

a = Fraction(5, 10)  # (5 / 10) gets simplified to (1 / 2)
print(a)  # (1 / 2)

b = Fraction(1, 2)  # (1 / 2) is irreducible
print(b)  # (1 / 2)

print(-a)  # (-1 / 2)

print(a + b)  # (1 / 1)

print(a - b)  # (0 / 1)

print(a * b)  # (1 / 4)

print(a / b)  # (1 / 1)

print(a.reciprocal())  # (2 / 1)

print(a.evaluate())  # 0.5

print(a.is_improper())  # False

print(a.reciprocal().is_improper())  # True
'''

from __future__ import annotations


def gcd(x:int, y:int) -> int:
    '''
    Calculates the greatest common divisor between two integer values.
    '''
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x:int, y:int) -> int:
    '''
    Calculates the least common multiple between two integer values.
    '''
    return abs(x * y) // gcd(x, y)


class Fraction():

    def __init__(self, num:int, den:int):
        self.num = num  # numerator value
        self.den = den  # denominator value

        # a fraction that has 1 (or -1) as a numerator or
        # denominator is already simplified (we're 
        # just checking to potentially save on the 
        # amount of operations we're doing)
        if abs(self.num) != 1 and abs(self.den) != 1:
            d = gcd(self.num, self.den)
            self.num //= d
            self.den //= d

    def __str__(self) -> str:
        return "({} / {})".format(self.num, self.den)
    
    __repr__ = __str__

    def __neg__(self) -> Fraction:  # -Fraction
        return Fraction(-self.num, self.den)

    def __add__(self, other:Fraction) -> Fraction:  # Fraction + Fraction
        m = lcm(self.den, other.den)
        return Fraction((self.num * (m // self.den)) + (other.num * (m // other.den)), m)
    
    def __sub__(self, other:Fraction) -> Fraction:  # Fraction - Fraction
        # 'self' IS the class being acted on, think of it as being a variable
        # that is holding our instantiation
        return self + (-other)

    def __mul__(self, other:Fraction) -> Fraction:  # Fraction * Fraction
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other:Fraction) -> Fraction:  # Fraction / Fraction
        # same principle from __sub__ being used here. treat 'self' as just being
        # a variable that is holding the class being acted on 
        return self * other.reciprocal()

    def reciprocal(self) -> Fraction:
        return Fraction(self.den, self.num)

    def evaluate(self) -> float:
        return self.num / self.den

    def is_improper(self) -> bool:
        return self.num >= self.den
        

a = Fraction(5, 10)  # (5 / 10) gets simplified to (1 / 2)
print(a)  # (1 / 2)

b = Fraction(1, 2)  # (1 / 2) is irreducible
print(b)  # (1 / 2)

print(-a)  # (-1 / 2)

print(a + b)  # (1 / 1)

print(a - b)  # (0 / 1)

print(a * b)  # (1 / 4)

print(a / b)  # (1 / 1)

print(a.reciprocal())  # (2 / 1)

print(a.evaluate())  # 0.5

print(a.is_improper())  # False

print(a.reciprocal().is_improper())  # True


'''
                A question you might have:
        "Why would a class like this be necessary?"

Floating point values in many programming languages can be imprecise 
when going to extremely small decimal places. You might have come 
across this on your own time -- try evaluating:

print(0.1 + 0.2)

You'll end up printing: 0.30000000000000004

The reasons for why this happens is extremely complicated.
But, hopefully you can imagine that, if you were some sort of
rocket engineer--needing extremely accurate numbers lest you face 
catastrophic (and expensive) failures--you might want to consider 
expressing rational numbers as discrete integers, where you only 
evaluate them *after* doing higher-level manipulations, because these 
floating point discrepancies will stack on top of each other after 
many operations.

Integer values have their limitations, too, of course. You can't
express numbers to extremely large magnitudes without creating some
sort of auxiliary class to go further beyond the computer's maximum
integer size (which varies from computer to computer). Other than that,
integer operations are extremely safe compared to float operations.
The Python standard library actually includes a Fraction class just like
the one here, since there some programmers that need that kind of
ridiculous decimal precision.
'''