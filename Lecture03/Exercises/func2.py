def is_prime(n): pass

primes = [number for number in range(2, 100) if is_prime(number)]

def product(*nums, scale=1):
    p = scale
    for n in nums:
        p *= n
    return p

print(product(primes))
