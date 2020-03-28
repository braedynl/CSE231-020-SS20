class ComplexNumber(object):
    
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b
        
    def get_str(self):
        return "{}+{}i".format(self.real, self.imaginary)    # Complex number in standard form
    

c = ComplexNumber(3, 2)

c_str = c.get_str()

print(c_str)