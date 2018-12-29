d = {'b':1, 'c':22, 'a':10}
t = d.items()
print(t) # => dict_items([('b', 1), ('c', 22), ('a', 10)])
s = sorted(t)
print(s) # => [('a', 10), ('b', 1), ('c', 22)]

print(sorted([ (v, k) for k, v in d.items()]))
# => [(1, 'b'), (10, 'a'), (22, 'c')]