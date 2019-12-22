class Point:
    def __init__(self, x=0, y=0):  
        self.x = x
        self.y = y

    def rotate_90_CC(self):
        self.x, self.y = -self.y, self.x

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def	__str__(self):
        return "Point({0}, {1})".format(self.x, self.y)

o = Point()
print(o)      # Point(0, 0)

p1 = Point(3, 5)
p2 = Point(4, 6)
print(p1, p2)  # Point(3, 5) Point(4,6)

p1.rotate_90_CC()
print(p1)       # Point(-5, 3)
print(p1 + p2)  # Point(-1, 9)    
