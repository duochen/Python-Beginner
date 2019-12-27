my_set = set([3,5,9,12, 'US', 'CN'])
print(my_set) # => {3, 5, 'US', 9, 12, 'CN'}

my_set.discard(12)
print(my_set)  # => {3, 5, 'US', 9, 'CN'}

my_set.discard(15)
print(my_set) # => {3, 5, 'US', 9, 'CN'}

my_set.remove(15) # => KeyError: 15