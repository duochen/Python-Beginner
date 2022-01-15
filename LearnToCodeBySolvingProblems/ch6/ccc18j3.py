def distance_between(lst, i, j):
    """
    lst is a list of distances between cities.
    i and j are indices of cities.

    Return the distance between the city at index i and the city at index j.
    """
    if i < j:
        city1 = i
        city2 = j
    else:
        city1 = j
        city2 = i
    total = 0
    for k in range(city1, city2):
        total = total + lst[k]
    return total


lst = input().split()
for i in range(len(lst)):
    lst[i] = int(lst[i])

for i in range(len(lst) + 1):
    distances = []
    for j in range(len(lst) + 1):
        distances.append(str(distance_between(lst, i, j)))
    print(' '.join(distances))
