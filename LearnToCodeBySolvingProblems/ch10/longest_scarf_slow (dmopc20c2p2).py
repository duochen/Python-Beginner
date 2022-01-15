# This solution is not efficient enough to pass all test cases in time.


def leftmost_index(scarf, color):
    """
    scarf is a list of colors in the scarf.
    color is a color.

    Return the leftmost index of color in scarf,
    or -1 if color isn't in scarf at all.
    """
    for i in range(len(scarf)):
        if scarf[i] == color:
            return i
    return -1


def rightmost_index(scarf, color):
    """
    scarf is a list of colors in the scarf.
    color is a color.

    Return the rightmost index of color in scarf,
    or -1 if color isn't in scarf at all.
    """
    for i in range(len(scarf) - 1, -1, -1):
        if scarf[i] == color:
            return i
    return -1


lst = input().split()
n = int(lst[0])
m = int(lst[1])

scarf = input().split()
for i in range(n):
    scarf[i] = int(scarf[i])

max_length = 0

for i in range(m):
    relative = input().split()
    first = int(relative[0])
    last = int(relative[1])
    if leftmost_index(scarf, first) != -1 and leftmost_index(scarf, last) != -1:
        length = rightmost_index(scarf, last) - leftmost_index(scarf, first) + 1
        if length > max_length:
            max_length = length

print(max_length)
