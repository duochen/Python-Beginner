class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side):
        # call parent constructor, width and height are both sides
        super().__init__(side, side)

# subclass check
print(issubclass(Square, Rectangle))  # => True

r = Rectangle(3, 4)
print(r.area())         # => 12
print(r.perimeter())    # => 14

s = Square(2)
print(s.area())         # => 4
print(s.perimeter())    # => 8

print(isinstance(r, Rectangle))     # => True
print(isinstance(r, Square))        # => False
print(isinstance(s, Rectangle))     # => True
print(isinstance(s, Square))        # => True
