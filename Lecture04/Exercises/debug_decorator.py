def debug(function):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return function(*args, **kwargs)
    return wrapper

def foo(a, b, c=1):
    return (a + b) * c

woo = debug(foo)    
result = woo(2, 3)       # => Arguments: (2, 3) {}
print(result)            # => 5
result = woo(2, 1, c=3)  # => Arguments: (2, 1) {'c':3}
print(result)            # => 9
print(foo)               # <function foo at 0x...>
print(woo)               # <function debug.<locals>.wrapper at 0x...>

@debug
def myfoo(a, b, c=1):
    return (a + b) * c

result = myfoo(5, 3, c=2)  # => Arguments: (5, 3) {'c': 2}
print(result)              # => 16