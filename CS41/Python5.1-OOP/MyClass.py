class MyClass:
    """A simpe example class"""
    num = 12345
    def greet(self):
        return "Hello world!"

# Attribute References
print(MyClass.num)     # => 123245       (int object)
print(MyClass.greet)   # => <function f> (function object)

