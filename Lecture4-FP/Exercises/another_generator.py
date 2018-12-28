def generate_fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

g = generate_fibs()

print(next(g))  # => 1
print(next(g))  # => 1
print(next(g))  # => 2
print(next(g))  # => 3
print(next(g))  # => 5
print(max(g))   # Oh no! What happends?
