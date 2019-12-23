def debug(function):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return function(*args, **kwargs)

    return wrapper

@debug
def foo(a, b, c=1):
    return (a + b) * c

r = foo(5, 3, c=2)  # prints "Arguments: (5, 3) {'c': 2}"
print(r)

def goo(a, b, c=1):
    return (a + b) * c

goo = debug(goo)
x = goo(2, 3)
print(x)
y = goo(2, 1, c=3)
print(y)
print(goo)