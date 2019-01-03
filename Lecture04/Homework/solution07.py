def generate():
    yield "a"    
    yield "b"
    yield "c"
    yield "d"

g = generate()
print(next(g))    # => a
print(next(g))    # => b
print(next(g))    # => c
print(next(g))    # => d