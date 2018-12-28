def sqr(x): return x ** 2

items = [1, 2, 3, 4, 5]
result = list(map(sqr, items))
print(result) # => [1, 4, 9, 16, 25]

# is equal to the following one line
result = list(map((lambda x: x ** 2), items))
print(result) # => [1, 4, 9, 16, 25]