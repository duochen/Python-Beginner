# This is slower than the other provided solution, but still
# efficient enough to pass the time limit.
# The reason that this is slower is because it does complete search
# over 10000 options (the ranges),
# rather than only 1000 options (the smallest diamond).


def num_diamonds(diamonds, low, high):
    """
    diamonds is a list of diamond sizes.
    low is an integer giving the low end of the range.
    high is an integer giving the high end of the range.

    Return the number of diamonds whose sizes
    are between low and high.
    """
    total = 0
    for diamond in diamonds:
        if diamond >= low and diamond <= high:
            total = total + 1
    return total


input_file = open('diamond.in', 'r')
output_file = open('diamond.out', 'w')

lst = input_file.readline().split()
n = int(lst[0])
k = int(lst[1])

diamonds = []

for i in range(n):
    diamonds.append(int(input_file.readline()))

max_diamonds = 0

for low in range(1, 10001):
    result = num_diamonds(diamonds, low, low + k)
    if result > max_diamonds:
        max_diamonds = result

output_file.write(f'{max_diamonds}\n')

input_file.close()
output_file.close()
