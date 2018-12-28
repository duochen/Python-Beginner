class Complex:
    def __init__(self, realpart=0, imagpart=0):
        self.real = realpart
        self.imag = imagpart

# Make an instance object 'c'!
c = Complex(3.0, -4.5)

# Get attributes
print(c.real, c.imag)  # => 3.0 -4.5

# Set attributes
c.real = -9.2
c.imag = 4.1
print(c.real, c.imag)  # => -9.2 4.1     

