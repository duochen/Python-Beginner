class MyClass:
    """A simpe example class"""
    num = 12345
    def greet(self):
        return "Hello world!"

# Attribute References
print(MyClass.num)     # => 123245       (int object)
print(MyClass.greet)   # => <function f> (function object)

x = MyClass()
x.greet()     # 'Hello world!'
print(type(x.greet))       # method
print(type(MyClass.greet))  # function
print(x.num is MyClass.num)   # True
print(x.greet is MyClass.greet)  # False

