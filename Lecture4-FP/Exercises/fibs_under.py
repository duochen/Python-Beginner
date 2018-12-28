def generate_fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

def fibs_under(n):
    for fib in generate_fibs(): 
        if fib > n:
            break
        print(fib)

fibs_under(10)     # => 1 2 3 5 8   