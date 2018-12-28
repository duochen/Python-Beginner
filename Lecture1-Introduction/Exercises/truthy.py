# 'Falsy
print(bool(None))   # => False
print(bool(False))  # => False
print(bool(0))      # => False
print(bool(0.0))    # => False
print(bool(''))     # => False

# Empty data structures are 'falsy
print(bool([]))     # => False

# Everything else is 'truthy'
data = []
if data:
    print("Process data")
else:
    print("There's no data!") # => There's no data!
