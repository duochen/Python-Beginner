class MyClass:
    """A simple example class"""
    num = 12345
    def greet(self):
        return "Hello world!"

# Attribute References
MyClass.num        # => 12345           (int object)        
MyClass.greet      # => <function f>    (function object)   

x = MyClass()
print(x.greet())

print(type(x.greet))            # method
print(type(MyClass.greet))      # function
print(x.num is MyClass.num)     # True
print(x.greet is MyClass.greet) # False