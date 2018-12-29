d = dict()
d['a'] = 1
d['b'] = 2
print(d)          # => {'a': 1, 'b': 2}
print(d.get['a']) # => 1
print(d['c'])     # =>  KeyError: 'c'
print(d.get('c', 0))  # => 0