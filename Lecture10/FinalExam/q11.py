class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x + 1
        self.y = y + 1

p = Point()
print(p.x, p.y)