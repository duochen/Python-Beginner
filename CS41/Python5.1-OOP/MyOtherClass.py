class MyOtherClass():
    num = 12345
    def __init__(self):
        self.num = 0

x = MyOtherClass()
print(x.num)     # 0 or 12345?
del x.num
print(x.num)     # 0 or 12345?