# Suppose we want to find 2 * 3 * 5 * 7 * … up to 100  
def is_prime(n):	
    pass	# Some implementation

# Product accepts any number of arguments
def product(*nums, scale=1):
    p = scale
    for n in nums:
        p *= n
    return p

# Extract all the primes
primes = [number for number in range(2, 100)  
    if is_prime(number)]

primes = [2, 3, 5]  
print(product(*primes))    # => 30

