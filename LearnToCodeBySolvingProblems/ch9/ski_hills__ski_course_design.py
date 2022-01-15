MAX_DIFFERENCE = 17
MAX_HEIGHT = 100


def cost_for_range(heights, low, high):
    """
    heights is a list of hill heights.
    low is an integer giving the low end of the range.
    high is an integer giving the high end of a range.

    Return the cost of changing all heights of hills to be
    between low and high.
    """
    cost = 0
    for height in heights:
        if height < low:
            cost = cost + (low - height) ** 2
        elif height > high:
            cost = cost + (height - high) ** 2
    return cost


input_file = open('skidesign.in', 'r')
output_file = open('skidesign.out', 'w')

n = int(input_file.readline())

heights = []

for i in range(n):
    heights.append(int(input_file.readline()))

min_cost = cost_for_range(heights, 0, MAX_DIFFERENCE)

for low in range(1, MAX_HEIGHT + 1):
    result = cost_for_range(heights, low, low + MAX_DIFFERENCE)
    if result < min_cost:
        min_cost = result

output_file.write(f'{min_cost}\n')

input_file.close()
output_file.close()
