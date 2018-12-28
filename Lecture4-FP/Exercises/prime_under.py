def make_divisibility_test(n):
    def divisible_by_n(m):
        return m % n == 0
    return divisible_by_n

def primes_under(n):
    tests = []
    # will hole [div_by_2, div_by_3, div_by_5, ...]

    for i in range(2, n):
        # implement is_prime using our divis. tests
        if not any(map(lambda test: test(i), tests)):
            tests.append(make_divisibility_test(i))
            yield i    

result = list(primes_under(10))
print(result)