# This solution is not efficient enough to pass all test cases in time.


MAX_LENGTH = 200000


def num_destroyed(stalagmites, stalactites, cave_height, height):
    """
    stalagmites is a list of stalagmite sizes.
    stalactites is a list of stalactite sizes.
    cave_height is the height of the cave.
    height is the height at which the firefly flies.

    Return the number of obstacles that the firefly destroys.
    """
    total = 0
    for stalagmite in stalagmites:
        if stalagmite >= height:
            total = total + 1
    for stalactite in stalactites:
        if cave_height - stalactite + 1 <= height:
            total = total + 1
    return total


lst = input().split()
cave_length = int(lst[0])
cave_height = int(lst[1])

stalagmites = []
stalactites = []

for i in range(cave_length):
    if i % 2 == 0:
        stalagmites.append(int(input()))
    else:
        stalactites.append(int(input()))

min_destroyed = MAX_LENGTH
num_heights = 0

for height in range(1, cave_height + 1):
    result = num_destroyed(stalagmites, stalactites, cave_height, height)
    if result < min_destroyed:
        min_destroyed = result
        num_heights = 1
    elif result == min_destroyed:
        num_heights = num_heights + 1

print(min_destroyed, num_heights)
