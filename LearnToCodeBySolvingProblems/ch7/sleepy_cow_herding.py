input_file = open('herding.in', 'r')
output_file = open('herding.out', 'w')

locations = input_file.readline().split()

for i in range(3):
    locations[i] = int(locations[i])

locations.sort()


# Minimum number of moves

# No gaps; no moves
if locations[0] + 1 == locations[1] and locations[1] + 1 == locations[2]:
    min_moves = 0
# One gap; one move
elif locations[0] + 2 == locations[1] or locations[1] + 2 == locations[2]:
    min_moves = 1
else:
    min_moves = 2

output_file.write(f'{min_moves}\n')


# Maximum number of moves

# It's possible to move a cow into each location of the biggest gap
gap1 = locations[1] - locations[0] - 1
gap2 = locations[2] - locations[1] - 1
if gap1 >= gap2:
    max_moves = gap1
else:
    max_moves = gap2

output_file.write(f'{max_moves}\n')


input_file.close()
output_file.close()
