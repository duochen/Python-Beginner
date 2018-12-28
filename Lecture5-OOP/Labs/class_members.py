class Vector3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        r = Vector3()
        r.x = self.x + other.x
        r.y = self.y + other.y
        r.z = self.z + other.z
        return r

    def __sub__(self, other):
        r = Vector3()
        r.x = self.x - other.x
        r.y = self.y - other.y
        r.z = self.z - other.z
        return r

    def __mul__(self, n):
        r = Vector3()
        r.x = self.x * n
        r.y = self.y * n
        r.z = self.z * n
        return r

    def __truediv__(self, n):
        r = Vector3()
        r.x = self.x / n
        r.y = self.y / n
        r.z = self.z / n
        return r
    
    def __floordiv__(self, n):
        r = Vector3()
        r.x = self.x // n
        r.y = self.y // n
        r.z = self.z // n
        return r

    def show(self):
        print(self.x, self.y, self.z)

v1 = Vector3(1, 2, 3)        
v2 = Vector3(4, 5, 6)
v3 = v1 + v2
v3.show()
v4 = v1 - v2
v4.show()
v5 = v1 * 3
v5.show()
v6 = v1/2
v6.show()
