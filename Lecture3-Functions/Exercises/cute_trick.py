x = 3
foo = 'fighter'   
y = 4
bar = 'bell'   
z = 5

print("{z}^2 = {x}^2 + {y}^2".format(x=x, y=y, z=z))
# => 5^2 = 3^2 + 4^2
print("{z}^2 = {x}^2 + {y}^2".format(**locals()))
# => 5^2 = 3^2 + 4^2
# Equivalent to .format(x=3, foo='fighter', y=4, ...)
