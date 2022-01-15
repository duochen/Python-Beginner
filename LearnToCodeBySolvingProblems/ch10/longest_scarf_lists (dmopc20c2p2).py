# Alternate solution using lists instead of dicts.
# We preallocate two lists of the correct size,
# and set all of their values to -1.
# We then update the index of each color we see in the scarf.


MAX_COLORS = 1000000


lst = input().split()
n = int(lst[0])
m = int(lst[1])

scarf = input().split()
for i in range(n):
    scarf[i] = int(scarf[i])

leftmost_index= [-1] * (MAX_COLORS + 1)
rightmost_index = [-1] * (MAX_COLORS + 1)

for i in range(n):
    color = scarf[i]
    if leftmost_index[color] == -1:
        leftmost_index[color] = i
        rightmost_index[color] = i
    else:
        rightmost_index[color] = i

max_length = 0

for i in range(m):
    relative = input().split()
    first = int(relative[0])
    last = int(relative[1])
    if leftmost_index[first] != -1 and leftmost_index[last] != -1:
        length = rightmost_index[last] - leftmost_index[first] + 1
        if length > max_length:
            max_length = length

print(max_length)
