x = range(-5, 5)
result = filter(lambda num : num < 0, x)
print(list(result))  # => [-5, -4, -3, -2, -1]
