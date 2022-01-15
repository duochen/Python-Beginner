def num_steps(ocean, cur_row, cur_col):
    """
    ocean is the ocean grid.
    cur_row is the current row; cur_col is the current column.

    Return the number of steps to get from (start_row, start_col)
    to the target, or -1 if not possible.
    """
    total = 0
    while True:
        symbol = ocean[cur_row][cur_col]
        if symbol == 'x':  # Target
            return total
        elif symbol == 'o':  # Back to start
            return -1
        elif symbol == '.':  # Can't move
            return -1
        elif symbol == '<':  # Move west
            cur_col = cur_col - 1
        elif symbol == '>':  # Move east
            cur_col = cur_col + 1
        elif symbol == 'v':  # Move south
            cur_row = cur_row + 1
        elif symbol == '^':  # Move north
            cur_row = cur_row - 1
        total = total + 1


lst = input().split()
num_rows = int(lst[0])
num_cols = int(lst[1])

start_row = -1
start_col = -1

ocean = []

for i in range(num_rows):
    row = input()
    ocean.append(row)
    if 'o' in row:
        start_row = i
        start_col = row.find('o')

steps = []

# East
steps.append(num_steps(ocean, start_row, start_col + 1))

# North
steps.append(num_steps(ocean, start_row - 1, start_col))

# South
steps.append(num_steps(ocean, start_row + 1, start_col))

# West
steps.append(num_steps(ocean, start_row, start_col - 1))

best = -1
for num_steps in steps:
    if best == -1 or (num_steps >= 0 and num_steps < best):
        best = num_steps
if best == -1:
    print(':(')
else:
    print(':)')
    # Check in alphabetical order (E, N, S, W)
    if steps[0] == best:
        print('E')
    elif steps[1] == best:
        print('N')
    elif steps[2] == best:
        print('S')
    else:
        print('W')
