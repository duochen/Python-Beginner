def generate_ints(n):
    for i in range(n):
        yield i

g = generate_ints(3)
print(type(g))   # => <class 'generator'>
print(next(g))   # => 0
print(next(g))   # => 1
print(next(g))   # => 2
print(next(g))   # raises StopIteration