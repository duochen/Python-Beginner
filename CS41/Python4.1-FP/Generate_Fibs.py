def generate_fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

g = generate_fibs()

def fibs_under(n):
    for fib in generate_fibs(): # Loops over 1, 1, 2...
        if fib > n:
            break
        print(fib)

fibs_under(20)

print(next(g))  # => 1
print(next(g))  # => 1
print(next(g))  # => 2
print(next(g))  # => 3
print(next(g))  # => 5
print(max(g))   # Oh no! What happen?


