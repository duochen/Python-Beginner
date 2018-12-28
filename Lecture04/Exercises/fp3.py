m = map(lambda val : val **2, range(10))
print(list(m))

f = filter(lambda pair: pair[1] > 0, [(4,1), (3, -2), (8,0)])
print(list(f))