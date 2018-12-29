d = dict()
d['a'] = 2
d['b'] = 4
for (k, v) in d.items():
    print(k, v)   # => a 2 b 4

tups = d.items()
print(tups)       # => dict_items([('a', 2), ('b', 4)])
print(type(tups)) # => <class 'dict_items'>