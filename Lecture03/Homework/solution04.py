def maximum(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
        return maxnum

print(maximum(3, 2, 8))         # => 8
print(maximum(1, 5, 9, -2, 2))  # => 9