class MyClass:
    """A simple example class"""
    def __init__(self, message, firstname):
        self.message = message
        self.firstname = firstname
   
    def greet(self):
        return self.message + ' ' + self.firstname
    
    def add(self, a, b):
        return a + b

x = MyClass("Hello!", "Duo")
print(x.greet())