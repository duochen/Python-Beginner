squares = [x**2 for x in range(4)]
print(squares)   # => [0, 1, 4, 9]

squares = []
for x in range(4):
    squares.append(x**2)
print(squares)   # => [0, 1, 4, 9]

combs = [(x, y) for x in [1,2] for y in [3,1] if x != y]
print(combs)

combs = []
for x in [1,2]:
    for y in [3,1]:
        if x != y:
            combs.append((x, y))
print(combs)            