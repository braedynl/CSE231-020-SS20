from __future__ import annotations

class AmazonItem():

    def __init__(self, name:str, brand:str, price:float, percent_off:float):
        self.name = name
        self.brand = brand
        self.price = price
        self.percent_off = percent_off

    def __str__(self) -> str:
        return "AmazonItem(name={}, brand={}, price={}, percent_off={})".format(
            repr(self.name), repr(self.brand), self.price, self.percent_off
        )
    
    __repr__ = __str__
    
    def __add__(self, other:AmazonItem) -> float:
        return self.display_price() + other.display_price()

    def display_price(self) -> float:
        return self.price - (self.price * self.percent_off)

a = AmazonItem("Macbook Air", "Apple", 999.99, 0.05)
b = AmazonItem("iPhone 12", "Apple", 799.99, 0.0)

print(sum([a, b]))