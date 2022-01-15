def explode_left_one(hay_bales, explode_index, radius):
    """
    hay_bales is a sorted list of hay bale positions.
    explode_index is the index of the hay bale that is exploded.
    radius is the radius of the explosion.

    Return the index of the leftmost hay bale within the radius that explodes.
    """
    if explode_index == 0:
        return explode_index
    i = explode_index - 1
    while i >= 0 and hay_bales[explode_index] - hay_bales[i] <= radius:
        i = i - 1
    return i + 1


def explode_left(hay_bales, explode_index):
    """
    hay_bales is a sorted list of hay bale positions.
    explode_index is the index of the hay bale that is exploded.

    Return the index of the leftmost hay bale that explodes.
    """
    radius = 1
    done = False
    while not done:
        leftmost = explode_left_one(hay_bales, explode_index, radius)
        if leftmost == explode_index:
            done = True
        else:
            explode_index = leftmost
            radius = radius + 1
    return leftmost


def explode_right_one(hay_bales, explode_index, radius):
    """
    hay_bales is a sorted list of hay bale positions.
    explode_index is the index of the hay bale that is exploded.
    radius is the radius of the explosion.

    Return the index of the rightmost hay bale in the radius that explodes.
    """
    if explode_index == len(hay_bales) - 1:
        return explode_index
    i = explode_index + 1
    while i < len(hay_bales) and hay_bales[i] - hay_bales[explode_index] <= radius:
        i = i + 1
    return i - 1


def explode_right(hay_bales, explode_index):
    """
    hay_bales is a sorted list of hay bale positions.
    explode_index is the index of the hay bale that is exploded.

    Return the index of the rightmost hay bale that explodes.
    """
    radius = 1
    done = False
    while not done:
        rightmost = explode_right_one(hay_bales, explode_index, radius)
        if rightmost == explode_index:
            done = True
        else:
            explode_index = rightmost
            radius = radius + 1
    return rightmost


input_file = open('angry.in', 'r')
output_file = open('angry.out', 'w')

n = int(input_file.readline())

hay_bales = []

for i in range(n):
    hay_bales.append(int(input_file.readline()))

hay_bales.sort()

max_exploded = 1

for i in range(n):
    leftmost_index = explode_left(hay_bales, i)
    rightmost_index = explode_right(hay_bales, i)
    exploded = rightmost_index - leftmost_index + 1
    if exploded > max_exploded:
        max_exploded = exploded

output_file.write(f'{max_exploded}\n')

input_file.close()
output_file.close()
