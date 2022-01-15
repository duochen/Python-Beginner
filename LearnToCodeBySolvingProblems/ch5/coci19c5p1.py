lst = input().split()
n = int(lst[0])
m = int(lst[1])

grid = []

for i in range(n):
    # Add '.' on the right to avoid index error when '*' was at right
    row = list(input()) + ['.']
    grid.append(row)
# Add row of '.' on the bottom to avoid index error when '*' was at bottom
grid.append(['.'] * (m + 1))

rectangles = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            rectangles = rectangles + 1

            # Find right edge of rectangle
            right = j
            while grid[i][right + 1] == '*':
                right = right + 1

            # Delete rectangle
            row = i
            while grid[row][j] == '*':
                for k in range(j, right + 1):
                    grid[row][k] = '.'
                row = row + 1

print(rectangles)
