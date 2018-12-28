def is_even(num):
    return num % 2 == 0

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34]
a = [num for num in nums if is_even(num)]
print(a) # => [2, 8, 34]