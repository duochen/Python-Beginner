def num_diamonds(diamonds, k, smallest):
    """
    diamonds is a list of diamond sizes.
    k is the maximum allowed difference between diamond sizes.
    smallest is the size of a diamond.

    Return the number of diamonds that can be displayed using
    smallest as the smallest diamond.
    """
    total = 0
    for diamond in diamonds:
        if diamond >= smallest and diamond - smallest <= k:
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

for diamond in diamonds:
    result = num_diamonds(diamonds, k, diamond)
    if result > max_diamonds:
        max_diamonds = result

output_file.write(f'{max_diamonds}\n')

input_file.close()
output_file.close()
