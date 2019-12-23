triple = lambda x : x * 3  # NEVER EVER DO THIS

# Squares from 0**2 to 9**2
a = map(lambda val: val ** 2, range(10))
print(list(a))

b = filter(lambda pair: pair[1] > 0, [(4,1), (3, -2), (8, 0)])
print(list(b))
