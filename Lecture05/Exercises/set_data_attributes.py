class MyOtherClass():
    num = 12345
    def __init__(self):
        self.num = 0

c = MyOtherClass()
# You can set attributes on instance (and class) objects 
# on the fly (we usedd this in the constructor!)
c.num = 1
while c.num < 10:
    c.num = c.num * 2
    print(c.num)        
del c.num

# prints 2, 4, 8, 16