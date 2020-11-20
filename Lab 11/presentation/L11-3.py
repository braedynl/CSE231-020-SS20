class ComplexNumber():
    
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b
    
    # What we had previously:

    # def get_str(self):
    #     # Complex number in standard form
    #     return "{}+{}i".format(self.real, self.imaginary)
    
    # We don't want to have to call this ^ every time
    # we want to print a string version of our class, right?
    
    def __str__(self):
        return "{}+{}i".format(self.real, self.imaginary)
    
    def __repr__(self):
        return self.__str__()
    
    # you can also do:
    # __repr__ = __self__
    # if you're making them identical

c = ComplexNumber(3, 2)

print(c)    # We can just print our instance now