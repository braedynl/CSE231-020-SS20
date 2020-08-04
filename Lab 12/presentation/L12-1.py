class ComplexNumber(object):

    def __init__(self, real, imaginary):
        self.real_ = real
        self.imaginary_ = imaginary
    
    def __add__(self, other):  # Assuming `other` is another ComplexNumber() instance
        real = self.real_ + other.real_
        imaginary = self.imaginary_ + other.imaginary_
        return ComplexNumber(real, imaginary)
    
    def __str__(self):
        return "{}+{}i".format(self.real_, self.imaginary_)

C1 = ComplexNumber(3, 6)
print(C1)

C2 = ComplexNumber(4, 5)
print(C2)

C3 = C2 + C1
print(C3)