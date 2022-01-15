def explains_spottiness(spotty_grid, plain_grid, i):
    """
    spotty_grid is the grid of spotty cow characters.
    plain_grid is the grid of plain cow characters.
    i is a column index in the grids.

    Return True if column i explains spottiness, False otherwise.
    """
    spotty_letters = ''
    for row in spotty_grid:
        spotty_letters = spotty_letters + row[i]
    plain_letters = ''
    for row in plain_grid:
        plain_letters = plain_letters + row[i]

    for char in spotty_letters:
        if char in plain_letters:
            return False

    return True


input_file = open('cownomics.in', 'r')
output_file = open('cownomics.out', 'w')

lst = input_file.readline().split()
n = int(lst[0])
m = int(lst[1])

spotty_grid = []
plain_grid = []

for i in range(n):
    spotty_grid.append(input_file.readline().rstrip())

for i in range(n):
    plain_grid.append(input_file.readline().rstrip())

num_positions = 0

for i in range(m):
    if explains_spottiness(spotty_grid, plain_grid, i):
        num_positions = num_positions + 1

output_file.write(f'{num_positions}\n')

input_file.close()
output_file.close()
