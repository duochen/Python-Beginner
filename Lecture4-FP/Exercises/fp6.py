def perform_twice(fn, *args, **kwargs):
    fn(*args, **kwargs)
    fn(*args, **kwargs)

perform_twice(print, 5, 10, sep='&', end='...')    

def make_divisibility_test(n):
    def divisible_by_n(m):
        return m % n == 0
    return divisible_by_n

div_by_3 = make_divisibility_test(3)
f = filter(div_by_3, range(10))  # generate 0, 3, 6, 9
print(list(f))

result = make_divisibility_test(5)(10)
print(result)