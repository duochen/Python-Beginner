squares = {x: x*x for x in range(3)}
print(squares)   # => {0: 0, 1: 1, 2: 4}

squares = {}
for x in range(3):
    squares[x] = x*x
print(squares)   # => {0: 0, 1: 1, 2: 4}