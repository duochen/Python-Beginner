n = int(input())
changes = input()

grid = []

for i in range(2 * n):
    row = []
    for j in range(n):
        row.append('.')
    grid.append(row)

worth = 0

for i in range(n):
    if changes[i] == '+':
        grid[worth + n][i] = '/'
        worth = worth + 1
    elif changes[i] == '-':
        worth = worth - 1
        grid[worth + n][i] = '\\'
    else:
        grid[worth + n][i] = '_'

all_dots = ['.'] * n

for i in range(2 * n - 1, -1, -1):
    if grid[i] != all_dots:
        print(''.join(grid[i]))
