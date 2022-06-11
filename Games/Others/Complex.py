class Complex:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

#######################################

c =  Complex()
print(c.real, c.imag)

c1 = Complex(3.0, -4.5)
print(c1.real, c1.imag)