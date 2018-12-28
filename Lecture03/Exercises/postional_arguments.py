# Product accepts any number of arguments
def product(*nums, scale=1):
    p = scale
    for n in nums:
        p *= n
    return p

# Suppose we want a product function that works as so:
product(3, 5)       # => 15
product(3, 4, 2)    # => 24
product(3, 5, scale=10)  # => 150  