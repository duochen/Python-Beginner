class Point:
    def __init__(self, x = 7, y = 3):
        self.x = x
        self.y = y
    
    def sub(self):
        result = self.x - self.y
        return result

myresult1 = Point()
myresult2 = Point(11,5)
print(myresult1.sub(), myresult2.sub())