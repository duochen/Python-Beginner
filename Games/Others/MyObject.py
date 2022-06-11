class MyClass:
    """A simple example class"""
    num = 12345
    def __init__(self):
        self.number = 4567

    def greet(self):
        return "Hello world!"

print(MyClass.num)  

my = MyClass()
my.greet()  
print(my.number)
