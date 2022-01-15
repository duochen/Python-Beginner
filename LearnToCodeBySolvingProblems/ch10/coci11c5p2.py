lst = input().split()
n = int(lst[0])
m = int(lst[1])

tree_heights = input().split()
for i in range(len(tree_heights)):
    tree_heights[i] = int(tree_heights[i])

tree_heights.sort()

total_cut = 0
i = n - 2

while total_cut < m:
    # What is the height difference between this tree and the previous tree we processed?
    height_diff = tree_heights[i + 1] - tree_heights[i]
    # And how many trees have we processed?
    num_trees = n - i - 1
    # Each processed tree gives us height_diff new wood
    total_cut = total_cut + height_diff * num_trees
    i = i - 1

excess = total_cut - m
reduce = 0

# We have tried cutting at the height of each tree.
# This might lead to cutting more wood than necessary.
# If that happens, figure out how much higher we can cut to still cut enough wood.
if excess > 0:
    reduce = excess // (n - i - 2)

print(tree_heights[i + 1] + reduce)
