x = [9, 8, 7]
x[2] = 6
y = 'ABC'
y[2] = 'D'  # => TypeError: 'str' object does not support item assignment
z = (5, 4, 3)
z[2] = 0    # => TypeError: 'tuple' object does not support item assignment