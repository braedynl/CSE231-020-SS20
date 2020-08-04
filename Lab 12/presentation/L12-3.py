class ComplexNumber(object):

    def __init__(self, real, imaginary):
        self.real_ = real
        self.imaginary_ = imaginary
    
    def __add__(self, int_):  # Still assuming parameter two is an int
        self.real_ += int_
    
    def __str__(self):
        return "{}+{}i".format(self.real_, self.imaginary_)

C1 = ComplexNumber(2, 3)
C1 + 2
print(C1)