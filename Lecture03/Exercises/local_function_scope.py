x = 2
def foo(y):
    z = 5  
    print(locals())        # => {'y': 3, 'z': 5}
    print(globals()['x'])  # => 2
    print(x, y, z)         # => 2 3 5

foo(3)

