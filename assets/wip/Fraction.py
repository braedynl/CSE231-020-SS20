
from __future__ import annotations

def gcd(x:int, y:int) -> int:
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x:int, y:int) -> int:
    return abs(x * y) // gcd(x, y)


class Fraction():

    def __init__(self, num:int, den:int):
        self.num = num
        self.den = den
        self.simplify()
    
    def __str__(self) -> str:
        return "({} / {})".format(self.num, self.den)
    
    __repr__ = __str__

    def __neg__(self) -> Fraction:
        return Fraction(-self.num, self.den)

    def __add__(self, other:Fraction) -> Fraction:
        m = lcm(self.den, other.den)
        a = m // self.den
        b = m // other.den
        return Fraction((self.num * a) + (other.num * b), m)
    
    def __sub__(self, other:Fraction) -> Fraction:
        return self + (-other)

    def __mul__(self, other:Fraction) -> Fraction:
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other:Fraction) -> Fraction:
        return self * other.reciprocal()

    def simplify(self) -> None:
        d = gcd(self.num, self.den)
        self.num = self.num // d
        self.den = self.den // d

    def reciprocal(self) -> Fraction:
        return Fraction(self.den, self.num)

    def evaluate(self) -> float:
        return self.num / self.den

    def is_improper(self) -> bool:
        return self.num >= self.den
        

a = Fraction(1, 2)
b = Fraction(1, 2)

print(a - b)