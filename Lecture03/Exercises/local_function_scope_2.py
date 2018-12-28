x = 2
def foo(y):
    x = 41
    z = 5  
    print(locals())        # => {'y': 3, 'x': 41, 'z': 5}
    print(globals()['x'])  # => 2
    print(x, y, z)         # => 41 3 5

foo(3)