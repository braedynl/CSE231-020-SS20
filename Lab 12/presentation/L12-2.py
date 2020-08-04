class ComplexNumber(object):

    def __init__(self, real, imaginary):
        self.real_ = real
        self.imaginary_ = imaginary
    
    def __add__(self, int_):  # Now we're assuming the second parameter to be an int
        real = self.real_ + int_
        return ComplexNumber(real, self.imaginary_)
    
    def __str__(self):
        return "{}+{}i".format(self.real_, self.imaginary_)

C1 = ComplexNumber(2, 3)
C2 = C1 + 2