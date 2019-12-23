# Build an iterator over [1,2,3]
it = iter([1,2,3])

print(next(it))  # => 1
print(next(it))  # => 2
print(next(it))  # => 3
print(next(it))  # raises StopIteration error