tuple = ('rahul', 100, 60.4, 'deepak')
tuple1 = ('sanjay', 10)
print(tuple)      # => ('rahul', 100, 60.4, 'deepak')
print(tuple[2:])  # => (60.4, 'deepak')
print(tuple1[0])  # => sanjay
tuple2 = tuple + tuple1
print(tuple2)     # => ('rahul', 100, 60.4, 'deepak', 'sanjay', 10)