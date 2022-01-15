def is_first_better(grid, cow_a, cow_b):
    """
    grid is a two-dimensional list of gymnastics ratings.
    cow_a is the index of a cow.
    cow_b is the index of another cow.

    Return True if cow_a is consistently better than cow_b,
    False otherwise.
    """
    better = True
    i = 0
    while i < len(grid) and better:
        if grid[i].index(cow_a) > grid[i].index(cow_b):
            better = False
        else:
            i = i + 1
    return better


input_file = open('gymnastics.in', 'r')
output_file = open('gymnastics.out', 'w')

lst = input_file.readline().split()
k = int(lst[0])
n = int(lst[1])

grid = []

for i in range(k):
    row = input_file.readline().split()
    for j in range(n):
        row[j] = int(row[j])
    grid.append(row)

consistent_pairs = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j and is_first_better(grid, i, j):
            consistent_pairs = consistent_pairs + 1

output_file.write(f'{consistent_pairs}\n')

input_file.close()
output_file.close()
