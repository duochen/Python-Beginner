from bisect import bisect_left


MAX_LENGTH = 200000


def num_destroyed(stalagmites, stalactites, cave_height, height):
    """
    stalagmites is a sorted list of stalagmite sizes.
    stalactites is a sorted list of stalactite sizes.
    cave_height is the height of the cave.
    height is the height at which the firefly flies.

    Return the number of obstacles that the firefly destroys.
    """
    destroyed_stalagmites = len(stalagmites) - bisect_left(stalagmites, height)
    destroyed_stalactites = (len(stalactites) -
                             bisect_left(stalactites, cave_height + 1 - height))
    return destroyed_stalagmites + destroyed_stalactites


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

stalagmites.sort()
stalactites.sort()

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
