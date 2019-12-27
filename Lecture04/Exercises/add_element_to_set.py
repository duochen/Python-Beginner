my_set = set() # empty set
my_set.update([9, 12])
print(my_set)  # => {9, 12}
my_set.update((3,5)) # => {9, 3, 12, 5}
print(my_set)
my_set.update("SIKANDER")
print(my_set) # => {'K', 3, 5, 'S', 9, 12, 'E', 'D', 'R', 'N', 'I', 'A'}

my_set.update(("US", "CN"))
print(my_set) # => {'N', 3, 'R', 5, 'A', 9, 'D', 12, 'K', 'I', 'CN', 'US', 'E', 'S'}

my_set.update(4,5)  # => TypeError: 'int' object is not iterable