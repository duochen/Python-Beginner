def make_divisibility_test(n):
    def divisible_by_n(m):
        return m % n == 0
    return divisible_by_n

div_by_3 = make_divisibility_test(3)
a = filter(div_by_3, range(10))  # generate 0, 3, 6, 9
print(list(a))
make_divisibility_test(5)(10)