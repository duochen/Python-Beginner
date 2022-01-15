def num_neighbours(grid, row, col):
    """
    grid is a grid of seating information.
    row is a row index in grid.
    col is a column index in grid.

    Return number of neighbours of grid[row][col]
    """
    biggest_row = len(grid) - 1
    biggest_col = len(grid[0]) - 1
    total = 0

    # Eight directions to check

    # Right
    if col < biggest_col and grid[row][col + 1] == 'o':
        total = total + 1
    # Left
    if col > 0 and grid[row][col - 1] == 'o':
        total = total + 1
    # Down
    if row < biggest_row and grid[row + 1][col] == 'o':
        total = total + 1
    # Up
    if row > 0 and grid[row - 1][col] == 'o':
        total = total + 1
    # Right down
    if (col < biggest_col and row < biggest_row and
            grid[row + 1][col + 1] == 'o'):
        total = total + 1
    # Right up
    if col < biggest_col and row > 0 and grid[row - 1][col + 1] == 'o':
        total = total + 1
    # Left down
    if col > 0 and row < biggest_row and grid[row + 1][col - 1] == 'o':
        total = total + 1
    # Left up
    if col > 0 and row > 0 and grid[row - 1][col - 1] == 'o':
        total = total + 1

    return total


def mirko_location(grid):
    """
    grid is a grid of seating information.

    Return [row, col] of where Mirko will sit;
    if there is no free seat, return [-1, -1].
    """
    mirko_row = -1
    mirko_col = -1
    most = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '.':
                neighbours = num_neighbours(grid, row, col)
                if neighbours > most:
                    most = neighbours
                    mirko_row = row
                    mirko_col = col
    return [mirko_row, mirko_col]


lst = input().split()
r = int(lst[0])
s = int(lst[1])

grid = []

for i in range(r):
    grid.append(list(input()))

lst = mirko_location(grid)
mirko_row = lst[0]
mirko_col = lst[1]
if mirko_row >= 0 and mirko_col >= 0:
    grid[mirko_row][mirko_col] = 'o'  # Mirko sits

handshakes = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'o':
            handshakes = handshakes + num_neighbours(grid, row, col)

# If we find that person A shakes hands with person B, then later we'll find
# that person B shakes hands with Person A.
# That is, we're double-counting the handshakes, and need to divide by 2.
handshakes = handshakes // 2

print(handshakes)
